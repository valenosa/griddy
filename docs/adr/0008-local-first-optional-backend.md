# ADR-0008: Local-first architecture with an optional backend

- **Status:** Accepted
- **Date:** 2026-10-23
- **Type:** Product

## Context

The distribution model is undecided (P-02): open-source self-hosted, a paid hosted product, or both (open core). A hosted backend is likely eventually, and the Instagram API phase needs one.

## Alternatives considered

- **Backend and accounts from the start.** Rejected: server cost and complexity before the product is validated, and it closes the self-hosted path.
- **Local-only forever.** Rejected: rules out API publishing, sync and multi-device use.

## Decision

- Griddy is **local-first**: the full planning experience works offline, with all data on the device.
- The app requests **persistent storage** and offers **backup export and import** to a single file.
- All data access goes through a **repository interface**; a sync backend is a pluggable implementation added later. The UI never talks to storage or network directly.
- The commercial distribution model stays open.

## Consequences

- No server cost until the API phase; photos never leave the device unless the user shares or backs them up.
- Data loss is possible if the browser's site data is cleared (S-04); mitigated by persistent storage and backups.
- Future sync requires stable IDs and timestamps on every entity from day one.
