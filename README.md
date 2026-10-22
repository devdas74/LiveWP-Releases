<h1 align="center">LiveStagix</h1>

<p align="center">
  <strong>Make your screen move.</strong><br>
  Photo and video live wallpapers, motion controls, device-aware preparation and built-in media tuning.
</p>

<p align="center">
  <a href="https://github.com/devdas74/LiveWP-Releases/releases/latest"><strong>⬇ Download the latest APK</strong></a>
  &nbsp; · &nbsp;
  <a href="https://github.com/devdas74/LiveWP-Releases/releases">All releases</a>
  &nbsp; · &nbsp;
  <a href="https://github.com/sponsors/devdas74">Support development</a>
</p>

<p align="center">
  <img src="assets/screenshots/controls-overview.webp" alt="LiveStagix Controls screen showing media selection, prepared wallpapers, orientation and wallpaper search" width="340">
</p>

<p align="center"><em>Real LiveStagix app screenshot</em></p>

---

## Your wallpaper, your way

LiveStagix turns photos and videos into live wallpapers and gives you tools to prepare, frame and personalize them.

- **Photos and videos:** preview your selection in Live Stage before applying it.
- **Device-aware preparation:** adjust crop and framing, then prepare media for your device's display and supported media capabilities.
- **Prepare and reuse:** keep prepared wallpapers in your library instead of repeating the same preparation.
- **Prepared media details:** review image dimensions and file information, plus video codec, frame rate and bitrate when available.
- **Find a photo:** search the web for portrait wallpaper images directly from Controls.

## Motion that responds to you

Photo wallpapers can use gyroscope-based effects, including 2D pan, 3D tilt and depth, and Z-axis rotation. Edge Safety helps protect the edges while the image moves, and quick presets make it easier to tune sensitivity and stabilization. Motion controls are photo-focused; video wallpapers bypass gyro motion.

<details>
  <summary><strong>View the motion controls screenshot</strong></summary>
  <p align="center">
    <img src="assets/screenshots/motion-controls.webp" alt="LiveStagix photo motion settings showing gyro pan, tilt, rotation, edge safety and quick presets" width="340">
  </p>
</details>

## Video enhancements and rendering

On supported devices, video wallpapers can use **Frame Interpolation** for smoother motion and **Smart Upscale** for enhancement. These features depend on device support and runtime conditions, so an enabled setting does not guarantee that processing stays active at all times.

Choose **Auto**, **Modern** or **Compatibility** rendering. Advanced Settings shows both the **requested** renderer and the renderer currently **active**; they may differ when the selected path is unavailable.

Features and performance vary with Android version, graphics hardware, supported codecs and runtime conditions.

<details>
  <summary><strong>View Advanced Settings</strong></summary>
  <p align="center">
    <img src="assets/screenshots/engine-settings.webp" alt="LiveStagix Advanced Settings showing theme appearance, requested and active renderer, optional diagnostics and device profile" width="320">
  </p>
</details>

## Tune prepared photos and videos

LiveStagix includes a built-in **Media Tuner** for prepared media. In Live Stage, open the sliders control to tune the prepared photo or video.

- **Light:** Brightness, Contrast, Highlights and Shadows.
- **Color:** Saturation and Temperature.
- **Details:** Denoise, Structure and Sharpness.

Use **Before** to compare the adjustments with the unadjusted media by pressing and holding it. Closing the tuner keeps pending adjustments, so you can return to the stage without losing them. Tap **Apply** to create a separate tuned prepared copy; the existing prepared version is preserved, and the wallpaper that is already active is not changed automatically.

## Updating a wallpaper that's already active

When LiveStagix is already the active wallpaper, applying new prepared media first attempts to update its content in place. When that succeeds, the wallpaper changes without reopening Android's wallpaper preview.

If an in-place update fails, LiveStagix retries up to **three times**, with a short pause between attempts. If all three fail, it falls back to the established wallpaper replacement flow and opens Android's wallpaper preview and confirmation.

## Get started

1. [Download the latest APK](https://github.com/devdas74/LiveWP-Releases/releases/latest) and install it.
2. Open LiveStagix and choose a photo or video. You can also search for a photo from Controls.
3. Switch to **Live Stage**, adjust the framing if needed, and tap **Prepare**.
4. After preparation, use the tuner to create a tuned copy if desired, or tap **Set as Wallpaper**.
5. For first-time setup or replacement, complete Android's wallpaper preview and confirmation.

## Frequently asked questions

**Why are some controls unavailable?**  
Motion controls are intended for photo wallpapers; video enhancements are intended for video wallpapers. Other options depend on your device's capabilities.

**Does tuning overwrite my prepared media?**  
No. Applying tuning creates a separate prepared version. The tuner also prevents direct tuning of the wallpaper currently active in Android.

**Will every phone support the same enhancements?**  
No. Android version, graphics hardware, codecs and runtime load affect which paths can be used and how well they perform.

**Does an in-place wallpaper update always work?**  
No. LiveStagix retries up to three times, then uses its existing replacement flow if needed.

**Where can I check for app updates?**  
Open **Advanced Settings** to check manually. LiveStagix also checks when opened, at most once every 24 hours; it does not need a separate daily background service.

## About

This repository distributes official LiveStagix APK releases. The source code and build system are maintained separately.

LiveStagix is proprietary software. No open-source license is granted by this repository.
