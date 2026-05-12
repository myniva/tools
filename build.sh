#!/usr/bin/env bash
set -euo pipefail

# ── 1. Generate metadata ──────────────────────────────────────────────────────
python3 build_dates.py
python3 build_index.py

# ── 2. Inject shared footer into every HTML tool ─────────────────────────────
#
# Appends  <script src="footer.js?HASH"></script>  just before </body>.
# Skips index.html (the homepage already has its own structure).
#
FOOTER_HASH=$(git log -1 --format="%H" -- footer.js 2>/dev/null || echo "dev")
FOOTER_SHORT=$(echo "$FOOTER_HASH" | cut -c1-8)

SCRIPT_TAG="<script src=\"footer.js?${FOOTER_SHORT}\"></script>"

for file in *.html; do
  [[ "$file" == "index.html" ]] && continue

  # Skip if already injected (idempotent)
  if grep -q "footer.js" "$file"; then
    continue
  fi

  awk -v tag="$SCRIPT_TAG" '
    /<\/body>/ { sub(/<\/body>/, tag "\n</body>") }
    { print }
  ' "$file" > "$file.tmp" && mv "$file.tmp" "$file"

  echo "  footer → $file"
done

echo "Build complete."
