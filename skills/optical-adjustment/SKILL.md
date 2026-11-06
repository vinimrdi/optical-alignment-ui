---
name: optical-adjustment
description: Evidence-based optical adjustment skill for AI agents and designers. Apply precision-vs-perception corrections in digital UI—typography overshoot, optical alignment of icons and shapes, visual weight, color balance, button labels, and optical sizing—when creating, reviewing, or polishing interfaces. Use for icon centering, play buttons, circle-vs-square scale, icon+label pairs, ALL CAPS sizing, button text vertical alignment, optical margin, and font-optical-sizing. Do not use for pure brand illustration, accessibility-only audits without visual balance issues, or inventing universal pixel offsets without context.
metadata:
  author: vinimrdi
  version: "1.0.0"
  language: en
  tags: [ux, ui, visual-design, typography, optical-adjustment, optical-alignment, agent-skills, pixel-craft]
---

# Optical Adjustment — Precision vs Perception

Practical skill for making interfaces *look* balanced when mathematical alignment does not. Software centers bounding boxes and matches hex values; human vision weighs shape, contact with guides, and context. This skill teaches when and how to compensate—without inventing rules or ignoring accessibility.

## Scope and rigor

Optical adjustment is a craft practice grounded in type design, visual perception, and interface detailing. It is **not** a scientific law with a single formula for every case.

Correctly distinguish:
- **Heuristic / practice** — play-icon nudge, caps size reduction, icon+label alignment
- **Type mechanics** — overshoot, optical margin alignment (documented in type literature)
- **Engineering aid** — area-matched scale, centroid alignment, CSS `font-optical-sizing` / `opsz`

Do not assign undeserved precision. Prefer the smallest effective correction. Re-check contrast and touch targets after any change.

## When to activate

Activate when the task involves:
- Icons or glyphs that look off-center inside buttons, chips, or hit areas
- Circles, triangles, or irregular shapes next to squares or text
- Play, chevron, caret, or other asymmetric icons
- Icon + label rows that feel misaligned
- ALL CAPS next to sentence case at the same font-size
- Button or chip label vertical balance (cap-height vs x-height, descenders)
- Typography polish: overshoot awareness, optical margin, optical sizing
- Design-system exceptions for visual balance without breaking the grid

## When NOT to use

Do **not** treat optical adjustment as primary when:
- The only issue is accessibility contrast, focus order, or semantics (handle those first)
- There is no visual composition to judge (pure logic or API work)
- The user only wants brand illustration style with no UI balance claim
- A universal “always +2px” rule is requested with no component context
- Mathematical alignment already matches perception for that shape and size

## Mandatory method: What, Why, Who, Where, When, How

For every recommendation:

1. **WHAT** — What looks wrong or what compensation is proposed?
2. **WHY** — Which perceptual factor (weight, contact with guides, area, overshoot)?
3. **WHO** — Who sees it (all users; density at small sizes; high-DPI)?
4. **WHERE** — Component, screen, or token?
5. **WHEN** — When the correction applies; when pure geometry is enough?
6. **HOW** — Concrete change (offset, scale, padding, color L/B) and how to verify?

State limits. Do not invent percentages or pixel values without context or a cited formula.

## Reasoning rules

- Start from the visible imbalance, not from a jargon label.
- Prefer grid and system spacing first; optical nudges refine, they do not replace structure.
- Keep outer frames and touch targets stable when only the glyph needs to move.
- Shift **against** visual weight (mass on the left → nudge shape toward the point/right).
- Label confidence: confirmed (clear asymmetry) / probable / hypothesis.
- After color nudges, re-validate WCAG contrast.
- Do not “fix” a typeface’s built-in overshoot; respect the font’s design.
- Prefer formulas (area, centroid) when automating; still judge the result at target size.
- Prefer the smallest effective intervention.

## Explain while applying (teach, don't just fix)

Whenever this skill is used, explain in plain language:
- The concept and category (type mechanic / UI heuristic / formula aid).
- Why it fits **this** shape, size, and context.
- Expected benefit and what would confirm it.
- Limits and confidence.

Proportional: one or two sentences per decision unless the change is high-impact.

## Workflow

### 1. Frame
What must look balanced (pair of shapes, icon in control, type lockup)? At what size?

### 2. Observe
Compare mathematical center/size/color to perceived balance. Note asymmetry, curves vs flats, filled vs text weight.

### 3. Explain
Name the factor (weight, overshoot, area, margin). Cite a real source when using a named mechanic or formula.

### 4. Design
Propose a minimal nudge, scale, padding, or token tweak. Preserve system metrics where possible.

### 5. Validate
View at target size and density; check neighboring components; check contrast and hit area.

## Analysis output format

**Finding**
- **What was observed:** concrete visual imbalance.
- **Evidence:** inspection at size; comparison to geometry.
- **Related concept:** overshoot / optical alignment / visual weight / optical size / …
- **What / Why / Who / Where / When / How**
- **Impact:** craft quality, perceived polish, consistency of system.
- **Severity:** 0–4 (0 preference … 4 breaks a primary control’s clarity).
- **Trade-off:** e.g. deviation from strict grid; maintenance of exceptions.
- **Validation:** screenshot at 1x/2x; side-by-side math vs optical.
- **Confidence:** confirmed / probable / hypothesis.

### Severity scale

| Level | Meaning |
|-------|---------|
| **0** | Preference only; no clear imbalance. |
| **1** | Subtle; noticed mainly by trained eyes. |
| **2** | Clear off-center or scale mismatch in a secondary control. |
| **3** | Primary control or key lockup looks wrong to many users. |
| **4** | Severe imbalance that undermines trust in a critical action control. |

## Symptom → concept index

| Symptom | Start here |
|---------|------------|
| Play triangle looks left-heavy in circle | Visual weight; centroid vs bounding box |
| Circle looks smaller than square of same box | Area / scale compensation |
| Icon looks low or high in button | Optical vertical alignment; cap vs x-height |
| Icon + text feel uneven | Icon–label optical alignment |
| ALL CAPS looks larger than mixed case | Caps optical size reduction |
| Round letters look short next to H/X | Overshoot (type) |
| Margin looks uneven with quotes/punctuation | Optical margin alignment |
| Same hex, icon looks darker than text | Color weight; HSL/HSB lightness |
| Small text feels fragile / large text too heavy | Optical sizing (`opsz`) |
| Equal padding looks tight on one side | Visual weight; rounded corners contact |

## Reference library

Read only what you need:
- [Typography: overshoot, margin, optical size](references/typography.md)
- [Shapes, icons, and alignment](references/shapes-and-icons.md)
- [Color weight and layout components](references/color-and-components.md)
- [Formulas, limits, and sources](references/formulas-limits-sources.md)

Version history: [CHANGELOG.md](../../CHANGELOG.md).
