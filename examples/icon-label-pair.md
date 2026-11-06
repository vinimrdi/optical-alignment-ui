# Example: Icon + label feel uneven

## Context
Pill: leading chevron-right + “Continue”. Shared gap token. Flex vertical center on line box.

## Finding

**What was observed:** Chevron slightly low/high vs label cap mass.

**Evidence:** Native size; silhouette vs caps, not only viewBox.

**Related concept:** Icon–label optical alignment; line box vs ink.

**How:** Small asset pad or documented `translateY`; prefer asset if many instances. Do not burn the gap token to hide a bad glyph.

**Severity:** 1–2  
**Confidence:** Medium until checked at final weight/size  
**Outcome:** Propose or Implement after size check  
**Validation:** Bold/regular label; focus target unchanged  
