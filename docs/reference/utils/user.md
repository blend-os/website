---
icon: material/cog-box
description: "Reference for our installer"
---

<div class="grid cards" markdown>

-   # :material-cog-box: user ![v4 badge](../../assets/img/v4.svg){ .off-glb }
    -------

    <em>A container management CLI utility.</em>

    - Language: :misc-python:{ title=Python }
    - Size::material-approximately-equal:27 KB (part of `blend`)
    - GUI: :octicons-x-12:{ .red title="No" }
    - Comes with blendOS: :octicons-check-16:{ .green title="yes" }

    ------

    [:octicons-code-16: Source Code](https://github.com/blend-os/blend-inst){ .md-button target="_blank" rel="noopener noreferrer" }

</div>

!!! question "What is blend-inst?"
    [`user`](https://github.com/blend-os/blend/blob/main/user){ target="_blank" rel="noopener noreferrer" } is a part of [blend](https://github.com/blend-os/blend){ target="_blank" rel="noopener noreferrer" } in Python. It allows for container management through the command-line, a use-case that had not been considered prior to v3.

## :octicons-terminal-16: CLI usage

### :material-truck-cargo-container: Create a container

```bash
user create-container <CONTAINERNAME> <CONTAINERTYPE>
```
Creates a container of the selected container type.

### :material-delete: Remove a container

```bash
user remove-container <CONTAINERNAME>
```
Removes a container.

### :material-link: Create an association

```bash
user associate <BINARYNAME> <CONTAINERNAME>
```
Creates an association so that commonly-used binaries can be called without a suffix.

### :material-link: Delete an association

```bash
user dissociate <BINARYNAME>
```
Deletes an existing association.

### :material-package-variant-plus: Install a package

```bash
user install <CONTAINERNAME> <PKG1> [PKG2 PKG3 PKGs...]
```
Installs (a) package(s) to the selected container.

### :material-package-variant-remove: Remove a package

```bash
user remove <CONTAINERNAME> <PKG1> [PKG1 PKG2 PKGs...]
```

Removes (a) package(s) from the selected container.
