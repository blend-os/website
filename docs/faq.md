---
icon: material/chat-question
description: "blendOS FAQ"
---

# :material-chat-question: FAQ

## What desktops are officially supported?

- GNOME (`default-gnome` track)
- KDE Plasma (`plasma` track)
- XFCE
- Cinnamon
- MATE
- LXQt

## Why can't I use another init system?

blendOS relies heavily on [`systemd-nspawn`](https://wiki.archlinux.org/title/Systemd-nspawn){ target="_blank" rel="noopener noreferrer" } for containers, which is like `chroot` but on steroids. It is included with the {{ archpkg('systemd') }} package on Arch.
