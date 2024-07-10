---
draft: false
date: 2023-04-22
categories:
  - v2
  - stable
authors:
  - rs2009
comments: true
---

# blendOS v2 "Avial" is now available

We’re excited to announce the new stable release of blendOS v2 codenamed “Avial”, with a range of exciting new features!

Check out our video for a quick overview of all the new features: [https://youtu.be/\_OpKeqTtY1s](https://youtu.be/_OpKeqTtY1s).

Download: [https://github.com/blend-os/blendOS/releases/tag/23.04](https://youtu.be/_OpKeqTtY1s)

Discord: [https://discord.gg/m9JPmZB8Kd](https://youtu.be/_OpKeqTtY1s)

<!-- more -->

## Release notes

### Major changes

1. In addition to the apps available in containers, it’s now possible to install apps straight from the system Arch repos and the Chaotic-AUR repository, on the base itself. This is extremely useful if you want to install a third-party VPN app, for example, or some missing drivers.
    
2. `distrobox` has been replaced in favor of our own implementation using `podman` directly, built as part of blend, as it was impossible to implement certain features mentioned below using `distrobox`. A bit of code has been used from Distrobox in Blend for init and NVIDIA driver support.
    
3. Applications and binaries installed in containers now automatically and instantaneously appear on the base system, as expected from a blend of distributions.
    
4. Since you’re now probably wondering about potential conflicts between distributions and apps from them, we’re happy to inform you that we have developed a new priority-based system, that allows you to control which container’s binaries and apps should be given preference over those of others. Any system packages override this behavior, to avoid any system-container conflicts.
    
5. blendOS now follows a flavor and remix system, where remixes are community-developed variants of blendOS. You can use the official blendOS build webpage to easily create and submit your own blendOS remix, with a custom set of packages (including a desktop environment or window manager of your choice). Once approved, it will build on the blendOS build server.
    
6. It offers two official flavors now: a GNOME edition that uses GNOME 43.4, and a KDE Plasma edition that offers Plasma 5.27. The GNOME edition offers a nearly vanilla experience, aside from an auto-grouping system based on the ‘GNOME Dash Fix’ project, that automatically groups together apps belonging to different operating systems and categories. This behavior can be toggled from the blendOS Settings app.
    
7. Android apps are now supported out-of-the-box (using WayDroid), and you can easily install them from your favorite app stores like the Aurora Store or F-Droid, and use them just like native, windowed Linux apps. This is also useful for Android developers, as they can test their apps through WayDroid in Android Studio, just like regular Linux apps without the need for a heavy Android emulator.
    
8. You can install or use web apps/PWAs just like regular, desktop apps. You can also submit your own apps to the blendOS Web Store.
    
9. You can install system packages using `pacman` as you would on a regular Arch install, including DEs, thanks to an overlay system, that also allows you to rollback to existing snapshots in the event that anything goes wrong. In future, support for merging the overlay with the main root file system will also be added.
    

### Minor changes

1. The NVIDIA drivers are now included by default.
    
2. The ISO now supports BIOS and UEFI (32 bit and 64 bit) systems.
    
3. We’ve built a new installer framework, that installs both the official flavors of blendOS within 3 minutes each.
    

## Naming

We will be naming our releases after popular dishes, that represent the perfect blend of various unique and complementary ingredients, just like blendOS represents the perfect combo of various Linux distros, Android and web apps.

Our new stable release is named after the popular south Indian dish, ‘Avial’, which is a mixed vegetable curry made with coconut and yogurt. We’ll be conducting polls to name the future releases ;)

---

Special thanks to Ray Vermey, our community moderator and QA lead, and Tobiyo Kuujikai, our community moderator, for helping me with the testing of this release.
