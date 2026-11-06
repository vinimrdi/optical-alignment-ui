<div align="center">

# Optical Alignment UI

### Agent skill for **optical alignment** and **optical adjustment** in digital interfaces

**Precision vs perception** — evidence-based diagnosis when interfaces are mathematically centered but visually wrong.

Works with **Claude Code**, **Cursor**, **Codex**, **Lovable** (context attach), and other SKILL.md hosts—**verify discovery on your version**.

[![License: CC BY 4.0](https://img.shields.io/badge/docs-CC%20BY%204.0-lightgrey?style=flat-square)](https://creativecommons.org/licenses/by/4.0/)
[![Skill](https://img.shields.io/badge/skill-v1.4.0-blue?style=flat-square)](skills/optical-alignment-ui/SKILL.md)
[![Agents](https://img.shields.io/badge/agents-Claude%20%7C%20Cursor%20%7C%20Codex%20%7C%20Lovable-111827?style=flat-square)](docs/compatibility-and-integrations.md)
[![Language](https://img.shields.io/badge/language-English-blue?style=flat-square)](#language)

[Skill](skills/optical-alignment-ui/SKILL.md) · [Examples](examples/) · [Install](#install) · [Compatibility](docs/compatibility-and-integrations.md) · [SEO / AEO](docs/seo-and-discovery.md) · [Changelog](CHANGELOG.md)

</div>

---

## What is optical alignment in UI?

**Optical alignment** (optical adjustment / optical centering) shifts or scales UI so elements *look* balanced—even when boxes and equal margins say they are perfect.

Typical failures: play icons, circle vs square scale, icon+label pairs, uneven icon sets, ALL CAPS sizing, type overshoot and `font-optical-sizing`.

> We read with our eyes, not with rulers — Tobias Frere-Jones (type mechanics).

**v1.4 method:** evidence-based diagnosis → geometric aids (not absolute truth) → severity **and** confidence → Implement / Propose / **Abstain** → validate → design-system hand-off. No universal +2px rules. No shrinking touch targets for cosmetics.

---

## Related skill

**[UX Laws & Principles](https://github.com/vinimrdi/ux-laws-principles)** — task friction, heuristics, a11y.  
**This skill** — precision vs perception on icons and type.

---

## Install

```bash
git clone https://github.com/vinimrdi/optical-alignment-ui.git
mkdir -p ~/.claude/skills
cp -R optical-alignment-ui/skills/optical-alignment-ui ~/.claude/skills/optical-alignment-ui

# Cursor
mkdir -p ~/.cursor/skills
cp -R optical-alignment-ui/skills/optical-alignment-ui ~/.cursor/skills/optical-alignment-ui

# Shared agents path
mkdir -p ~/.agents/skills
cp -R optical-alignment-ui/skills/optical-alignment-ui ~/.agents/skills/optical-alignment-ui
```

```bash
npx skills add vinimrdi/optical-alignment-ui --skill optical-alignment-ui
```

**Layout:** `SKILL.md` must be at `optical-alignment-ui/SKILL.md`.

**Lovable:** attach `SKILL.md` + needed `references/` — do not assume auto-discovery.

Full matrix: [docs/compatibility-and-integrations.md](docs/compatibility-and-integrations.md).

---

## Ask your agent

```text
Use optical-alignment-ui on this toolbar.
Report severity AND confidence. Prefer pad-in-asset.
Abstain if evidence is weak. Do not change touch targets.
```

```text
/optical-alignment-ui
Play control looks off-center. Diagnose with geometric vs perceptual centers.
Outcome: Implement, Propose, or Abstain.
```

---

## What you get

| Piece | Role |
|-------|------|
| **SKILL.md** | Evidence workflow, severity × confidence, decision matrix |
| **evidence-and-validation** | Inspection + optical QA |
| **geometry-and-centroids** | Box / centroid / alpha / perception |
| **accessibility-and-constraints** | Hard stops (targets, contrast, focus) |
| **typography / shapes / color / implementation** | Domain depth |
| **examples/** | Worked findings |

---

## Method (short)

| Step | Action |
|------|--------|
| Capture | Context, size, theme, neighbors |
| Inspect | Native size; geometry + perception |
| Diagnose | Severity, confidence, intent |
| Act | Implement / Propose / Abstain |
| Validate | Before/after, DPR, set, a11y |
| Hand off | Named exception, no blind copy |

---

## Language

**English** is the official documentation language.

---

## License

Documentation: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

Educational craft material — not a substitute for type expertise, full accessibility audits, or user research.
