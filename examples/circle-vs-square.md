# Example: Circle looks smaller than square

## Context

Grid of media thumbs: some circular avatars, some rounded-square covers, both with width/height 40px.

## Finding

**What was observed:** Circles read smaller and lighter than rounded squares in the same row.

**Evidence:** Same CSS box; blur test still shows weaker mass on circles; known area difference.

**Related concept:** Area / scale compensation; keylines (equal visual size, not only equal box).

**What:** Equal bounding boxes ≠ equal perceived size.  
**Why:** A square occupies more area and contacts the imaginary frame more than a circle of the same width.  
**Who:** Users scanning mixed grids (feeds, pickers).  
**Where:** Avatar/cover components or keyline rules in the icon/media system.  
**When:** Circles paired with squares/rects at small UI sizes; less critical when shapes are isolated.  
**How:** Slightly increase circle diameter or live area (formula aid ≈ ×1.128 for equal *area*—then snap to pixels). Or define keylines so circle live area is larger than square live area inside a shared frame. Document the intent (equal area vs equal width).

**Impact:** Hierarchy and “importance” feel accidental.  
**Severity:** 2 in dense pickers; 1 in sparse layouts.  
**Trade-off:** Breaking naive “all 40px” tokens vs optical consistency.  
**Validation:** Row of mixed shapes at 1×; ensure layout shift and clipping still OK.  
**Confidence:** Confirmed direction; exact scale is product-specific.

### Formula reminder (aid, not dogma)

Equal **area** with square side `s`: circle diameter ≈ `s × √(4/π) ≈ s × 1.1284`. Snap for crispness when needed.
