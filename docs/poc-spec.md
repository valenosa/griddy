# Phase 1 Spec — Web PoC

Features and acceptance criteria for Phase 1. Part of the model level: it says **what** the PoC does; rules, parameters and assumptions it cites live in the [model document](model.md).

- **Version:** 0.1
- **Date:** 2026-10-23
- **Status:** Draft, pending owner approval

## Goal

Plan an Instagram Grid of photo Posts and Carousels on an Android phone, see an accurate preview, and hand each Post to Instagram at Export Quality without searching the gallery again.

## Target platforms

- **Primary:** latest two versions of Chrome on Android (ADR-0012).
- **Supported:** latest desktop Chrome, Firefox and Safari. Where the share sheet is unavailable, Share Handoff falls back to downloading the files.

---

## Features

### F-01 · Grid

- Shows all Posts of the Profile as Grid Thumbnails (R-13), three per row with Instagram's spacing, in Grid order (R-05).
- Carousels show a multi-photo badge.
- The Next Post (R-06) is highlighted.
- Published Posts are visually distinguished and locked (R-05).
- The header shows counts of Planned and Published Posts.
- **Done when** a Grid of 60 Posts renders and scrolls smoothly on a mid-range Android phone.

### F-02 · Create a Post

- "New post" opens the photo picker with multi-select, up to `MAX_SLIDES` photos (R-01).
- Slides are created in selection order with centered Crops (R-03) and `DEFAULT_ASPECT_RATIO` (R-02).
- The new Post is placed according to R-05.
- **Done when** a 10-photo Carousel can be created in under 15 seconds from tapping "New post".

### F-03 · Post editor

- Swipe through Slides, previewed at Export Quality (R-12), so the editor shows what Instagram will show.
- Thumbnail strip: reorder Slides with long-press drag, or with "Move" and arrow buttons.
- Add photos (R-01), remove a Slide with Undo (ADR-0010), and Replace a Slide's photo keeping its position and Crop.
- Share a Slide's **original** photo to another app (for example Snapseed); the original is used only for reframing and this action.
- Switch the Aspect Ratio between 1:1, 4:5 and 3:4; every Slide follows (R-02) and keeps its Crop per ratio (R-03).
- Removing the last Slide applies R-08.
- **Done when** every action above is reachable one-handed on a 6-inch screen and is reflected immediately in the Grid.

### F-04 · Reframe a Slide

- Opens from the editor. Drag to position and pinch to zoom; on desktop, drag plus wheel or slider.
- Rotate in 90° steps. Free-angle straightening is a later phase (ROADMAP).
- The photo always covers the frame (R-03).
- **Done when** switching ratio and back restores the exact framing, rotation included.

### F-05 · Reorder the Grid

- Long-press a Post and drag it to a new position.
- Accessible alternative: tap a Post, choose "Move", then buttons to move one position or one row; keyboard arrows on desktop.
- Moves respect R-05.
- **Done when** both methods produce the same result and are covered by end-to-end tests.

### F-06 · Share Handoff and publishing state

- "Share" on a Planned Post renders every Slide at Export Quality (R-12) as high-quality sRGB JPEG and opens the share sheet with all files.
- Fallback: download the files numbered in Slide order (`01.jpg`, `02.jpg`…).
- On return, Griddy asks whether the Post was published and applies R-07. "Mark as planned" reverts it.
- **Done when** a 10-Slide Carousel reaches Instagram's composer with all photos in the correct order (pending P-01).

### F-07 · Delete, Undo and Trash

- Deleting a Post applies R-09: immediate, with Undo, then Trash, then purge.
- "Empty trash" deletes permanently after one confirmation, the only confirmation dialog in the app.
- **Done when** a deleted Post can be restored from the Undo toast and from the Trash, back to its previous state.

### F-08 · Post history

- Every change records a Snapshot (R-10) with a timestamp and a short label ("Reordered slides", "Changed to 1:1").
- The history lists Snapshots newest first, with a preview; restoring one is itself undoable (R-10).
- **Done when** each change type listed in ADR-0010 produces a Snapshot that restores correctly.

### F-09 · Storage

- All data stays on the device; Photos are stored once (R-11).
- Persistent storage is requested when the first photo is added; the result is shown in Settings (S-04).
- Settings shows storage used by Photos, history and Trash.

### F-10 · Backup

- "Export backup" produces one file with all data and original Photos.
- "Import backup" restores it, replacing current data after one confirmation.
- A backup made on one device can be imported on another (for example phone to desktop through Google Drive). It is a copy, not sync: later changes on either device do not merge.
- **Done when** export, clear site data, import yields an identical Grid, Trash and history.

### F-11 · Themes

- Darkroom theme (light and dark) and one built-in alternative (ADR-0013).
- Theme picker; light or dark follows the system by default, with a manual override.
- **Done when** every theme passes WCAG 2.2 AA contrast.

### F-12 · Installable PWA

- Installable to the home screen, launches full screen and works offline after the first visit (ADR-0011).

---

## Non-functional requirements

| Area | Requirement |
|---|---|
| Accessibility | WCAG 2.2 AA; 44 px touch targets; drag alternatives; screen-reader labels; reduced motion ([design principles](design-principles.md)). |
| Privacy | No accounts, analytics or network calls beyond loading the app. Photos leave the device only through Share Handoff or Backup (ADR-0008). |
| Performance | The Grid uses small generated thumbnails, never originals. The app is interactive in under 2 seconds on a mid-range phone after the first load. |
| Quality | CI gates described in the [testing strategy](testing-strategy.md). |

## Out of scope for Phase 1

Video and Reels (ADR-0001), Instagram API sync and publishing (ADR-0003), import of Published Posts (ADR-0007), multiple Profiles (ADR-0004), custom theme editor and free-angle straightening (ROADMAP), captions and hashtags, scheduling, cloud sync.

## Pending items that affect this phase

P-01 (multi-photo share), P-03 (new Post placement), P-04 (testing review) and P-05 (storage persistence), described in the [model document](model.md), section 10.

## Changes

| Version | Date | Change | Reason |
|---|---|---|---|
| 0.1 | 2026-10-23 | Features renumbered F-01 to F-12; values replaced by parameter names; rules, risks and open questions moved to the model document and cited | Set up SDD documentation |
