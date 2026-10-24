# ADR-0001: Photos-only PoC, staged media roadmap

- **Status:** Accepted
- **Date:** 2026-10-23

## Context

Supporting video adds cropping, cover selection, large file sizes and on-device storage pressure. The core value (planning the grid and carousels) can be proven with photos alone.

## Decision

The PoC handles **photos only**. Media support grows in stages:

1. Photos (PoC)
2. Mixed carousels (a video Slide inside a photo Carousel)
3. Standalone video Posts
4. Reels

## Consequences

- The data model must not assume a Slide is always a photo: `Slide` carries a `mediaType` field from day one, with only `photo` implemented.
- Storage and export design must anticipate much larger files once video arrives.
