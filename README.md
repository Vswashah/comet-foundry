# Comet Foundry Website

Static site for Comet Foundry — a hacker house at UT Dallas.

## Structure

This repo has two parallel outputs built from the same source:

- **Multi-page site** (`index.html`, `about.html`, `programs.html`, etc.) — a
  traditional set of static HTML pages sharing `styles.css` and `script.js`.
  This is the version meant for real hosting (Netlify, Vercel, GitHub Pages,
  etc.) since each page is a real route.
- **`comet-foundry-spa.html`** — the entire site as a single self-contained
  file (inline CSS/JS, hash-based client-side routing). Useful for quick
  previews or embedding anywhere a single file is easier to drop in.

### Source / generators

The actual source of truth is Python:

- **`generate.py`** — generates all the multi-page `.html` files plus
  `styles.css` and reads/writes `script.js`. Run `python3 generate.py` to
  regenerate every page after editing content inside this file.
- **`build_spa.py`** — imports `generate.py`'s page bodies and assembles the
  single-file `comet-foundry-spa.html` version. Run `python3 build_spa.py`
  after `generate.py` to keep the SPA in sync.

To make a content or design change: edit `generate.py` (and `styles.css` /
`script.js` directly for styling/behavior), then run:

```bash
python3 generate.py
python3 build_spa.py
```

Both outputs will be regenerated from the same source.

## Pages

Home, About, Programs, Projects, Team, Partners, Events (+ event detail),
Blog, Apply, Privacy Policy, Terms of Use.

## Notes

- Fonts are loaded from Google Fonts (Space Grotesk, IBM Plex Mono, Caveat).
- No build tooling or dependencies required — everything is plain HTML/CSS/JS.
- Some content (Team roster, Projects, Blog, Partners) is intentionally left
  as placeholder / "Coming Soon" states pending real information.
