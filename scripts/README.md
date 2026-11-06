# Scripts — Optical Alignment UI

Diagnostic tools. **Centroid output is not perceptual truth.**

```bash
pip install -r scripts/requirements.txt
python scripts/generate_fixtures.py   # fixtures/play-24.png
```

`cairosvg` also needs **system Cairo** (macOS: `brew install cairo`; Debian/Ubuntu: `libcairo2`).

## `centroid.py` (PNG / WebP + alpha)

```bash
python scripts/centroid.py fixtures/play-24.png --verbose
python scripts/centroid.py path/to/icon.png --json --threshold 8
```

## `svg_centroid.py` (SVG → raster at UI size)

```bash
python scripts/svg_centroid.py fixtures/play.svg --size 24 -v
python scripts/svg_centroid.py fixtures/play-loose-viewbox.svg --size 24 --json
python scripts/svg_centroid.py icons/play.svg --size 48 --write-png /tmp/play-48.png
```

## Smoke (from repo root)

```bash
python scripts/generate_fixtures.py
python scripts/centroid.py fixtures/play-24.png --json
python scripts/svg_centroid.py fixtures/play.svg --size 24 --json
```

Expect `ok: true` and non-null `alpha_centroid`. Loose viewBox fixture should show larger `offset_from_canvas` and often `likely_viewbox_or_padding_issue: true`.

## Interpretation

| Signal | Action |
|--------|--------|
| Large offset vs canvas | Inspect viewBox / export padding first |
| Offset vs ink bbox on play triangle | Normal asymmetry; pad-in-asset + eye |
| Numbers look fine, UI still wrong | Perception/context — Abstain from blind CSS |

Full method: `skills/optical-alignment-ui/SKILL.md`.
