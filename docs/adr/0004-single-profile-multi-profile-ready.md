# ADR-0004: Single Profile in the PoC, model ready for many

- **Status:** Accepted
- **Date:** 2026-10-23
- **Type:** Product

## Context

The owner plans one account today. Managing several accounts is a likely future need (creators, small businesses, a hosted product).

## Alternatives considered

- **Multi-profile UI from the start.** Rejected: extra screens and states with no current user need.
- **No Profile entity at all.** Rejected: adding it later would require migrating every stored Post.

## Decision

The PoC plans exactly one Profile, but `Profile` exists as an entity and every Post belongs to one.

## Consequences

- Multi-profile support becomes a UI change, not a data migration.
- [ROADMAP.md](../../ROADMAP.md) includes a multiple-Profiles phase.
