#!/usr/bin/env python3
"""
Alpha-weighted centroid diagnostic for Optical Alignment UI.

Centroid is a geometry tool — not guaranteed perceptual center.
See skills/optical-alignment-ui/references/geometry-and-centroids.md

Usage:
  python scripts/centroid.py icon.png
  python scripts/centroid.py icon.png --json --threshold 8
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def load_rgba(path: Path):
    try:
        from PIL import Image
    except ImportError as e:
        raise SystemExit(
            "Pillow is required: pip install pillow\n"
            f"Original error: {e}"
        ) from e

    im = Image.open(path)
    if im.mode != "RGBA":
        im = im.convert("RGBA")
    return im


def analyze(im, threshold: int) -> dict:
    """
    threshold: minimum alpha (0-255) to count as ink for bbox;
    centroid always weights by alpha (pixels below threshold contribute 0).
    """
    w, h = im.size
    pixels = im.load()

    sum_a = 0.0
    sum_ax = 0.0
    sum_ay = 0.0

    min_x, min_y = w, h
    max_x, max_y = -1, -1
    ink_count = 0

    for y in range(h):
        for x in range(w):
            r, g, b, a = pixels[x, y]
            if a <= 0:
                continue
            # Weighted centroid uses full alpha mass
            sum_a += a
            sum_ax += x * a
            sum_ay += y * a
            if a >= threshold:
                ink_count += 1
                if x < min_x:
                    min_x = x
                if y < min_y:
                    min_y = y
                if x > max_x:
                    max_x = x
                if y > max_y:
                    max_y = y

    canvas_cx = (w - 1) / 2.0
    canvas_cy = (h - 1) / 2.0

    if sum_a <= 0:
        return {
            "ok": False,
            "error": "no_visible_pixels",
            "width": w,
            "height": h,
            "threshold": threshold,
            "canvas_center": {"x": canvas_cx, "y": canvas_cy},
        }

    alpha_cx = sum_ax / sum_a
    alpha_cy = sum_ay / sum_a

    if ink_count == 0:
        ink_bbox = None
        ink_bbox_center = None
        offset_from_ink = None
    else:
        ink_bbox = {
            "left": min_x,
            "top": min_y,
            "right": max_x,
            "bottom": max_y,
            "width": max_x - min_x + 1,
            "height": max_y - min_y + 1,
        }
        ink_cx = (min_x + max_x) / 2.0
        ink_cy = (min_y + max_y) / 2.0
        ink_bbox_center = {"x": ink_cx, "y": ink_cy}
        offset_from_ink = {
            "x": alpha_cx - ink_cx,
            "y": alpha_cy - ink_cy,
        }

    result = {
        "ok": True,
        "width": w,
        "height": h,
        "threshold": threshold,
        "ink_pixel_count": ink_count,
        "alpha_mass_sum": sum_a,
        "canvas_center": {"x": canvas_cx, "y": canvas_cy},
        "alpha_centroid": {"x": alpha_cx, "y": alpha_cy},
        "ink_bbox": ink_bbox,
        "ink_bbox_center": ink_bbox_center,
        "offset_from_canvas": {
            "x": alpha_cx - canvas_cx,
            "y": alpha_cy - canvas_cy,
        },
        "offset_from_ink_bbox": offset_from_ink,
        "disclaimer": (
            "Alpha centroid is a diagnostic mass center, not perceptual center. "
            "Judge at target UI size; prefer pad-in-asset for hand-off."
        ),
    }
    return result


def format_human(data: dict, verbose: bool) -> str:
    if not data.get("ok"):
        return (
            f"Error: {data.get('error', 'unknown')}\n"
            f"Image: {data.get('width')}×{data.get('height')}\n"
        )

    lines = [
        f"Size:              {data['width']}×{data['height']} px",
        f"Alpha threshold:   {data['threshold']} (ink bbox)",
        f"Ink pixels:        {data['ink_pixel_count']}",
        "",
        f"Canvas center:     ({data['canvas_center']['x']:.3f}, {data['canvas_center']['y']:.3f})",
        f"Alpha centroid:    ({data['alpha_centroid']['x']:.3f}, {data['alpha_centroid']['y']:.3f})",
        f"Offset vs canvas:  ({data['offset_from_canvas']['x']:+.3f}, {data['offset_from_canvas']['y']:+.3f}) px",
    ]

    if data.get("ink_bbox_center"):
        ib = data["ink_bbox"]
        lines += [
            f"Ink bbox:          L{ib['left']} T{ib['top']} R{ib['right']} B{ib['bottom']} "
            f"({ib['width']}×{ib['height']})",
            f"Ink bbox center:   ({data['ink_bbox_center']['x']:.3f}, {data['ink_bbox_center']['y']:.3f})",
            f"Offset vs ink box: ({data['offset_from_ink_bbox']['x']:+.3f}, "
            f"{data['offset_from_ink_bbox']['y']:+.3f}) px",
        ]

    lines += ["", data["disclaimer"]]

    if verbose:
        lines += [
            "",
            "Hints:",
            "  • Large offset vs canvas + ink in one corner → fix viewBox/export padding first.",
            "  • Offset vs ink bbox ≠ 0 on triangles is normal; still judge by eye at UI size.",
            "  • Export PNG at target control size on transparent background for best signal.",
        ]

    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Alpha-weighted centroid diagnostic for optical alignment. "
            "Not a substitute for perceptual judgment."
        )
    )
    parser.add_argument("image", type=Path, help="PNG/WebP/GIF path (alpha preferred)")
    parser.add_argument(
        "--threshold",
        type=int,
        default=1,
        metavar="A",
        help="Min alpha 0-255 for ink bbox (default: 1)",
    )
    parser.add_argument("--json", action="store_true", help="Print JSON only")
    parser.add_argument("--verbose", "-v", action="store_true", help="Extra hints")
    args = parser.parse_args(argv)

    if not args.image.is_file():
        print(f"File not found: {args.image}", file=sys.stderr)
        return 1

    if not (0 <= args.threshold <= 255):
        print("--threshold must be 0-255", file=sys.stderr)
        return 1

    im = load_rgba(args.image)
    data = analyze(im, args.threshold)
    data["source"] = str(args.image)

    if args.json:
        print(json.dumps(data, indent=2))
    else:
        print(format_human(data, args.verbose))

    return 0 if data.get("ok") else 2


if __name__ == "__main__":
    raise SystemExit(main())
