---
icon: material/file-star
description: "system.yaml config reference"
---

<div class="grid cards" markdown>

-   # :material-file-star: system.yaml ![v4 badge](../../assets/img/v4.svg)
    -------

    <em>Manage your whole system with one file.</em>

    - Language: :misc-yaml:{ title="YAML" }
    - Comes with blendOS: :octicons-check-16:{ .green title="Yes" }

    --------
    ```title="File Location"
    󰉋 /
    └── 󱀺 system.yaml
    ```

    --------

    To edit the file, just open it in your favorite text editor ({{ inlinealert("warning", ":fontawesome-solid-exclamation:", "Warning", "You will need root privileges." ) }}).

</div>

## :material-clipboard-text: Reference

!!! note ""
    **Any options marked with a :material-cog-box: next to their name in the expanded view can be set by a track.**

!!! info ""
    More info on the possible values of these options is given in the next section.

--8<-- "docs/reference/configs/files/system.yaml.md"

## :material-train: Tracks

!!! danger "Always use the `.yaml` extension when creating track files!"
    {{ reference("utils", "akshara") }} always looks for files with the `.yaml` extension, not `.yml`.

Tracks are like mini `system.yaml` files that you can create. They can inherit other tracks, or be entirely custom. They can be used to set default values for a certain configuration, like a desktop.

### :material-map: Track layout

A track is structured *exactly* like a `system.yaml`, minus the `repo` bit (or other bits depending on inheritance).

As an example of a custom track, let's look at the official {{ track("blendos-base") }} track:

??? code "blendos-base.yaml"
    ```yaml
    --8<-- "https://github.com/blend-os/tracks/raw/main/blendos-base.yaml"
    ```

Here, the `track` value is set to `custom` (no `impl`), indicating a fully custom track. This track is setting default values for whomever uses it.

Tracks can also inherit from eachother (see next section).

### :material-account-child: Inheritance

Inherited tracks are the most common type of track. They can be used to tack on different desktops, additional drivers/programs, to another track.

An example of this is the official {{ track("plasma") }} track.

??? code "plasma.yaml"
    ```yaml
    --8<-- "https://github.com/blend-os/tracks/raw/main/plasma.yaml"
    ```

All of our desktop tracks inherit {{ track("blendos-base") }}. If you're creating a new desktop/WM track **do this as well**.

To inherit a track, simply set an `impl` and a `track` value in your track file.

!!! example
    ```yaml title="my-awesome-track.yaml"
    impl: 'https://github.com/blend-os/tracks/raw/main'

    track: blendos-base

    packages:
      - 'some-desktop'
    ```

    This track now inherits from {{ track("blendos-base") }}, and adds a desktop to it.

If you're creating a fully custom track and **do not** want to inherit, simply set your `track` to `custom` with no `impl` (as mentioned above).

### :octicons-repo-16: Creating a track repo/webserver

First, create a repo on your favorite git forge, and put all your track files in the root of it.

!!! tip "If you want to do this quickly, just fork our [track repo](https://github.com/blend-os/tracks){ rel="noopener noreferrer" target="_blank" }!"

Once that is done, you'll need to make your `impl` URL.

!!! abstract "impl URL structure"
    === ":simple-github: Github"
        `https://github.com/USER/REPO/raw/BRANCH`
    === ":fontawesome-brands-gitlab: Gitlab"
        `https://GITLAB-SERVER/USER/REPO/-/raw/BRANCH`
        
        - `GITLAB-SERVER`: Your gitlab server (usually `gitlab.com`)
    === ":simple-gitea: Gitea/Forgejo"
        `https://GITEA-SERVER/USER/REPO/raw/branch/BRANCH`

        - `GITEA-SERVER`: Your Gitea/Forgejo server (`codeberg.org` is a popular one)
    === ":simple-bitbucket: Bitbucket"
        `https://bitbucket.org/USER/REPO/raw/FULL_COMMIT_HASH/`

        - `FULL_COMMIT_HASH`: The full hash of the latest commit (you can get this under `Commits`)
    -----
    - `USER`: Your username
    - `REPO`: The repo
    - `BRANCH`: Your branch (usually `main` or `master`)

*[git forge]: A git storage service like GitHub or GitLab

## :material-folder-open: Custom repositories
