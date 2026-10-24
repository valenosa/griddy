# ADR-0002: React + TypeScript + Vite as the application stack

- **Status:** Accepted
- **Date:** 2026-10-23

## Context

The project is both a personal tool and a portfolio piece aimed at the international market. It starts as a mobile web app and is expected to become an Android APK later.

## Decision

Build the app with **React + TypeScript + Vite**, hosted in a Git repository. The same codebase will be wrapped with **Capacitor** for the Android build.

## Alternatives considered

- **Single hand-written HTML file:** fastest to start, weak as a portfolio piece, hard to grow.
- **Native Android (Kotlin):** best device integration, but no web version and requires a full rewrite of the PoC.
- **React Native / Flutter:** viable, but the PoC must run in a phone browser today, which favors a web-first stack.

## Consequences

- One codebase for web and Android.
- Device-specific features (file storage, share) must sit behind small adapters so the web and Capacitor implementations can differ.
