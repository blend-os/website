---
icon: material/laptop
description: "Installing blendOS on a normal PC"
---

# :material-laptop: Normal PC

<figure markdown="span">
  ![install-banner](../assets/img/install-banner.svg){ width="1000" }
  <figcaption></figcaption>
</figure>

------

## :material-clipboard-list-outline: Requirements

!!! question inline end "How can I check if I'm 64-bit?"
    **:material-microsoft-windows: Windows**:
    Consult [Microsoft's guide](https://support.microsoft.com/en-us/windows/which-version-of-windows-operating-system-am-i-running-628bec99-476a-2c13-5296-9dd081cdd808).

    **:material-apple: MacOS**: Click the :material-apple: and choose **About This Mac**. Anything other than *Intel Core Solo* or *Intel Core Duo* under **CPU** is **64-bit**.

    **:simple-linux: Linux**:
    Run `#!bash getconf LONG_BIT` in a terminal. The resulting number should be **64**.

- :material-cpu-64-bit: A <span class="red" title="Required">**64-bit**</span> CPU, from no earlier than <span class="orange" title="Recommended">2009</span>.
- :fontawesome-solid-memory: A minimum of <span class="orange" title="Recommended">4 GBs</span> of RAM and <span class="red" title="Required">**25 GBs**</span> of storage.
- :material-usb-flash-drive: A spare USB drive, with a minimum size of <span class="red" title="Required">**4GBs**</span>.
- :material-lan: A <span class="red" title="Required">**network connection**</span>, for the installer
- :material-clock: Time
- :material-file-code: (**Optional**{ .blue }) Basic YAML knowledge

## :material-package-down: Download blendOS

You can get the current v4 testing edition from the following mirrors:

<div class="grid" markdown>

[:material-google-drive: Google Drive](https://drive.google.com/file/d/1Paf7mR2t_hw-eC5a3li4Umm02HV40TOf/view){ .md-button target="_blank" rel="noopener noreferrer" }
[:simple-mega: Mega](https://mega.nz/file/zEgnDDJY#m2S7tzufQFnjdvjaNTrLas-cNVqxbFYbGAXN_bMj_ao){ .md-button target="_blank" rel="noopener noreferrer" }
[:octicons-download-16: Sahilister](https://mirrors.sahilister.in/blendos/testing/blendos-20240310-x8664.iso){ .md-button target="_blank" }
[:octicons-download-16: AsteriskCloud](https://blend.asterisk.lol/api/public/dl/fgwYJnFQ){ .md-button target="_blank" }


</div>

We also have a [:fontawesome-solid-magnet: Magnet](magnet:?xt=urn:btih:cd1f5df0d6fff42a6aa7096c7696a7e535bfd2a2&dn=blendos-20240310-x8664.iso&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337%2Fannounce&tr=udp%3A%2F%2Ffosstorrents.com%3A6969%2Fannounce&tr=http%3A%2F%2Ffosstorrents.com%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A6969%2Fannounce&tr=http%3A%2F%2Ftracker.openbittorrent.com%3A80%2Fannounce&tr=udp%3A%2F%2Ftracker.torrent.eu.org%3A451%2Fannounce&ws=https%3A%2F%2Fmirrors.sahilister.in%2Fblendos%2Ftesting%2Fblendos-20240310-x8664.iso&ws=https%3A%2F%2Fqiwi.lol%2Fb8Mn0216-blendOS-2024.iso&ws=http%3A%2F%2Ffosstorrents.com%2Fdirect-links%2Fblendos-20240310-x8664.iso){ title="From FossTorrents" rel="noopener noreferrer" } link available from our [FossTorrents](https://fosstorrents.com/distributions/blendos/){ target="_blank" } page.

## :material-lightning-bolt: Flash a USB


=== ":octicons-star-fill-16: Etcher"
    Download Etcher from https://etcher.io and plug in your USB.
    
    You can click the button below[^1] to download and automatically flash the ISO.

    [![flash-with-etcher](https://balena.io/flash-with-etcher.png)](https://efp.balena.io/open-image-url?imageUrl=https://mirrors.sahilister.in/blendos/testing/blendos-20240310-x8664.iso)

    If you already have an ISO, pick your downloaded ISO, your USB drive, and hit `Flash!`.

    ![etcher-1](../assets/img/etcher-1.png)

=== "Rufus (DD mode)"

    Open your ISO in Rufus, and hit `START`. When prompted, choose **DD Mode**!
=== "DD"
    Open a terminal and type the following:

    ```sh
    sudo dd if="path_to_blendos.iso" of="/dev/sdX" bs=4M status=progress
    ```

    Replace `/dev/sdX` with your USB's identifier (found via `lsblk`)
------

[^1]: This only works with installed versions of Etcher, not portable ones.

## :material-package-variant: Install blendOS

Now we can get on to actually installing this distro.

### :material-power: Boot the USB

First, find your **one-time boot** key. You can do this by searching:

- `<YOUR_MOTHERBOARD_MANUFACTURER_HERE> one-time boot key`

or

- `<YOUR_MOTHERBOARD_MANUFACTURER_HERE> bios setup key`

<small markdown><span class="tip">:octicons-light-bulb-16: **Tip:** Common boot keys include: ++f12++, ++esc++, ++f2++, ++f10++ and ++f11++. </span></small>

Plug your USB in and spam that key while turning on your PC.

You should see some kind of boot menu, choose your USB device. If you get booted to a diagnostic screen or get a "secure boot violation" error, see the below abstract.

??? abstract "Disabling Secure Boot"
    Enter your BIOS setup and find a section called **Secure Boot** (or if it doesn't exist, look under **Boot**). Turn **Secure Boot** (also called **UEFI Secure Boot**) off.

    -----
    If you want to know what Secure Boot is, see [Microsoft's article on it](https://learn.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-secure-boot).



If you're asked to boot something, make sure `Arch Linux` or `blendOS` is selected, then press ++enter++.

From there, the installer should open and you can follow the install steps.