# LiveWP

**LiveWP** is an Android live wallpaper app by **Davesya** for turning your photos and videos into live wallpapers, with native motion effects, video processing, performance controls, and a Floating Island-style runtime interface.

## What is LiveWP?

LiveWP combines a media-preparation system with a native Android live-wallpaper engine.

Choose a photo, video, or preset, prepare it for your device, and then set it as your Android live wallpaper. Photo wallpapers can respond to device movement, while video wallpapers use the dedicated video playback and processing path.

## Lightweight by Design

LiveWP is built to offer advanced live-wallpaper features without keeping every processing path running all the time. The app continuously adapts its work to the device, the media being displayed, the current screen state, and actual renderer load. Features are activated only when their conditions are met, and power- or performance-heavy work is reduced or paused when it is not useful.

The systems that help keep LiveWP lightweight include:

- **Device-aware media preparation** — photos are downsampled to a suitable wallpaper size instead of keeping unnecessarily large images in memory; videos are cropped to the device aspect ratio, prepared at no more than the device's display resolution, capped to the device refresh rate, and given a resolution/FPS-appropriate bitrate.
- **Efficient video preparation** — prepared videos have audio removed, use HEVC/H.265 when supported, and have an H.264/AVC fallback when HEVC conversion is not available.
- **Preparation reuse and bounded cache** — already-prepared media is reused instead of being processed again, while the prepared-media cache is kept within a 200 MB limit by removing the oldest unprotected entries when necessary.
- **Automatic Pause & Load Protection** — Auto Pause is a complete protection system, not just a single pause switch. It can stop rendering work when the wallpaper is not visible, when the battery is low, when Android Battery Saver is active, or when the renderer is under sustained strain. Under renderer strain, LiveWP first reduces its effective FPS, can temporarily bypass Smart Upscale, and only then enters a harder pause when necessary; it resumes after the renderer recovers.
- **Selective Frame Interpolation** — FI does not constantly generate frames. It only becomes active when the measured source video FPS is suitable for the device refresh rate, with the source limited to roughly half the display refresh ceiling so generated frames can fit within that ceiling.
- **Selective Smart Upscale** — SU only processes video when the prepared source resolution is below the wallpaper output size. It can also be temporarily bypassed automatically when sustained renderer load requires additional protection, without permanently changing the user's setting.
- **Adaptive renderer selection** — Auto renderer mode can choose the modern OpenGL ES path when supported and fall back to the compatibility path when necessary instead of forcing one rendering path on every device.
- **Media-specific processing** — photo wallpapers use the motion-effects path, while video wallpapers bypass the photo motion-effects path, avoiding unnecessary gyro processing for video playback.
- **Optional diagnostics** — Event recording and diagnostic telemetry are opt-in tools and are not required for normal wallpaper operation.

These systems mean that LiveWP's feature list represents available capabilities, not a requirement for every device to run every effect continuously.

## Features

### 🖼️ Photo & Video Wallpapers
- Use photos or videos from your device as live wallpapers.
- Choose from bundled wallpaper presets.
- Keep prepared wallpapers available for reuse.

### ⚙️ Media Preparation & Optimization
- Prepares selected media before it is applied to the wallpaper engine.
- Adapts video output to the device display characteristics.
- Handles wallpaper-oriented cropping, resolution, frame rate, bitrate, and compatible video conversion where possible.
- Removes audio from prepared wallpaper videos.
- Prepares large photos for suitable wallpaper dimensions while preserving transparency when needed.
- Prepared media is cached locally so it can be reused without repeating preparation.

### 🔄 Preparation Recovery
- The original unprepared media is retained when preparation fails.
- Failed media can be prepared again instead of being permanently discarded.
- Successfully prepared media can be managed separately from the original gallery/preset source.

### 🌀 Gyroscope Motion Effects
Photo wallpapers support native device-motion effects with configurable controls for:
- **2D gyro motion**
- **3D gyro motion**
- **Depth**
- **X/Y sensitivity**
- **Motion translation**
- **Motion rotation**
- **Zoom response**

Video wallpapers bypass the photo wallpaper motion-effects path.

### 🎯 Auto Stabilisation
Photo motion includes automatic stabilization controls designed to smoothly return the wallpaper toward a stable position while helping maintain safe screen coverage.

### 🔄 Orientation Controls
Support for wallpaper media orientation at:
- 0°
- 90°
- 180°
- 270°

### 🎞️ Frame Interpolation
Video wallpapers include software frame interpolation controls.

- FI is enabled by default for newly selected videos.
- The user setting and actual renderer eligibility are handled separately.
- The native renderer only generates intermediate frames when the source frame rate is suitable for the device display refresh rate.

### ⏸️ Automatic Pause & Load Protection
The native renderer can reduce rendering work or pause wallpaper processing when the wallpaper is not actively displayed or when sustained renderer load requires protection.

Manual video pause is also supported.

### 🏝️ Floating Island
LiveWP includes a native Floating Island-style runtime overlay that can show wallpaper and renderer information such as:
- Wallpaper state
- Runtime status
- FPS information
- Frame interpolation state
- Processing/status information

The overlay operates independently of the main LiveWP interface.

### 💡 Status LED
The runtime status system provides visual state indication for wallpaper and motion activity, including states for:
- Active wallpaper / working effects
- Auto-pause
- Manually disabled effects
- Processing
- Failed wallpaper application
- Runtime errors

### 🎨 Theme Support
The app supports:
- **System default**
- **Dark**
- **Light**

### 🧰 Diagnostics & Event Recording
Optional troubleshooting tools can record and inspect native wallpaper and runtime events, including engine, rendering, processing, and diagnostic information.

These tools are intended for troubleshooting and are not required for normal wallpaper operation.

## How to use

1. Open **LiveWP**.
2. Select a photo, video, or preset.
3. Open **Live Stage**.
4. Press **Prepare**.
5. After successful preparation, press **Set as Wallpaper**.
6. Complete Android's wallpaper confirmation step.

Prepared media can be reused without repeating the preparation process.

## Android compatibility

LiveWP is designed for Android devices with live-wallpaper support. Availability and behavior can vary by Android version, device manufacturer, and vendor-specific restrictions.

On some Xiaomi / POCO / HyperOS devices, the system may restrict or change how third-party live wallpapers are exposed or applied.

## What’s new

The latest LiveWP update brings a major upgrade to video rendering, enhancement controls, and runtime status reporting.

### 🚀 New Renderer System
- Adds **Renderer 3.0** with modern OpenGL ES support.
- **Auto** renderer selection can use the modern renderer when supported and fall back to the compatibility renderer when needed.
- Renderer selection is available in the advanced diagnostic/runtime settings.

### ✨ Smart Upscale
- Adds **Smart Upscale (SU)** for lower-resolution video.
- Supports **Snapdragon Game Super Resolution (SGSR)** on compatible Snapdragon/Adreno devices.
- Includes a **Linear Sharpener** fallback for broader compatibility.
- Adds adjustable SU quality/performance control up to **100%**.
- SU activation is handled separately from simply enabling the feature, so the runtime can report when upscaling is actually active.

### 🎞️ Improved Video Enhancements
- Frame Interpolation (FI) and Smart Upscale can be controlled together from the video enhancement master control.
- Runtime status distinguishes enabled enhancements from enhancements that are actively processing.
- Video enhancement status can be reported to the Floating Island and status LED without depending on the expanded overlay remaining visible.

### 🏝️ Improved Runtime Feedback
- Floating Island now provides clearer video enhancement status information.
- Status reporting includes active Smart Upscale backend information where available.
- The runtime LED continues to provide compact health/status feedback while the wallpaper is running.

### ⚡ Performance & Reliability
- Video rendering and enhancement paths have received performance-oriented improvements.
- Renderer and enhancement behavior are designed to adapt to device capabilities instead of assuming a single hardware path.

## Download

This repository is the **official public distribution repository** for LiveWP.

**[Download LiveWP from Releases](https://github.com/devdas74/LiveWP-Releases/releases)**

Current releases are provided as **beta builds**.

## Repository & source code

This repository contains **release APKs and release information only**.

The LiveWP application source code and build system are maintained separately in a **private repository**.

## License

LiveWP is proprietary software. No open-source license is granted by this repository.
