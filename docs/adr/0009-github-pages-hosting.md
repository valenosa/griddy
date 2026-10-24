# ADR-0009: Host the web app on GitHub Pages

- **Status:** Accepted
- **Date:** 2026-10-23
- **Type:** Technical

## Context

Local data is bound to the app's origin (URL). Moving the app to a new URL later strands existing data unless the user restores a backup.

## Alternatives considered

- **Claude artifact hosting.** Rejected: fast, but the URL is not owner-controlled.
- **Vercel or Netlify.** Viable, but adds an account and service with no advantage for a static PoC.

## Decision

Deploy to **GitHub Pages** from the first release, built and published by GitHub Actions on every push to `main` that passes CI.

## Consequences

- Stable, owner-controlled URL and a public demo for the portfolio.
- A future custom domain is an origin change: it must ship together with a backup and restore prompt.
