# ADR-0013: Theming through design tokens

- **Status:** Accepted
- **Date:** 2026-10-23
- **Type:** Product

## Context

The default identity is "Darkroom": graphite surfaces, an amber safelight accent and monospaced labels. The owner wants user-configurable colors, custom saved themes and several built-in themes.

## Alternatives considered

- **Hard-coded single theme.** Rejected: adding themes later would mean touching every component.
- **Full theme editor in the PoC.** Rejected: valuable but not core; postponed to a later phase.

## Decision

- Every UI color comes from **semantic design tokens** (for example surface, text, accent). Components never use raw color values.
- A **Theme** is a named set of token values with a light and a dark variant.
- **PoC:** the built-in Darkroom theme plus one alternative, and a theme picker.
- **Later phase:** custom theme editor (pick colors, save, share), validated against WCAG contrast before saving.

## Consequences

- Adding a theme is data, not code.
- The contrast validator protects accessibility for user-made themes.
- The Grid preview always reflects the photos, never the theme.
