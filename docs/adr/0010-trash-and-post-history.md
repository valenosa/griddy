# ADR-0010: Instant delete with Undo, Trash, and per-Post history

- **Status:** Accepted
- **Date:** 2026-10-23
- **Type:** Product

## Context

Deleting must be fast (no confirmation dialogs), but mistakes must be recoverable, both for whole Posts and for edits inside a Post: crops, photo replacements, added or removed Slides, reordering, ratio changes.

## Alternatives considered

- **Confirmation dialog before every delete.** Rejected: slow, and users click through dialogs without reading.
- **Undo toast only.** Rejected: a mistake noticed minutes later is unrecoverable.
- **Global undo stack instead of per-Post history.** Rejected: undoing one Post's mistake would undo unrelated later work on other Posts.
- **Snapshots that copy images.** Rejected: storage would explode; unnecessary because media is immutable.

## Decision

- **Undo toast:** every destructive action executes immediately and offers Undo for `UNDO_WINDOW_SECONDS`.
- **Trash:** deleted Posts move to a Trash and can be restored for `TRASH_RETENTION_DAYS`, then are purged.
- **Post history:** every change to a Post records a **Snapshot** that can be restored. Retention: `HISTORY_RETENTION_DAYS` or the last `HISTORY_MIN_SNAPSHOTS` Snapshots per Post, whichever keeps more.
- **Immutable media:** photos are stored once and never modified; Snapshots reference photos by ID.

## Consequences

- History is cheap to store because Post state without images is small.
- Replaced or removed photos stay on the device until no Post, Trash item or Snapshot references them (R-11); storage use is shown in Settings.
- Snapshots are a natural unit for future cloud sync.
