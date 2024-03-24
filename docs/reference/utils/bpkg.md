---
icon: material/package-variant-closed
description: "Reference for bpkg"
---

<div class="grid cards" markdown>

-   # :material-package-variant-closed: bpkg ![v3 badge](https://img.shields.io/badge/v3-red) ![v4 badge](https://img.shields.io/badge/v4-green)
    -------

    <em>Our universal package manager.</em>

    - Language: :misc-python:{ title=Python }
    - Size: unknown, waiting for gitlab to come back online.
    - GUI: :octicons-x-12:{ .red title="No" }

    --------
    ```title="Config file location"
    󱂵 ~
    └── 󰉋 .config
        └── 󰈮 bpkg.yaml
    ```

    ------

    [:material-download: Download](https://git.blendos.co/blendOS/bpkg/-/archive/main/bpkg-main.tar.gz){ .md-button target="_blank" rel="noopener noreferrer" } [:octicons-code-16: Source Code](https://git.blendos.co/blendos/bpkg){ .md-button target="_blank" rel="noopener noreferrer" }

</div>
??? question "What is bpkg?"
    `bpkg` is our package management utility that allows you to use the package managers of all your containers. This allows you to quickly install packages from any repo.

## :material-package-variant-plus: Installation

Unzip the file into any folder (open it with your archive manager), then open your terminal.

`cd` to the folder you extracted it to, then do `#!bash chmod +x install.sh && ./install.sh`.

## :material-file-cog: Configuration

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

## :material-clipboard-text: Reference

### :material-file-code: `bpkg.yaml`

`bpkg` will generate a config file at first run.

!!! warning ""
    The config file will need to be updated every time you add or delete a container by running `#!bash bpkg overwrite-config` in your terminal.

Its contents will look something like this based on your containers:

??? abstract "Obtaining the container list"
    The container list is obtained by using the following commands:

    ```bash
    podman ps -a --no-trunc --size --format '{{.Names}}'
    ```
    ```bash
    podman ps -a --no-trunc --size --format '{{.Image}}'
    ```

    The YAML code is generated from the output.

--8<-- "docs/reference/utils/files/bpkg.yaml.md"

### :octicons-terminal-16: CLI Usage

!!! note ""
    `<>` denotes a required parameter, `[]` denotes an optional one.

    !!! example ""
        **Example:** `[-c <container>]`. The `-c` argument is optional, but if you choose to use it `<container>` is required.

#### :material-package-variant-plus: Install a package
```bash
bpkg install <package> [-c <container>]
```
This will search for the package in your installed distros and install it from the first package manager it finds by your order of preference, though you can specify a specific container.
#### :material-package-variant-remove: Remove a package
```bash
bpkg remove <package> [-c <container>]
```
This will remove a package that you installed from a container of your choice or from the first container in your list the package is found in.
#### :material-package-down: Update packages
```bash
bpkg update [-c <container>]
```
This will update all the packages in all your containers, or you can specify a specific one. If update_flatpak is set to true in the config, this will also update your flatpaks.
#### :octicons-search-16: Package Search
```bash
bpkg search <package> [-c <container>]
```
You can search for a package in all of your containers, or specify a specific one.
#### :material-clipboard-text: Container list
```bash
bpkg list-containers
```
Lists all containers on your system (even if they aren't in the config).
#### :material-refresh: Config Regeneration
```bash
bpkg overwrite-config
```
This will pull all your containers and generate a new config file, overwriting your current one. It is recommended to run this after creating or deleting containers.



## :octicons-container-24: Container URL List

### v3

--8<-- "docs/reference/container-list/v3.md"

### v4 ![testing badge](https://img.shields.io/badge/testing-#237c4dff)

--8<-- "docs/reference/container-list/v4.md"
