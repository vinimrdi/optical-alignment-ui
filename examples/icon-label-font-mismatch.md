# Example: Icon + label break after font fallback

## Context
Chevron + “Continue” tuned against Brand Sans. Production stack falls back to system UI on some OS.

## Finding

**What was observed:** On fallback face, chevron looks high relative to the label.

**Evidence:** Same CSS; metrics (cap-height, sidebearings) differ by face; pair only checked on brand font in design.

**Related concept:** Font metrics; platform fallback ([platform-behavior](../skills/optical-alignment-ui/references/platform-behavior.md)).

**How:** Re-validate critical pairs on primary + fallback stacks; prefer pad-in-asset for chevron; avoid face-specific `translateY` without documenting stacks.

**Severity:** 2 where fallback is common  
**Confidence:** High when reproduced on target OS  
**Outcome:** Implement after fallback check; else Propose  
**Validation:** Brand + system font; sm/md button sizes  
