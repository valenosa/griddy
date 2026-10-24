# Glossary

Domain language of **Griddy**. Code, docs and UI use these terms with exactly these meanings. Behavior rules (`R-xx`) and parameters live in the [model document](docs/model.md).

| Term | Definition | See |
|---|---|---|
| **Aspect Ratio** | The shape shared by every Slide of a Post: `1:1`, `4:5` or `3:4`. Set per Post, never per Slide. | R-02, ADR-0006 |
| **Carousel** | A Post with two or more Slides. | R-01 |
| **Cover** | The first Slide of a Post; it is what appears in the Grid. | R-04 |
| **Crop** | How a Slide's photo is framed inside an Aspect Ratio: position, zoom and rotation. Stored per Slide and per Aspect Ratio; the photo itself is never modified. | R-03 |
| **Export Quality** | A Slide rendered from its photo and Crop at the size Instagram displays. | R-12 |
| **Grid** | The ordered collection of Posts in a Profile, three per row, newest at top-left. | R-05 |
| **Grid Thumbnail** | How a Post's Cover appears in the Grid on mobile Instagram, independent of the Post's Aspect Ratio. | R-13 |
| **Next Post** | The Planned Post that should be published next. | R-06 |
| **Photo** | An original image file added by the user. Stored once, never modified. | R-03, R-11 |
| **Planned Post** | A Post that exists only in Griddy. Editable. | R-07 |
| **Post** | One Grid tile, with one or more Slides and one Aspect Ratio. | |
| **Profile** | One Instagram account whose Grid is planned. | ADR-0004 |
| **Publish Order** | Planned Posts are published bottom-up, starting with the Next Post, because Instagram places the newest post at top-left. | R-06 |
| **Published Post** | A Post that exists on Instagram. Not editable or movable. | R-05, ADR-0007 |
| **Replace** | Swapping a Slide's photo for another, for example an edited version, keeping its position and Crop. | F-03 |
| **Share Handoff** | Sending a Planned Post's Slides, in order and at Export Quality, to the Android share sheet. | ADR-0003, R-14 |
| **Slide** | One media item inside a Post. Photos only in Phase 1. | ADR-0001 |
| **Snapshot** | A saved state of a Post, recorded on every change, that can be restored. | R-10 |
| **Theme** | A named set of color tokens with light and dark variants. | ADR-0013 |
| **Trash** | Holds deleted Posts temporarily so they can be restored. | R-09 |
