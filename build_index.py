"""
Generate index.html from README.md.

Converts the Markdown to HTML, wraps it in a styled page with a nav header,
and optionally injects a "Recently Added" section from tools.json.
"""
import json
import textwrap
from pathlib import Path

import markdown

root = Path(__file__).parent

NAV_STYLE = """
<style>
  *, *::before, *::after { box-sizing: border-box; }
  :root {
    --accent: #5b4fcf;
    --accent-dark: #3d35a0;
    --text: #24292e;
    --muted: #586069;
    --border: #e1e4e8;
    --bg: #ffffff;
  }
  body {
    margin: 0;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
                 Helvetica, Arial, sans-serif;
    color: var(--text);
    background: var(--bg);
  }
  .site-nav {
    background: linear-gradient(135deg, var(--accent) 0%, var(--accent-dark) 100%);
    color: white;
    padding: 18px 24px 16px;
  }
  .site-nav h1 {
    margin: 0 0 4px;
    font-size: 1.5rem;
    font-weight: 700;
    letter-spacing: -0.3px;
  }
  .site-nav p {
    margin: 0;
    font-size: 0.9rem;
    opacity: 0.85;
  }
  .content {
    max-width: 820px;
    margin: 0 auto;
    padding: 32px 24px 64px;
  }
  h2 { color: var(--accent); border-bottom: 2px solid var(--border); padding-bottom: 6px; }
  a { color: var(--accent); }
  a:hover { color: var(--accent-dark); }
  ul { padding-left: 1.4em; }
  li { margin: 6px 0; }
  .recently-added {
    background: #f6f8fa;
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 18px 22px;
    margin-bottom: 28px;
  }
  .recently-added h2 { margin-top: 0; }
  .recently-added ul { margin: 0; }
  @media (max-width: 600px) {
    .content { padding: 20px 14px 48px; }
  }
</style>
"""


def build_recently_added(tools_json: Path, n: int = 5) -> str:
    if not tools_json.exists():
        return ""
    tools = json.loads(tools_json.read_text())
    tools.sort(key=lambda t: t.get("created", ""), reverse=True)
    recent = tools[:n]
    if not recent:
        return ""
    items = "\n".join(
        f'      <li><a href="/{t["slug"]}">{t["title"]}</a>'
        f' — {t.get("description", "")}</li>'
        for t in recent
    )
    return textwrap.dedent(f"""
      <div class="recently-added">
        <h2>Recently Added</h2>
        <ul>
      {items}
        </ul>
      </div>
    """)


def build_index():
    readme = (root / "README.md").read_text()
    body_html = markdown.markdown(readme, extensions=["tables", "fenced_code"])

    recently = build_recently_added(root / "tools.json")

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>tools</title>
  {NAV_STYLE}
</head>
<body>
  <nav class="site-nav">
    <h1>tools</h1>
    <p>A collection of single-file browser tools and CLI scripts.</p>
  </nav>
  <div class="content">
    {recently}
    {body_html}
  </div>
</body>
</html>
"""
    out = root / "index.html"
    out.write_text(html)
    print(f"Wrote {out}")


if __name__ == "__main__":
    build_index()
