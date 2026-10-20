# LiveStagix

An Android live wallpaper app for photos and videos.

## Features

- **Photo and video live wallpapers** with an immersive **Live Stage** preview.
- **Custom crop positioning** followed by device-aware media preparation for a suitable crop and output on your display.
- **Update wallpaper content in place** when LiveStagix is already active, avoiding the Android preview flow when the update succeeds.
- **Automatic update recovery:** an in-place content update is attempted up to three times. If all attempts fail, LiveStagix falls back to its established replacement flow and opens Android's wallpaper preview/confirmation.
- **Photo and video loading placeholders** with lightweight motion; the video placeholder remains until its first frame is ready.
- **Gyroscope motion effects** for photos.
- **Video enhancements** including **Frame Interpolation** and **Smart Upscale** on supported devices.
- **Renderer choices** for Auto, Modern and Compatibility modes, subject to device support.
- **Floating status pill** for wallpaper/runtime status.
- **Prepared media library** so prepared results can be reused without repeating the preparation process.
- **In-app update checking:** check manually in Advanced Settings, or let LiveStagix check when opened. Automatic checks are limited to once per 24 hours.

## Getting started

1. [Download the latest APK](https://github.com/devdas74/LiveWP-Releases/releases/latest).
2. Install and open LiveStagix.
3. Select a photo or video, or find a photo using wallpaper search.
4. Open **Live Stage** and tap **Prepare**.
5. When preparation finishes, tap **Set as Wallpaper**.
6. For a first-time setup or replacement, complete Android's wallpaper preview and confirmation steps.

## Updating an active wallpaper

When LiveStagix is already the active wallpaper, applying newly prepared media attempts to update the current wallpaper's content in place. If that succeeds, the new content becomes active without reopening Android's wallpaper preview.

If the in-place update fails, LiveStagix automatically retries up to three times. If all three attempts fail, it falls back to the established replacement flow and opens Android's wallpaper preview/confirmation.

## Compatibility

Available features and enhancement performance vary by device, Android version, supported codecs and graphics hardware.

## About

This repository distributes official LiveStagix APK releases. Source code and the build system are maintained separately.

LiveStagix is proprietary software. No open-source license is granted by this repository.
