# Testing Strategy (draft, pending review)

## Layers

| Layer | Tool | What it covers |
|---|---|---|
| **Unit** | Vitest | Pure domain logic with no browser APIs: reordering Posts and Slides, Publish Order and Next Post, Crop math per Aspect Ratio, snapshot creation and restore, Trash expiry rules, backup serialization. |
| **Integration** | Vitest + fake-indexeddb | The storage repository against a real IndexedDB implementation: save/load, photo garbage collection, backup export → import round trip. |
| **End-to-end** | Playwright, mobile viewport (Pixel-class device) | Critical user flows in a real browser. |
| **Accessibility** | axe-core inside Playwright | Automated WCAG checks on every main screen. |
| **Static** | TypeScript strict, ESLint, Prettier | Type errors, code smells, formatting. |

## Critical end-to-end flows

1. Create a carousel from several photos, reorder Slides, remove one, add one.
2. Reorder the Grid with long-press drag, and with the accessible "Move" alternative.
3. Switch a Post between 1:1, 4:5 and 3:4 and confirm Crops are preserved.
4. Delete a Post, Undo it; delete again, restore it from Trash.
5. Edit a Post several times and restore an earlier snapshot.
6. Share Handoff produces images at Export Quality, in Slide order.
7. Export a backup, clear data, import it, and get the same Grid.

## CI

GitHub Actions on every push and pull request: typecheck → lint → unit/integration → build → end-to-end. Deploy to GitHub Pages only from `main` when everything passes.

## Not automated (manual checklist)

- Real Android share sheet into Instagram and Snapseed.
- PWA install on a physical device.
