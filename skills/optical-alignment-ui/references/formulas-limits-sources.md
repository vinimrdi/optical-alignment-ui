# Formulas, limits, and sources

## Useful formulas (aids, not dogma)

| Intent | Aid |
|--------|-----|
| Circle same *area* as square of side *s* | Circle diameter ≈ *s* × √(4/π) ≈ *s* × 1.1284 |
| Equilateral triangle in circle | Align triangle **centroid** to circle center (not only bounding-box center) |
| Type overshoot order of magnitude | ~1–3% of cap/x-height for rounds; often more for points (judge per face; Karow cited ~3% / ~5% for O / A in literature) |

Snap to device pixels when rendering crispness is required.

## Hard limits

1. **No universal pixel offset** for all icons.
2. **Context rules:** size, stroke, fill, neighbors, and density change the result.
3. **Accessibility and targets** outrank pure polish.
4. **Fonts already encode overshoot**—do not fight the face.
5. **Formulas help automation;** human judgment at target size still closes the loop.
6. **Blog heuristics** (caps −2px, etc.) are starting points, not standards.
7. **Physical optics / lab alignment repos are out of scope** for this skill.

## Competitive landscape (agent skills / GitHub)

As of the 1.1.0 audit:

| Kind | Examples | Relation to this skill |
|------|----------|------------------------|
| **Dedicated optical-alignment UI agent skill** | *None found* | This skill targets the gap |
| **Partial mentions** | `afterxleep/agents` pixel-perfect (optical centering notes) | Narrow fragment; not a full method |
| **Broad UI/UX skills** | apple-design-skill, OJO Design Skills, ux-optimization | Cover craft/HIG broadly; not specialized here |
| **Wrong domain** | 3doptix, laser alignment, eyeglass agents | Physical optics / other |
| **Libraries** | canvas “optical-properties” experiments | Tooling aids, not agent methodology |

**Positioning:** deepest specialized agent skill for precision-vs-perception in **digital UI**, with platform HIG + type mechanics + FE hand-off—not a generic “make it pretty” prompt.

## Source list (verified topics; prefer originals)

### Type mechanics
- Tobias Frere-Jones — Typeface Mechanics (overshoot; eye over ruler).
- Wikipedia — *Overshoot (typography)*; *Optical margin alignment*.
- Peter Karow — *Digital Formats for Typefaces* (overshoot magnitudes cited in secondary sources).
- MDN — `font-optical-sizing`; Variable Fonts guide (`opsz`).
- Google Fonts Knowledge — Optical Size axis (`opsz`).
- Microsoft Learn — Character design standards (visual equality ≠ mathematical equality); XAML `OpticalMarginAlignment`.

### Platform / industry UI
- Apple Human Interface Guidelines — Icons: geometric vs optical centering; padding in assets.
- Material Design — icon keyline grids (live area by shape).
- Research summarizing Apple/Google/IBM icon visual size & alignment practice (e.g. studies on icon-set visual size optimization).

### UI craft
- Luke Jones — *Optical Adjustment – Logic vs. Designers* (Marvel App Blog / Medium).
- Marc Edwards (Bjango) — *Formulas for optical adjustments*.
- Slava Shestopalov — *Optical effects in user interfaces* (Design Bridges).
- Ivan Grekov (Bumble Tech) — Optical alignment for frontend developers (barycentre / production).

### Portuguese-language introductions (secondary)
- Bruna Carvalho — UX Collective Brasil / Usemobile (ajuste óptico).
- Matatias — Portuguese presentation of Jones’s optical adjustment piece.

Use secondary posts to teach; prefer primary type and platform sources when stating mechanics or CSS/HIG behavior.

## Glossary

| Term | Meaning |
|------|--------|
| **Optical adjustment** | Deliberate deviation from pure geometry so perception reads balanced. |
| **Optical alignment** | Positioning by perceived center/edge, not only bounding box. |
| **Visual weight** | Perceived mass from area, density, contrast, and asymmetry. |
| **Overshoot** | Drawing rounds/points past flat guides so sizes look equal. |
| **Optical margin alignment** | Hanging punctuation/diagonals into the margin for a straight text edge. |
| **Optical size (`opsz`)** | Size-specific letterform optimization in (variable) fonts. |
| **Centroid / barycentre** | Geometric center of mass of a shape; useful for triangle centering. |
| **Keyline** | Shape-specific live area inside a shared icon frame. |
