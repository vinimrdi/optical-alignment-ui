# Accessibility and constraints

Optical correction is **craft**. It must not trade away accessibility or semantics.

This skill does **not** replace a full WCAG audit. It does hard-stop unsafe “polish.”

## Never do (optical fix bans)

Optical alignment must **not**:

- Shrink the **interactive target** below the product’s minimum (or applicable WCAG target-size expectations) to hide a bad drawing
- Reduce **legibility** of text or icons that convey meaning
- Create **ambiguity** in icon meaning
- Remove or obscure **focus** visibility
- Worsen **contrast** below required thresholds for the content type
- Introduce harmful **clipping** or overlap of essential content
- Change **reading order** or control **semantics**
- Rely on motion demos that ignore **`prefers-reduced-motion`**

## Separate concepts

| Concept | Role |
|---------|------|
| **Visual size of the glyph** | What the eye judges for balance |
| **Interactive target** | Hit/focus area — may be larger than the glyph |
| **Non-text contrast** | UI component contrast rules where applicable |
| **Text contrast** | Text and text-like content |

Nudging a glyph inside a stable 44×44 (or policy) target is preferred over resizing the control for cosmetics.

## Color changes

If compensating “weight” with lightness or opacity:

1. Prefer geometry/stroke fixes first ([color-and-components.md](color-and-components.md)).
2. Re-validate contrast after any color change.
3. Check both themes.

## Motion

If illustrating before/after with animation, respect `prefers-reduced-motion`. Optical alignment itself does not require motion.

## Normative pointer

- **W3C WCAG 2.2** — use for applicable success criteria (contrast, target size, motion, focus). Cite the specific criterion when making a compliance claim; do not invent pass/fail without checking the criterion text.

## Pairing

For task-level a11y and heuristic review, use **[ux-laws-principles](https://github.com/vinimrdi/ux-laws-principles)** first when the issue is interaction or understanding, not pure optical balance.
