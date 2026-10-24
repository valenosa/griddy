# ADR-0007: No import of Published Posts in the PoC; sync is required for stable

- **Status:** Accepted
- **Date:** 2026-10-23

## Context

Showing the real, already-published grid is essential: without it the plan can drift from the actual Profile. The only legitimate way to read it is the official Instagram API. The owner currently has no published posts, so in the PoC everything planned is new.

## Decision

- The PoC does **not** import or manually load Published Posts.
- A Planned Post becomes Published when the user confirms it after a Share Handoff.
- **Grid sync through the official API is a release requirement for the first stable version.**

## Consequences

- Posts published outside Griddy are invisible until the API phase.
- Scraping and unofficial APIs are rejected (ADR-0003).
