# Fixtures

Minimal assets for **smoke tests** of diagnostic scripts. Not production icon sets.

| File | Purpose |
|------|---------|
| `play.svg` | Right-pointing play triangle in a tight 24×24 viewBox |
| `play-loose-viewbox.svg` | Same idea with loose viewBox (ink upper-left) |
| `play-24.png` | Raster for `centroid.py` (generate if missing) |

```bash
pip install -r scripts/requirements.txt

# Create PNG if not present
python scripts/generate_fixtures.py

python scripts/centroid.py fixtures/play-24.png --json
python scripts/svg_centroid.py fixtures/play.svg --size 24 --json
python scripts/svg_centroid.py fixtures/play-loose-viewbox.svg --size 24 --json
```
