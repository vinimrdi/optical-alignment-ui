<div align="center">

# Optical Alignment UI

### Agent skill for **optical alignment** and **optical adjustment** in digital interfaces

**Precision vs perception** — fix icons, type, and layout that are mathematically centered but visually wrong.

Works with **Claude Code**, **Cursor**, **Codex**, **Lovable** (context), and any tool that loads `SKILL.md`.

[![License: CC BY 4.0](https://img.shields.io/badge/docs-CC%20BY%204.0-lightgrey?style=flat-square)](https://creativecommons.org/licenses/by/4.0/)
[![Skill](https://img.shields.io/badge/skill-v1.2.0-blue?style=flat-square)](skills/optical-alignment-ui/SKILL.md)
[![Agents](https://img.shields.io/badge/agents-Claude%20%7C%20Cursor%20%7C%20Codex%20%7C%20Lovable-111827?style=flat-square)](docs/compatibility-and-integrations.md)
[![Language](https://img.shields.io/badge/language-English-blue?style=flat-square)](#language)

[Skill](skills/optical-alignment-ui/SKILL.md) · [Install](#install) · [Compatibility](docs/compatibility-and-integrations.md) · [SEO / AEO](docs/seo-and-discovery.md) · [Changelog](CHANGELOG.md)

</div>

---

## What is optical alignment in UI?

**Optical alignment** (also called **optical adjustment** or **optical centering**) is the practice of shifting or scaling UI elements so they *look* balanced to the human eye—even when bounding boxes, grids, and equal pixel margins say they are already “perfect.”

Common failures this skill targets:

- **Play buttons** and asymmetric icons that look off-center in a circle or square hit area
- **Circles next to squares** that share a box size but not visual weight
- **Icon + label** rows that feel uneven
- **Icon sets** that look inconsistent at the same frame size
- **ALL CAPS** that appears larger than sentence case at the same `font-size`
- **Typography overshoot**, optical margin, and CSS **`font-optical-sizing` / `opsz`**

> We read with our eyes, not with rulers — Tobias Frere-Jones (type mechanics).

Grounded in **Apple HIG** optical centering, Material-style **keylines**, type overshoot literature, and production **pad-in-asset** hand-off—not universal +2px mythology.

---

## Install

### Claude Code

```bash
git clone https://github.com/vinimrdi/optical-adjustment.git
mkdir -p ~/.claude/skills
cp -R optical-adjustment/skills/optical-alignment-ui ~/.claude/skills/optical-alignment-ui
# Project scope: .claude/skills/optical-alignment-ui
```

Then start a **new session** and run `/optical-alignment-ui` or describe an off-center icon.

### Cursor

```bash
mkdir -p ~/.cursor/skills
cp -R optical-adjustment/skills/optical-alignment-ui ~/.cursor/skills/optical-alignment-ui
# Or: .cursor/skills/ · .agents/skills/
```

Use `/optical-alignment-ui` or `@` attach in Agent chat.

### Codex / shared agents path

```bash
mkdir -p ~/.agents/skills
cp -R optical-adjustment/skills/optical-alignment-ui ~/.agents/skills/optical-alignment-ui
```

### Lovable and chat UIs

Attach `skills/optical-alignment-ui/SKILL.md` plus needed files from `references/`. Prefer **review-only**, then implement with the [implementation prompt](docs/compatibility-and-integrations.md#implementation-prompt-after-approval).

### CLI

```bash
npx skills add vinimrdi/optical-adjustment --skill optical-alignment-ui
```

**Layout rule:** `SKILL.md` must be at `optical-alignment-ui/SKILL.md` (no extra nesting).

Full matrix: **[docs/compatibility-and-integrations.md](docs/compatibility-and-integrations.md)**.

> **Note:** GitHub may still show the repo slug `optical-adjustment`. Rename to `optical-alignment-ui` in Settings for a matching URL and stronger SEO slug.

---

## Ask your agent

```text
Use the Optical Alignment UI skill on this toolbar.
Flag mathematical vs optical centering. Prefer pad-in-asset for hand-off.
Do not change touch targets. Explain each nudge in plain language.
```

```text
/optical-alignment-ui
This play control looks off-center. Align the glyph only; keep the frame fixed.
```

```text
Audit icon set visual weight at 24px. Circles vs squares vs arrows.
Propose minimal corrections and design-system exception names.
```

---

## What you get

| Piece | Role |
|-------|------|
| **[SKILL.md](skills/optical-alignment-ui/SKILL.md)** | Triggers, method, severity, progressive disclosure |
| **Typography** | Overshoot, optical margin, `opsz`, caps, button labels |
| **Shapes & icons** | Weight, play/send, keylines, icon sets |
| **Implementation** | Asset padding, CSS, FE barycentre, platform APIs |
| **Compatibility** | Claude, Cursor, Codex, Lovable |
| **SEO / AEO** | Definitions, FAQ, discovery keywords |

---

## Method (short)

| Step | Action |
|------|--------|
| Observe | Imbalance at target size (optional blur test) |
| Explain | Weight, contact, area, overshoot, keyline |
| Correct | Smallest nudge or pad-in-asset; preserve targets |
| Validate | 1×/2×, set review, contrast |

Pairs with UX-laws / accessibility skills: **task and a11y first**, optical polish second.

---

## FAQ

**Mathematical vs optical alignment?**  
Math uses boxes and equal margins; optical uses perceived mass so the UI *looks* centered.

**Why is this an agent skill?**  
Coding agents default to geometric centering. This skill teaches when perception should win—and how to hand off fixes without breaking design systems.

**Claude / Cursor / Lovable?**  
Yes—see [compatibility](docs/compatibility-and-integrations.md).

More: [docs/seo-and-discovery.md](docs/seo-and-discovery.md).

---

## Language

**English** is the official documentation language (SEO and collaboration).

---

## License

- **Documentation:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

---

## Maintainers

Educational craft material. Does not replace type design expertise, full accessibility audits, or user research.

**Topics to add in GitHub About:** `optical-alignment` · `optical-adjustment` · `ui-design` · `agent-skills` · `claude-code` · `cursor` · `typography` · `icons`
