# Methodology

AfrPowerOS is evidence-first. A dataset record with no source is worse than no
record at all, because it looks authoritative. Everything below exists to keep
the dataset honest.

## 1. Confidence labels

Every country record carries one confidence label. These are judgements about
*how confident we are that the record is true*, not about who we'd like to win.

| Label | Definition | Examples |
|---|---|---|
| `Verified` | Stated by a primary source: national nuclear agency, regulator, IAEA press release, government statement, or a credible contract announcement. | "IAEA INIR mission completed"; "vendor shortlist announced". |
| `Inference` | A reasonable reading of verified evidence, but the fact itself is not directly stated. | "Program is in Phase 2" inferred from an INIR follow-up mission; capacity figures inferred from two reactors × 1,200 MW. |
| `Speculation` | A hypothesis not yet backed by evidence. Use sparingly; label it clearly. | "Country X could choose vendor Y." |
| `Unverified` | Reported by media but not confirmed by a primary source. | An industry-press claim that a government denied. |

**Rule:** when unsure between two labels, choose the more conservative one.

## 2. Source tiers

1. **Primary** — IAEA (press releases, INIR/SEED reports), national nuclear
   agencies, regulators, energy ministries, signed intergovernmental
   agreements, official procurement notices.
2. **Reliable secondary** — World Nuclear News, Nuclear Engineering
   International, Reuters, national wire services, recognized industry
   analysts *when quoting or reporting primary material*.
3. **Weak** — blogs, social media, un-cited listicles. Not acceptable as the
   only source for a fact; acceptable only as a pointer to primary material.

A `Verified` label requires at least one source at tier 1 or 2.

## 3. Dates and numbers

- Only record dates that exist in a source. Do not reconstruct dates from
  memory or "about" phrasing.
- Figures (capacity, access rates, installed capacity) are approximations;
  prefer the source's own figure and keep the unit consistent (GW vs MW).
- Every record carries `last_verified` so stale data is visible.

## 4. Neutrality

- Track what programs *are*, not what we wish they were.
- Do not take sides between vendors or supplier countries. Vendor names are
  recorded as facts about the program (e.g., "vendors in selection"), not as
  endorsements.
- Scope is strictly **civilian** peaceful use and energy infrastructure. No
  weapons, weapons-adjacent enrichment, or safeguards-evasion content.

## 5. Corrections

Errors are normal and welcome. Open a `data` issue or a pull request:

1. State the wrong value and the corrected value.
2. Provide the source URL(s).
3. Propose a confidence label.

Maintainers review, merge, and bump `CHANGELOG.md` + `last_verified`.

## 6. Validation

`scripts/validate.py` (Python standard library only) enforces structure, types,
enums, date formats, source presence, and JSON↔CSV consistency. CI runs it on
every push and pull request.
