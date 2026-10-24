# ADR-0011: Ship the web app as an installable PWA

- **Status:** Accepted
- **Date:** 2026-10-23
- **Type:** Product

## Context

The owner uses Griddy on a phone and wants it to feel like an app before the APK exists. Planning sessions may happen without connectivity.

## Alternatives considered

- **Plain website.** Rejected: opens inside the browser chrome and needs a connection.
- **Wait for the APK.** Rejected: delays daily use, and the web version remains useful for iOS and open-source users.

## Decision

The web app is a Progressive Web App: web manifest, home-screen install, full-screen launch and offline support through a service worker.

## Consequences

- The web version stays a first-class channel after the APK exists.
- Inside the Capacitor APK the service worker is disabled.
