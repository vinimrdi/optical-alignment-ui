# Typography: overshoot, metrics, optical size

## Font metrics the agent must not confuse

| Metric | Role |
|--------|------|
| **Baseline** | Line glyphs sit on |
| **x-height / cap-height** | Body of lowercase / flat caps |
| **Ascender / descender** | Extents beyond x-height / baseline |
| **em box / line box** | CSS layout box — not the same as ink |
| **Ink / glyph bounds** | Actual drawing extent |
| **Advance width** | Horizontal advance including sidebearings |

**Do not** “fix” a baseline mismatch by randomly changing `line-height` or `translateY` on whole strings without understanding ink vs line box.

Prefer: align icon to a declared text metric (cap-height or midpoint rule) and document the system choice.

## Overshoot

**Category:** Type design mechanic.

Round or pointed forms (O, A, V, …) are drawn slightly beyond flat guides so they *appear* the same size as H/X/E.

**Typical magnitude (guidance):** ~1–3% of cap/x-height for O; points often more. Karow is often cited (~3% O, ~5% A)—always judge the face.

**UI rule:** Do not clip a professional font’s overshoot to “match the grid.” When drawing geometric marks beside type, allow slight overshoot for circles and peaks. Check small-size rasterization.

**References:** Frere-Jones Typeface Mechanics; Wikipedia *Overshoot (typography)*.

## Optical margin alignment

Punctuation and some diagonals hang slightly into the margin so the **text edge** looks straight. Mostly body text; limited pure-CSS support. Not a substitute for measure and leading.

**Reference:** Wikipedia *Optical margin alignment*.

## Optical size (`opsz`) and variable fonts

**Category:** Type + CSS.

Optical size designs adjust letterforms for the size they are set (sturdier at small sizes; finer at large).

### Agent checklist

1. Is the face **variable**?
2. Which axes exist (`opsz`, `wght`, `wdth`, `GRAD`, …)?
3. What is current `font-optical-sizing`? (`auto` is default when supported.)
4. Avoid overriding `font-variation-settings` unless necessary.
5. Compare at real UI sizes.
6. Do **not** confuse optical sizing with merely changing `font-size`.

```css
font-optical-sizing: auto;
/* explicit only when required */
font-variation-settings: "opsz" 14;
```

**Limit:** No effect without optical-size masters in the font file.

**References:** MDN `font-optical-sizing`; MDN Variable fonts guide; Google Fonts Knowledge Optical Size axis.

## Fallback and rasterization

Fallback faces change metrics—re-check icon+label pairs if the stack shifts. At small sizes, hinting and DPR affect perceived alignment; validate at target DPR.

## ALL CAPS next to mixed case

Caps at the same computed size often look larger. If parity is the goal, a modest relative reduction may help; if emphasis is the goal, keep size. Face-dependent.

**Reference:** Luke Jones, *Optical Adjustment – Logic vs. Designers*.

## Button label vertical alignment

Centering by **line box** ≠ centering by **cap-height / ink mass**. Descenders pull weight down. Prefer system rules; small documented nudges for icon+label pairs.

**Reference:** Shestopalov, *Optical effects in user interfaces*.

## Intrinsic type design vs component compensation

| Adjust in the **font** | Adjust in the **component** |
|------------------------|-----------------------------|
| Overshoot, sidebearings, opsz masters | Icon pad-in-asset, label alignment tokens |

Do not rewrite professional outlines in CSS to erase overshoot.
