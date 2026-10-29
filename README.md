<h1 align="center">✦ LiveStagix</h1>

<p align="center">
  <strong>Make your screen move.</strong><br>
  Turn your photos and videos into live wallpapers with motion effects, device-aware preparation, and built-in media tuning.
</p>

<p align="center">
  <a href="https://github.com/devdas74/LiveWP-Releases/releases/latest"><img src="https://img.shields.io/badge/Download-Latest%20APK-8B5CF6?style=for-the-badge&logo=android&logoColor=white" alt="Download the latest APK"></a>
  <a href="https://github.com/devdas74/LiveWP-Releases/releases"><img src="https://img.shields.io/badge/Browse-All%20Releases-302447?style=for-the-badge&logo=github&logoColor=white" alt="Browse all releases"></a>
  <a href="https://github.com/sponsors/devdas74"><img src="https://img.shields.io/badge/Support-Development-6D28D9?style=for-the-badge&logo=githubsponsors&logoColor=white" alt="Support development"></a>
</p>

<p align="center">
  <strong>PHOTO</strong> &nbsp;·&nbsp; <strong>VIDEO</strong> &nbsp;·&nbsp; <strong>MOTION</strong> &nbsp;·&nbsp; <strong>ENHANCEMENTS</strong>
</p>

---

## Your screen, in motion

LiveStagix makes it easy to turn a photo or video into a live wallpaper, shape it for your display, and keep prepared versions ready to reuse.

- **Photo and video wallpapers** — preview your selection on LiveStage before applying it.
- **Device-aware preparation** — frame and prepare media for your display and supported media capabilities.
- **Prepare and reuse** — keep prepared versions in your library instead of repeating the same preparation.
- **Prepared media details** — check image dimensions and file information, plus video codec, frame rate, and bitrate when available.
- **Find a photo** — search the web for portrait wallpaper images directly from Controls.

## Motion for photos

Give photo wallpapers a little life with three motion styles:

| Effect | What it does |
|---|---|
| **2D Motion** | Pans the image as your phone moves. |
| **3D Motion** | Adds tilt, perspective, and depth. |
| **Rotation** | Rotates the image around the Z-axis. |

**Edge Safety** helps prevent empty edges as the image moves. Sensitivity, stabilization, and quick presets let you tune how the motion feels. Photo motion controls are not used for video wallpapers.

## Video enhancements

On supported devices, video wallpapers can use:

- **Frame Interpolation** — generates intermediate frames for smoother motion.
- **Smart Upscale** — enhances video detail using the available rendering path.

Availability and results depend on the device, graphics hardware, video codec, and runtime load. An enhancement being enabled in Settings does not guarantee that processing will remain active under every condition.

### Choose a rendering path

Select **Auto**, **Modern**, or **Compatibility** in Advanced Settings. The requested renderer and the renderer actually running can differ when a preferred path is unavailable.

## Tune prepared media

The built-in **Media Tuner** helps refine a prepared photo or video without editing the original source.

| Group | Adjustments |
|---|---|
| **Light** | Brightness, Contrast, Highlights, Shadows |
| **Color** | Saturation, Temperature |
| **Details** | Denoise, Structure, Sharpness |

Press and hold **Before** to compare your adjustments with the unadjusted media. Tap **Apply** to create a separate tuned prepared version. Your existing prepared version is preserved, and the wallpaper already active in Android is not changed automatically.

## Updating an active wallpaper

When LiveStagix is already the active wallpaper, applying new prepared media first attempts to update the content in place. If that fails, the app retries up to **three times**. If all attempts fail, it falls back to Android's wallpaper preview and confirmation flow.

## Get started

1. **[Download the latest APK](https://github.com/devdas74/LiveWP-Releases/releases/latest)** and install it.
2. Open LiveStagix and choose a photo or video in Controls. You can also search for a photo.
3. Open **LiveStage**, adjust the framing if needed, and tap **Prepare**.
4. When preparation finishes, optionally tune the media or tap **Set as Wallpaper**.
5. Choose Home, Lock, or Both when offered, then complete Android's wallpaper confirmation.

## Frequently asked questions

**Why are some controls unavailable?**  
Motion effects are for photo wallpapers; video enhancements are for video wallpapers. Other options depend on device capabilities and runtime conditions.

**Does tuning overwrite my prepared media?**  
No. Applying tuning creates a separate prepared version. The original source and base prepared version remain available.

**Will every phone support the same enhancements?**  
No. Android version, graphics hardware, supported codecs, and runtime load affect which processing paths are available and how well they perform.

**How do I check for updates?**  
Open **Advanced Settings** to check manually. LiveStagix also checks when it opens and returns to the foreground; it does not require a separate daily background service. The GitHub APK uses GitHub releases for update discovery.

## About

This repository distributes official LiveStagix APK releases. The source code and build system are maintained separately.

LiveStagix is proprietary software. This repository does not grant an open-source license.
