# Example: Centered at 2×, wrong at 1×

## Context
Hairline outline icon, coordinates at half-pixels, previewed on retina. QA screenshot at DPR 1.

## Finding

**What was observed:** Icon looks soft or optically shifted on 1×; fine on 2× designer display.

**Evidence:** Fractional stroke positions; different raster between DPRs—not a true asymmetric mass problem.

**Related concept:** Pixel alignment / DPR ([platform-behavior](../skills/optical-alignment-ui/references/platform-behavior.md)).

**How:** Snap strokes to whole pixels when 1× crispness is required; re-export. Do not add a “perceptual” translate that only masks 1× raster.

**Severity:** 2 for products that ship 1×  
**Confidence:** High if 1× vs 2× comparison exists  
**Outcome:** Implement asset/grid snap  
**Validation:** 1× and 2× screenshots; no target change  
