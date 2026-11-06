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

## Source list (verified topics; prefer originals)

### Type mechanics
- Tobias Frere-Jones — Typeface Mechanics (overshoot; eye over ruler).
- Wikipedia — *Overshoot (typography)*; *Optical margin alignment*.
- Peter Karow — *Digital Formats for Typefaces* (overshoot magnitudes cited in secondary sources).
- MDN — `font-optical-sizing`; Variable Fonts guide (`opsz`).
- Google Fonts Knowledge — Optical Size axis (`opsz`).

### UI craft
- Luke Jones — *Optical Adjustment – Logic vs. Designers* (Marvel App Blog / Medium): alignment, colour, scale, caps.
- Marc Edwards (Bjango) — *Formulas for optical adjustments*: area scale, triangle centers, caution on over-complex color rules.
- Slava Shestopalov — *Optical effects in user interfaces* (Design Bridges): shape balance, button label metrics.

### Portuguese-language introductions (secondary)
- Bruna Carvalho — UX Collective Brasil / Usemobile articles on ajuste óptico (aligned with the Jones-style teaching).
- Matatias — Portuguese translation/presentation of Jones’s optical adjustment piece.

Use secondary posts to teach; prefer primary type and platform sources when stating mechanics or CSS behavior.

## Glossary

| Term | Meaning |
|------|--------|
| **Optical adjustment** | Deliberate deviation from pure geometry so perception reads balanced. |
| **Optical alignment** | Positioning by perceived center/edge, not only bounding box. |
| **Visual weight** | Perceived mass from area, density, contrast, and asymmetry. |
| **Overshoot** | Drawing rounds/points past flat guides so sizes look equal. |
| **Optical margin alignment** | Hanging punctuation/diagonals into the margin for a straight text edge. |
| **Optical size (`opsz`)** | Size-specific letterform optimization in (variable) fonts. |
| **Centroid** | Geometric center of mass of a shape; useful for triangle centering. |
