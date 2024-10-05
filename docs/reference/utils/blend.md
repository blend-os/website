---
icon: material/blender
description: The container backend
---

<div class="grid cards" markdown>

-   # :material-blender: <span class="notranslate">blend</span> ![v4 badge](../../assets/img/v4.svg){ .off-glb }
    -------

    <em>The container backend.</em>

    !!! danger
        This tool **is not** meant to be used directly, but rather through **System** (blendOS settings) and `user`.

        Only use it for debugging or scripting, and if you know what you're doing.

    - Language: :misc-python:{ title=Python }
    - Size::material-approximately-equal:19.2 KB
    - GUI: :octicons-check-16:{ .green title="Yes, blend-settings" }
    - Comes with blendOS: :octicons-check-16:{ .green title="Yes" }

    ------
    [:octicons-code-16: Source Code](https://github.com/blend-os/blend){ .md-button target="_blank" rel="noopener noreferrer" }

</div>

!!! question "What is `blend`?"
    `blend` is the backend that performs a multitude of tasks, from creating and managing containers, to handling how they appear in your host shell, to making app entries for container apps.

    It is built on top of [Podman](https://podman.io){ target="_blank" rel="noopener noreferrer" } with some code from Distrobox for NVIDIA support.

## :material-clipboard-text: Reference

The table of distributions is below:

--8<-- "docs/reference/container-list/v4.md"

## :octicons-terminal-16: CLI

!!! warning
    This app cannot be run as root.

### :material-flag: Global flags

| Flag   | Description |
| -------- | ------- |
| `-y`/`--noconfirm` | Skip confirmation (in the container too) |
| `-v`/`--version`  | Print the version number |
| `-h`/`--help` | Print the (useless) help screen |

Some other flags are command-specific.

!!! note
    There are other undocumented functions not listed in the command map, which can't be used, and commands referenced in info statements that don't exist.

### :material-arrow-right-box: Enter a container

```sh
blend enter -cn <CONTAINER NAME>
```
Same as `user enter`.

### :material-cog-box: Run a command in a container

```sh
blend exec -cn <CONTAINER NAME> <command>
```
Runs the specified command in the specified container.

### :material-plus-box: Create a container

```sh
blend create-container -cn <name> -d <distro>
```
Creates a container with the specified distro.

### :material-minus-box: Remove a container

```sh
blend remove-container -cn <CONTAINER_NAME>
```
Removes the specified container.

### :material-clipboard-list: List all containers

```sh
blend list-containers
```
Prints the container list to the terminal.

### :material-play-box: Start all containers

```sh
blend start-containers
```
Starts all installed containers.

### :octicons-sync-16: Update containers

```sh
blend sync -cn <CONTAINER_NAME> -d <DISTRO> 
```
Updates all packages in the container.


