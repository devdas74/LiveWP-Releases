# LiveStagix

**LiveStagix** is an Android live-wallpaper app by **Davesya** that turns photos and videos into live wallpapers, with photo motion effects, video enhancements, device-aware media preparation, and a native Floating Island-style runtime interface.

This repository distributes public release APKs. The application source code and build system are maintained separately.

## Features

### 🖼️ Photo and Video Wallpapers
- Use a photo or video from your device as a live wallpaper.
- Search the web for portrait wallpaper photos.
- Preview media in **Live Stage** before applying it.
- Reuse media that has already been prepared.

### ⚙️ Device-Aware Media Preparation
LiveStagix prepares selected media before handing it to the Android wallpaper engine. Depending on the media and device, preparation can handle:
- Wallpaper aspect-ratio cropping and orientation.
- Suitable output dimensions and video frame rate.
- Video bitrate and compatible codec conversion when possible.
- Audio removal from prepared wallpaper videos.
- Image scaling while preserving transparency where required.
- Local caching of prepared media to avoid repeating successful preparation.

If preparation fails, the original selected media is retained so you can try again.

### 🌀 Photo Motion Effects
Photo wallpapers support native gyroscope-based motion controls, including:
- 2D and 3D motion.
- Sensitivity and axis controls.
- Depth, translation, rotation, and zoom response.
- Automatic stabilisation to help the wallpaper return smoothly toward a stable position while keeping screen coverage.

Video wallpapers use a separate playback path and do not use the photo gyro-motion effects.

### 🎞️ Video Enhancements
- **Frame Interpolation (FI)** can generate intermediate frames for suitable video sources. The renderer decides whether the source frame rate is eligible for the device's display refresh rate.
- **Smart Upscale (SU)** can enhance lower-resolution video when supported and useful for the output size.
- Smart Upscale includes **Snapdragon Game Super Resolution (SGSR)** for compatible Snapdragon/Adreno devices and a **Linear Sharpener** option for broader compatibility.
- Enhancement settings and actual runtime activity are treated separately; an enabled feature is not necessarily processing at every moment.

### 🎮 Graphics Renderer
- **Auto** selects a supported rendering path for the device.
- **Modern** uses the modern OpenGL ES renderer where available.
- **Compatibility** provides an alternative rendering path for devices that need it.
- The runtime can report the renderer that is actually active.

### 🏝️ Floating Island and Runtime Status
The native Floating Island-style overlay works independently of the main app interface. Depending on the current state, it can show wallpaper/runtime information such as FPS, enhancement activity, and status feedback.

A runtime status indicator helps distinguish active operation, automatic pause, processing, disabled effects, and errors.

### ⚡ Automatic Pause and Load Protection
The wallpaper engine can reduce rendering work or pause processing when the wallpaper is not visible or when sustained load requires protection. Runtime behaviour depends on device capabilities, current media, and renderer conditions.

### 🎨 Appearance and Diagnostics
- **System default**, **Dark**, and **Light** appearance modes.
- Optional troubleshooting tools for native events, renderer behaviour, processing, FPS, gyro diagnostics, and watchdog status.
- Diagnostic tools are intended for troubleshooting and are not required for normal wallpaper use.

## How to set a wallpaper

1. Open **LiveStagix**.
2. Select a photo or video from your device, or find a photo using web wallpaper search.
3. Open **Live Stage**.
4. Press **Prepare** and let preparation finish.
5. Press **Set as Wallpaper**.
6. Complete Android's wallpaper preview and confirmation steps.

Prepared media can be reused without repeating preparation.

## Android compatibility

LiveStagix is designed for Android devices that support live wallpapers. Availability and behaviour can vary by Android version, device manufacturer, and vendor-specific restrictions.

On some Xiaomi, POCO, and HyperOS devices, system restrictions may change how third-party live wallpapers appear in the wallpaper selector or how they are applied.

## 🔮 Coming Soon

### Customisable Home Screen and Lock Screen

Customisation for the **Home Screen and Lock Screen** is planned for a future update. This feature is **not available in the current Stable release**, and no release date is being promised.

## Download

This is the **official public release repository** for LiveStagix.

**[Download LiveStagix from Releases](https://github.com/devdas74/LiveWP-Releases/releases)**

Current releases are provided as **beta builds**.

## Source code

This repository contains release APKs and release information only. The application source code and build system are maintained in a separate private repository.

## License

LiveStagix is proprietary software. No open-source license is granted by this repository.
