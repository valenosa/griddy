# ADR-0011: Ship the web app as an installable PWA

- **Status:** Accepted
- **Date:** 2026-10-23

## Decision

The web app is a Progressive Web App: web manifest, home-screen install, full-screen launch and offline support through a service worker.

## Consequences

- The web version stays a first-class distribution channel after the APK exists (iOS users, open-source users, quick access without a store).
- Inside the Capacitor APK the PWA layer is unused but harmless; the service worker is disabled there.
