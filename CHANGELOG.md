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
  instant load; `scripts/build_site.py` regenerates the embedded dataset.
