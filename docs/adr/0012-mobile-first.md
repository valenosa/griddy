# ADR-0012: Mobile-first, desktop supported

- **Status:** Accepted
- **Date:** 2026-10-23

## Context

The owner plans and publishes from an Android phone; Instagram itself is a phone app. Desktop is useful for long planning sessions.

## Decision

- Griddy is designed **for phones first** (360–430 px wide, touch). Every feature must be fully usable one-handed on a phone.
- Desktop is supported with a responsive layout: the Grid stays at phone proportions, and the Post editor opens in a side panel instead of a full screen.

## Input per platform

| Action | Phone | Desktop |
|---|---|---|
| Reorder Posts / Slides | Long-press and drag | Mouse drag |
| Accessible alternative | Tap → "Move" → arrow buttons | Same, plus keyboard arrows |
| Reframe a Slide | Drag + pinch | Drag + scroll wheel / slider |
| Share Handoff | Android share sheet | Download files (share sheet if the browser supports it) |

## Consequences

- End-to-end tests run primarily on a phone viewport (see testing strategy).
- Desktop layouts are an enhancement, never a requirement for a feature to ship.
