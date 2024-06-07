---
icon: material/list-status
description: "Post-install guide for advanced users, or Arch Linux users."
---


# :material-list-status: Arch User Guide

!!! info "This is not just for new users"
    This article describes how you can get around blendOS and summarizes blendOS's core functionality in a concise manner, making it easy to decide if blendOS is for you. (Refer to the table of contents to the right if you're on a computer and the table is visible to you. On mobile, open the hamburger menu, and click the table of contents icon.)

This guide will quickly familiarize you with how you can get around blendOS as a prior Arch Linux user through the terminal (this guide is also quite handy if you're a semi-experienced user of other Linux distributions).

## :material-file: Default [`system.yaml`](../../reference/configs/system.md)

Begin by opening the [:material-file-star: `system.yaml`](../../reference/configs/system.md) file (at the / of your main partition).

```bash
sudo nano /system.yaml
```

You should be greeted by a file with contents similar to the following (there might be a few differences here and there, of course):

```yaml
impl: https://github.com/blend-os/tracks/raw/main
repo: https://pkg-repo.blendos.co
track: default-gnome
```

If you're on a computer with an NVIDIA GPU, you may also see the following lines towards the end of the file:

```yaml
packages:
    - 'nvidia-dkms'
```

Wondering where they came from? These lines were appended automatically to the end of the [:material-file-star: `system.yaml`](../../reference/configs/system.md) as part of the installation process, as the installer detected the presence of an NVIDIA GPU and chose to install the latest proprietary driver for NVIDIA GPUs.

## :material-package: Arch Linux packages

That brings us to how you can install other Arch Linux packages. Edit the [:material-file-star: `system.yaml`](../../reference/configs/system.md) file to look like the following:

```yaml
impl: https://github.com/blend-os/tracks/raw/main
repo: https://pkg-repo.blendos.co
track: default-gnome

packages:
    - 'chromium'
    # if you're on a system with an NVIDA GPU, keep the 'nvidia-dkms' package unless you'd like to remove the proprietary NVIDIA driver
```

!!! warning "Use spaces for indentation in `system.yaml`!"
    The YAML format doesn't allow tabs, and only spaces are allowed for indentation. It is also worth noting that like Python, indentation is mandatory, and is integral to parsing.

Now run `sudo akshara update`, and reboot your computer once it completes. On the next boot, you should find the Chromium browser installed on your computer, as an Arch Linux package. You can even add a desktop environment (useful with the {{ track("blendos-base") }} track or kernel (required with the `custom` track) under the `packages` section.

## :material-arrow-up-bold-hexagon-outline: Updating your computer

It is advised that you run `sudo akshara update` every few days to keep your system in sync with the Arch Linux repositories and AUR. Of course, you also have to run `sudo akshara update` every time you modify [:material-file-star: `system.yaml`](../../reference/configs/system.md) for your system to reflect any changes in that file. The System application on blendOS also presents an option to 'update your system' (which runs `sudo akshara update`) under the System tab, if you prefer a UI.

## :material-arch: AUR packages

To install packages from the AUR, create an `aur-packages` section in [:material-file-star: `system.yaml`](../../reference/configs/system.md) and list any AUR packages you would like to have on your computer underneath it, as follows:

```yaml
aur-packages:
    - 'visual-studio-code-bin'
```

The above example adds the VS Code AUR package to your. Of course, you'd have to run `sudo akshara update` and reboot to find Visual Studio Code on your computer.

## :material-train: Switching to other desktop environments or a clean Arch-like system (tracks)

```yaml
track: default-gnome
```

This line in [:material-file-star: `system.yaml`](../../reference/configs/system.md) defines the track used by your system, and you can simply change it to use a different desktop environment, or use the {{ track("blendos-base") }} track to not have a desktop environment. Here are the tracks offered by the blendOS team:

* {{ track("blendos-base") }}: track without a desktop environment; suitable for headless use or use with custom DEs (use the `nmtui` command to connect to a wireless network)
* {{ track("default-gnome") }}: variant of the {{ track("gnome") }} track with certain changes suitable for a new user, default track
* {{ track("gnome") }}: variant of the {{ track("blendos-base") }} track with GNOME
* {{ track("plasma") }}: variant of the {{ track("blendos-base") }} track with KDE Plasma 6
* {{ track("mate") }}: variant of the {{ track("blendos-base") }} track with MATE
* {{ track("xfce") }}: variant of the {{ track("blendos-base") }} track with XFCE
* {{ track("cinnamon") }}: variant of the {{ track("blendos-base") }} track with Cinnamon
* {{ track("lxqt") }}: variant of the {{ track("blendos-base") }} track with LXQt

!!! danger "Always include `linux` or another kernel package and `networkmanager` if using the `custom` track!"
    The `custom` track does **not** include a kernel out-of-the-box, so you must add a kernel like `linux` or `linux-zen` to the `packages` (or `aur-packages`) list. It is also highly advised that you include the `networkmanager` package (or equivalent) for more straightforward internet access (`nmtui` for connecting to wireless networks).

* `custom`: includes no packages, so you must include a kernel like `linux` or `linux-zen`, and for network access, you **must** include the `networkmanager` package, or another similar package; this track is only for experienced Arch Linux users, {{ track("blendos-base") }} is often sufficiently low-level.

## :octicons-container-16: Containers (apps from other distros)

Now, you might want to install applications from other distributions like Ubuntu or Fedora, usually if they're not available in the Arch repositories or as Flatpaks. You can do so through containers. Container management is also available through the System app, but we will be using the `user` CLI utility in this guide. Initializing Android app support will not be discussed here either, as it is primarily for GUI (Wayland) users and can easily be initialized through the System app.

### :material-truck-cargo-container: Container management

#### :material-train-car-container: Supported container types

--8<-- "docs/reference/container-list/v4.md"

#### :octicons-package-16: Creating containers

Here's how you can create a Debian (`debian`, as shown in the above table) container named `my-first-container`.

```bash
user create-container my-first-container debian
```

After its creation is complete, you'll find that all of its binaries will be available on the host with the suffix .my-first-container. For example:

* **apt** in the container -> **apt.my-first-container** on the host
* **dpkg** in the container -> **dpkg.my-first-container** on the host
* **bash** in the container -> **bash.my-first-container** on the host

!!! warning "Containers cannot be renamed."
    `blend` does not currently support renaming containers, so if you'd like to continue using this container, it is advised you name it something more precise than `my-first-container`.

#### :octicons-package-dependencies-16: Removing containers

Just run:

```bash
user remove-container my-first-container
```

#### :octicons-package-dependents-16: Entering containers

There are multiple ways in which you can enter a container. The first one is to use user to enter a container, as shown below (terminal window on the host):

```bash
user enter my-first-container
```

The second, less common one, would be to run `bash.my-first-container` in a regular shell.

### :octicons-arrow-switch-16: Associations

#### :material-plus: Creating associations

Getting tired of running apt.my-first-container all the time? You can shorten it to apt by simply running the command below (in a terminal window on the host):

```bash
user associate apt my-first-container
```

You can now install a package with `sudo apt install [pkg]` from a regular shell.

#### :material-minus: Deleting associations

Just run:

```bash
user dissociate apt
```

### :material-package-variant-closed: Packages

#### :material-package-variant-plus: Installing packages

Aside from entering a shell, calling the container's package manager, or using associations, you can also simply use `user` to install packages within a container:

```bash
user install my-first-container hello # 'hello' is the name of the package
```

#### :material-package-variant-closed-minus: Removing packages

Similarly, you can also remove packages with `user`:

```bash
user remove my-first-container hello
```


This is all you need to know to get around blendOS using the command-line, and you should not have any trouble managing your system now. Feel free to join our [Discord server](https://discord.gg/fvMpV8ZNxD){ target="_blank" relk="noopener noreferrer" } if you need help or encounter any bugs though!
