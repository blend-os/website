---
draft: false
date: 2023-11-24
categories:
  - v4
  - alpha
authors:
  - rs2009
---

# blendOS v4 Alpha

We're glad to announce the first **alpha** release of **blendOS v4**!

It's the first release of blendOS that is **fully declarative**, allowing you to have any packages, kernels or drivers on a **base Arch system** of your liking, while shipping pre-configured GNOME, KDE, XFCE, MATE and Budgie images if you'd like not to deal with the hassle of setting everything up yourself.

<!-- more -->

```yaml
# /system.yaml

repo: 'https://pkg-repo.blendos.co/'

impl: 'https://github.com/blend-os/tracks/raw/main'

track: 'plasma'

packages:
    - 'micro' # the best text editor out there ;)
    - 'firefox'
    - 'caddy'

services:
    - 'caddy'

package-repos:
    - name: 'chaotic-aur'
      repo-url: 'https://cdn-mirror.chaotic.cx/$repo/$arch'
```

The above configuration, for example, allows you to have a blendOS installation with **KDE Plasma**, Firefox, the Caddy web server, and the Chaotic AUR package repository.

You can now use **any desktop environment** or packages from the Arch repositories simply, by replacing the `track` variable with `blendos-base` and adding the packages for the desktop environment to the `packages` list/array, essentially delivering an **atomic Arch Linux system** with a package set of your choice.

This release also reduces the reliance on the blendOS servers for updates. It generates root filesystems locally for updates, instead of pulling them from a centralized, hardcoded update server.

At the moment, there aren't built installation ISOs of v4. However, if you'd like to replace an Arch Linux installation with it, here's what you need to do:

1. Ensure you're using `mkinitcpio` for generating your initramfs (not `dracut`), and `GRUB` as your bootloader. Also, full-disk encryption isn't supported currently.
    
2. Add the following lines to the end of the `/etc/pacman.conf` file.
    
    ```ini
    [breakfast]
    SigLevel = Never
    Server = https://pkg-repo.blendos.co
    ```
    
3. Create a `/system.yaml` file with the following contents.
    
    ```yaml
    # /system.yaml
    
    repo: 'https://pkg-repo.blendos.co/'
    
    impl: 'https://github.com/blend-os/tracks/raw/main'
    
    track: 'plasma' # or 'xfce' or 'mate'
    
                    # GNOME isn't recommended
                    # at the moment as it is
                    # known to be be buggy.
    
    packages:
        - 'firefox'
    #   - 'nvidia-dkms' if you're using an NVIDIA GPU
    ```
    
4. Run `sudo pacman -Sy akshara`.
    
5. Add `akshara` after `base udev` in `/etc/mkinitcpio`. (**HOOKS**)
    
6. Run `sudo mkinitcpio -P; sudo akshara update`.
    
7. Reboot your system. You're good to go!
    
    To update your system to the latest versions of Arch packages, just run `sudo akshara update` and reboot.
    
    ---
    
    Special thanks to Ray Vermey, our community moderator and QA lead/“Master Chief Tester” for testing the alpha release, Jaoheah & Asterisk for doing the docs and helping with the infra, Noa Himesaka for helping with testing and creating the T2 Linux variant of blendOS, Antiz for helping with debugging GDM, SvGaming for helping with docs and bpkg, and last but definitely not the least, Tobiyo Kuujikai, our community moderator.
