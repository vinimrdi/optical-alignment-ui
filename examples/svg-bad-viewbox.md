# Example: SVG with wrong viewBox (not a true optical problem)

## Context
24×24 icon button. Path ink sits in the upper-left of a loose `viewBox="0 0 48 48"` with large empty space. Layout centers the SVG element.

## Finding

**What was observed:** Glyph looks high-left inside the button.

**Evidence:** Native 24px; inspecting SVG shows ink bounds far from viewBox center. Geometric “centering” centers the **viewBox**, not the ink.

**Related concept:** Asset metadata / ink bounds (engineering), not pure perceptual weight.

**Diagnosis:** False optical bug — **viewBox/padding error**.

**How:** Tighten viewBox to ink (+ intentional optical pad if needed). Prefer pad-in-asset after bounds are correct. Do **not** start with CSS translate.

**Severity:** 2–3  
**Confidence:** High (metadata explains the shift)  
**Outcome:** **Implement** asset fix  
**Anti-pattern avoided:** Runtime nudge on broken viewBox ([anti-patterns](../skills/optical-alignment-ui/references/anti-patterns.md))  
**Validation:** Ink center ≈ layout center at 24px; set review; target unchanged  
