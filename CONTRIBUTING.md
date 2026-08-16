# Contributing to AfrPowerOS

Thank you for contributing. This project is evidence-first: the dataset's only real asset is its accuracy and traceability.

## Types of contribution

- **Data corrections** — a country record is wrong, outdated, or missing a source.
- **New countries** — add a country we don't cover yet.
- **Methodology** — improve how we label confidence, verify sources, or version data.
- **Tooling** — validation scripts, CI, schema improvements.
- **Documentation** — README, docs/, examples.

## Ground rules

1. **Every data record needs a source.** No source, no merge. Sources should be primary where possible: national nuclear agencies, regulators, IAEA, government statements, reputable industry press (World Nuclear News, Nuclear Engineering International, etc.).
2. **Use confidence labels honestly.** `Verified` / `Inference` / `Speculation` / `Unverified` — defined in `docs/methodology.md`. When unsure, choose the *more conservative* label.
3. **Never invent data.** If you cannot verify it, mark it `Unverified` or omit it.
4. **Keep it civilian and neutral.** This project covers peaceful, civilian nuclear energy and energy infrastructure. No content related to weapons, weapons-related enrichment, or safeguards evasion. No vendor cheerleading — we track what programs *are*, not what we wish they were.

## Getting started

```bash
git clone https://github.com/kawacukennedy/afrpoweros.git
cd afrpoweros
python3 scripts/validate.py
```

Run the validator before pushing. CI runs the same command.

## Workflow

1. Fork the repository.
2. Create a branch: `git checkout -b feat/<branch-name>` (e.g., `feat/add-ethiopia`, `fix/rwanda-inir-date`).
3. Make your change; update `CHANGELOG.md` under "Unreleased".
4. Run `python3 scripts/validate.py`.
5. Open a pull request against `main` using the PR template.
6. Reference any related issue (e.g., `Closes #12`).

## Commit messages

Use [Conventional Commits](https://www.conventionalcommits.org/):

```
feat(data): add Ethiopia country record
fix(data): correct Rwanda INIR mission date
docs(methodology): clarify confidence labels
chore(ci): validate CSV in CI
```

## Review expectations

- Data changes: expect a request for your sources.
- Keep PRs focused. One logical change per PR.
- Be kind and specific in reviews — many contributors are students and early-career professionals, and this project exists to help people like them get into the industry.

## Code of Conduct

All contributors must follow the [Code of Conduct](CODE_OF_CONDUCT.md).

## Security

Found a security issue? Report it privately per [SECURITY.md](SECURITY.md) — never in a public issue.
