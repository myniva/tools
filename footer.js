/**
 * Shared footer for all tools.
 * Injected by build.sh before </body> in every *.html file.
 *
 * Features:
 *  - Renders a slim footer with: Home | Source | Updated <date>
 *  - Fetches tool slug → last-commit date from dates.json (cached in sessionStorage)
 *  - Auto-detects page background to pick contrasting footer text colour
 */
(async function () {
  const GITHUB_REPO = "ch01bnb/tools";
  const slug = location.pathname.replace(/^\/|\.html$/g, "").split("/").pop();

  // ── helpers ──────────────────────────────────────────────────────────────

  function isDarkBackground() {
    const bg = getComputedStyle(document.body).backgroundColor;
    const m = bg.match(/rgba?\((\d+),\s*(\d+),\s*(\d+)/);
    if (!m) return false;
    const [r, g, b] = m.slice(1).map(Number);
    // Perceived luminance (ITU-R BT.709)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b < 128;
  }

  async function fetchDates() {
    const KEY = "__tools_dates";
    const cached = sessionStorage.getItem(KEY);
    if (cached) return JSON.parse(cached);
    try {
      const r = await fetch("/dates.json");
      if (!r.ok) return {};
      const data = await r.json();
      sessionStorage.setItem(KEY, JSON.stringify(data));
      return data;
    } catch {
      return {};
    }
  }

  // ── build footer DOM ──────────────────────────────────────────────────────

  const dates = await fetchDates();
  const updatedDate = dates[slug] || null;

  const dark = isDarkBackground();
  const textColor = dark ? "rgba(255,255,255,0.8)" : "#555";
  const borderColor = dark ? "rgba(255,255,255,0.15)" : "#e1e4e8";
  const linkColor = dark ? "#a5b4fc" : "#5b4fcf";

  const footer = document.createElement("footer");
  footer.style.cssText = `
    margin-top: 48px;
    padding: 14px 20px;
    border-top: 1px solid ${borderColor};
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    font-size: 0.82rem;
    color: ${textColor};
    display: flex;
    gap: 16px;
    flex-wrap: wrap;
    align-items: center;
  `;

  const linkStyle = `color:${linkColor};text-decoration:none;`;

  const sourceUrl = `https://github.com/${GITHUB_REPO}/blob/main/${slug}.html`;

  const parts = [
    `<a href="/" style="${linkStyle}">Home</a>`,
    `<a href="${sourceUrl}" target="_blank" rel="noopener" style="${linkStyle}">Source</a>`,
  ];

  if (updatedDate) {
    const historyUrl = `https://github.com/${GITHUB_REPO}/commits/main/${slug}.html`;
    parts.push(
      `<a href="${historyUrl}" target="_blank" rel="noopener" style="${linkStyle}">Updated ${updatedDate}</a>`
    );
  }

  footer.innerHTML = parts.join(
    `<span style="color:${borderColor};user-select:none">|</span>`
  );

  document.body.appendChild(footer);
})();
