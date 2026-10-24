# Architecture Decision Records

Every significant decision about Griddy is recorded here, one file per decision. ADRs are the project's decision register: the model document and the SDD cite them by ID (`ADR-0006`) and never restate their reasoning.

## Index

| ADR | Title | Type | Status |
|---|---|---|---|
| [ADR-0001](0001-photos-only-poc-media-roadmap.md) | Photos-only PoC, staged media roadmap | Product | Accepted |
| [ADR-0002](0002-react-typescript-vite.md) | React + TypeScript + Vite as the application stack | Technical | Accepted |
| [ADR-0003](0003-share-handoff-now-graph-api-later.md) | Share Handoff in the PoC, Instagram API publishing as a priority phase | Product | Accepted |
| [ADR-0004](0004-single-profile-multi-profile-ready.md) | Single Profile in the PoC, model ready for many | Product | Accepted |
| [ADR-0005](0005-english-everywhere.md) | English for code, docs and UI | Product | Accepted |
| [ADR-0006](0006-post-level-aspect-ratio-non-destructive-crop.md) | Aspect Ratio per Post, non-destructive Crop per Slide | Product | Accepted |
| [ADR-0007](0007-no-published-post-import-in-poc.md) | No import of Published Posts in the PoC; sync is required for stable | Product | Accepted |
| [ADR-0008](0008-local-first-optional-backend.md) | Local-first architecture with an optional backend | Product | Accepted |
| [ADR-0009](0009-github-pages-hosting.md) | Host the web app on GitHub Pages | Technical | Accepted |
| [ADR-0010](0010-trash-and-post-history.md) | Instant delete with Undo, Trash, and per-Post history | Product | Accepted |
| [ADR-0011](0011-installable-pwa.md) | Ship the web app as an installable PWA | Product | Accepted |
| [ADR-0012](0012-mobile-first.md) | Mobile-first, desktop supported | Product | Accepted |
| [ADR-0013](0013-theming-with-design-tokens.md) | Theming through design tokens | Product | Accepted |

`python tools/verify_docs.py` checks that this index matches the files.

## Types

Ask: **would two implementations that differ in this decision give the user a different result?**

- **Product:** yes. It changes what users see, can do or risk (Trash retention, mobile-first, local-first storage).
- **Technical:** no. It changes how Griddy is built, not what it does (framework, hosting).

Small implementation choices that do not deserve an ADR go in the SDD as `T-xx` entries.

## Statuses

| Status | Meaning |
|---|---|
| Proposed | Under discussion; not to be implemented yet. |
| Accepted | In force. |
| Superseded by ADR-NNNN | Replaced; kept for history. |
| Deprecated | No longer applies, with no replacement. |

## Rules

1. **Copy [template.md](template.md)** to `NNNN-short-title.md` with the next free number. Numbers are never reused.
2. **Accepted ADRs are immutable.** To change a decision, write a new ADR and mark the old one `Superseded by ADR-NNNN`. Typo and link fixes are fine.
3. **Add the row to the index** in the same commit.
4. **Propagate:** update the model document and the SDD sections that cite the decision, in the same commit (see [docs/README.md](../README.md)).
