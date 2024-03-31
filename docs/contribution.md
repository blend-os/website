---
icon: material/handshake
description: "Our contribution guide"
---

# :material-handshake: Contributing

## :material-newspaper-variant: Docs

Our docs are powered by [:simple-materialformkdocs: Material for MkDocs](https://squidfunk.github.io/mkdocs-material){ rel="noopener noreferrer" target="_blank" } Community Edition.

### :material-script-text: Rules

If you would like to add to our docs (please do), you should follow these simple rules.

1. **Keep it local.** If you use any external assets, *download them*. Only do not download something if it is dynamic (like a status badge) or there is no other way (i.e. emoji). Static badges, script links pointing to fixed versions, fonts, images, files, download them all. Save them in the right category in the `docs/assets` folder. This is to minimize external requests. 
2. **Use frontmatter.** Set an `icon` and `description` for every page (examples can be seen in the source of any page). Include all pages in the `nav` component of `mkdocs.yml` unless there is a reason not to.
3. **Be descriptive.** When writing config and CLI references especially, try to *show, not tell*. A full description of this approach can be seen in the Diátaxis framework: https://diataxis.fr/reference-explanation/
4. **Follow the format.** We have established formats for directory pages and references. Follow them. References begin with a reference card. Config references need to use code annotations. CLI references should be easy-to-read lists (showing the code like in the `bpkg` reference is optional). Directory pages should use cards to show what users can click on.
5. **Keep it navigateable.** Mobile users should not have to open the hamburger menu to get anywhere on the site from the root (they can still use it to go back or to skip directory pages).
6. **Be semi-casual.** For guides, you may find it better to be less distant from the reader. However, you need to also offer a reliable explanation of steps. References however, should always be distant (rule 3).
7. **Use the features given to you.** Be expressive! You are writing with the most powerful documentation framework out there, so *use it!* Don't be afraid to try something new.

*[directory pages]: Pages that show a list of possible paths in a folder, i.e. /install
*[Directory pages]: Pages that show a list of possible paths in a folder, i.e. /install
*[hamburger menu]: Those 3 lines mobile users see in the upper left.

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

#### **:material-exclamation-thick: Admonitions** ([`admonition`](https://python-markdown.github.io/extensions/admonition/){ target="_blank" rel="noopener noreferrer"})
```html
!!! <type> "<title>"
    text

??? note "collapsable"
    text

!!! note inline-end <!-- or inline --> "Inline"
    text
```

In addition to the [regular admonition types](https://squidfunk.github.io/mkdocs-material/reference/admonitions/#supported-types){ target="_blank" rel="noopener noreferrer" }, we have also added a `code` admonition for making collapsable codeblocks:

```md
??? code "file_name.ext"
    ```
    code here, no space between admonition and code
    ```
```
??? code "file_name.ext"
    ```
    code here
    ```
#### **:material-emoticon: Emojis/Icons** ([`emoji`](https://facelessuser.github.io/pymdown-extensions/extensions/emoji/){ target="_blank" rel="noopener noreferrer" })

Call them via their shortcode:
```
:lobster:
```
:lobster:

Call icons the same way:

```
:material-home:
```
:material-home:

One thing that is a bit different on these docs vs. other sites is you can use icons *in codeblocks*. Our codeblocks use a *Nerd Font*, which allows you to use icons within your code.

```
󰋜 I'm an icon!
```

Visit the cheatsheet: https://www.nerdfonts.com/cheat-sheet{ target="_blank" rel="noopener noreferrer" }

Find the icon you want and hover over it. In the copy section, hit `Icon`. Your editor will probably not be able to render the icon as it is not using a Nerd Font. Rest assured, it will render in your preview.

#### **:material-language-css3: CSS in Markdown** ([`attr_list`](https://python-markdown.github.io/extensions/attr_list/){ target="_blank" rel="noopener noreferrer" } & [`pm_attr_list`](https://github.com/paulmelis/pm_attr_list){ target="_blank" rel="noopener noreferrer" })
```md
[link](url){ option=value .class #id }
```
#### **:material-language-html5: Markdown in HTML** ([`md_in_html`](https://python-markdown.github.io/extensions/md_in_html/){ target="_blank" rel="noopener noreferrer" })
```html
<div markdown>
  **Markdown works** __just fine!__{ .someclass }
</div>
```

#### **:fontawesome-solid-scissors: Code Snippets** ([`snippets`](https://facelessuser.github.io/pymdown-extensions/extensions/snippets/){ target="_blank" rel="noopener noreferrer" })
!!! info "File paths are relative to the repo root."

```md
;--8<-- "link_or_file.ext"
```
```md
  ```
  ;--8<-- "link_or_file.ext"
  ```
```

We use this to make reusable Markdown snippets, and pull the latest version of a code file.

#### **:material-keyboard: Keybinds** ([`keys`](https://facelessuser.github.io/pymdown-extensions/extensions/keys/){ target="_blank" rel="noopener noreferrer" })

```md
++ctrl+alt+delete++
```
renders to: 

++ctrl+alt+delete++
#### **:octicons-link-16: Automatic Links** ([`magiclink`](https://facelessuser.github.io/pymdown-extensions/extensions/magiclink/){ target="_blank" rel="noopener noreferer" })

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
    See the full [reference](https://squidfunk.github.io/mkdocs-material/reference/){ target="_blank" rel="noopener noreferrer" } and [extension list](https://squidfunk.github.io/mkdocs-material/setup/extensions/){ target="_blank" rel="noopener noreferrer" } for more cool features.

### :material-cog: Macros

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

### :material-language-css3: CSS classes

CSS classes you can use:

!!! note "`.small` is depreceated, please use `<small>`"

```css title="extra.css"
--8<-- "https://git.blendos.co/asterisk/blend-docs-material/-/raw/main/docs/assets/css/extra.css:classes"
```

You can apply CSS to a whole block like this:

```md
some text
{ .class }
```

to icons:

```md
:material-cog:{ .yellow }
```

or even to bits of text:

```html
Hi this text is <span class="yellow">**yellow**</span> but this text is normal!
```

Tables too:

```md
|---------|-----------|
I HATE MARKDOWN TABLES { .someclass } | a |
```

as well as lists:

```md
1. a
{ .someclass }
1. b
{ #id }
```

!!! abstract "Extra features in attr_list"
    We use a fork of `attr_list` to support lists and tables. More info is [here](https://github.com/paulmelis/pm_attr_list){ target="_blank" rel="noopener noreferrer" }.