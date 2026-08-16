# AGENTS.md — guidance for AI coding agents

This file gives AI coding agents (e.g., opencode, Claude Code, Copilot)
working in this repository the rules they need to follow.

## Repository purpose

AfrPowerOS is an evidence-first, open dataset about civilian African nuclear
and energy infrastructure. Accuracy and traceability are the product.

## Hard rules

1. **Never fabricate data, sources, or dates.** Every dataset record must have
   a source URL and a confidence label. If you cannot verify a fact, mark it
   `Unverified` or leave it out — never invent.
2. **Stay civilian and neutral.** No content related to weapons, weapons-grade
   enrichment, plutonium production, safeguards evasion, or export-control
   circumvention. Do not take sides between vendors; track what programs are.
3. **Do not add comments to code unless asked.** Follow existing style.
4. **Run `python3 scripts/validate.py` after any data/schema change.** CI runs
   the same check.
5. **Update `CHANGELOG.md` (under `Unreleased`) when you make user-visible
   changes.** Follow Conventional Commits for commit messages.
6. **Keep dependencies at zero** for validation tooling — the validator runs
   with the Python standard library only.
7. **No secrets in the repo.** Never commit tokens, keys, or credentials.

## Data model

The dataset lives in `data/afrpoweros.json` (schema in `data/schema.json`,
documentation in `docs/data-model.md`). Flat summary in `data/countries.csv`.
When both files exist they must be consistent — the validator checks this.

## Confidence labels

`Verified` (primary source), `Inference` (reasonable reading of verified
evidence), `Speculation` (hypothesis), `Unverified` (reported, not confirmed).
See `docs/methodology.md`. Choose the more conservative label when unsure.

## Commands

- Validate everything: `python3 scripts/validate.py`
- Example usage: `python3 examples/quickstart.py`
