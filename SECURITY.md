# Security Policy

## Scope

AfrPowerOS is a data and documentation project. Its main risk surface is:

- **Data integrity** — a malicious or accidental edit that plants false "verified" information about nuclear or energy programs.
- **Supply chain** — dependencies used by validation scripts or future web tooling.
- **Collaboration abuse** — bad actors misusing the issue tracker, PRs, or CI to spread disinformation or execute code on CI runners.

## Reporting a vulnerability

**Do not open a public issue for a security problem.** Report privately:

- GitHub: use the **private vulnerability reporting** feature on the repository (Security → Report a vulnerability), or
- Email: `security@` placeholder — replace with your public reporting address when available.

## Response expectations

- **Acknowledgment:** within 72 hours.
- **Triage:** within 5 business days.
- **Coordinated disclosure:** we follow a 90-day coordinated disclosure window for confirmed issues.

## Supported versions

| Version | Supported |
|---|---|
| `main` (latest) | ✅ |
| Tagged releases | ✅ |
| Older releases | ❌ — upgrade to latest |

## Data integrity policy

The dataset uses confidence labels (`Verified` / `Inference` / `Speculation` / `Unverified`) defined in `docs/methodology.md`. Records may never be labelled `Verified` without a source. The validator in CI rejects records that lack a source URL.
