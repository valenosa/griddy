# Phase 1 — Web PoC Specification

- **Status:** Draft, pending owner approval
- **Date:** 2026-10-23
- Terms follow [CONTEXT.md](../CONTEXT.md). Decisions are referenced by ADR number.

## Goal

Plan an Instagram grid of photo Posts and Carousels on an Android phone, see an accurate preview, and hand each Post to Instagram at full quality without searching the gallery again.

## Target platforms

- **Primary:** latest two versions of Chrome on Android (ADR-0012).
- **Supported:** latest desktop Chrome, Firefox and Safari. Where the share sheet is unavailable, Share Handoff falls back to downloading the files.

---

## Features and acceptance criteria

### F1 — Grid
- Shows all Posts of the Profile in 3 columns with Instagram's mobile 3:4 Grid Thumbnails and spacing, newest at top-left.
- Carousels show a multi-photo badge.
- The Next Post (lowest Planned Post, ADR-0007) is highlighted.
- Published Posts appear below Planned Posts and are visually distinguished and locked.
- Header shows counts of Planned and Published Posts.
- **Done when** a grid of 60 Posts renders and scrolls smoothly on a mid-range Android phone.

### F2 — Create a Post
- "New post" opens the photo picker with multi-select (1–20 photos).
- Slides are created in selection order, each with a centered Crop.
- Default Aspect Ratio: 4:5. The new Post is placed at the top of the Grid.
- **Done when** a 10-photo Carousel can be created in under 15 seconds from tapping "New post".

### F3 — Post editor
- Swipe through Slides at the Post's Aspect Ratio.
- Thumbnail strip: reorder Slides with long-press drag, or "Move" with arrow buttons.
- Add photos (respecting the 20-Slide limit), remove a Slide (Undo toast), Replace a Slide's photo keeping position and Crop.
- Share a single Slide's **original** photo to another app (e.g. Snapseed).
- Switch Aspect Ratio between 1:1, 4:5 and 3:4; every Slide follows (ADR-0006).
- Removing the last Slide deletes the Post (to Trash).
- Slides are previewed at Export Quality (1080 px wide, rendered from original + Crop), so the editor shows what Instagram will show. The original is used only for reframing and for sharing the original to other apps.
- **Done when** every action above is reachable with one hand on a 6" screen and is reflected immediately in the Grid.

### F4 — Reframe a Slide
- Opens from the editor. Drag to position, pinch to zoom; desktop uses drag + wheel/slider.
- The photo always covers the frame (no empty edges).
- The Crop is stored per Aspect Ratio; switching ratio and back restores it.
- Rotate in 90° steps. The Crop model stores rotation in degrees from day one, so free-angle straightening (later phase) needs no data migration.

### F5 — Reorder the Grid
- Long-press a Post and drag it to a new position.
- Accessible alternative: tap a Post → "Move" → buttons to move one position or one row; keyboard arrows on desktop.
- Published Posts cannot be moved and Planned Posts cannot be moved below them.

### F6 — Share Handoff and publishing state
- "Share" on a Planned Post renders every Slide at Export Quality (1080 px wide, JPEG, sRGB, high quality) in Slide order and opens the share sheet with all files.
- Fallback: download the files, numbered in order (`01.jpg`, `02.jpg`…).
- On return, Griddy asks "Did you publish it?"; "Yes" marks the Post as Published.
- A Published Post can be returned to Planned ("Mark as planned") to fix mistakes.
- **Done when** a 10-Slide Carousel reaches Instagram's post composer with all photos in the correct order (see Risk R1).

### F7 — Delete, Undo and Trash (ADR-0010)
- Deleting a Post is immediate with an Undo toast (5 seconds).
- Deleted Posts go to Trash, restorable for 30 days, purged automatically afterwards.
- "Empty trash" deletes permanently after one confirmation (the only confirmation dialog in the app).

### F8 — Post history (ADR-0010)
- Every change to a Post records a Snapshot with timestamp and a short label ("Reordered slides", "Changed to 1:1").
- The history lists Snapshots newest first, with a preview; restoring one records a new Snapshot, so restores are undoable.
- Retention: 30 days or the last 50 Snapshots per Post, whichever keeps more.

### F9 — Storage (ADR-0008)
- All data in IndexedDB; photos stored once and never modified.
- Persistent storage is requested when the first photo is added; the result is shown in Settings.
- Settings shows storage used (photos, history, trash).

### F10 — Backup
- "Export backup" produces one file containing all data and original photos.
- "Import backup" restores it, replacing current data after one confirmation.
- A backup made on one device can be imported on any other device running Griddy (e.g. phone → desktop via Google Drive). This is a copy, not sync: later changes on either device do not merge.
- **Done when** export → clear site data → import yields an identical Grid, Trash and history.

### F11 — Themes (ADR-0013)
- Darkroom theme (light and dark) and one built-in alternative.
- Theme picker; light/dark follows the system by default with a manual override.
- All themes pass WCAG 2.2 AA contrast.

### F12 — Installable PWA (ADR-0011)
- Installable to the home screen, launches full screen, works fully offline after the first visit.

---

## Non-functional requirements

| Area | Requirement |
|---|---|
| Accessibility | WCAG 2.2 AA; 44 px touch targets; drag alternatives; screen-reader labels; reduced motion (see design principles). |
| Privacy | No accounts, analytics or network calls beyond loading the app. Photos never leave the device except through Share Handoff or Backup. |
| Performance | Grid uses small generated thumbnails, never full-resolution originals. App interactive in under 2 s on a mid-range phone after first load. |
| Quality | CI gates: typecheck, lint, unit and integration tests, end-to-end tests, accessibility checks (see testing strategy). |

## Out of scope for Phase 1

Video, Reels, Instagram API (sync and publishing), import of existing Published Posts, multiple Profiles, custom theme editor, captions and hashtags, scheduling, cloud sync.

## Risks to verify first

- **R1 — Multi-photo share into Instagram.** Whether Instagram on Android accepts several images from the web share sheet as one Carousel, and keeps their order, must be tested on a real phone before building F6 in full. Fallback: share one at a time in order, or numbered downloads.
- **R2 — Storage eviction.** Behavior of persistent storage on the owner's phone and browser; mitigated by Backup.
- **R3 — Large photos.** Memory use when rendering 20 full-resolution photos for export on a mid-range phone; render sequentially.

## Revisit later

- Whether new Posts go to the top of the Grid or next to the Next Post (owner unsure; top chosen for now).
