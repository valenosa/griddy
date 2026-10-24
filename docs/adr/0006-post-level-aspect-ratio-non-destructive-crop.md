# ADR-0006: Aspect Ratio per Post, non-destructive Crop per Slide

- **Status:** Accepted
- **Date:** 2026-10-23

## Context

Instagram applies one shape to every Slide of a Post (the first Slide's). The owner wants to switch a Post's shape freely to compare how it looks, without losing work.

## Decision

- Aspect Ratio is a property of the **Post**: `1:1`, `4:5` or `3:4`. Default: `4:5`.
- Each Slide keeps its **original photo untouched** and stores a **Crop per Aspect Ratio** (position and zoom). Switching ratio and back restores the previous framing.
- New Slides get a centered Crop by default; the user can reframe by dragging and pinching.
- Export Quality images are rendered at Share Handoff time from original + Crop.

## Consequences

- Behavior matches Instagram: one shape per Post, every Slide follows it.
- Originals are stored at full resolution, which increases storage use; acceptable for photos.
- When the API phase arrives, 3:4 Posts must be flagged as not API-publishable (see CONTEXT.md constraints).
