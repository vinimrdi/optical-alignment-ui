# Examples — Optical Alignment UI

Worked findings in the skill output format (severity × confidence × outcome). Illustrative inspections—not live product measurements. Pixel values, when shown, are **case-specific**, not universal rules.

## Core set

| File | Scenario |
|------|----------|
| [play-button.md](play-button.md) | Play triangle in a circular control |
| [icon-label-pair.md](icon-label-pair.md) | Chevron + text label |
| [circle-vs-square.md](circle-vs-square.md) | Avatar circle vs rounded-square thumb |
| [icon-set-toolbar.md](icon-set-toolbar.md) | Mixed silhouettes in one toolbar |

## Regression / failure modes (v1.5)

| File | Scenario |
|------|----------|
| [svg-bad-viewbox.md](svg-bad-viewbox.md) | “Optical” bug that is actually bad viewBox |
| [outline-vs-filled.md](outline-vs-filled.md) | Same outer size, different visual weight |
| [linebox-vs-ink.md](linebox-vs-ink.md) | Text centered on line box, ink looks low |
| [icon-label-font-mismatch.md](icon-label-font-mismatch.md) | Icon tuned for one face, fallback breaks pair |
| [dpr-one-shift.md](dpr-one-shift.md) | Looks centered at 2×, soft/shifted at 1× |
| [toolbar-local-fix-breaks-set.md](toolbar-local-fix-breaks-set.md) | One icon “fixed,” row becomes uneven |
