---
# Title is set in mkdocs.yml
icon: simple/system76 # Your icon, see https://squidfunk.github.io/mkdocs-material/reference/icons-emojis/
description: "Setting up COSMIC in blendOS."
---

<!-- made because system76 uses one URL for distro listings :)
Pointing people to the download page would be cruel.
-->

<!-- The top-level header *must* look like this (uses the same icon defined in the frontmatter)-->

# :simple-system76: COSMIC Setup

By ![Ast3risk-ops](https://github.com/Ast3risk-ops.png){ width=30 .circle } [@Ast3risk-ops](https://asterisk.lol){ target="\_blank" rel="noopener noreferrer "}

<!-- you can also paste a gitlab.com, blendOS gitlab, bitbucket or 𝕏 profile link here, or make a Markdown link of this format:

[@Your_Username](link-to-site-or-profile)

The image can also be a local one, store it in docs/assets/img/guides

![Your Profile Picture](../assets/img/guides/your_picture.png)

-->

1. [**:material-hammer-wrench: Install blendOS**](../install/normal-pc.md)
2. Edit [:material-file-star: `system.yaml`](../reference/configs/system.md) and change to the COSMIC track:
```yaml title="/system.yaml"
track: "cosmic"
```
3. Run `#!bash sudo akshara update`
4. On reboot, you'll see a user called `gnome-initial-setup`. Click the Users icon in the greeter and change to your user.
