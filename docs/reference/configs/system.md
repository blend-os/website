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

<style>
.md-typeset__table {
  width: 100%;
}

.md-typeset__table table:not([class]) {
  display: table
}
</style>
!!! question "What is system.yaml?"
    `system.yaml` is a simple host system configuration. It allows you to tweak many essential aspects of the host quickly and easily.

    ------



    | :octicons-check-circle-fill-12: `system.yaml` **is...**      | :octicons-x-circle-fill-12: `system.yaml` **is not...**      |
    | :-------------: | :-------------: |
    | :octicons-check-16: ...device-independent and transferrable | :octicons-x-12: ...advanced, config is quite simple. |
    | :octicons-check-16: ...simple | :octicons-x-12: ...like NixOS |
    | :octicons-check-16: ...deployable, [via tracks](#tracks) | :octicons-x-12: ...the way to use most apps on blendOS |


## :material-clipboard-text: Reference

!!! note ""
    **Any options marked with a :material-cog-box: next to their name in the expanded view can be set by a track.**

!!! info ""
    All values shown here are default values or examples. You can find the default value (as well as info and examples) in the tooltip (:material-plus-circle:).

--8<-- "docs/reference/configs/files/system.yaml.md"

## :material-train: Tracks

!!! danger "Always use the `.yaml` extension when creating track files!"
    {{ reference("utils", "akshara") }} always looks for files with the `.yaml` extension, not `.yml`.

Tracks are like mini `system.yaml` files that you can create. They can inherit other tracks, or be entirely custom. They can be used to set default values for a certain configuration, like a desktop.

### :material-map: Track layout

A track is structured *exactly* like a `system.yaml`, `repo` and all (yes you must set the `repo`, `impl`, and `track`).

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

!!! warning "Reinheritance"
    If your track inherits a track that inherits another track (reinheritance), issues *may* result, like certain sections of the file being ignored. This is due to an {{ reference("utils", "akshara") }} bug we are still investigating.

### :octicons-repo-16: Creating a track repo/webserver

First, create a repo on your favorite git forge, and put all your track files in the root of it.

!!! tip "If you want to do this quickly, just fork our [track repo](https://github.com/blend-os/tracks){ rel="noopener noreferrer" target="_blank" }!"

Once that is done, you'll need to make your `impl` URL.

!!! abstract "impl URL structures for common git forges"
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
    - `USER`: Your username
    - `REPO`: The repo
    - `BRANCH`: Your branch (usually `main` or `master`)

*[git forge]: A git storage service like GitHub or GitLab

If you're using a webserver, put all the files in one folder. Your `impl` URL is the URL to that folder.

## :material-folder-open: Custom repositories

Custom repositories in `system.yaml` are quite easy.

If we use the [`arch-mact2`](https://mirror.funami.tech/arch-mact2/){ target="_blank" rel="noopener noreferrer" } repo as an example, the repo folder structure is like this:

``` title="mirror.funami.tech"
󰉋 /
└── 󰉋 arch-mact2
    └── 󰉋 os
        └── 󰉋 x86_64
            └── <repo files>
```

We can replace some of these with values.

``` title="mirror.funami.tech"
󰉋 /
└── 󰉋 $repo
    └── 󰉋 os
        └── 󰉋 $arch
            └── <repo files>
```

In `system.yaml`, `$arch` corresponds to your system's architecture (currently `x86_64`) and `$repo` corresponds to your `name` parameter. 

These variables are parsed by pacman, so never remove or change them from your mirror URL. 

Configuring this mirror in system.yaml would look like this:

```yaml title="system.yaml"
package-repos:
  - name: 'arch-mact2'
    repo-url: 'https://mirror.funami.tech/$repo/os/$arch/'
```

Corresponding to this in `pacman.conf`:

```ini title="pacman.conf"
[arch-mact2]
Server = https://mirror.funami.tech/$repo/os/$arch
SigLevel = Never
```