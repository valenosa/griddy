# ADR-0013: Theming through design tokens

- **Status:** Accepted
- **Date:** 2026-10-23

## Context

The default identity is "Darkroom": graphite surfaces, an amber safelight accent, monospaced labels. The owner wants user-configurable colors, custom saved themes and several built-in themes.

## Decision

- Every color in the UI comes from **semantic design tokens** (CSS custom properties such as `--surface`, `--text`, `--accent`). Components never use raw color values.
- A **Theme** is a named set of token values with a light and a dark variant.
- **PoC:** ships the built-in **Darkroom** theme (light and dark variants) plus one alternative, and a theme picker.
- **Later phase:** custom theme editor (pick colors, save, export/share), validated against WCAG contrast before saving.

## Consequences

- Adding themes is data, not code.
- The contrast validator protects accessibility when users build their own themes.
- The Grid preview always reflects the photos, never the theme.
