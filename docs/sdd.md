# Griddy — Technical Specification (SDD)

The contract for implementing Griddy without ambiguity. It derives from the model level and cites it by identifier instead of repeating it.

- **Version:** 0.3
- **Based on:** model v0.1 (`model.md`), Phase 1 spec v0.2 (`poc-spec.md`)
- **Date:** 2026-10-24
- **Status:** Draft, stage A (skeleton)

## 0. How to use this document

**For whoever implements, person or agent:**

- Implement only what is specified here. If something is ambiguous, stop and ask instead of deciding.
- Never change the model from the implementation. If the model is wrong or incomplete, raise it and fix it upstream first ([docs/README.md](README.md)).
- Follow the stages in section 10.
- Each module states, in a header comment, which SDD sections and model identifiers it implements.

**Identifiers defined here:** `T-xx` minor technical decisions (section 11), `INV-xx` invariants (section 6), `PR-xx` tests (section 9). Model identifiers (`ADR-NNNN`, `S-xx`, `R-xx`, `P-xx`, `F-xx`) are cited, never redefined.

**Build stages of this document:**

| Stage | Sections | Owner review |
|---|---|---|
| A. Skeleton | 0 to 3, titles of the rest, traceability matrix | — |
| B. Core | 4, 5 (domain and storage) and 6 | Yes |
| C. Rest | 5 (UI and platform), 7 and 8 | Yes |
| D. Tests | 9 | Yes, together with P-04 |
| E. Closing | 10, verification against the model | Yes |

## 1. Implementation scope

- **Phase 1:** features F-01 to F-12 of the [Phase 1 spec](poc-spec.md).
- **Pending items:**

| Pending | Blocks | Plan |
|---|---|---|
| P-01 | Completion of F-06 | Verify first with a minimal test page on the owner's phone (`experiments/p01-share/`, T-03, T-04); implement the fallback if it fails |
| P-03 | Nothing | Implement R-05 as written; placement is isolated in one function |
| P-04 | Section 9 | Review when the project skeleton exists |
| P-05 | Nothing | F-09 reports the actual result; backups mitigate |

- **Technical risk:** rendering up to `MAX_SLIDES` full-resolution photos for export may exhaust memory on mid-range phones. Mitigation: render Slides sequentially and release each bitmap before the next (detail in section 5, stage C).

## 2. Stack and code structure

Stack fixed by ADR-0002: React, TypeScript in strict mode, Vite. Hosting by ADR-0009. PWA by ADR-0011.

Module layout (T-01):

| Module | Responsibility | May depend on |
|---|---|---|
| `src/domain` | Entities, rules R-xx and invariants as pure functions. No browser APIs, no React. | `src/config` |
| `src/config` | Parameters from the model (T-02). | — |
| `src/storage` | Repository interface and its IndexedDB implementation (ADR-0008). | `src/domain` |
| `src/platform` | Adapters for share, file picking, persistent storage and rendering; web now, Capacitor later (ADR-0002). | `src/domain` |
| `src/features` | Use cases: create Post, reorder, share, restore Snapshot… | `src/domain`, `src/storage`, `src/platform` |
| `src/ui` | React components, theming (ADR-0013), accessibility. | `src/features`, `src/domain` |

Dependencies point inward only: `ui → features → storage / platform → domain → config`. Lint rules enforce it.

Throwaway experiments live outside `src/`, in `experiments/` (T-03).

Libraries: decided in section 11 as they are chosen.

## 3. Configuration

- Every parameter of the model (model section 7) is exported from `src/config/parameters.ts` under the same name. Values are not repeated in this document.
- A unit test compares `src/config/parameters.ts` with the model's Parameters table, so the two cannot drift (planned as a PR in section 9).
- Derived values, such as export heights per Aspect Ratio, are computed from parameters in `src/domain`, never written by hand.

## 4. Data structures

Pending (stage B). Must cover Profile, Post, Slide, Photo, Crop, Snapshot and Theme (model section 5), with stable IDs and timestamps on every entity (ADR-0008).

## 5. Components

Pending (stages B and C).

## 6. Invariants

Pending (stage B).

## 7. Outputs and interfaces

Pending (stage C). Must cover the Export Quality image format (R-12) and the backup file format with its version (F-10).

## 8. Errors and edge cases

Pending (stage C).

## 9. Test plan

Pending (stage D). Approach in the [testing strategy](testing-strategy.md).

## 10. Implementation stages

Pending (stage E). The first stage is the minimal test page that resolves P-01 (`experiments/p01-share/`, T-03).

## 11. Technical decisions

Significant technical decisions are ADRs of type Technical (ADR-0002, ADR-0009). Smaller ones are recorded here.

### T-01 · Layered module structure with inward dependencies

- **Origin:** ADR-0002, ADR-0008
- **Decision:** the module layout and dependency rule of section 2.
- **Why:** keeps the domain testable without a browser and lets storage and platform adapters be swapped (cloud sync, Capacitor) without touching UI or rules.
- **Alternatives:** feature folders with mixed concerns (faster at first, but storage and platform code leak everywhere).

### T-02 · Parameters in a single configuration module

- **Origin:** model section 7
- **Decision:** parameters live in `src/config/parameters.ts` with the model's names; no literal values elsewhere in the code.
- **Why:** one place to change a value; a test keeps it equal to the model.
- **Alternatives:** values inline where used (drift and hidden duplicates).

### T-03 · Experiments as self-contained pages in `experiments/`

- **Origin:** CLAUDE.md working rules (experiments that resolve a `P-xx` stay out of `src/`)
- **Decision:** each experiment lives in `experiments/<p-xx>-<slug>/` as a static page with no build step, no dependencies and no network calls, plus a README stating which pending item it resolves and how to run it. Values it borrows from the model (for example `EXPORT_WIDTH_PX`) are copies marked as such; the app never imports from `experiments/`. Once the result is recorded in the model, the folder is kept as a record or removed.
- **Why:** an experiment can run on the owner's phone before the project skeleton exists, and cannot leak into the app.
- **Alternatives:** a route inside the future app (needs the skeleton first, delaying P-01); a claude.ai artifact (Web Share inside a sandboxed frame is not guaranteed, and the URL is not owner-controlled, as in ADR-0009).

### T-04 · Publish experiments on GitHub Pages before the app exists

- **Origin:** ADR-0009, T-03
- **Decision:** the `Pages` workflow publishes `experiments/` under `/experiments/` on GitHub Pages after the `Docs` workflow passes on a push to `main`. When the app's build pipeline exists it takes over the Pages deployment and decides whether experiments stay published.
- **Why:** Web Share with files needs HTTPS; Pages is the hosting already decided and gives an owner-controlled URL at no cost.
- **Alternatives:** a third-party proxy serving files from GitHub (an extra service for no gain); local network serving (no HTTPS, so sharing files is unavailable).

## 12. Traceability matrix

Every accepted ADR, every rule and every feature appears here. Planned locations until code exists.

| Item | SDD sections | Modules | Tests |
|---|---|---|---|
| ADR-0001 | 4 | `domain` | Pending |
| ADR-0002 | 2, T-01 | All | — |
| ADR-0003 | 5, 7 | `platform`, `features` | Pending |
| ADR-0004 | 4 | `domain`, `storage` | Pending |
| ADR-0005 | 2 | `ui` | — |
| ADR-0006 | 4, 5 | `domain`, `platform` | Pending |
| ADR-0007 | 5 | `domain`, `features` | Pending |
| ADR-0008 | 2, 4, 5 | `storage` | Pending |
| ADR-0009 | 10 | CI | — |
| ADR-0010 | 4, 5 | `domain`, `storage`, `features` | Pending |
| ADR-0011 | 10 | `ui` | Pending |
| ADR-0012 | 5 | `ui` | Pending |
| ADR-0013 | 5 | `ui` | Pending |
| R-01 | 5, 6 | `domain` | Pending |
| R-02 | 5, 6 | `domain` | Pending |
| R-03 | 4, 5, 6 | `domain`, `platform` | Pending |
| R-04 | 5 | `domain` | Pending |
| R-05 | 5, 6 | `domain` | Pending |
| R-06 | 5 | `domain` | Pending |
| R-07 | 5 | `domain`, `features` | Pending |
| R-08 | 5 | `domain` | Pending |
| R-09 | 5 | `domain`, `features` | Pending |
| R-10 | 5 | `domain`, `storage` | Pending |
| R-11 | 5, 6 | `storage` | Pending |
| R-12 | 5, 7 | `domain`, `platform` | Pending |
| R-13 | 5 | `domain`, `ui` | Pending |
| F-01 | 5 | `ui` | Pending |
| F-02 | 5 | `features`, `ui` | Pending |
| F-03 | 5 | `features`, `ui` | Pending |
| F-04 | 5 | `features`, `ui` | Pending |
| F-05 | 5 | `features`, `ui` | Pending |
| F-06 | 5, 7 | `platform`, `features`, `ui` | Pending |
| F-07 | 5 | `features`, `ui` | Pending |
| F-08 | 5 | `features`, `ui` | Pending |
| F-09 | 5 | `storage`, `platform`, `ui` | Pending |
| F-10 | 5, 7 | `storage`, `features`, `ui` | Pending |
| F-11 | 5 | `ui` | Pending |
| F-12 | 10 | `ui` | Pending |

## 13. Changes

| Version | Date | Change | Reason |
|---|---|---|---|
| 0.1 | 2026-10-23 | Stage A skeleton: scope, stack, structure, configuration, T-01 and T-02, traceability matrix | Based on model v0.1 and Phase 1 spec v0.1 |
| 0.2 | 2026-10-24 | "Based on" updated to Phase 1 spec v0.2; no content change | Phase 1 spec approved |
| 0.3 | 2026-10-24 | T-03 (experiments folder) and T-04 (experiments on GitHub Pages); P-01 plan and section 10 point to the test page | P-01 test page |
