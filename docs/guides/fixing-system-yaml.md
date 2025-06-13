---
# title is set in mkdocs.yml
icon: material/pipe-wrench # Your icon, see https://squidfunk.github.io/mkdocs-material/reference/icons-emojis/
description: "Fixing your system.yaml file"
---

<!-- The top-level header *must* look like this (uses the same icon defined in the frontmatter)-->

# :material-pipe-wrench: Fixing System.yaml

By ![Your Profile Picture](https://github.com/Ast3risk-ops.png){ width=30 .circle } [@Ast3risk-ops](https://asterisk.lol){ target="_blank" rel="noopener noreferrer" }

<!-- you can also paste a gitlab.com, blendOS gitlab, bitbucket or 𝕏 profile link here, or make a Markdown link of this format:

[@Your_Username](link-to-site-or-profile)

The image can also be a local one, store it in docs/assets/img/guides

![Your Profile Picture](../assets/img/guides/your_picture.png)

-->

If you're experiencing issues with, really, anything package-related, the main culprit is usually your [:material-file-star: `system.yaml`](../reference/configs/system.md) file.

Follow these steps to diagnose your issue. Once you're done fixing your file, run `#!sh sudo akshara update`.

1. **Verify you have the required lines.**
    
    
    These three lines should be at the top of the file:
    ```yaml title="system.yaml"
    repo: 'https://pkg-repo.blendos.co' 
    arch-repo: 'https://geo.mirror.pkgbuild.com' 
    impl: 'https://github.com/blend-os/tracks/raw/main'
    ```

1. **Verify you do not have the same block specified twice.**
    
    For example, this file has the same block (`#!yaml repo:`) specified twice.
    ```yaml title="broken-system.yaml"
    impl: https://github.com/blend-os/tracks/raw/main
    repo: https://pkg-repo.blendos.co

    repo: https://pkg-repo.blendos.co # Remove this
    packages:
      - nvidia-dkms
    services:
      - switcheroo-control
    ```

1. **Check indentation**
    
    YAML is very picky about indentation. Remember to indent all sub items by 2 *spaces* ({{ inlinealert("orange", ":fontawesome-solid-exclamation:", "Warning", "Do not use the ++tab++ key.") }})

    For example, this is indented wrong:
    ```yaml title="broken-system.yaml"
    services:
    - switcheroo-control
    ```
    It should be:
    ```yaml title="system.yaml"
    services:
      - switcheroo-control
    ```

If it's still not working, reach out to us on one of our [chatrooms](../index.md) to get help.
