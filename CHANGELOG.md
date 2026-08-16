# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Initial project skeleton.
- Repository governance files (README, LICENSE, LICENSE-DATA, CONTRIBUTING, CODE_OF_CONDUCT, SECURITY, CHANGELOG, AGENTS, CITATION, .editorconfig, .gitignore).
- CI workflow: schema + dataset + CSV validation on push and pull request.
- Dependabot for `pip` and GitHub Actions dependencies.
- Issue templates (bug report, feature request, data correction) and pull request template.
- `data/afrpoweros.json` dataset seed: Rwanda, Kenya, Ghana, Egypt, South Africa, Uganda, Tanzania, Nigeria, Zambia, Morocco, Algeria.
- `data/schema.json` JSON Schema for the dataset.
- `data/countries.csv` flat summary table.
- `scripts/validate.py` dependency-free validator.
- `examples/quickstart.py` example script.
- `docs/` (data model, methodology, roadmap).
- Static GitHub Pages map (`site/`): pure-SVG choropleth of African program
  status, hover tooltips, click-to-table; dataset inlined as static JS for
  instant load; `scripts/build_site.py` regenerates the embedded dataset and
  injects a content-hash cache-buster into asset URLs.
- Expanded dataset to 20 countries: added Ethiopia, Sudan, Tunisia, Zimbabwe,
  Senegal, Mali, Niger, Eswatini and DR Congo (all `Verified`, with IAEA,
  government and industry sources).
- Site homepage: live stats row (countries, verified records, active
  programmes) and a "Contribute" call-to-action section with links to issues
  and the contribution guide.
- `scripts/build_site.py`: version hash now includes site sources
  (`app.js`, `styles.css`, `index.html`, `data/africa.js`) so asset URLs
  rotate whenever either the dataset or the site code changes.
- Security hardening: all dataset-derived strings are HTML-escaped before
  being rendered by `site/app.js`, and `scripts/validate.py` now rejects
  markup characters (`<`, `>`) in string fields so a compromised data PR
  cannot inject script into the live site.
- `CODEOWNERS`: explicit path rules for `/data/`, `/scripts/`, `/site/` and
  `/.github/` so guard-rail changes always require maintainer review.
- Free weekly newsletter: `/newsletter` page with Buttondown subscribe form
  (free tier, no watermarks) and a public issue archive on GitHub Pages.
  Homepage and footer link to it; `scripts/build_site.py` copies and
  cache-busts newsletter pages. Issue 001 published.
- Fully automated newsletter pipeline: `scripts/newsletter.py` generates a
  weekly digest from the dataset and sends it via the Buttondown API
  (`scripts/newsletter.py --draft` to stage, `--send` to publish); the
  `newsletter` GitHub Actions workflow sends every Tuesday at 09:00 UTC and on
  manual dispatch. Subscribe forms use the real Buttondown username `kawacu`;
  the newsletter page links to the canonical live archive.
