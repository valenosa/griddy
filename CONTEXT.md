# Domain Context & Glossary

> Project: **Griddy**
> This file is the single source of truth for domain language. Code, docs and UI must use these terms.

## Purpose

A mobile-first planner to design an Instagram profile grid before publishing: arrange posts, build carousels, preview exactly how the profile will look, and hand finished posts to Instagram without hunting for the photos again.

## Glossary

| Term | Definition | Notes |
|---|---|---|
| **Profile** | One Instagram account whose grid is being planned. | PoC supports exactly one. Modeled as an entity so multi-profile is possible later (ADR-0004). |
| **Grid** | The ordered collection of Posts shown in a Profile, 3 per row, newest at top-left. | Mirrors the Instagram profile view. |
| **Post** | One grid tile. Contains one or more Slides and has one Aspect Ratio. | A Post with one Slide is a single-photo post. |
| **Slide** | One media item inside a Post. | PoC: photos only (ADR-0001). |
| **Carousel** | A Post with 2 or more Slides. | Max 20 when posting from the Instagram app; max 10 via the publishing API. |
| **Cover** | The first Slide of a Post; it is what appears in the Grid. | Reordering Slides can change the Cover. |
| **Aspect Ratio** | The shape shared by every Slide of a Post: `1:1`, `4:5` or `3:4`. | Set per Post, never per Slide (ADR-0006). |
| **Crop** | How a Slide's original photo is framed inside the Post's Aspect Ratio (position + zoom). | Stored per Slide and per Aspect Ratio; the original photo is never modified. |
| **Grid Thumbnail** | How a Post's Cover appears in the Grid: a center 3:4 crop on mobile. | Independent of the Post's Aspect Ratio. |
| **Planned Post** | A Post that exists only in Griddy, not yet on Instagram. | Editable. |
| **Published Post** | A Post that already exists on Instagram. | Not editable. PoC: only Posts marked published from Griddy; external sync arrives with the API phase (ADR-0007). |
| **Publish Order** | Planned Posts must be published bottom-up: the one closest to the Published Posts goes first. | Because Instagram places the newest post at top-left. |
| **Next Post** | The Planned Post that should be published next according to Publish Order. | Highlighted in the UI. |
| **Share Handoff** | Sending a Planned Post's Slides, in order and at export quality, to the Android share sheet. | PoC publishing mechanism (ADR-0003). After sharing, the user confirms whether it was published. |
| **Replace** | Swapping a Slide's photo for another (e.g. an edited version from Snapseed), keeping its position and Crop. | |
| **Trash** | Holds deleted Posts for 30 days so they can be restored. | ADR-0010. |
| **Snapshot** | A saved state of a Post, recorded on every change, that can be restored. | ADR-0010. |
| **Export Quality** | Slides rendered at 1080 px wide: 1080×1080 (1:1), 1080×1350 (4:5), 1080×1440 (3:4). | |

## Known platform constraints

- Instagram crops every Slide of a Carousel to the first Slide's ratio.
- The publishing API accepts only ratios from 4:5 to 1.91:1, so **3:4 Posts cannot be published via the API**, and carousels via the API are limited to **10 Slides**. Relevant for the API phase.
- Reading a Profile's grid or publishing automatically requires a professional (Creator or Business) Instagram account.

## Open questions

- Distribution model: open-source self-hosted vs. paid hosted product (see grilling session).
