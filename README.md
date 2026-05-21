# tools

A collection of single-file browser tools and CLI scripts.

Inspired by [tools.simonwillison.net](https://tools.simonwillison.net/).

## Why single-file tools?

Single-file browser tools run entirely in the browser — no server, no login, no data leaving your device.
[InBrowser.App](https://inbrowser.app/) puts it well: fast, private, and ready at any time — that's how tools should be.
ThoughtWorks even featured the pattern on their [Tech Radar Vol. 34](https://www.thoughtworks.com/radar/techniques/html-tools):
packaging a utility as a single HTML file avoids the overhead of binaries or package managers, works anywhere a browser runs, and the source is right there to inspect.

## Tools

### Text & Data

- [JSON Formatter](json-formatter) — Prettify and validate JSON with syntax highlighting
- [Base64](base64) — Encode and decode Base64 strings (standard and URL-safe)
- [Hash Text](hash-text) — Generate SHA-256 / SHA-512 hashes using the Web Crypto API
- [VTT Formatter](vtt-formatter) — Convert Teams WebVTT transcripts to clean speaker blocks for LLMs

## Adding a new tool

See [TOOLS_GUIDE.md](TOOLS_GUIDE.md) for instructions on creating and publishing new tools.
