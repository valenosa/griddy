# ADR-0010: Instant delete with Undo, Trash, and per-Post history

- **Status:** Accepted
- **Date:** 2026-10-23

## Context

Deleting must be fast (no confirmation dialogs), but mistakes must be recoverable, both for whole Posts and for edits inside a Post (crops, photo replacements, added or removed Slides, reordering, ratio changes).

## Decision

- **Undo toast:** every destructive action executes immediately and shows an Undo toast for a few seconds.
- **Trash:** deleted Posts move to a Trash and can be restored for **30 days**, then are purged.
- **Post history:** every change to a Post records a **snapshot** of the Post's state. The user can browse the history of a Post and restore any snapshot. Retention: 30 days or the last 50 snapshots per Post, whichever keeps more.
- **Immutable media:** photos are stored once, by ID, and never modified. Snapshots reference photo IDs, so a snapshot is a few hundred bytes, not a copy of the images.
- A photo is garbage-collected only when no live Post, Trash item or snapshot references it.

## Consequences

- History is cheap to implement and store because media is immutable and Post state is small.
- Replaced or removed photos stay on the device until their history expires; storage use grows accordingly and is shown in Settings.
- Snapshots are a natural unit for future cloud sync.
