---
icon: material/home
description: "blendOS home page"
title: "Home"
glightbox: false
hide:
  - toc
---

<style>
  .md-content__button {
    display: none;
  }

  #blendos-logo {
    margin-bottom: 0;
  }

  #blendos-title .headerlink {
    display: none;
  }

  .built-with-footer {
    display: none;
  }
</style>

<div align="center" markdown>

![logo](assets/img/logo.svg){ #blendos-logo width=100 }

<h1 style="margin-bottom: 0.2em;" id="blendos-title" class="notranslate">blendOS</h1>

--------

<em>**Arch Linux made declarative, immutable and atomic. With Android app support and Fedora, Debian, CentOS Stream and Ubuntu containers available, as well as system packages/DEs/kernels from Arch Linux and the AUR.**</em>

![screenshot](assets/img/blendOS-v4-screenshot.png){ width=650 }

<the-fold></the-fold>

<!-- 
<figure markdown="span">
  ![hero](assets/img/hero.png){ width="720" }
  <figcaption></figcaption>
</figure>
-->

<!-- <em>**Beautiful.** **Efficient.** **Elegant.**</em> -->


[:material-hammer-wrench: Install blendOS](install/README.md){ .md-button .mt-1 .notranslate data-umami-event="Install Button" } [:material-cog: Intro to blendOS](install/post-install/intro.md){ .md-button .mt-1 .notranslate data-umami-event="Introduction for Arch users" }
[:material-newspaper: Blog](blog/index.md){ .md-button .mt-1 data-umami-event="Blog button" }
[:material-book-open-variant: Guides](guides/README.md){ .md-button .mt-1 data-umami-event="Guides Button"}
<br><br>[:fontawesome-brands-discord: Discord](https://discord.gg/fvMpV8ZNxD){ .md-button .notranslate target="_blank" rel="noopener noreferrer" } [:fontawesome-brands-telegram: Telegram](https://t.me/blendos){ .md-button .notranslate target="_blank" rel="noopener noreferrer" } [:simple-matrix: Matrix](https://matrix.to/#/#blendos:matrix.org){ .md-button .notranslate target="_blank" rel="noopener noreferrer" } [:material-forum: AnswerOverflow](https://www.answeroverflow.com/c/1068192254365282405){ .notranslate .md-button target="_blank" rel="noopener noreferrer" } [:fontawesome-solid-ellipsis-vertical: Other Socials](#footer){ .md-button }

------
</div>

<div align="center" markdown>

<div class="grid cards" markdown>

-   :material-file-code:{ .lg .middle } __Declarative__

    ---

    blendOS v4 is fully declarative, allowing you to use [custom packages, kernels, drivers and desktop environments](reference/configs/system.md) on a minimal, [deployable](reference/configs/system.md#tracks), atomic Arch Linux base system.

-   :material-arrow-up-bold-hexagon-outline:{ .lg .middle } __Atomic__

    ---

    Unlike most other operating systems, blendOS ensures your system does not end up in a half-broken state by [replacing](reference/nerdy-stuff/atomicity.md) your old root filesystem with a new one cleanly.

-   :material-puzzle:{ .lg .middle } __Extensible__

    ---

    blendOS offers support for applications and binaries from [several distributions](reference/container-list.md) and Android, without the fear of breaking your system through the use of `podman` containers.

-   :material-account:{ .lg .middle } __Friendly__

    ---

    Thanks to its [**immutable nature**](reference/nerdy-stuff/immutability.md), blendOS prevents you from wrecking your system if you were to try to delete system directories, and makes troubleshooting issues intuitive for any user.


</div>

------

<em>**Flatpak** applications are supported out-of-the-box, and so are Arch Linux & AUR packages through the `/system.yaml` file. Support for applications from **Android**, **Fedora**, **Ubuntu**, **Debian** and [more](reference/container-list.md) can be enabled through the System app on blendOS.</em>
</div>

<!-- <b><h2>Written by:</h2></b> -->

---------

###### Footer { style="visibility: hidden;width: 0; height: 0;" }
