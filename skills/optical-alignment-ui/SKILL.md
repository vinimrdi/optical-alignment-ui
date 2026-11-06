---
name: optical-alignment-ui
description: >
  Optical alignment and optical adjustment for digital UI (precision vs perception).
  Use when icons look off-center, play buttons lean left, circles look smaller than
  squares, icon sets feel uneven, icon+label pairs misalign, ALL CAPS looks oversized,
  button labels sit wrong, or type needs overshoot / optical margin / font-optical-sizing.
  Apply evidence-based diagnosis, geometric vs perceptual centers, smallest effective
  correction, and design-system hand-off. Do not invent universal +2px rules, reduce
  touch targets, or treat centroid as absolute optical truth.
metadata:
  author: vinimrdi
  version: "1.5.0"
  language: en
  tags: optical-alignment, optical-adjustment, optical-centering, ui, ux, typography, icons, agent-skills, claude-code, cursor, lovable, pixel-perfect, visual-balance
---

# Optical Alignment UI — Precision vs Perception

**Agent skill** for making digital interfaces *look* balanced when mathematical alignment does not. Software centers bounding boxes; human vision weighs shape, contact with guides, contrast, and context.

Invoke as `/optical-alignment-ui` where supported, or attach this folder as context. Progressive disclosure: load [references/](references/) only when needed. Worked samples: [examples/](../../examples/).

## Compatible agents

See [docs/compatibility-and-integrations.md](../../docs/compatibility-and-integrations.md). Distinguish *format support*, *path discovery*, and *ability to follow instructions*.

## Companion skill

Task friction, heuristics, a11y: **[ux-laws-principles](https://github.com/vinimrdi/ux-laws-principles)**. Job first; optical craft second.

## Scope and rigor

Optical alignment is craft—not a single formula for every case.

| Kind | Examples |
|------|----------|
| **Heuristic / practice** | Play-icon nudge, caps size, icon+label midline |
| **Platform guidance** | Icon composition notes; Material keylines |
| **Type mechanics** | Overshoot, optical margin |
| **Engineering aid** | Area scale, geometric/alpha centroid — **diagnostic, not absolute optical truth** |

Prefer smallest effective correction. No universal pixel offsets. Re-check contrast and touch targets after changes.

## Outcomes (mandatory)

| Outcome | When |
|---------|------|
| **Implement** | Evidence sufficient, low risk, a11y safe |
| **Propose** | Plausible; needs human judgment |
| **Abstain** | No imbalance, weak evidence, or wrong skill |

## Severity and confidence (independent)

**Severity** 0–4 = impact if real. **Confidence** High / Medium / Low / Unverified = evidence strength.  
*Severity 3 + Confidence Low* → Propose or gather evidence — do not implement.

## Evidence-Based Optical Workflow

1. **Context capture** — component, size, state, background, DPR, typeface, neighbors  
2. **Baseline inspection** — native use size; light/dark if both ship  
3. **Geometric analysis** — box vs centroid vs alpha bounds; SVG metadata  
4. **Perceptual assessment** — weight, negative space, contrast; artifact vs composition  
5. **Diagnosis** — cause, severity, confidence, **compensation intent**  
6. **Minimal intervention** — preserve frame and hit target; prefer pad-in-asset  
7. **Visual validation** — before/after, set, theme, clipping  
8. **Design-system hand-off** — named exception + “do not copy blindly”  

Details: [evidence-and-validation.md](references/evidence-and-validation.md) · [geometry-and-centroids.md](references/geometry-and-centroids.md) · [accessibility-and-constraints.md](references/accessibility-and-constraints.md)

## Geometric decision matrix (summary)

| Problem | Prefer first |
|---------|--------------|
| Symmetric filled rect | Bounding-box center |
| Filled play triangle | Centroid as **check**; eye + pad-in-asset |
| Outline stroke icons | Perceptual + stroke mass; not fill centroid alone |
| Soft/raster edges | Alpha-weighted bounds if measurable |
| Circle vs square size | **Name intent** (area / weight / keyline occupancy) |
| Uneven icon set | Keylines + per-glyph weight; even frames |
| “Optical” bug with wrong viewBox | **Fix asset metadata first** |

## Reasoning rules

- Visible imbalance first, not jargon  
- Grid first; optical refine  
- Shift against visual weight  
- Color last (geometry → stroke → contrast → chroma)  
- Do not fight typeface overshoot  
- Do not one-offset an entire set  
- Check [anti-patterns.md](references/anti-patterns.md) before applying popular “fixes”  
- Explain while applying, proportionally  

## When to activate / when not

**Activate:** off-center glyphs, asymmetric icons, circle/square scale, icon+label, uneven sets, caps, overshoot/margin/`opsz`, AI UI grid-correct but optically wrong, asset hand-off.

**Skip as primary:** a11y-only; no composition; illustration-only; universal +2px; physical optics; math already matches perception.

## Analysis output format

- What observed · Evidence · Related concept  
- What / Why / Who / Where / When / How  
- Compensation intent (if scale/offset)  
- Impact · Severity · Confidence · **Outcome**  
- Trade-off · Validation plan · Hand-off name  

## Symptom → concept

| Symptom | Start here |
|---------|------------|
| Play looks left-heavy | Visual weight; centroid diagnostic |
| Circle smaller than square | Intent + area/keyline |
| Icon low/high in button | Pad-in-asset; vertical optical |
| Icon + text uneven | Line box vs ink |
| Set uneven at same box | Keylines; set review |
| Same hex, different weight | Geometry first |
| Aligned in design tool, off at 1× | Pixel/DPR raster ([platform-behavior](references/platform-behavior.md)) |
| Isolated OK, toolbar broken | Set regression example |

## Reference library

- [Evidence and validation](references/evidence-and-validation.md)  
- [Geometry and centroids](references/geometry-and-centroids.md)  
- [Accessibility and constraints](references/accessibility-and-constraints.md)  
- [Anti-patterns](references/anti-patterns.md)  
- [Platform behavior](references/platform-behavior.md)  
- [Typography](references/typography.md)  
- [Shapes and icons](references/shapes-and-icons.md)  
- [Color and components](references/color-and-components.md)  
- [Implementation](references/implementation.md)  
- [Formulas, limits, sources](references/formulas-limits-sources.md)  
- [Examples](../../examples/)  

Version: [CHANGELOG.md](../../CHANGELOG.md).
