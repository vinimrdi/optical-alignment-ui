<div align="center">

# Optical Alignment UI

**Precision vs perception for digital UI.**

Typography overshoot, icon centering, visual weight, color balance, and optical sizing—for agents and designers who refuse “mathematically centered, visually wrong.”

[![License: CC BY 4.0](https://img.shields.io/badge/docs-CC%20BY%204.0-lightgrey?style=flat-square)](https://creativecommons.org/licenses/by/4.0/)
[![Skill](https://img.shields.io/badge/skill-v1.0.1-blue?style=flat-square)](skills/optical-alignment-ui/SKILL.md)
[![Language](https://img.shields.io/badge/language-English-blue?style=flat-square)](#language)

**No universal +2px mythology. No ignoring WCAG after a color nudge. No fighting a typeface’s own overshoot.**

[Skill](skills/optical-alignment-ui/SKILL.md) · [References](skills/optical-alignment-ui/references/) · [Changelog](CHANGELOG.md)

</div>

---

## Why this exists

AI-generated and grid-only UIs often align bounding boxes and still look wrong: play icons lean left, circles look smaller than squares, caps shout next to sentence case, icons sit low in buttons.

This skill is a portable method so agents **name the perceptual issue**, apply the **smallest effective compensation**, and keep **sources and limits** honest—alongside normal UI/UX practice.

> We read with our eyes, not with rulers — Tobias Frere-Jones (type mechanics).

Pairs well with evidence-based UX methodology skills (task friction, heuristics, accessibility). Optical alignment is **craft and perception**, not a substitute for usability research.

---

## Install

```bash
git clone https://github.com/vinimrdi/optical-alignment-ui.git
cp -r optical-alignment-ui/skills/optical-alignment-ui ~/.claude/skills/optical-alignment-ui
# or: ~/.cursor/skills/  ·  project .claude/skills/
```

Until the repository is renamed on GitHub, the current clone URL may still be:

```bash
git clone https://github.com/vinimrdi/optical-adjustment.git
```

If a skills CLI supports this repo:

```bash
npx skills add vinimrdi/optical-alignment-ui
```

**Lovable / chat:** attach `skills/optical-alignment-ui/SKILL.md` and needed files under `references/` as context. Prefer read-only review before implementation.

---

## Ask your agent

```text
Review this icon button set with the Optical Alignment UI skill.
Flag mathematical vs optical centering. Do not change touch targets.
Explain each nudge in plain language.
```

```text
This play control looks off-center. Apply optical alignment only to the glyph.
Cite visual weight / centroid reasoning. Keep the frame fixed.
```

```text
Audit this toolbar: circle avatars next to rounded-square thumbs,
ALL CAPS badges next to sentence-case labels. Propose minimal corrections.
```

---

## What you get

| Piece | Role |
|-------|------|
| **[SKILL.md](skills/optical-alignment-ui/SKILL.md)** | Activation, method, output format, severity |
| **Typography** | Overshoot, optical margin, `opsz`, caps, button labels |
| **Shapes & icons** | Weight, play icon, circle/square, icon+label |
| **Color & components** | Lightness vs mass, spacing, system exceptions |
| **Formulas & sources** | Area scale, centroid, limits, bibliography |

---

## Method (short)

| Step | Action |
|------|--------|
| Observe | What looks unbalanced at target size? |
| Explain | Weight, contact, area, overshoot, margin? |
| Correct | Smallest nudge; preserve targets and tokens |
| Validate | 1x/2x view; contrast; neighboring components |

---

## When to use / when not

| Use when | Skip when |
|----------|-----------|
| Icons feel off-center in controls | Accessibility-only issues with no balance claim |
| Geometric pairs look unequal | No UI composition to judge |
| Type lockups or caps sizing feel wrong | Request for one magic offset for all icons |
| Polishing agent-generated UI | Pure illustration / brand art |

---

## Language

**English** is the official documentation language.

---

## License

- **Documentation:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
- **Code** (when present): MIT

---

## Maintainers

Maintained by **Planner**. Educational craft material — does not replace type design expertise, full accessibility audits, or user research.

**Repository:** [github.com/vinimrdi/optical-alignment-ui](https://github.com/vinimrdi/optical-alignment-ui) (rename from `optical-adjustment` in GitHub Settings if not done yet)
