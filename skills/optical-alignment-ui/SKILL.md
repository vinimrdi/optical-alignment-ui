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
  version: "1.5.1"
  language: en
  tags: optical-alignment, optical-adjustment, optical-centering, ui, ux, typography, icons, agent-skills, claude-code, cursor, lovable, pixel-perfect, visual-balance
---

# Optical Alignment UI — Precision vs Perception

**Agent skill** for making digital interfaces *look* balanced when mathematical alignment does not.

Invoke as `/optical-alignment-ui` where supported, or attach this folder as context. Progressive disclosure: load [references/](references/) only when needed. Examples: [examples/](../../examples/). Centroid tool: [scripts/centroid.py](../../scripts/centroid.py).

## Compatible agents

See [docs/compatibility-and-integrations.md](../../docs/compatibility-and-integrations.md).

## Companion skill

**[ux-laws-principles](https://github.com/vinimrdi/ux-laws-principles)** — task first; optical craft second.

## Scope and rigor

| Kind | Examples |
|------|----------|
| **Heuristic / practice** | Play-icon nudge, caps size, icon+label |
| **Platform guidance** | Keylines; platform icon notes |
| **Type mechanics** | Overshoot, optical margin |
| **Engineering aid** | Area scale, geometric/alpha centroid — **diagnostic only** |

Optional measurement:

```bash
pip install pillow
python scripts/centroid.py icon.png --verbose
```

Prefer smallest effective correction. No universal pixel offsets. Re-check contrast and targets after changes.

## Outcomes (mandatory)

| Outcome | When |
|---------|------|
| **Implement** | Evidence sufficient, low risk, a11y safe |
| **Propose** | Plausible; needs human judgment |
| **Abstain** | No imbalance, weak evidence, or wrong skill |

## Severity and confidence (independent)

**Severity** 0–4 · **Confidence** High / Medium / Low / Unverified  
*Severity 3 + Confidence Low* → do not implement yet.

## Evidence-Based Optical Workflow

1. Context capture  
2. Baseline at native size  
3. Geometric analysis (box / centroid / alpha — optional `centroid.py`)  
4. Perceptual assessment  
5. Diagnosis (intent, severity, confidence)  
6. Minimal intervention (prefer pad-in-asset)  
7. Visual validation  
8. Design-system hand-off  

Details: [evidence-and-validation.md](references/evidence-and-validation.md) · [geometry-and-centroids.md](references/geometry-and-centroids.md) · [accessibility-and-constraints.md](references/accessibility-and-constraints.md) · [anti-patterns.md](references/anti-patterns.md)

## Geometric decision matrix (summary)

| Problem | Prefer first |
|---------|--------------|
| Symmetric filled rect | Bounding-box center |
| Filled play triangle | Centroid check + eye + pad-in-asset |
| Outline icons | Stroke mass; not fill centroid alone |
| Soft/raster edges | `centroid.py` / alpha weights |
| Circle vs square size | **Name intent** |
| Uneven icon set | Keylines + set review |
| Bad viewBox | Fix asset first |

## Reasoning rules

Visible imbalance first · Grid first · Shift against weight · Color last · Do not fight type overshoot · No one-offset for whole sets · Check anti-patterns · Explain while applying

## When to activate / when not

**Activate:** off-center glyphs, asymmetric icons, circle/square scale, icon+label, uneven sets, caps, overshoot/`opsz`, AI UI optically wrong, asset hand-off.

**Skip as primary:** a11y-only; no composition; illustration-only; universal +2px; physical optics.

## Analysis output format

What observed · Evidence · Concept · What/Why/Who/Where/When/How · Intent · Impact · Severity · Confidence · **Outcome** · Trade-off · Validation · Hand-off

## Reference library

- [Evidence](references/evidence-and-validation.md) · [Geometry](references/geometry-and-centroids.md) · [A11y](references/accessibility-and-constraints.md)  
- [Anti-patterns](references/anti-patterns.md) · [Platform](references/platform-behavior.md)  
- [Typography](references/typography.md) · [Shapes](references/shapes-and-icons.md) · [Color](references/color-and-components.md) · [Implementation](references/implementation.md)  
- [Formulas & sources](references/formulas-limits-sources.md) · [Examples](../../examples/) · [Scripts](../../scripts/)  

Version: [CHANGELOG.md](../../CHANGELOG.md).
