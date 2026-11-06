---
name: optical-alignment-ui
description: >
  Optical alignment and optical adjustment for digital UI (precision vs perception).
  Use when icons look off-center, play buttons lean left, circles look smaller than
  squares, icon sets feel uneven, icon+label pairs misalign, ALL CAPS looks oversized,
  button labels sit wrong, or type needs overshoot / optical margin / font-optical-sizing.
  Apply smallest effective optical centering, visual weight, keyline, and pad-in-asset
  corrections grounded in Apple HIG, Material keylines, and type mechanics. Do not use
  for pure accessibility-only issues, physical optics, or inventing universal +2px rules.
metadata:
  author: vinimrdi
  version: "1.3.0"
  language: en
  tags: optical-alignment, optical-adjustment, optical-centering, ui, ux, typography, icons, agent-skills, claude-code, cursor, lovable, pixel-perfect, visual-balance
---

# Optical Alignment UI — Precision vs Perception

**Agent skill** for making digital interfaces *look* balanced when mathematical alignment does not. Software centers bounding boxes and matches hex values; human vision weighs shape, contact with guides, and context.

Invoke as `/optical-alignment-ui` where slash skills are supported, or attach this folder as context (Lovable, chat UIs). Progressive disclosure: load [references/](references/) only when the task needs depth. Worked samples: [examples/](../../examples/).

## Compatible agents

| Agent | How to load |
|-------|-------------|
| **Claude Code** | `~/.claude/skills/optical-alignment-ui/` or project `.claude/skills/optical-alignment-ui/` → `/optical-alignment-ui` |
| **Cursor** | `.cursor/skills/`, `~/.cursor/skills/`, or `.agents/skills/` (also reads `.claude/skills/`) |
| **Codex / OpenCode / Gemini CLI** | `~/.agents/skills/optical-alignment-ui/` or project `.agents/skills/` |
| **Lovable / chat** | Attach `SKILL.md` + relevant `references/*.md`; prefer review before write |
| **Other SKILL.md agents** | Copy folder so `SKILL.md` is directly inside `optical-alignment-ui/` |

Full install matrix: [docs/compatibility-and-integrations.md](../../docs/compatibility-and-integrations.md).

## Companion skill

For task-level UX (heuristics, cognitive load, accessibility, anti–dark-pattern): **[ux-laws-principles](https://github.com/vinimrdi/ux-laws-principles)**. Run that for job-to-be-done friction; use **this** skill for optical craft on icons and type.

## Scope and rigor

Optical alignment is a craft practice grounded in type design, platform HIGs, visual perception, and interface detailing. It is **not** a scientific law with a single formula for every case.

Correctly distinguish:
- **Heuristic / practice** — play-icon nudge, caps size reduction, icon+label alignment
- **Platform guidance** — Apple HIG optical centering; Material icon keylines; Fluent/XAML optical margin
- **Type mechanics** — overshoot, optical margin alignment (type literature)
- **Engineering aid** — area-matched scale, centroid/barycentre alignment, CSS `font-optical-sizing` / `opsz`

Do not assign undeserved precision. Prefer the smallest effective correction. Re-check contrast and touch targets after any change.

## When to activate

Activate when the task involves:
- Icons or glyphs that look off-center inside buttons, chips, or hit areas
- Circles, triangles, or irregular shapes next to squares or text
- Play, chevron, caret, send, download, or other asymmetric icons
- Icon + label rows that feel misaligned
- Icon **sets** that share a frame size but look uneven in visual weight
- ALL CAPS next to sentence case at the same font-size
- Button or chip label vertical balance (cap-height vs x-height, descenders)
- Typography polish: overshoot awareness, optical margin, optical sizing
- Design-system exceptions for visual balance without breaking the grid
- Hand-off of SVG/PNG assets so developers can geometrically center a pre-padded asset
- Polishing AI-generated UI that is grid-correct but optically wrong

## When NOT to use

Do **not** treat optical alignment as primary when:
- The only issue is accessibility contrast, focus order, or semantics (handle those first)
- There is no visual composition to judge (pure logic or API work)
- The user only wants brand illustration style with no UI balance claim
- A universal “always +2px” rule is requested with no component context
- Mathematical alignment already matches perception for that shape and size
- The topic is physical optics, AR/VR lab alignment, or non-UI “optical” systems

## Mandatory method: What, Why, Who, Where, When, How

For every recommendation:

1. **WHAT** — What looks wrong or what compensation is proposed?
2. **WHY** — Which perceptual factor (weight, contact with guides, area, overshoot)?
3. **WHO** — Who sees it (all users; density at small sizes; high-DPI)?
4. **WHERE** — Component, screen, asset, or token?
5. **WHEN** — When the correction applies; when pure geometry is enough?
6. **HOW** — Concrete change (offset, scale, padding in asset, color L/B) and how to verify?

State limits. Do not invent percentages or pixel values without context or a cited formula.

## Reasoning rules

- Start from the visible imbalance, not from a jargon label.
- Prefer grid and system spacing first; optical nudges refine, they do not replace structure.
- Keep outer frames and touch targets stable when only the glyph needs to move.
- Prefer **padding the asset** so geometric center of the file equals optical center of the glyph (Apple HIG pattern)—especially for design systems.
- Shift **against** visual weight (mass on the left → nudge shape toward the point/right).
- For icon sets, equalize **visual size/weight**, not only bounding boxes (Apple, Google, IBM guidance).
- Label confidence: confirmed (clear asymmetry) / probable / hypothesis.
- After color nudges, re-validate WCAG contrast.
- Do not “fix” a typeface’s built-in overshoot; respect the font’s design.
- Prefer formulas (area, centroid) when automating; still judge the result at target size.
- Prefer the smallest effective intervention.
- **Explain while applying** in plain language so the user learns why (proportional, not lecture).

## Workflow

### 1. Frame
What must look balanced (pair of shapes, icon in control, type lockup, icon set)? At what size?

### 2. Observe
Compare mathematical center/size/color to perceived balance. Note asymmetry, curves vs flats, filled vs text weight. Optionally blur the composition—imbalance often remains visible when detail disappears.

### 3. Explain
Name the factor (weight, overshoot, area, margin, keyline). Cite a real source when using a named mechanic or formula.

### 4. Design
Propose a minimal nudge, scale, in-asset padding, or token tweak. Preserve system metrics where possible. Prefer hand-off that lets developers keep simple geometric centering.

### 5. Validate
View at target size and density (including 1x raster); check neighboring components and full icon set; check contrast and hit area.

## Analysis output format

**Finding**
- **What was observed:** concrete visual imbalance.
- **Evidence:** inspection at size; comparison to geometry.
- **Related concept:** overshoot / optical alignment / visual weight / optical size / keyline / …
- **What / Why / Who / Where / When / How**
- **Impact:** craft quality, perceived polish, consistency of system.
- **Severity:** 0–4 (0 preference … 4 breaks a primary control’s clarity).
- **Trade-off:** e.g. deviation from strict grid; maintenance of exceptions.
- **Validation:** screenshot at 1x/2x; side-by-side math vs optical; set review.
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
| Circle looks smaller than square of same box | Area / scale compensation; keylines |
| Icon looks low or high in button | Optical vertical alignment; Apple HIG padding-in-asset |
| Icon + text feel uneven | Icon–label optical alignment |
| Icon set looks uneven at same box size | Visual size / weight across set |
| ALL CAPS looks larger than mixed case | Caps optical size reduction |
| Round letters look short next to H/X | Overshoot (type) |
| Margin looks uneven with quotes/punctuation | Optical margin alignment |
| Same hex, icon looks darker than text | Color weight; HSL/HSB lightness |
| Small text feels fragile / large text too heavy | Optical sizing (`opsz`) |
| Equal padding looks tight on one side | Visual weight; rounded corners contact |
| Sharp shapes look small next to soft ones | Sharp-edge scale compensation |

## Reference library (progressive disclosure)

Read only what you need:
- [Typography: overshoot, margin, optical size](references/typography.md)
- [Shapes, icons, and alignment](references/shapes-and-icons.md)
- [Color weight and layout components](references/color-and-components.md)
- [Implementation (design systems & front-end)](references/implementation.md)
- [Formulas, limits, and sources](references/formulas-limits-sources.md)
- [Worked examples](../../examples/)

Version history: [CHANGELOG.md](../../CHANGELOG.md).
