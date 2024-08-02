---
description: 'Building a blendOS ISO'
icon: material/disc
---

# :material-disc: ISO Building

You will need a system running [:material-arch: Arch Linux](https://archlinux.org){ target="_blank" rel="noopener noreferrer" } or a derivative of it.


To build a blendOS ISO, do the following:

1. Install {{ archpkg("archiso") }}
   ```bash
   sudo pacman -S archiso
   ```
2. Clone the [build repo](https://git.blendos.co/blendOS/image-builder){ target="_blank" rel="noopener noreferrer" }
   ```bash
   git clone https://git.blendos.co/blendOS/image-builder.git
   ```
3. Build the ISO
   ```bash
   cd image-builder && sudo mkarchiso -v -w workdir/ -o out/ .
   ```
The ISO will appear in the `out` folder.

!!! note "Rebuilds"
    For rebuilds, you'll need to remove the `out` and `workdir` folders.

    ```sh
    sudo rm -rf ./out ./workdir
    ```
    <small>\* `sudo` is required as `archiso` creates these folders as root.</small>
