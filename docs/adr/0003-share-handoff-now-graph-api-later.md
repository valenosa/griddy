# ADR-0003: Share Handoff in the PoC, Instagram API publishing as a priority phase

- **Status:** Accepted
- **Date:** 2026-10-23
- **Type:** Product

## Context

Direct publishing is one of the most valuable features for the owner. Automatic publishing is only possible through Meta's official Instagram API, which requires a professional account, a registered Meta app and media hosted at a public URL (S-03). None of that exists in a local-first PoC (ADR-0008).

## Alternatives considered

- **Build API publishing into the PoC.** Rejected: requires a backend, cloud hosting and Meta setup before the planner itself is validated.
- **Unofficial methods (scraping, private APIs, password sharing).** Rejected permanently: they break Instagram's terms and put the account at risk.
- **No publishing help at all.** Rejected: finding the photos again is the main pain point.

## Decision

- **PoC:** publish via **Share Handoff**: Griddy sends a Planned Post's Slides, in order and at Export Quality, to the Android share sheet, where the user picks Instagram.
- **Later phase (high priority):** integrate the official Instagram API for publishing and for reading the Published Posts.

## Consequences

- The PoC still removes the main pain point.
- The API phase introduces a backend and cloud media hosting, which ADR-0008 keeps possible.
- API constraints (S-02) mean some Posts valid in the app cannot be published via the API; Griddy must flag them in that phase.
- Feasibility of multi-photo Share Handoff is pending verification (P-01).
