# ADR-0012: Mobile-first, desktop supported

- **Status:** Accepted
- **Date:** 2026-10-23
- **Type:** Product

## Context

The owner plans and publishes from an Android phone; Instagram itself is a phone app. Desktop is useful for long planning sessions.

## Alternatives considered

- **Desktop-first.** Rejected: the main usage and the publishing flow happen on the phone.
- **Phone only.** Rejected: desktop support is cheap with a responsive layout and helps long sessions.

## Decision

- Griddy is designed **for phones first** (360–430 px wide, touch). Every feature must be fully usable one-handed on a phone.
- Desktop is supported with a responsive layout: the Grid keeps phone proportions and the Post editor opens in a side panel.

| Action | Phone | Desktop |
|---|---|---|
| Reorder Posts or Slides | Long-press and drag | Mouse drag |
| Accessible alternative | Tap, "Move", arrow buttons | Same, plus keyboard arrows |
| Reframe a Slide | Drag and pinch | Drag and scroll wheel or slider |
| Share Handoff | Android share sheet | Download files, or share sheet if supported |

## Consequences

- End-to-end tests run primarily on a phone viewport.
- Desktop layouts are an enhancement, never a requirement for a feature to ship.
