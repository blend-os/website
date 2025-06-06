---
icon: material/package-variant-closed
description: "Reference for bpkg"
---

<div class="grid cards" markdown>

-   # :material-package-variant-closed: bpkg ![v3 badge](../../assets/img/v3.svg){ .off-glb } ![v4 badge](../../assets/img/v4.svg){ .off-glb }
    -------

    <em>Our universal package manager.</em>

    - Language: :misc-python:{ title=Python }
    - Size::material-approximately-equal:27.63 KB
    - GUI: :octicons-x-12:{ .red title="No" }
    - Comes with blendOS: :octicons-x-12:{ .red title="No" }

    --------
    ```title="Config file location"
    📁 ~
    └── 📁 .config
        └── ⭐ bpkg.yaml
    ```

    ------

    [:material-download: Download](https://git.blendos.co/blendOS/bpkg/-/archive/main/bpkg-main.tar.gz){ .md-button target="_blank" rel="noopener noreferrer" } [:octicons-code-16: Source Code](https://git.blendos.co/blendos/bpkg){ .md-button target="_blank" rel="noopener noreferrer" }

</div>
!!! question "What is bpkg?"
    `bpkg` is our package management utility that allows you to use the package managers of all your containers. This allows you to quickly install packages from any repo.

## :material-package-variant-closed-plus: Installation

Unzip the file into any folder (open it with your archive manager), then open your terminal.

`cd` to the folder you extracted it to, then do `#!bash chmod +x install.sh && ./install.sh`.

## :material-clipboard-text: Reference

### :material-file-code: `bpkg.yaml`

`bpkg` will generate a config file at first run.

!!! warning ""
    The config file will need to be updated every time you add or delete a container by running `#!bash bpkg overwrite-config` in your terminal.

Its contents will look something like this based on your containers:

??? abstract "Obtaining the container list"
    The container list is obtained by using the following commands:
    {% raw %}
    ```bash
    podman ps -a --no-trunc --size --format '{{.Names}}'
    ```
    ```bash
    podman ps -a --no-trunc --size --format '{{.Image}}'
    ```
    {% endraw %}
    The YAML code is generated from the output.

--8<-- "docs/reference/utils/files/bpkg.yaml.md"

## :material-file-cog: Configuration

!!! warning "Changes made here will be overwritten whenever you run `bpkg overwrite-config`!"

### Changing Priority

**To change the priority, change the order of the entries.** In the [reference file](#reference), the Arch container will be checked first, followed by Ubuntu 22.04, Fedora 38, etc.

If we change the config file so it starts like this:

```yaml
containers:
  - name: ub
    distro: ubuntu-22.04
  - name: ar
    distro: arch
...
```

then the Ubuntu 22.04 container will be checked first.

### Excluding Containers

To exclude a container from `bpkg`, remove it from the config.

If we remove Arch so the config file looks like this:

```yaml
containers:
  - name: ub
    distro: ubuntu-22.04
  - name: fe
    distro: fedora-38
...
```

then the Arch container will not be used by `bpkg`.

## :octicons-terminal-16: CLI

#### :fontawesome-solid-question: Help Page

```bash
bpkg
```

Shows a help page.

#### :material-package-variant-plus: Install a package

```bash
bpkg install <package>
```

This will search for the package in your installed distros and install it from the first package manager it finds by your order of preference in [`bpkg.yaml`](#bpkgyaml). Use `user install <container> <package>` to install to a specific container.

#### :material-package-variant-remove: Remove a package

```bash
bpkg remove <package>
```

This will remove a package from the first container in [`bpkg.yaml`](#bpkgyaml) the package is found in. Use `user remove <container> <package>` to remove from a specific container.

#### :material-package-down: Update packages

```bash
bpkg update
```

This will update all the packages in all your containers. If `update_flatpak` is set to <span class="green">true</span> in the config, this will also update your Flatpaks.

#### :octicons-search-16: Package Search

```bash
bpkg search <package>
```

You can search for a package in all of your containers.


#### :material-clipboard-list: Container list

```bash
bpkg list-containers
```

Lists all containers on your system (even if they aren't in the config).

#### :material-refresh: Config Regeneration

!!! tip "Run this after creating or deleting containers to ensure your config file is always up-to-date!"

```bash
bpkg overwrite-config
```

This will pull all your containers and generate a new config file, overwriting your current one.

{{ inlinealert("red", ":material-lightning-bolt:", "Danger", "YOU WILL LOSE ALL YOUR CHANGES!" ) }}

## :octicons-container-24: Container List

You can view the container list here:

[View Container List :octicons-arrow-right-16:](../container-list.md){ .md-button }
