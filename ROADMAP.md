# Roadmap

Preliminary. Each phase ends in a usable release and gets its own spec before implementation.

## Phase 1 — Web PoC

Spec: [docs/poc-spec.md](docs/poc-spec.md)

- Grid with long-press drag reordering
- Photo Posts and Carousels: add, remove and reorder Slides
- Aspect Ratio per Post (1:1, 4:5, 3:4) with non-destructive Crop
- Grid preview matching Instagram's mobile 3:4 thumbnails
- Next Post indicator and Share Handoff at Export Quality
- Local storage with persistent-storage request
- Backup export / import
- Undo, Trash and per-Post history
- Installable PWA, mobile-first layout with desktop support
- Darkroom theme (light + dark) plus one built-in alternative, theme picker

## Phase 2 — Android APK
- Wrap the web app with Capacitor
- Native share and file storage adapters

## Phase 3 — Instagram API (required for first stable release)
- Sync Published Posts from the real Profile
- Publish directly from Griddy
- Backend and cloud media hosting
- Flag Posts that the API cannot publish (S-02)

## Phase 3.5 — Editing and personalization
- Theme editor with contrast validation, save and share themes
- Free-angle straightening (slider, alignment grid, automatic zoom to cover the frame)

## Phase 4 — Video inside Carousels
## Phase 5 — Standalone video Posts
## Phase 6 — Reels
## Phase 7 — Multiple Profiles
