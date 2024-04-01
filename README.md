# Blend Docs Material

New BlendOS docs (WIP). Built with Material for MkDocs  

## Development

Local development is quite easy. You'll only need:

- Python ≥ 3.8
- `pip` package manager (included with Python on Windows)

Simply cd in and run (this command only has to be run once):

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