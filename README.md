# Blend Docs Material

New BlendOS docs (WIP). Built with Material for MkDocs.

Please read the [contribution guide](https://blend-docs-material.pages.dev/contributing#docs) for information on additional features, classes and macros.

# Table of Contents

1. [Rules](#rules)
2. [Local Development](#local-development)
3. [Credit](#credit)

# Rules

1. **Keep it local.** If you use any external assets, *download them*. Only do not download something if it is dynamic (like a status badge) or there is no other way (like emoji). Static badges, script links pointing to fixed versions, fonts, images, files, download them all. Save them in the right category in the `docs/assets` folder. This is to minimize external requests.
2. **Link code properly.** Any code snippets you add should be snippet links to the original file if applicable. You can pull specific lines or even create sections to do this. Only do not do this if it would be way too cumbersome.
3. **External links should open in a new tab with no referrer.** (unless you have a specific reason not to) Make links like this:
    ```md
    https://google.com{ target="_blank" relk="noopener noreferrer" }
    [link text](https://google.com){ target="_blank" rel="noopener noreferrer" }
    ```
4. **Use frontmatter.** Set an `icon` and `description` for every page (examples can be seen in the source of any page). Include all pages in the [`nav:` component](https://www.mkdocs.org/user-guide/configuration/#nav) of `mkdocs.yml` unless there is a reason not to.
5. **Be descriptive.** When writing config and CLI references especially, try to *show, not tell*. A full description of this approach can be seen in the Diátaxis framework: [diataxis.fr/reference-explanation/](https://diataxis.fr/reference-explanation/)
6. **Follow the format.** We have established formats for directory pages and references. Follow them. Headers have icons. References begin with a reference card. Config references need to use code annotations. CLI references should be easy-to-read lists (showing the code like in the `bpkg` reference is optional). Directory pages should use cards to show what users can click on.
7. **Keep it navigateable.** Mobile users should not have to open the hamburger menu to get anywhere on the site from the root (they can still use it to go back or to skip directory pages).
8. **Be semi-casual.** For guides, you may find it better to be less distant from the reader. However, you need to also offer a reliable explanation of steps. You can decide what that looks like. References however, should always be distant (rule 5).
9. **Use the features given to you.** Be expressive! You are writing with one of the most powerful documentation frameworks out there, so *use it!* Don't be afraid to try something new in your writing, style or layout.
10. **Always have a Javascript-free option.** You can use the [`noJs`](https://blend-docs-material.pages.dev/contributing/#javascript) system to pull this off.
11. **Always give your headers icons.** This helps them look nice, and will be even nicer once the `typeset` plugin hits the community edition.
12. **Header titles must match page titles.** Each page will have one level 1 header. Make your header like this: `# :<icon-you-used>: <nav-title>`
13. **Merge to [`dev`](https://git.blendos.co/blendOS/website/-/tree/dev).** This way you can preview everything before pushing it out.

# Local Development

Local development is quite easy. You'll only need:

- Python ≥ 3.8
- `pip` package manager (included with Python on Windows)

Simply cd in and run (this command only has to be run once):

<details>
<summary>If you can't use pip directly</summary>

Use `pipenv`.

Install pipenv [from pypi](https://pipenv.pypa.io/en/latest/installation.html) or your package manager.

Then do the following in the project folder:

```
pipenv install
```

Then, as `pipenv` says, you can use `pipenv shell` and `pipenv run`:

```
pipenv run mkdocs serve
```

</details>



```bash
pip install -r requirements.txt
```

From there, start the dev server:

```bash
mkdocs serve
```

The server will reload after every save.  

If you want to build the website into static HTML run this command (this isn't required for contribution, the CI/CD server does it automatically):

```bash
mkdocs build
```

# Credit

Moved to the [credits page](https://blend-docs-material.pages.dev/credits).
