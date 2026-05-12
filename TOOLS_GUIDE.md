# Tools Guide

How to create and publish a new tool.

## Creating a new HTML tool

Each tool lives in a single self-contained `.html` file at the repo root.

### File naming

Use lowercase kebab-case: `my-tool.html`

### Required structure

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Tool</title>
    <style>
        * { box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }
        @media (max-width: 600px) {
            body { padding: 10px; }
        }
    </style>
</head>
<body>
    <h1>My Tool</h1>
    <p>Short description of what this does.</p>

    <!-- tool UI here -->

    <script>
        // all JS inline
    </script>
</body>
</html>
```

### Key conventions

- **No build step** — one `.html` file, inline `<style>` and `<script>`.
- **No CSS frameworks** — plain CSS with Flexbox/Grid.
- **Real-time where possible** — respond to `input` events, not button clicks.
- **Copy-to-clipboard** — use `navigator.clipboard.writeText()`.
- **Show/hide results** — toggle a `.visible` CSS class, not `display` manipulation.
- **External libraries** — load from a CDN via `<script src>` or ES module import.

### After creating the tool

1. Add an entry to `README.md` under the appropriate section.
2. Commit — the commit message becomes part of the tool's history.
3. The CI/CD pipeline generates `index.html` and injects the shared footer.

## Creating a docs file

Each tool can have an optional `<slug>.docs.md` describing what it does. This is
shown on the colophon page and used for search indexing. Keep it to 2–4 sentences.

```markdown
Paste any JSON text to format and validate it instantly. The output is
syntax-highlighted and auto-indented with two spaces. Invalid JSON is flagged with
a descriptive error message.
```

## Python tools

Standalone Python scripts go in the `/python/` directory. They should be runnable
with `uv run` and include inline dependency metadata where needed:

```python
# /// script
# requires-python = ">=3.12"
# dependencies = ["httpx", "click"]
# ///
import click
...
```

## Publishing

Push to `main` — GitHub Actions builds the site and deploys it to GitHub Pages.
