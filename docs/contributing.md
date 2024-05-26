---
icon: material/handshake
description: "Our contribution guide"
---

# :material-handshake: Contributing

## :material-mirror: Mirroring

If you'd like to mirror our package repo and/or ISOs, here's the basics for it.

### :material-chart-bar: Current (ish) stats

- :material-folder-zip: Size: :material-approximately-equal:3 GB (repo and current testing ISO)
- :material-file-multiple: Number of files: 36
- :material-server: Mirrors: 7 (excluding cloud storage services)
- :material-earth-box: Coverage: NA, EU, AU/NZ, KP
- :material-refresh: Rsync: :octicons-x-12:{ .red } (available from other mirrors)

A mirror list is available on the [download](download/README.md) page.

### :material-clipboard-list: Procedure

If you'd like to mirror, great! Here's the steps:

1. Note down your mirror's bandwidth (in Gbps), country, name, and what you'll be serving (ISO-only, repo-only or both)
1. Clone the master package repo mirror via `wget` and grab the latest ISO (or rsync with another mirror)
1. Contact Asterisk via one of our chatrooms (in the footer of this page) to get your mirror listed

??? abstract "`wget` mirroring"
    Otus has provided a cronjob for this:

    ```
    0 * * * * wget --mirror --no-parent --no-host-directories -P $WEB_FOLDER https://pkg-repo.blendos.co/ && find $WEB_FOLDER -type f -name 'index.html*' -delete
    ```

    Where `$WEB_FOLDER` is your web data folder.

    This tells wget to download everything without any parent or domain folders, then we use `find` to remove all the `index.html` files.

    I wish we had `rsync` too, but here we are. :expressionless:

### :material-note: Notes

You will be asked if you'd like to be used as a webseed for the [FOSS Torrents torrent](https://fosstorrents.com/distributions/blendos/){ target="_blank" rel="noopener" }. This is totally up to you.

You will be added to our [status page](https://status.asterisk.lol/status/blendos){ target="_blank" rel="noopener" } and pinged every 60 seconds. Please give us details if we need to ping something specific or if you want notifications.

If you have any questions, just contact us.


*[NA]: North America
*[EU]: European Union
*[AU/NZ]: Australia & New Zealand
*[KP]: Korean Peninsula (South Korea)

## :material-newspaper-variant: Docs

Our docs are powered by [:simple-materialformkdocs: Material for MkDocs](https://squidfunk.github.io/mkdocs-material){ rel="noopener noreferrer" target="_blank" } Community Edition.

### :material-script-text: Rules

If you would like to add to our docs (please do), you should follow these simple rules.

1. **Keep it local.** If you use any external assets, *download them*. Only do not download something if it is dynamic (like a status badge) or there is no other way (like emoji). Static badges, script links pointing to fixed versions, fonts, images, files, download them all. Save them in the right category in the `docs/assets` folder. This is to minimize external requests.
2. **Link code properly.** Any code snippets you add should be snippet links to the original file if applicable. You can pull specific lines or even create sections to do this. Only do not do this if it would be way too cumbersome.
3. **External links should open in a new tab with no referrer.** (unless you have a specific reason not to) Make links like this:
    ```md
    https://google.com{ target="_blank" relk="noopener noreferrer" }
    [link text](https://google.com){ target="_blank" rel="noopener noreferrer" }
    ```
4. **Use frontmatter.** Set an `icon` and `description` for every page (examples can be seen in the source of any page). Include all pages in the `nav` component of `mkdocs.yml` unless there is a reason not to.
5. **Be descriptive.** When writing config and CLI references especially, try to *show, not tell*. A full description of this approach can be seen in the Diátaxis framework: https://diataxis.fr/reference-explanation/{ target="_blank" rel="noopener noreferrer" }
6. **Follow the format.** We have established formats for directory pages and references. Follow them. Headers have icons. References begin with a reference card. Config references need to use code annotations. CLI references should be easy-to-read lists (showing the code like in the `bpkg` reference is optional). Directory pages should use cards to show what users can click on.
7. **Keep it navigateable.** Mobile users should not have to open the hamburger menu to get anywhere on the site from the root (they can still use it to go back or to skip directory pages).
8. **Be semi-casual.** For guides, you may find it better to be less distant from the reader. However, you need to also offer a reliable explanation of steps. You can decide what that looks like. References however, should always be distant (rule 5).
9. **Use the features given to you.** Be expressive! You are writing with one of the most powerful documentation frameworks out there, so *use it!* Don't be afraid to try something new in your writing, style or layout.

*[directory pages]: Pages that show a list of possible paths in a folder, i.e. /install
*[Directory pages]: Pages that show a list of possible paths in a folder, i.e. /install
*[hamburger menu]: Those 3 lines mobile users see in the upper left.

### :octicons-code-16: Development

Local development is quite easy. You'll only need:

- :material-language-python: Python ≥ 3.8
- :material-package-variant: `pip` package manager (included with Python on Windows)

Simply cd in and run (this command only has to be run once):

```bash
pip install -r requirements.txt
```

From there, start the dev server:

```bash
mkdocs serve
```

The server will reload after every save.

If you want to build the website into static HTML, run this command (this isn't required for contribution, the CI/CD server does it automatically):

```bash
mkdocs build
```

### :material-pencil-box: Writing

To learn how to write with Material for MkDocs, consult their [reference](https://squidfunk.github.io/mkdocs-material/reference/){ target="_blank" rel="noopener noreferrer" } and [extension list](https://squidfunk.github.io/mkdocs-material/setup/extensions/){ target="_blank" rel="noopener noreferrer" } to see its special components.

!!! question "Looking for examples?"
    Just click the :material-eye: on any page to view its source code!

!!! note ""
    Images and internal links are created **relative** to the file you're currently editing. Links should link to the markdown file itself, not a path. (e.x. `reference/README.md` `../assets/img/file.png`)

An overview of a few cool features you can use (**:material-star-box: denotes a custom feature**):

#### **:material-exclamation-thick: Admonitions** ([`admonition`](https://python-markdown.github.io/extensions/admonition/){ target="_blank" rel="noopener noreferrer"})
```html
!!! <type> "<title>"
    text

??? note "collapsable"
    text

!!! note inline-end <!-- or inline --> "Inline"
    text

??? abstract follow "󰩳 This one's header will follow you down the page."
    looooong text 
```

In addition to the [regular admonition types](https://squidfunk.github.io/mkdocs-material/reference/admonitions/#supported-types){ target="_blank" rel="noopener noreferrer" }, we have also added a `code` admonition for making collapsable codeblocks:

```md
??? code "󰩳 file_name.ext"     <-- 󰩳 This has follow on by default
    ```
    code here, no space between admonition and code
    ```
```
??? code ":material-star-box: file_name.ext"
    ```
    code here
    ```

As well as a `collapse` admonition:

```md
??? collapse "󰩳 X lines collapsed"    <-- 󰩳 This also has follow on by default
    1

    2
    
    3
```

??? collapse ":material-star-box: X lines collapsed"
    1

    2

    3

And `video`:

```html
??? video "󰩳 Video Guide"
    <center>
    <video src="/assets/vid/example.webm" controls></video>
    <p>You should set a width and height if the video is too big, 
    and muted if it has no sound. 
    This p section can be omitted if no caption is required.<p>
    </center>

```

??? video ":material-star-box: Video Guide"
    <center>
    <video src="/assets/vid/example.webm" controls></video>
    <p>You should set a width and height if the video is too big, and muted if it has no sound.
    This p section can be omitted if no caption is required.<p>
    </center>

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

One thing that is a bit different on these docs vs. other sites is you can use icons :material-star-box: *in codeblocks*. Our codeblocks use a *Nerd Font*, which allows you to use icons within your code.

```
󰩳 I'm an icon!
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

### :material-cog: :material-star-box: Macros

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

### :material-language-css3: :material-star-box: CSS classes

**CSS classes you can use:**

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

:material-star-box: Tables too:

```md
|---------|-----------|
I HATE MARKDOWN TABLES 󰩳 { .someclass } | a |
```

:material-star-box: as well as lists:

```md
1. a 󰩳
{ .someclass }
1. b 󰩳
{ #id }
```

!!! info "Extra features in attr_list"
    We use a fork of `attr_list` to support lists and tables. More info is [here](https://github.com/paulmelis/pm_attr_list){ target="_blank" rel="noopener noreferrer" }.
