# Design Principles

## 1. Photos first
The interface is quiet so the photos are the loudest thing on screen. Neutral surfaces, one accent color, no decorative gradients.

## 2. Own identity, faithful preview
Griddy has its own look. Only the Grid preview mimics Instagram's geometry (3 columns, 3:4 mobile thumbnails, spacing) so the preview is trustworthy. No Instagram logos, icons or brand colors.

## 3. Avoid the generic "AI-generated" look
- No default component-library styling left untouched.
- No purple-to-blue gradients, glassmorphism, emoji used as icons, or oversized rounded cards everywhere.
- A deliberate type pairing, a real spacing scale and consistent icon set.
- Microcopy written by a person: short, specific, no filler.

## 4. Fast like Instagram
Gestures over dialogs: long-press to drag, swipe through Slides, instant delete with Undo (ADR-0010).

## 5. Accessible by default (WCAG 2.2 AA)
- Text and controls meet contrast requirements in light and dark themes.
- Touch targets at least 44×44 px.
- Every drag interaction has a non-drag alternative (e.g. "Move" mode with arrow buttons), as required by WCAG 2.5.7.
- Screen-reader labels on every Post and Slide ("Post 3 of 12, carousel, 4 photos, 4:5").
- Respects reduced-motion and system theme.
