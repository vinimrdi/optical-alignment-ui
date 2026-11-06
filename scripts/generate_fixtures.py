#!/usr/bin/env python3
"""Generate fixtures/play-24.png for centroid.py smoke tests."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "fixtures" / "play-24.png"


def main() -> int:
    try:
        from PIL import Image, ImageDraw
    except ImportError:
        raise SystemExit("pip install pillow") from None

    im = Image.new("RGBA", (24, 24), (0, 0, 0, 0))
    draw = ImageDraw.Draw(im)
    # Matches fixtures/play.svg path mass (play triangle)
    draw.polygon([(8, 5.5), (8, 18.5), (19, 12)], fill=(17, 17, 17, 255))
    OUT.parent.mkdir(parents=True, exist_ok=True)
    im.save(OUT)
    print(f"Wrote {OUT} ({OUT.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
