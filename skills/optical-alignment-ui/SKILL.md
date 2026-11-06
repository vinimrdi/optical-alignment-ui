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
  version: "1.4.0"
  language: en
  tags: optical-alignment, optical-adjustment, optical-centering, ui, ux, typography, icons, agent-skills, claude-code, cursor, lovable, pixel-perfect, visual-balance
---

# Optical Alignment UI — Precision vs Perception

**Agent skill** for making digital interfaces *look* balanced when mathematical alignment does not. Software centers bounding boxes; human vision weighs shape, contact with guides, contrast, and context.

Invoke as `/optical-alignment-ui` where supported, or attach this folder as context. Progressive disclosure: load [references/](references/) only when needed. Worked samples: [examples/](../../examples/).

## Compatible agents

See [docs/compatibility-and-integrations.md](../../docs/compatibility-and-integrations.md). Do **not** assume universal auto-discovery: distinguish *format support*, *path discovery*, and *ability to follow instructions*.

## Companion skill

Task friction, heuristics, a11y review: **[ux-laws-principles](https://github.com/vinimrdi/ux-laws-principles)**. Job first; optical craft second.

## Scope and rigor

Optical alignment is craft grounded in type design, platform guidance, and perception. It is **not** a single formula for every case.

Distinguish honestly:

| Kind | Examples |
|------|----------|
| **Heuristic / practice** | Play-icon nudge, caps size reduction, icon+label midline |
| **Platform guidance** | Apple HIG notes on geometric vs optical icon balance; Material keylines |
| **Type mechanics** | Overshoot, optical margin (type literature) |
| **Engineering aid** | Area scale, geometric/alpha centroid — **diagnostic tools, not absolute optical truth** |

**Centroid is a geometry tool for diagnosis, not a guarantee of perceptual center.** Color, stroke, background, size, and neighbors still matter.

Prefer the smallest effective correction. Never invent universal pixel offsets. Re-check contrast and touch targets after any change.

## Outcomes (mandatory)

Every case ends as one of:

| Outcome | When |
|---------|------|
| **Implement** | Evidence sufficient, low risk, targets/contrast safe |
| **Propose** | Plausible fix needs human or product judgment |
| **Abstain** | No clear imbalance, insufficient evidence, or wrong skill |

A professional skill teaches the agent **not** to touch what is already correct.

## Severity and confidence (independent axes)

**Severity** = impact if the imbalance is real.  
**Confidence** = strength of evidence that it *is* real and correctly diagnosed.

### Severity (0–4)

| Level | Meaning |
|-------|---------|
| **0** | Preference only |
| **1** | Subtle; trained eyes mainly |
| **2** | Clear imbalance on a secondary control |
| **3** | Evident on an important control or lockup |
| **4** | Harms clarity of a critical action |

### Confidence

| Level | Meaning |
|-------|---------|
| **High** | Reproducible imbalance at use size, isolated and in context |
| **Medium** | Consistent visual read; limited measurement |
| **Low** | Limited inspection; hypothesis |
| **Unverified** | Could not inspect real rendering |

Example: *Severity 3, Confidence Low* → do **not** implement; propose or gather evidence.

## Evidence-Based Optical Workflow

### 1. Context capture
Component, size, state, background, scale/DPR, platform, typeface, neighbors.

### 2. Baseline inspection
Inspect at **native use size** (not only zoomed). Optional blur test. Note light/dark if both ship.

### 3. Geometric analysis
Bounding-box center vs geometric centroid vs alpha-weighted bounds when available. Inspect SVG `viewBox`, stroke, transforms. See [geometry-and-centroids.md](references/geometry-and-centroids.md).

### 4. Perceptual assessment
Visual weight, negative space, contrast, stroke vs fill, neighbors. Separate **rendering artifact** (hinting, DPR) from true composition imbalance.

### 5. Diagnosis
Cause, severity, confidence, correction method. Name the **compensation intent** when scaling (equal area ≠ equal visual weight ≠ equal prominence).

### 6. Minimal intervention
Smallest change; preserve grid, outer frame, and **interactive target**. Prefer **pad-in-asset** for systems so code can keep geometric centering.

### 7. Visual validation
Before/after at use size; related components; theme; clipping/overflow/`transform-origin`. See [evidence-and-validation.md](references/evidence-and-validation.md).

### 8. Design-system hand-off
Name the exception, scope, and “do not copy blindly” criteria.

Full QA detail: [evidence-and-validation.md](references/evidence-and-validation.md).  
Hard a11y limits: [accessibility-and-constraints.md](references/accessibility-and-constraints.md).

## Geometric decision matrix (summary)

| Problem shape | Prefer first |
|---------------|--------------|
| Symmetric rect/square fill | Bounding-box center often enough |
| Filled polygon (e.g. equilateral play) | Geometric centroid as **diagnostic**; still judge by eye |
| Soft/transparent edges, raster, complex SVG | Alpha-weighted bounds if measurable |
| Asymmetric stroke icons | Optical judgment + pad-in-asset; centroid of fill path only is incomplete |
| Circle vs square **size** | State intent: equal area (√(4/π) aid) vs equal visual weight vs equal frame occupancy |
| Icon set row | Keylines + per-glyph optical weight; keep frames even |

## Reasoning rules

- Start from visible imbalance, not jargon.
- Grid and system spacing first; optical nudges refine.
- Shift **against** visual weight (mass left → nudge toward tip/right for LTR play).
- Color lightness is **not** the first lever: geometry → stroke/area → contrast → then chroma.
- Do not fight a typeface’s built-in overshoot.
- Do not apply one offset to every icon in a set.
- Label compensation intent when using formulas.
- **Explain while applying**, proportional, plain language.

## When to activate / when not

**Activate:** off-center glyphs, asymmetric icons, circle/square scale, icon+label, uneven icon sets, caps sizing, type overshoot/margin/`opsz`, AI UI that is grid-correct but optically wrong, asset hand-off for optical center.

**Do not use as primary:** a11y-only issues; no composition to judge; brand illustration only; universal +2px requests; physical optics / lab alignment; math already matches perception.

## Analysis output format

**Finding**
- **What was observed**
- **Evidence** (native size? context? before state?)
- **Related concept**
- **What / Why / Who / Where / When / How**
- **Compensation intent** (if scale/offset): equal area / visual size / visual weight / frame occupancy / prominence
- **Impact**
- **Severity** (0–4)
- **Confidence** (High / Medium / Low / Unverified)
- **Outcome** (Implement / Propose / Abstain)
- **Trade-off**
- **Validation plan**
- **Hand-off** (exception name if any)

## Symptom → concept index

| Symptom | Start here |
|---------|------------|
| Play triangle looks left-heavy | Visual weight; centroid vs box (diagnostic) |
| Circle looks smaller than square | State intent; area aid vs weight |
| Icon low/high in button | Optical vertical align; pad-in-asset |
| Icon + text uneven | Icon–label; line box vs ink |
| Icon set uneven at same box | Visual size/weight; keylines |
| ALL CAPS larger than mixed | Caps optical size |
| Round letters short vs H/X | Overshoot (type) |
| Quotes make margin uneven | Optical margin |
| Same hex, icon darker than text | Geometry first; then contrast |
| Small text fragile / display heavy | `opsz` if face supports it |
| Sharp shapes small next to soft | Sharp-edge scale heuristic |

## Reference library

- [Evidence and validation](references/evidence-and-validation.md)
- [Geometry and centroids](references/geometry-and-centroids.md)
- [Accessibility and constraints](references/accessibility-and-constraints.md)
- [Typography](references/typography.md)
- [Shapes and icons](references/shapes-and-icons.md)
- [Color and components](references/color-and-components.md)
- [Implementation](references/implementation.md)
- [Formulas, limits, sources](references/formulas-limits-sources.md)
- [Examples](../../examples/)

Version: [CHANGELOG.md](../../CHANGELOG.md).
