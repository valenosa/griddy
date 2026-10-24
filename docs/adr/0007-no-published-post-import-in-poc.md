# ADR-0007: No import of Published Posts in the PoC; sync is required for stable

- **Status:** Accepted
- **Date:** 2026-10-23
- **Type:** Product

## Context

Showing the real, already-published grid is essential: without it the plan drifts from the actual Profile. The only legitimate way to read it is the official Instagram API (ADR-0003). The owner currently has no published posts, so everything planned in the PoC is new.

## Alternatives considered

- **Manual upload of already-published photos.** Rejected for the PoC: no current need, and it would be thrown away once API sync exists.
- **Scraping the public profile.** Rejected: breaks Instagram's terms (ADR-0003).

## Decision

- The PoC does **not** import or manually load Published Posts.
- A Planned Post becomes Published when the user confirms it after a Share Handoff.
- **Grid sync through the official API is a release requirement for the first stable version.**

## Consequences

- Posts published outside Griddy are invisible until the API phase.
- Publish Order and Next Post rely on the user confirming publications (R-05, R-06).
