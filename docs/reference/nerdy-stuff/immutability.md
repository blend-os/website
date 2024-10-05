---
icon: material/layers
description: How blendOS's immutability works
---

# :material-layers: Immutability

!!! warning "This is a work in progress!"

blendOS's immutability is layered, like any other immutable distro. Here's how it works:

(mermaid chart here)

1. `overlayfs` is used to mount a read-only filesystem atop `/usr/` and `/var/lib/pacman`
1. A read-write filesystem is mounted atop `/usr/local` for custom system-wide configuration
1. `/etc/` and the user's home folder remain writeable
