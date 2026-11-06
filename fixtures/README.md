# Fixtures

Minimal assets for **smoke tests** of diagnostic scripts. Not production icon sets.

| File | Purpose |
|------|---------|
| `play.svg` | Right-pointing play triangle in a tight 24×24 viewBox |
| `play-loose-viewbox.svg` | Same paths in a large viewBox (ink upper-left) — metadata problem |
| `play-24.png` | Rasterized play mark for `centroid.py` without cairosvg |

```bash
pip install -r scripts/requirements.txt
python scripts/centroid.py fixtures/play-24.png --json
python scripts/svg_centroid.py fixtures/play.svg --size 24 --json
python scripts/svg_centroid.py fixtures/play-loose-viewbox.svg --size 24 --json
```
