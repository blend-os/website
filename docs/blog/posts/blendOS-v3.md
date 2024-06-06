---
draft: false
date: 2023-07-08
categories:
  - v3
  - stable
authors:
  - rs2009
---

# blendOS v3 "Bhatura" is now available

blendOS v3 “Bhatura” has now been released, with a host of new features, including the ability to switch between 7 desktop environments with `system track`, seamless atomic background updates, support for 10 container distributions and Nix, reproducible systems (containers and dotfiles), new developer-friendly CLI utilities for system and user operations and a lot more.

<!-- more -->

Download and install: [https://docs.blendos.co/guides/installation-guide/#mirror-list](https://docs.blendos.co/guides/installation-guide/#mirror-list)

Discord: [https://discord.gg/m9JPmZB8Kd](https://docs.blendos.co/guides/installation-guide/#mirror-list)

## Release notes

### System updates

![System updates](https://blendos.co/blog-assets/blendos-v3/updates.svg align="left")

Unlike traditional Linux distributions, blendOS uses ISOs for updates, with your system being rebuilt on an update. Thanks to zsync, the update download size usually hovers around 10-100 MiBs, contrary to what you might have assumed.

Updates are downloaded in the background, and on the next boot, replace the current root filesystem while keeping any custom system packages you install (more on that later).

This update architecture resolves a major flaw with rolling-release distributions like Arch Linux, and allows us to confirm an update isn’t going to render your system unusable prior to rolling it out, thus providing a great deal of stability.

### DE support

![Desktop environments](https://blendos.co/blog-assets/blendos-v3/desktops.svg align="left")

blendOS now supports 7 desktop environments, including GNOME, KDE Plasma, Cinnamon, XFCE, Deepin, MATE and LXQt. You can switch between desktop environments easily and instantaneously with `system track`.

You can submit one of your own by adding it to [https://github.com/blend-os/manifests/blob/main/default.xml](https://docs.blendos.co/guides/installation-guide/#mirror-list) and submitting a pull request. Here’s what the GNOME profile looks like, for example:

```xml
<profile name="gnome" dm="gdm">
    <!-- WayDroid -->
    <pkg>waydroid-blend-git</pkg>
    <pkg>waydroid-image</pkg>

    <!-- GNOME packages -->
    <pkg>gnome</pkg>
    <pkg>adw-gtk3</pkg>
    <pkg>gnome-software</pkg>
    <pkg>gnome-shell-extension-blur-my-shell</pkg>
    <pkg>gnome-shell-extension-appindicator</pkg>
</profile>
```

### Reproducibility

It now allows you to reproduce your dotfiles, containers and associations through a simple YAML configuration file, like the one below:

```yaml
modules:
    ssh:
        enabled: true
        allowed_keys: []

    gnome:
        enabled: true
        style: light
        gtk-theme: 'adw-gtk3'
        icon-theme: 'Adwaita'
        titlebar:
            button-placement: 'right'

            double-click-action: 'toggle-maximize'
            middle-click-action: 'minimize'
            right-click-action: 'menu'


containers:
    # Containers go here
    ubuntu: 
        distro: ubuntu-23.04
        packages:
            - brz
            - devscripts
        commands:
            - 'echo "info: commands provided as strings, like this one, are run with bash"'
    
    debian:
        distro: debian
        packages:
            - git
            - cowsay
            - live-build
        commands:
            - sudo ln -sf ../../games/cowsay /usr/bin/cowsay
            - sudo ln -sf ../../games/cowthink /usr/bin/cowthink
            - ['cowsay', 'commands provided in the form of a list, like this one, are executed directly inside containers']

    kali: 
        distro: kali-linux
        packages:
            - metasploit-framework

associations:
    # Associations go here
    apt: ubuntu
    hello: ubuntu
    debuild: ubuntu
    git: debian
    lb: debian
    msfconsole: kali
```

The above configuration can be saved to a file named `~/Downloads/user.yaml` and imported with `user cadre ~/Downloads/user.yaml`, for example.

Read more at [https://docs.blendos.co/docs/utilities/blend-user/#writing-a-configuration-and-importing-it-on-other-systems](https://docs.blendos.co/guides/installation-guide/#mirror-list).

### Simplified application installation

![App installation](https://blendos.co/blog-assets/blendos-v3/apps.png align="left")

Now, you can simply double-click a DEB, RPM, *pkg.tar.zst* or an APK to install it to a container. (for APKs, you need to initialize Android app support from the **blendOS Settings** app)

### New CLI utilities

![New utilities](https://blendos.co/blog-assets/blendos-v3/system-user.svg align="left")

blendOS v3 introduces two new command line utilities, `system` and `user`, and both of these are designed to make the lives of developers much, much easier.

`system` allows you to install packages on the host itself, such as drivers and virtualization software from the Arch Linux repositories (`system install` and `system remove`). Speaking of which, unlike quite a few other immutable distributions, blendOS supports software such as VirtualBox if installed on the host.

`user` is a replacement for the old `blend` CLI (was deprecated in v2). It allows you to create and manage containers and associatiions, as well as generate and move dotfiles and containers between different blendOS machines, as touched upon in the previous section.

### Supported distributions

![Distributions](https://blendos.co/blog-assets/blendos-v3/distros.svg align="left")

The following distributions are now supported for containers, and you can use Nix too with a single/multi-user installation, just like on any regular Linux distribution:

* Arch
    
* AlmaLinux 9
    
* Crystal Linux
    
* Debian
    
* Fedora 38
    
* Kali Linux (rolling)
    
* Neurodebian Bookworm
    
* Rocky Linux
    
* Ubuntu 22.04
    
* Ubuntu 23.04
    

## Naming

Just like with the previous release, this one is named after another popular dish (or to be precise, bread) in the Indian subcontinent, the “bhatura” (my personal favorite, and something most Indians are probably familiar with).

---

Special thanks to Ray Vermey, our community moderator and QA lead/“Master Chief Tester” for testing the ISOs thoroughly, Asterisk for helping with docs and infra, Noa Himesaka for helping with testing and creating the T2 Linux variant of blendOS, SvGaming for helping with docs, and last but not the least, Tobiyo Kuujikai, our community moderator.
