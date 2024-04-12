---
icon: material/monitor-shimmer
description: "Customizing your newly installed blendOS system"
---

# :material-monitor-shimmer: System Customization

System customization are done through the [:material-file-star: `system.yaml`](../../reference/configs/system.md) file. This guide will explain how to use it to customize different parts of your system.

Scroll down to learn more!

## :material-train-variant: Alternate track repos

<div class="grid cards" markdown>
-   :material-arrow-collapse:{ .lg .middle } __ico277's stripped tracks__
    
    !!! danger "This repo is not up to date!"

    A seriously stripped back track (experienced users only). Lacks all blendOS apps. Maintained by [ico277](https://github.com/ico277){ target="_blank" rel="noopener noreferrer" }.

    ---
    **impl URL:** `https://github.com/ico277/blendos-tracks/raw/main`

    ---
    **Removed packages:**
        
    ??? collapse "28 lines collapsed"
        - {{ archpkg('b43-fwcutter') }}
        - {{ archpkg('bind') }}
        - `blend-settings`
        - {{ archpkg('brltty') }}
        - {{ archpkg('broadcom-wl-dkms') }}
        - {{ archpkg('cryptsetup') }}
        - {{ archpkg('dhclient') }}
        - {{ archpkg('dmidecode') }}
        - {{ archpkg('espeakup') }}
        - {{ archpkg('hyperv') }}
        - {{ archpkg('irssi') }}
        - {{ archpkg('linux-atm') }}
        - {{ archpkg('linux-firmware-marvell') }}
        - {{ archpkg('mc') }}
        - {{ archpkg('memtest86+') }}
        - {{ archpkg('nbd') }}
        - {{ archpkg('neovim') }}
        - {{ archpkg('nilfs-utils') }}
        - {{ archpkg('pcsclite') }}
        - {{ archpkg('ppp') }}
        - {{ archpkg('pptp-client') }}
        - {{ archpkg('syslinux') }}
        - {{ archpkg('tcpdump') }}
        - {{ archpkg('tpm2-tss') }}
        - {{ archpkg('udftools') }}
        - {{ archpkg('vpnc') }}
        - {{ archpkg('wvdial') }}
        - {{ archpkg('xl2tpd') }}
        - {{ archpkg('ttf-jetbrains-mono') }}
    
    **Added packages:**
      
      - {{ archpkg('base-devel') }}

    **Additional tracks:**

      - {{ custom_track('https://github.com/ico277/blendos-tracks/raw/main', 'blendos-desktop') }} \- Adds GPU drivers and Pipewire

-   :fontawesome-brands-apple:{ .lg .middle } __T2 Tracks__
    
    !!! danger "This repo is not up to date!"
    
    Makes blendOS compatible with T2 devices as part of the [t2linux project](https://t2linux.org){ target="_blank" rel="noopener noreferrer" }. Maintained by [Noa Himesaka](https://noa.codes){ target="_blank" rel="noopener noreferrer" }.
    
    ---
    **impl URL:** `https://github.com/noahimesaka1873/blendos-tracks-t2/raw/main`

    `blendos-base` is now `blendos-base-t2`.

    ---

    **Removed packages:**
      
      - {{ archpkg('amd-ucode') }}
      - {{ archpkg('linux-zen') }}
      - {{ archpkg('linux-zen-headers') }}
      - {{ archpkg('broadcom-wl-dkms') }}
    
    **Added packages:**

      - `linux-xanmod-t2`
      - `linux-xanmod-t2-headers`
      - `t2fanrd`
      - `tiny-dfr`
      - `apple-t2-audio-config`
    
    **Build commands:**

    ```bash
    bash <(wget -qO- https://wiki.t2linux.org/tools/firmware.sh)`
    ```

    **Added repos:**

      - [`arch-mact2`](https://mirror.funami.tech/arch-mact2/os/x86_64/){ target="_blank" rel="noopener noreferrer" }
        ```
        https://mirror.funami.tech/$repo/os/$arch
        ```

-   :material-memory:{ .lg .middle } __Driverless Tracks__
    
    Default tracks, but with a few driver packages removed to speed up build time. Maintained by [Asterisk](https://asterisk.lol){ target="_blank" rel="noopener" }.
  
    ---
    **impl URL:** `https://github.com/ast3risk-ops/blendos-tracks-driverless`

    ---

    **Removed Packages:**

    - {{ archpkg('broadcom-wl-dkms') }}
    - {{ archpkg('linux-atm') }}
    - {{ archpkg('linux-firmware-marvell') }}
</div>

*[Removed packages]: Packages that have been removed from blendos-base or a rename of it
*[Added packages]: Packages that have been added to blendos-base or a rename of it

## :material-package-variant-closed-plus: Adding host packages

!!! info "blendOS is based on Arch by the way."

Add stuff under [`packages`](../../reference/configs/system.md#reference) like so (packages must be from the Arch repos, [our repo](https://pkg-repo.blendos.co){ target="_blank" rel="noopener noreferrer" }, or any custom repos you add):

```yaml
packages:
  - 'some-driver'
  - 'some-other-arch-thing'

```

??? abstract "Adding the Chaotic AUR"
    The Chaotic AUR is a pacman repo with precompiled AUR packages. It holds a lot of popular AUR packages on a global CDN.

## :material-monitor-multiple: Changing desktop

## :fontawesome-solid-paintbrush: Themes

Themes should work as normal.
