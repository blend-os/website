---
icon: material/book-open-variant
description: blendOS community guides
---

# :material-book-open-variant: Guides

These are community-written guides for blendOS.

!!! note "Disclaimer"

    This section is for user-specific, app-specific or miscellaneous guides. Anything specific to a utility, official guide, or config should be contributed to their respective pages.

    These guides are validated by the blendOS team, but they do not reflect the views of the team or the project. If you have issues with a guide, contact its creator.

## :material-file-document-plus: Recent Guides

<!-- maximum of 10 -->
<!-- example: 

- [:guide-icon: Guide Title](guide.md) by (paste your github, gitlab.com, blendOS gitlab, bitbucket or 𝕏 profile link here, it'll become a formatted link){ target="_blank" rel="noopener noreferrer" }

-or-

- [:guide-icon: Guide Title](guide.md) by [@your_username](link-to-your-website-or-profile-elsewhere-or-email-or-something){ target="_blank" rel="noopener noreferrer" }

-->

- [:octicons-container-16: Using Podman](using-podman.md) by [@Ast3risk-ops](https://asterisk.lol){ target="_blank" rel="noopener noreferrer" }
- [:material-pipe-wrench: Fixing System.yaml](fixing-system-yaml.md) by [@Ast3risk-ops](https://asterisk.lol){ target="_blank" rel="noopener noreferrer" }

## :fontawesome-solid-question: How do I write a guide?

It's pretty simple (and requires [Git](https://git-scm.com){ target="_blank" rel="noopener noreferrer" } and [Python](https://python.org){ target="_blank" rel="noopener noreferrer" } (already installed if you're on Linux) to be installed, we'll walk you through it).

You'll also wanna see our [contributing information](../contributing.md#docs) for how to write with Material for MkDocs and our style rules.

!!! info "Installing Git"
    Git is a CLI version control tool (from your terminal)
    
    On Windows you can use Git Bash (part of [Git for Windows](https://git-scm.com/downloads/win){ target="_blank" rel="noopener noreferrer" })

    On macOS you can install the XCode command line tools (type `git` into your terminal, you'll be prompted)

    On Linux, use your package manager (usually preinstalled)

    If this sounds too hard, you can use one of many Git GUI programs (**not Github Desktop**, that won't work with Gitlab).

    If you have Git installed, most editors will also have a Git client (Source Control in VSCode) that will handle everything for you.

??? abstract "Setting up your local Git profile"
    You'll want to do this for your profile to show up properly in commit history.

    Do the following:

    ```sh
    git config --global user.name "Your Username"
    ```

    ```sh
    git config --global user.email "Your Gitlab commit email"
    ```

    If you already have set this up for Github and use different values, `cd` to your cloned project and use `git config` (without `--global`)

If you need a crash course on Git, there's plenty available online. Here's the basic writing steps:

1. Sign up to our [Gitlab instance](https://git.blendos.co/users/sign_up){ target="_blank" rel="noopener noreferrer" data-umami-event="Gitlab signup" } and verify your account (more info about that during signup, you just have to contact an admin)
2. Fork the [docs repo](https://git.blendos.co/blendos/website){ target="_blank" rel="noopener noreferrer" } (click Fork at the top, make sure to choose **All branches**)
3. Clone your fork (Click clone, then copy the `Clone with HTTPS` url and clone it with your Git program):
   ```
   git clone <YOUR_CLONE_URL>
   ```
4. `cd` to your cloned folder and change to the `dev` branch:
   ```
   git checkout dev
   ```
5. Copy `docs/guides/example.md` to a new file in the same folder and edit it (don't edit the template directly)
6. Add your guide to `mkdocs.yml`:
   ```yaml title="mkdocs.yml"
   nav:
     # other navigation items
     - Guides:
       - Guides: guides/README.md
       - Your Guide Title: guides/your-guide.md
   ```
7. Edit `docs/guides/README.md` to add your guide to the [recent guides](#recent-guides) following the example in the comment
8. To preview your changes, see the guide in the [contributing section](../contributing.md#local-development)
9.  Create an [**access token**](https://git.blendos.co/-/user_settings/personal_access_tokens){ target="_blank" rel="noopener noreferrer" } (tick the `write_repository` and `read_repository` boxes) to authenticate your changes.
10.  Commit your changes (you'll be asked for a username and password, put your username for the username, then for the password, put your access token):
   ```
   git add * && git commit -m "your commit message" && git push origin dev
   ```
11. Make a [merge request](https://git.blendos.co/blendOS/website/-/merge_requests/new){ target="_blank" rel="noopener noreferrer" } from your fork to the main repo (**check to make sure the merge destination is the `dev` branch**)