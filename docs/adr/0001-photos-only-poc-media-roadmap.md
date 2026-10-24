# ADR-0001: Photos-only PoC, staged media roadmap

- **Status:** Accepted
- **Date:** 2026-10-23
- **Type:** Product

## Context

Supporting video adds cropping over time, cover selection, large files and on-device storage pressure. The core value (planning the Grid and Carousels) can be proven with photos alone.

## Alternatives considered

- **Photos and video from the start.** Rejected: multiplies PoC scope and storage risk before the core idea is validated.
- **Photos only, no video plan.** Rejected: video and Reels are central to Instagram; ignoring them would force a redesign later.

## Decision

The PoC handles **photos only**. Media support grows in stages, in this order:

1. Photos (PoC)
2. Mixed Carousels (a video Slide inside a photo Carousel)
3. Standalone video Posts
4. Reels

## Consequences

- The data model must not assume a Slide is always a photo: each Slide carries a media type from day one, with only `photo` implemented.
- Storage and export design must anticipate much larger files once video arrives.
- The phase order is recorded in [ROADMAP.md](../../ROADMAP.md).
