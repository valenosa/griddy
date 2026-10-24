# ADR-0008: Local-first architecture with an optional backend

- **Status:** Accepted
- **Date:** 2026-10-23

## Context

The distribution model is undecided: open-source self-hosted, a paid hosted product, or both (open core). A hosted backend is likely eventually, and the Instagram API phase needs one. Meta requires App Review for an app that publishes on behalf of other people; self-hosters can instead use their own Meta app in development mode.

## Decision

- Griddy is **local-first**: the full planning experience works offline, with all data on the device (IndexedDB).
- The app requests **persistent storage** and offers **backup export/import** to a single file.
- All data access goes through a **repository interface**. A sync backend is a pluggable implementation added later; the UI never talks to storage or network directly.
- The commercial distribution model stays open.

## Consequences

- No server cost until the API phase.
- Data loss is possible if the browser's site data is cleared; mitigated by persistent storage and backups.
- Adding sync later requires stable IDs and timestamps on every entity from day one (UUIDs, `createdAt`, `updatedAt`).
