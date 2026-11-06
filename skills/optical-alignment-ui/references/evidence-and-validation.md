# Evidence and validation

## Goal

Stop agents from turning a vague “looks off” feeling into a confident CSS nudge without proof.

## Evidence-Based Optical Diagnosis

### Required observations

1. **Native size** — inspect at the size users see, not only zoomed artboards.
2. **Isolated and in context** — glyph alone and inside the real control/row.
3. **Geometric vs visual** — note box center vs estimated mass center vs perceived center.
4. **Artifact check** — is the issue DPR rounding, hinting, compression, or true composition?
5. **Before state** — record baseline (screenshot or precise description) before changing.

### Optional aids

- Blur test (imbalance often survives blur).
- Side-by-side math-centered vs candidate optical.
- Light and dark themes when both ship.

### Evidence vs hypothesis

| Claim type | Example |
|------------|---------|
| **Evidence** | “At 24×24 in the toolbar, the send glyph’s mass sits low-left relative to neighbors.” |
| **Hypothesis** | “Users will trust the control less.” |

Do not present hypotheses as confirmed impact without data.

## Outcomes

| Outcome | Gate |
|---------|------|
| **Implement** | Confidence Medium or High; severity justifies work; a11y constraints pass |
| **Propose** | Medium/Low confidence or high product risk |
| **Abstain** | Confidence Unverified/Low with weak severity, or no real imbalance |

## Optical QA protocol (implementation)

After a change:

1. Before/after at use size.
2. **DPR** — check 1× when relevant; 2×/3× if the product ships there.
3. **Component sizes** — sm/md/lg variants if they share the asset.
4. **Clipping / overflow / transform-origin** — nudge must not crop or mis-rotate.
5. **Theme** — light/dark.
6. **Neighbors** — full toolbar or set, not only the one glyph.
7. **Interactive target** — hit area dimensions unchanged unless explicitly redesigned.
8. **Contrast** — if color changed, re-check WCAG for applicable text/non-text rules.

## Regression questions

- Does the exception encourage copy-paste offsets elsewhere?
- Does pad-in-asset keep developer centering simple?
- Would a new icon in the set reintroduce uneven weight?

## What not to claim

- Do not claim user-test proof from inspection alone.
- Do not claim “Apple requires X” without the specific HIG citation verified.
- Do not treat equal-area scale as mandatory visual-weight equality.
