---
icon: material/chat-question
description: "blendOS FAQ"
---

# :material-chat-question: FAQ

## What desktops are officially supported?

- GNOME (`default-gnome` track)
- KDE Plasma (`plasma` track)
- XFCE (`xfce` track)
- Cinnamon (`cinnamon` track)
- MATE (`mate` track)
- LXQt (`lxqt` track)

You can [make your own tracks](reference/configs/system.md#tracks) to support whatever desktop or WM you want, this is just what we offer by default.

## Why can't I use another init system?

blendOS relies heavily on [`systemd-nspawn`](https://wiki.archlinux.org/title/Systemd-nspawn){ target="_blank" rel="noopener noreferrer" } for containers, which is like `chroot` but on steroids. It is included with the {{ archpkg('systemd') }} package on Arch.

## Why are my alises not showing up on fish?

blendOS has a file in `/etc/profile.d` that tells POSIX-compliant shells (i.e. bash, zsh) where to find your container binaries. These shells source it by default and understand the format. Fish is not POSIX-compliant. All you have to do is add the following to your `~/.config/fish/config.fish`:

```fish
if status is-login
    exec bash -c "test -e /etc/profile.d/blend.sh && source /etc/profile.d/blend.sh;\
    exec fish"
end
```

## What should go on the host?

Things like:

- Drivers
- Terminal emulators
- Web Browsers
- File managers
- Desktops/WMs
- Podman containers
- Anything that doesn't work in containers or as a flatpak


