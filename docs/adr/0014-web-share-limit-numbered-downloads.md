# ADR-0014: Web Share Handoff up to the browser's file limit, numbered downloads above it

- **Status:** Accepted
- **Date:** 2026-10-24
- **Type:** Product

## Context

The P-01 test on the owner's phone showed that Share Handoff works as ADR-0003 intends: Instagram receives several shared photos as one Carousel, in order (S-08). It also showed that Chrome on Android refuses to share more than `WEB_SHARE_MAX_FILES` files at once (S-07), while Instagram Posts accept up to `MAX_SLIDES` Slides (S-02). On the web, a Post with more Slides than the browser allows cannot be handed off in one share. The owner rarely makes Carousels that large.

## Alternatives considered

- **Limit Posts to `WEB_SHARE_MAX_FILES` Slides in Phase 1.** Rejected: the owner could not plan Carousels that Instagram allows, only to remove the restriction again in the APK phase.
- **Share in several batches, or one Slide at a time.** Rejected: each share opens a new Instagram Post, so the Slides never join one Carousel.
- **Bring the APK phase forward.** Rejected for now: large Carousels are rare, and Phase 2 already removes the limit (ROADMAP).

## Decision

- `MAX_SLIDES` stays as it is; planning is not limited by the browser.
- A Post with at most `WEB_SHARE_MAX_FILES` Slides is handed off in one share (ADR-0003).
- A larger Post, or any Post where the browser cannot share files, gets numbered downloads in Slide order instead, with a short explanation of why (R-14).

## Consequences

- Publishing a Post above the limit is manual: the user picks the downloaded files in Instagram's gallery in Slide order. The gallery's own order is not reliable (observed in the P-01 test), and exports carry no visible numbers (R-12).
- From the web, downloads land in the browser's Download folder; an album of its own needs the native app.
- The APK phase uses native sharing, which has no such limit; this ADR is revisited then.
- ADR-0003 stays in force; this decision resolves its pending verification (P-01).
