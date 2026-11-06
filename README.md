<div align="center">

# Optical Alignment UI

### Agent skill for **optical alignment** and **optical adjustment** in digital interfaces

**Precision vs perception** — evidence-based diagnosis when UI is mathematically centered but visually wrong.

[![License: CC BY 4.0](https://img.shields.io/badge/docs-CC%20BY%204.0-lightgrey?style=flat-square)](https://creativecommons.org/licenses/by/4.0/)
[![Skill](https://img.shields.io/badge/skill-v1.5.3-blue?style=flat-square)](skills/optical-alignment-ui/SKILL.md)
[![Agents](https://img.shields.io/badge/agents-Claude%20%7C%20Cursor%20%7C%20Codex%20%7C%20Lovable-111827?style=flat-square)](docs/compatibility-and-integrations.md)

[Skill](skills/optical-alignment-ui/SKILL.md) · [Examples](examples/) · [Scripts](scripts/) · [Install](#install) · [Changelog](CHANGELOG.md)

</div>

---

## What is optical alignment in UI?

Shifting or scaling UI so elements *look* balanced—even when boxes and equal margins say they are perfect. Covers play icons, circle vs square scale, icon sets, icon+label, caps, overshoot, and `font-optical-sizing`.

**Method (v1.5.3):** evidence → geometry aids (not absolute truth) → severity **×** confidence → **Implement / Propose / Abstain** → optical QA → design-system hand-off. See [anti-patterns](skills/optical-alignment-ui/references/anti-patterns.md).

Companion: **[UX Laws & Principles](https://github.com/vinimrdi/ux-laws-principles)** (task first; optical second).

---

## Install

```bash
git clone https://github.com/vinimrdi/optical-alignment-ui.git
mkdir -p ~/.claude/skills
cp -R optical-alignment-ui/skills/optical-alignment-ui ~/.claude/skills/optical-alignment-ui
# Cursor: ~/.cursor/skills/ · shared: ~/.agents/skills/
```

```bash
npx skills add vinimrdi/optical-alignment-ui --skill optical-alignment-ui
```

`SKILL.md` must sit at `optical-alignment-ui/SKILL.md`. Lovable: **attach** files—do not assume auto-discovery.  
Details: [docs/compatibility-and-integrations.md](docs/compatibility-and-integrations.md).

### Diagnostic scripts (optional)

```bash
pip install -r scripts/requirements.txt

# Raster
python scripts/centroid.py fixtures/play-24.png --verbose

# SVG at UI size (cairosvg needs system Cairo)
python scripts/svg_centroid.py fixtures/play.svg --size 24 -v
python scripts/svg_centroid.py fixtures/play-loose-viewbox.svg --size 24 --json
```

See [scripts/README.md](scripts/README.md).

---

## Ask your agent

```text
Use optical-alignment-ui on this toolbar.
Severity AND confidence. Check anti-patterns.
Abstain if evidence is weak. Prefer pad-in-asset. No touch-target changes.
```

---

## What you get

| Piece | Role |
|-------|------|
| **SKILL.md** | Workflow, outcomes, decision matrix |
| **geometry / evidence / a11y** | Diagnosis and hard stops |
| **anti-patterns / platform-behavior** | Avoid false fixes and raster traps |
| **examples/** | Core + regression cases |
| **scripts/** | `centroid.py`, `svg_centroid.py` |
| **fixtures/** | Sample PNG/SVG for smoke checks |

---

## Language & license

English · Documentation [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Educational craft—not a full a11y or user-research substitute.
