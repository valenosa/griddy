# ADR-0005: English for code, docs and UI

- **Status:** Accepted
- **Date:** 2026-10-23
- **Type:** Product

## Context

Griddy targets an international audience and serves as a portfolio piece for international reviewers. The owner is a Spanish speaker.

## Alternatives considered

- **Spanish everywhere.** Rejected: limits the audience and the portfolio reach.
- **Spanish docs, English code.** Rejected: splits the project in two languages and makes contributions harder.

## Decision

All code, documentation, commit messages and UI text are in English. UI strings live in one place so localization can be added later.

## Consequences

- Spanish (or other) UI localization is a later addition, not a rewrite.
