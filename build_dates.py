"""
Generate dates.json — maps each HTML tool slug to its most recent git commit date.
Used by footer.js to display "Updated YYYY-MM-DD".
"""
import json
import subprocess
from pathlib import Path

root = Path(__file__).parent
dates = {}

for html_file in sorted(root.glob("*.html")):
    slug = html_file.stem
    result = subprocess.run(
        ["git", "log", "-1", "--format=%aI", "--", html_file.name],
        capture_output=True,
        text=True,
        cwd=root,
    )
    date_str = result.stdout.strip()
    if date_str:
        dates[slug] = date_str[:10]  # YYYY-MM-DD

output = root / "dates.json"
output.write_text(json.dumps(dates, indent=2, sort_keys=True) + "\n")
print(f"Wrote {len(dates)} entries to {output}")
