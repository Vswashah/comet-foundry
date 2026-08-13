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

## CI/CD

Every push and pull request to `main` runs `.github/workflows/ci.yml`, which:

1. Regenerates the site from source (`generate.py` then `build_spa.py`) and
   fails if the result differs from what's committed — this catches the case
   where someone edited `generate.py`/`styles.css`/`script.js` but forgot to
   re-run the generators before committing.
2. Checks the inline JavaScript in `comet-foundry-spa.html` for syntax errors.
3. Checks every internal `href="*.html"` link across the site actually
   points to a file that exists.

If all of that passes, the PR/push is good to merge or deploy.

**Deployment** is handled separately by Vercel's native GitHub integration
(connected to this repo) — every push to `main` deploys automatically there.
This workflow doesn't deploy anything itself; it's a quality gate, not a
deploy step.

## Notes

- Fonts are loaded from Google Fonts (Space Grotesk, IBM Plex Mono, Caveat).
- No build tooling or dependencies required — everything is plain HTML/CSS/JS.
- Some content (Team roster, Projects, Blog, Partners) is intentionally left
  as placeholder / "Coming Soon" states pending real information.
# Comet Foundry
