# Formulas, limits, and sources

## Formulas (aids — declare intent)

| Intent | Aid |
|--------|-----|
| Circle same **area** as square side *s* | \( d = s\sqrt{4/\pi} \approx 1.1284\,s \) |
| Equilateral triangle mass center | Geometric centroid (diagnostic) |
| Type overshoot order of magnitude | ~1–3% cap/x-height for rounds; points often more (face-specific) |

Snap to pixels when crispness requires it.

## Hard limits

1. No universal pixel offset.
2. Context (size, stroke, neighbors, DPR) changes results.
3. Accessibility and targets outrank pure polish.
4. Fonts encode overshoot—do not fight the face.
5. Centroid ≠ guaranteed perceptual center.
6. Equal area ≠ equal visual weight ≠ equal prominence.
7. Physical optics / lab alignment are out of scope.

## Source hygiene

Each technical claim should be traceable when challenged:

| Field | Purpose |
|-------|---------|
| Name | Identify material |
| URL | Verify |
| Category | Standard / docs / article / research |
| Supported claim | What it actually backs |
| Limits | Avoid over-claim |
| Last checked | Freshness |

### Core sources (topics verified in project research; re-open URLs when making compliance claims)

| Source | Supports |
|--------|----------|
| Tobias Frere-Jones — Typeface Mechanics | Overshoot; eye over pure ruler |
| Wikipedia — Overshoot (typography); Optical margin alignment | Definitions; secondary pointers |
| MDN — `font-optical-sizing`; Variable fonts | CSS optical sizing behavior |
| Google Fonts Knowledge — Optical Size axis | `opsz` concept |
| Marc Edwards (Bjango) — Formulas for optical adjustments | Area scale; centroid discussion |
| Material Design — icon keylines | Live area by shape family |
| Apple Human Interface Guidelines — Icons / related | Platform icon composition; **cite specific page** when attributing |
| Microsoft Learn — character design standards; XAML OpticalMarginAlignment | Visual equality in type; specific API behavior |
| W3C WCAG 2.2 | Applicable a11y constraints |
| Luke Jones — Optical Adjustment | UI heuristic examples |
| Slava Shestopalov — Optical effects in UI | Icon/button optical tips |
| Ivan Grekov (Bumble) — Optical alignment for FE | Production/barycentre framing |

Secondary language posts (UX Collective Brasil, etc.) are teaching aids—prefer primary type/platform sources for mechanics.

## Competitive landscape note

Claims that this is the “only” specialized agent skill are **time-bound audits**, not permanent proof. Re-search before marketing exclusivity.

## Glossary

| Term | Meaning |
|------|--------|
| Optical adjustment / alignment | Deliberate deviation from pure geometry for perceived balance |
| Visual weight | Perceived mass from area, density, contrast, asymmetry |
| Overshoot | Rounds/points past flat guides |
| Keyline | Shape-specific live area inside a shared frame |
| Geometric centroid | Area center of mass |
| Alpha-weighted centroid | Opacity-weighted center |
| Perceptual center | Judged visual balance in context |
