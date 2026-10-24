# Griddy

A mobile-first planner for your Instagram grid. Arrange posts, build carousels, frame every photo, preview exactly how your profile will look, then hand each post to Instagram at full quality without digging through your gallery again.

## Status

Phase 1 (web PoC): the [Phase 1 spec](docs/poc-spec.md) is approved; implementation has not started. Sharing to Instagram was verified on the owner's phone ([P-01 test](experiments/p01-share/README.md), ADR-0014).

Next steps, in order:

1. SDD stage B: data structures, core components and invariants ([SDD](docs/sdd.md)), with owner review.

## Highlights (Phase 1)

- Drag-to-reorder grid with Instagram's current portrait thumbnails
- Carousels with fast slide reordering, adding, removing and replacing
- 1:1, 4:5 and 3:4 posts with non-destructive framing
- Share straight to Instagram at export quality
- Undo, trash and per-post history
- Local-first and private: your photos never leave your device unless you share them
- Installable PWA, works offline

## Documentation

Griddy is built with Spec-Driven Development. Start at [docs/README.md](docs/README.md) for the map of documents, or jump to:

- [Model document](docs/model.md): what Griddy does and why
- [Architecture decisions](docs/adr/README.md)
- [Roadmap](ROADMAP.md)
- [Phase 1 spec](docs/poc-spec.md)
- [Technical specification (SDD)](docs/sdd.md)

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).
