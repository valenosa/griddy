# ADR-0003: Share Handoff in the PoC, Instagram API publishing as a priority phase

- **Status:** Accepted
- **Date:** 2026-10-23

## Context

Direct publishing is one of the most valuable features for the owner. Automatic publishing is only possible through Meta's official Instagram API, which requires a professional (Business or Creator) account, a registered Meta app, and media hosted at a public URL. None of that exists in a local-first PoC.

## Decision

- **PoC:** publish via **Share Handoff**: the app sends a Planned Post's Slides, in order, to the Android share sheet, where the user picks Instagram.
- **Future phase (high priority):** integrate the official Instagram API for publishing (and, likely, reading the published grid).

## Consequences

- The PoC still removes the main pain point (finding the photos again).
- The API phase introduces a backend and cloud media hosting; storage design must allow that transition (see storage ADR, pending).
- Unofficial methods (scraping, private APIs, password sharing) are explicitly rejected: they break Instagram's terms and risk the account.
