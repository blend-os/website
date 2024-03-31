---
icon: material/handshake
description: "Our contribution guide"
---

# :material-handshake: Contributing

## :material-newspaper-variant: Docs

Our docs are powered by [:simple-materialformkdocs: Material for MkDocs](https://squidfunk.github.io/mkdocs-material){ rel="noopener noreferrer" target="_blank" } Community Edition.

### :octicons-code-16: Development

Local development is quite easy. You'll only need:

- :material-language-python: Python 3.9+

Simply cd in and run:

```bash
pip install -r requirements.txt
```

From there, start the dev server:

```bash
mkdocs serve
```

The server will reload after every save.

### :material-pencil-box: Writing

To learn how to write with Material for MkDocs, consult their [reference](https://squidfunk.github.io/mkdocs-material/reference/){ target="_blank" rel="noopener noreferrer" } and [extension list](https://squidfunk.github.io/mkdocs-material/setup/extensions/){ target="_blank" rel="noopener noreferrer" } to see its special components.

!!! question "Looking for examples?"
    Just click the :material-eye: on any page to view its source code!

An overview of a few cool features you can use:

### **:material-language-css3: CSS in Markdown** ([`attr_list`](https://python-markdown.github.io/extensions/attr_list/){ target="_blank" rel="noopener noreferrer" })
  ```md
  [link](url){ option=value .class #id }
  ```
### **:material-language-html5: Markdown in HTML** ([`md_in_html`](https://python-markdown.github.io/extensions/md_in_html/){ target="_blank" rel="noopener noreferrer" })
```html
<div markdown>
  **Markdown works** __just fine!__{ .someclass }
</div>
```

### **:fontawesome-solid-scissors: Code Snippets** ([`snippets`](https://facelessuser.github.io/pymdown-extensions/extensions/snippets/){ target="_blank" rel="noopener noreferrer" })
!!! info "File paths are relative to the repo root."

```md
;--8<-- "link_or_file.ext"
```

We use this to make reusable Markdown snippets, and pull the latest version of a code file.

### **:material-keyboard: Keybinds** ([`keys`](https://facelessuser.github.io/pymdown-extensions/extensions/keys/){ target="_blank" rel="noopener noreferrer" })

```md
++ctrl+alt+delete++
```
renders to: 

++ctrl+alt+delete++
### **:octicons-link-16: Automatic Links** ([`magiclink`](https://facelessuser.github.io/pymdown-extensions/extensions/magiclink/){ target="_blank" rel="noopener noreferer" })

```md
https://google.com
```
renders to: https://google.com

It also works for Github/Gitlab/Bitbucket links too!

**Legend:** `!` = PR `#` = Issue `?` = discussion `...` = Compare

```md
MagicLink supports shorthand references for GitHub, GitLab, and Bitbucket issues (#1), pull/merge requests (!100), GitHub Discussion 
(https://github.com/facelessuser/pymdown-extensions/discussions/1173), commits (23bb7083b4699703241d7552ff666cf8cef61337), and compares 
(23bb7083b4699703241d7552ff666cf8cef61337...0abca9679ec09ca289c345cc8843497fc0f8be9b). You can also reference repositories (https://
github.com/facelessuser/pymdown-extensions) and users (@facelessuser). Mentions also works for social media (only Twitter is supported 
at this time).
```

> MagicLink supports shorthand references for GitHub, GitLab, and Bitbucket issues (#1), pull/merge requests (!100), GitHub Discussion (https://github.com/facelessuser/pymdown-extensions/discussions/1173), commits (23bb7083b4699703241d7552ff666cf8cef61337), and compares (23bb7083b4699703241d7552ff666cf8cef61337...0abca9679ec09ca289c345cc8843497fc0f8be9b). You can also reference repositories (https://github.com/facelessuser/pymdown-extensions) and users (@facelessuser). Mentions also works for social media (only Twitter is supported at this time).

If you do not specify a repo, the default repo will be used (here, it's https://github.com/blend-os/blendos).

You can also specify links to our git server:

!!! note "Gitlab subgroups do not work."

```md
@blendgit:asterisk
@blendgit:blendos/docs
```
@blendgit:asterisk

@blendgit:blendos/docs

!!! tip "There's a lot more!"
    See the full [reference](https://squidfunk.github.io/mkdocs-material/reference/){ target="_blank" rel="noopener noreferrer" } and [extension list](https://squidfunk.github.io/mkdocs-material/setup/extensions/){ target="_blank" rel="noopener noreferrer" } for more.

## :material-cog: Macros

We have set up [`mkdocs-macros`](https://mkdocs-macros-plugin.readthedocs.io/en/latest/) to turn MkDocs into more of a wiki engine.

We have created the following macros:

**Package links (v4 containers only)**

{% raw %}

```md
{{ aur("aur-package") }}
```
{% endraw %}

{{aur ("vesktop-bin") }}

{% raw %}

```md
{{ archpkg("some-package") }}
```
{% endraw %}

{{ archpkg("linux-zen") }}

{% raw %}
```md
{{ ubpkg("some-ubuntu-thing") }}
```
{% endraw %}

{{ ubpkg("software-properties-common") }}

{% raw %}
```md
{{ debpkg("some-debian-thing") }}
```
{% endraw %}

{{ debpkg("apt-transport-https") }}

{% raw %}
```md
{{ fedorapkg("some-fedora-thing") }}
```
{% endraw %}

{{ fedorapkg("dnf-utils") }}

**URL schemas**

{% raw %}
```md
{{ track("track-from-our-repo-without-extension") }}
```
{% endraw %}

{{ track("lxqt") }}

{% raw %}
```md
{{ custom_track("your-impl-url", "your-track-name-without-extension") }}
```
{% endraw %}

{{ custom_track("https://github.com/noahimesaka1873/blendos-tracks-t2/raw/main", "blendos-base-t2") }}

{% raw %}
```md
{{ reference("folder", "page") }}
```
{% endraw %}

{{ reference("utils", "bpkg") }}

## :material-language-css3: CSS classes

CSS classes you can use:

```css
--8<-- "https://git.blendos.co/asterisk/blend-docs-material/-/raw/main/docs/assets/css/extra.css:classes"
```