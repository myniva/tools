# tools

A collection of single-file browser tools, modelled on tools.simonwillison.net.

## Dev server

```bash
make serve        # starts python3 -m http.server 8080 on the remote
```

## Build

```bash
make build        # runs build.sh: regenerates index.html + dates.json, injects footer
```

Requires `python3` with the `markdown` package (`pip install markdown`).

## Adding a tool

1. Create `<slug>.html` at the repo root — single file, inline CSS and JS, no framework.
2. Create `<slug>.docs.md` with 2–4 sentences describing what it does.
3. Add a line to `README.md` under the right section — `build_index.py` turns that into `index.html`.
4. Commit — git history is used by `build_dates.py` to show "Updated" dates in the footer.

See `TOOLS_GUIDE.md` for conventions (real-time input events, copy-to-clipboard pattern,
show/hide via `.visible` class, CDN libraries, responsive breakpoint at 600px).

## Key files

| File | Role |
|---|---|
| `build.sh` | Main build script |
| `build_index.py` | README.md → index.html |
| `build_dates.py` | git log → dates.json |
| `footer.js` | Shared footer injected at build time (not in source HTML) |
| `.github/workflows/pages.yml` | Deploy to GitHub Pages on push to main |

## Notes

- Use `python3`, not `python` (the `python` command is not available on this machine).
- `footer.js` is injected by `build.sh` — raw HTML tool files do not include it.
- `dates.json` and `index.html` are build artefacts; they are committed by CI but can be
  regenerated locally with `make build`.
