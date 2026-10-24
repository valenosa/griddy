# ADR-0006: Aspect Ratio per Post, non-destructive Crop per Slide

- **Status:** Accepted
- **Date:** 2026-10-23
- **Type:** Product

## Context

Instagram applies one shape to every Slide of a Post: the first Slide's (S-02). The owner wants to switch a Post's shape freely to compare how it looks, without losing framing work, and to edit photos in other apps.

## Alternatives considered

- **Aspect Ratio per Slide.** Rejected: Instagram does not allow it, so the preview would lie.
- **Destructive crop (save a new cropped image).** Rejected: switching ratio would lose the rest of the photo and every change would duplicate images.
- **One Crop per Slide shared by all ratios.** Rejected: a framing that works in 1:1 rarely works in 3:4; switching back and forth would destroy work.

## Decision

- Aspect Ratio is a property of the **Post**, one of `1:1`, `4:5` or `3:4`, defaulting to `DEFAULT_ASPECT_RATIO`.
- Each Slide keeps its **original photo untouched** and stores **one Crop per Aspect Ratio**: position, zoom and rotation.
- Export Quality images are rendered from original + Crop at Share Handoff time.

## Consequences

- Behavior matches Instagram; switching ratio and back restores the previous framing.
- Originals are stored at full resolution, which increases storage use; acceptable for photos.
- Rotation is stored in degrees from day one: 90° steps in the PoC, free-angle straightening later with no data migration.
- 3:4 Posts cannot be published via the API (S-02); relevant for the API phase.
