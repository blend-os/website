---
icon: material/laptop
description: "Installing blendOS on a normal PC"
---

# :material-laptop: Normal PC

## :material-clipboard-list-outline: Requirements

!!! question inline end "How can I check my CPU?"
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