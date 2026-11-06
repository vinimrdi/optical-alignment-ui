# Anti-patterns — “fixes” that often make UI worse

Agents should **Abstain** or **Propose** rather than apply these blindly.

## Universal pixel offsets

**Bad:** `translateX(2px)` on every toolbar icon.  
**Why:** Silhouettes differ; one offset creates a new uneven set.  
**Do instead:** Per-glyph diagnosis; pad-in-asset; named exceptions only.

## Shrinking the hit target

**Bad:** Reduce button padding so the glyph “looks” centered in a tighter box.  
**Why:** Fails accessibility and usability.  
**Do instead:** Keep target; move ink inside the frame.

## Fighting the font’s overshoot

**Bad:** Clip or scale round glyphs to sit exactly on the baseline grid.  
**Why:** Makes type look smaller and uneven vs flats.  
**Do instead:** Respect face metrics; adjust geometric marks beside type if needed.

## Equal-area circle everywhere

**Bad:** Always scale circles ×1.1284.  
**Why:** Equal area ≠ equal visual weight with stroke, border, or neighbors.  
**Do instead:** Name intent; judge at target size; use keylines for sets.

## Lightness as first lever

**Bad:** Dim every filled icon to match text.  
**Why:** Hides geometry/stroke issues; risks contrast.  
**Do instead:** Geometry → stroke/area → contrast → then color; re-check WCAG.

## Runtime nudge when the viewBox is wrong

**Bad:** CSS translate to compensate a mis-authored SVG.  
**Why:** Multiplies across sizes and densities; next export breaks again.  
**Do instead:** Fix `viewBox`/ink padding in the asset (see examples).

## Optical fix that ignores the set

**Bad:** Perfect one icon; ship without reviewing the toolbar row.  
**Why:** Local win, global inconsistency.  
**Do instead:** Set-level validation before Implement.

## Treating centroid as perceptual law

**Bad:** “Centroid aligned ⇒ done.”  
**Why:** Stroke, contrast, and context remain.  
**Do instead:** Centroid as diagnostic; eye at native size closes the loop.

## Global vertical gravity shifts

**Bad:** Raise all modal illustrations by 4px site-wide.  
**Why:** Context-specific heuristic, not a system constant.  
**Do instead:** Case-by-case; document if a pattern truly repeats.

## Motion demos that ignore reduced motion

**Bad:** Animated before/after as the only way to “see” the fix.  
**Why:** Accessibility.  
**Do instead:** Static pairs; respect `prefers-reduced-motion`.
