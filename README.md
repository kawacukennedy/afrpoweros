# AfrPowerOS

![CI](https://github.com/kawacukennedy/afrpoweros/actions/workflows/ci.yml/badge.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![Data: CC BY 4.0](https://img.shields.io/badge/Data-CC%20BY%204.0-lightgrey.svg)
![Countries: 11](https://img.shields.io/badge/Countries-11-orange.svg)

**Open, cited intelligence on African nuclear & energy infrastructure programs.**

AfrPowerOS tracks every African country's civilian nuclear-energy programme — programme phase, IAEA milestone status, regulator, implementing agency, planned capacity, vendors, agreements, research reactors, and key events — as a free, machine-readable, fully sourced dataset.

The nuclear/energy information gap in Africa is real: announcements are scattered across government sites, IAEA press releases, and industry media, with no neutral, cited, machine-readable tracker. AfrPowerOS exists to fix that — and to give anyone (students, journalists, analysts, vendors, policymakers) a trustworthy starting point.

**Status: early-stage, community-built, evidence-first.** Every record carries a confidence label and source links. Errors are welcome — correct us via an issue or pull request.

## Why

- ~600 million people in sub-Saharan Africa lack electricity (World Bank/IMF).
- Africa hosts <2% of global data-center capacity; power is the binding constraint on AI infrastructure (IMF AI Preparedness Index; Microsoft–G42 Kenya project stalling on power).
- Only one African country operates a commercial nuclear plant (South Africa). Egypt is building; Ghana, Kenya, Uganda, Tanzania, Nigeria, Zambia, Rwanda and Algeria are in IAEA "milestones" preparation.

## Data

- `data/afrpoweros.json` — full dataset (structured, schema-validated).
- `data/countries.csv` — flat summary table.
- `data/schema.json` — JSON Schema for the dataset.
- Methodology: `docs/methodology.md`.

Every field carries a confidence label:

| Label | Meaning |
|---|---|
| `Verified` | Confirmed from a primary source (agency, regulator, IAEA, government). |
| `Inference` | Reasonable reading of verified evidence. |
| `Speculation` | Hypothesis; treat as unproven. |
| `Unverified` | Reported but not yet confirmed. Check before relying. |

## Quick start

```bash
git clone https://github.com/kawacukennedy/afrpoweros.git
cd afrpoweros
python3 scripts/validate.py        # validates schema + dataset + CSV (no dependencies)
```

Example (no dependencies):

```bash
python3 examples/quickstart.py
```

## Repository layout

```
.
├── LICENSE                  # MIT — code
├── LICENSE-DATA             # CC BY 4.0 — dataset
├── CONTRIBUTING.md          # how to contribute
├── CODE_OF_CONDUCT.md       # community standards
├── SECURITY.md              # vulnerability reporting
├── CHANGELOG.md             # release history
├── AGENTS.md                # guidance for AI coding agents
├── data/                    # dataset + schema
├── docs/                    # data model, methodology, roadmap
├── scripts/                 # validation tooling
└── examples/                # runnable examples
```

## Roadmap

See [`docs/roadmap.md`](docs/roadmap.md). Near-term: expand country coverage, add an "IAEA 19 infrastructure issues" readiness tracker per country, and a live web map.

## Contributing

Read [`CONTRIBUTING.md`](CONTRIBUTING.md) first. Data corrections, new countries, and methodology improvements are especially welcome. All contributions must include sources.

## Security

Report vulnerabilities privately — see [`SECURITY.md`](SECURITY.md). Never open a public issue for a security problem.

## License

- Code: [MIT](LICENSE)
- Dataset: [CC BY 4.0](LICENSE-DATA) — attribution required.

## Maintenance

Maintained by [@kawacukennedy](https://github.com/kawacukennedy) with community contributions. This is an honest early-stage project: it is maintained, but priorities shift with community feedback.
