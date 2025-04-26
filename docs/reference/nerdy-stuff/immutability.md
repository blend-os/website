---
icon: material/layers
description: How blendOS's immutability works
---

# :material-layers: Immutability

!!! warning "This is a work in progress!"

Immutablility means you can't edit system files directly. This is required to preserve [atomicity](atomicity.md), allows [tracks](../configs/system.md#tracks) to work properly and prevents you from destroying your system by accident.

blendOS's immutability is layered, like any other immutable distro. Here's how it works:

(mermaid chart here)

1. `overlayfs` is used to mount a read-only filesystem atop `/usr/` and `/var/lib/pacman`
1. A read-write filesystem is mounted atop `/usr/local` for custom system-wide configuration
1. `/etc/`, the user's home folder and `/usr/local` remain writeable

!!! tip "Anything created outside of existing system folders (i.e. stuff not in `/usr`, `/lib`, `/opt`, etc) is writeable."
