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

    To edit the file, just open it in your favorite text editor (<span class="warning">:fontawesome-solid-exclamation:You will need root privileges</span>).

</div>

## :material-clipboard-text: Reference

!!! note ""
    **Any options marked with a :material-cog-box: next to their name in the expanded view can be set by a track.**

!!! info ""
    More info on the possible values of these options is given in the next section.

--8<-- "docs/reference/configs/files/system.yaml.md"

## :material-train: Tracks

!!! danger "Always use the `.yaml` extension when creating track files!"

Tracks are like mini `system.yaml` files that you can create. They can inherit other tracks, or be entirely custom. They can be used to set default values for a certain configuration, like a desktop.

### :material-map: Track layout

A track is structured *exactly* like a `system.yaml`, minus the `repo` bit (or other bits depending on inheritance).

As an example of a custom track, let's look at the official {{ track("blendos-base") }} track:

??? code "blendos-base.yaml"
    ```yaml
    --8<-- "https://github.com/blend-os/tracks/raw/main/blendos-base.yaml"
    ```

Here, the `track` value is set to `custom`, indicating a fully custom track. This track is setting default values for whomever uses it.

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

### :octicons-repo-16: Creating a track repo/webserver

## :material-folder-open: Custom repositories

