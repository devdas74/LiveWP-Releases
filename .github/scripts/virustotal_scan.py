#!/usr/bin/env python3
"""Scan a published LiveStagix release APK and publish verified scan metadata."""

from __future__ import annotations

import datetime as dt
import hashlib
import json
import os
import pathlib
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import uuid

RELEASES_API = "https://api.github.com/repos/devdas74/LiveWP-Releases"
VT_API = "https://www.virustotal.com/api/v3"
APK_NAME = "LiveStagix_beta.apk"
STATUS_PATH = pathlib.Path("security/scan-status.json")
MAX_POLL_ATTEMPTS = 18
POLL_INTERVAL_SECONDS = 20


def request_bytes(url, method="GET", data=None, headers=None):
    request_headers = {"User-Agent": "LiveStagix-Security-Scan/1.0"}
    if headers:
        request_headers.update(headers)
    request = urllib.request.Request(url, data=data, headers=request_headers, method=method)
    try:
        with urllib.request.urlopen(request, timeout=90) as response:
            return response.read()
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        if exc.code == 429:
            retry_after = exc.headers.get("Retry-After", "not supplied")
            raise RuntimeError(f"VirusTotal rate limit reached; Retry-After: {retry_after}") from exc
        raise RuntimeError(f"HTTP {exc.code} for {url}: {detail[:500]}") from exc
    except urllib.error.URLError as exc:
        raise RuntimeError(f"Network request failed for {url}: {exc.reason}") from exc


def request_json(url, method="GET", data=None, headers=None):
    request_headers = {"Accept": "application/json"}
    if headers:
        request_headers.update(headers)
    raw = request_bytes(url, method=method, data=data, headers=request_headers)
    try:
        value = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise RuntimeError(f"Invalid JSON response from {url}") from exc
    if not isinstance(value, dict):
        raise RuntimeError(f"Unexpected response from {url}")
    return value


def load_release():
    event_path = os.environ.get("GITHUB_EVENT_PATH")
    event_name = os.environ.get("GITHUB_EVENT_NAME", "")

    if event_name == "release" and event_path:
        try:
            event = json.loads(pathlib.Path(event_path).read_text(encoding="utf-8"))
            tag = event.get("release", {}).get("tag_name")
        except (OSError, json.JSONDecodeError, AttributeError) as exc:
            raise RuntimeError(f"Cannot read published release event: {exc}") from exc

        if isinstance(tag, str) and tag:
            encoded_tag = urllib.parse.quote(tag, safe="")
            return request_json(RELEASES_API + "/releases/tags/" + encoded_tag)

    # Manual runs and workflow-file changes fall back to the latest published release.
    return request_json(RELEASES_API + "/releases/latest")


def select_apk(release):
    assets = release.get("assets")
    if not isinstance(assets, list):
        raise RuntimeError("The published release has no assets list.")

    apk = next(
        (asset for asset in assets if isinstance(asset, dict) and asset.get("name") == APK_NAME),
        None,
    )
    if not apk:
        raise RuntimeError(f"The release does not contain {APK_NAME}.")

    digest = apk.get("digest")
    if not isinstance(digest, str) or not digest.startswith("sha256:"):
        raise RuntimeError("GitHub did not provide SHA-256 metadata for this APK.")

    sha256 = digest[len("sha256:"):].lower()
    if len(sha256) != 64 or any(char not in "0123456789abcdef" for char in sha256):
        raise RuntimeError("GitHub returned a malformed SHA-256 digest.")

    download_url = apk.get("browser_download_url")
    if not isinstance(download_url, str):
        raise RuntimeError("The release APK has no download URL.")

    return apk, sha256


def download_verified(apk, expected_sha256):
    content = request_bytes(apk["browser_download_url"])
    actual_sha256 = hashlib.sha256(content).hexdigest()

    if actual_sha256 != expected_sha256:
        raise RuntimeError("Downloaded APK hash does not match GitHub metadata; refusing to submit it.")

    expected_size = apk.get("size")
    if isinstance(expected_size, int) and expected_size != len(content):
        raise RuntimeError("Downloaded APK size does not match GitHub metadata.")

    if not content:
        raise RuntimeError("Downloaded APK is empty.")

    return content


def multipart_file(filename, content):
    boundary = "----LiveStagixVirusTotal" + uuid.uuid4().hex
    head = (
        f"--{boundary}\r\n"
        f'Content-Disposition: form-data; name="file"; filename="{filename}"\r\n'
        "Content-Type: application/vnd.android.package-archive\r\n\r\n"
    ).encode("utf-8")
    body = head + content + f"\r\n--{boundary}--\r\n".encode("ascii")
    return body, boundary


def submit_file(api_key, content):
    endpoint = VT_API + "/files"

    if len(content) > 32 * 1024 * 1024:
        response = request_json(VT_API + "/files/upload_url", headers={"x-apikey": api_key})
        endpoint = response.get("data")
        if not isinstance(endpoint, str) or not endpoint.startswith("https://"):
            raise RuntimeError("VirusTotal did not return a valid large-file upload URL.")
        time.sleep(POLL_INTERVAL_SECONDS)

    body, boundary = multipart_file(APK_NAME, content)
    response = request_json(
        endpoint,
        method="POST",
        data=body,
        headers={
            "x-apikey": api_key,
            "Content-Type": f"multipart/form-data; boundary={boundary}",
        },
    )

    analysis_id = response.get("data", {}).get("id")
    if not isinstance(analysis_id, str) or not analysis_id:
        raise RuntimeError("VirusTotal did not return an analysis ID.")
    return analysis_id


def wait_for_analysis(api_key, analysis_id):
    url = VT_API + "/analyses/" + urllib.parse.quote(analysis_id, safe="")

    for attempt in range(1, MAX_POLL_ATTEMPTS + 1):
        time.sleep(POLL_INTERVAL_SECONDS)
        response = request_json(url, headers={"x-apikey": api_key})
        status = response.get("data", {}).get("attributes", {}).get("status")
        print(f"VirusTotal analysis status: {status or 'unknown'} ({attempt}/{MAX_POLL_ATTEMPTS})")

        if status == "completed":
            return
        if status not in ("queued", "in-progress", "in_progress", None):
            raise RuntimeError(f"Unexpected VirusTotal analysis status: {status}")

    raise RuntimeError("VirusTotal analysis did not finish within the polling window.")


def read_existing_status():
    try:
        value = json.loads(STATUS_PATH.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return {}
    except (OSError, json.JSONDecodeError) as exc:
        raise RuntimeError(f"Cannot read existing scan status: {exc}") from exc
    return value if isinstance(value, dict) else {}


def save_report(api_key, release, apk, sha256):
    report = request_json(VT_API + "/files/" + sha256, headers={"x-apikey": api_key})
    file_data = report.get("data", {})

    returned_hash = file_data.get("id")
    if returned_hash and returned_hash.lower() != sha256:
        raise RuntimeError("VirusTotal returned a report for a different SHA-256 hash.")

    attributes = file_data.get("attributes", {})
    stats = attributes.get("last_analysis_stats")
    if not isinstance(stats, dict) or not stats:
        raise RuntimeError("VirusTotal report has no completed engine statistics.")

    clean_stats = {
        str(key): int(value)
        for key, value in stats.items()
        if isinstance(value, int) and not isinstance(value, bool) and value >= 0
    }
    if not clean_stats:
        raise RuntimeError("VirusTotal returned no usable engine statistics.")

    timestamp = attributes.get("last_analysis_date")
    if not isinstance(timestamp, (int, float)):
        raise RuntimeError("VirusTotal report has no valid analysis timestamp.")

    analysis_date = dt.datetime.fromtimestamp(
        timestamp, tz=dt.timezone.utc
    ).replace(microsecond=0).isoformat().replace("+00:00", "Z")

    result = {
        "schemaVersion": 1,
        "status": "available",
        "releaseTag": release.get("tag_name") or "",
        "releaseName": release.get("name") or release.get("tag_name") or "LiveStagix release",
        "releaseUrl": release.get("html_url") or "https://github.com/devdas74/LiveWP-Releases/releases/latest",
        "publishedAt": release.get("published_at"),
        "fileName": apk.get("name") or APK_NAME,
        "fileSize": apk.get("size"),
        "sha256": sha256,
        "reportUrl": "https://www.virustotal.com/gui/file/" + sha256,
        "analysisDate": analysis_date,
        "publishedToRepositoryAt": dt.datetime.now(dt.timezone.utc).replace(
            microsecond=0
        ).isoformat().replace("+00:00", "Z"),
        "stats": clean_stats,
    }

    STATUS_PATH.parent.mkdir(parents=True, exist_ok=True)
    STATUS_PATH.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return result


def write_step_summary(result):
    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if not summary_path:
        return

    stats = result["stats"]
    total = sum(stats.values())

    with open(summary_path, "a", encoding="utf-8") as summary:
        summary.write(
            "## LiveStagix VirusTotal scan published\n\n"
            f"- Release: {result['releaseTag']}\n"
            f"- APK SHA-256: {result['sha256']}\n"
            f"- Malicious: **{stats.get('malicious', 0)}**\n"
            f"- Suspicious: **{stats.get('suspicious', 0)}**\n"
            f"- Engine results counted: **{total}**\n"
            f"- Analysis date: {result['analysisDate']}\n"
            f"- Report: {result['reportUrl']}\n\n"
            "A scan is a point-in-time signal, not a guarantee that software is completely safe.\n"
        )


def main():
    api_key = os.environ.get("VT_API_KEY", "").strip()
    if not api_key:
        raise RuntimeError("Missing VIRUSTOTAL_API_KEY repository secret.")

    release = load_release()
    apk, sha256 = select_apk(release)
    old_status = read_existing_status()

    if old_status.get("status") == "available" and old_status.get("sha256") == sha256:
        print(f"{release.get('tag_name', 'This release')} already has a report for this exact APK.")
        return

    print(f"Preparing {release.get('tag_name', 'published release')}.")
    content = download_verified(apk, sha256)
    print("Downloaded APK SHA-256 verified against GitHub release metadata.")

    analysis_id = submit_file(api_key, content)
    print("APK submitted to VirusTotal; waiting for analysis.")
    wait_for_analysis(api_key, analysis_id)

    # Keep the final report lookup outside the preceding polling request interval.
    time.sleep(POLL_INTERVAL_SECONDS)
    result = save_report(api_key, release, apk, sha256)
    write_step_summary(result)
    print("Published VirusTotal result: " + result["reportUrl"])


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print("ERROR: " + str(error), file=sys.stderr)
        raise SystemExit(1)
