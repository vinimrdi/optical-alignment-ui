#!/usr/bin/env python3
"""
SVG centroid diagnostic for Optical Alignment UI.

Rasterizes an SVG at a target pixel size (how it will be drawn in UI),
then computes the same alpha-weighted centroid metrics as centroid.py.

Centroid is diagnostic — not perceptual truth.
See skills/optical-alignment-ui/references/geometry-and-centroids.md

Usage:
  python scripts/svg_centroid.py icon.svg --size 24
  python scripts/svg_centroid.py icon.svg --size 48 --json
  python scripts/svg_centroid.py icon.svg --size 24 --write-png /tmp/icon-24.png -v

Dependencies:
  pip install pillow cairosvg
"""

from __future__ import annotations

import argparse
import io
import json
import re
import sys
from pathlib import Path

# Allow `python scripts/svg_centroid.py` from repo root
_SCRIPTS = Path(__file__).resolve().parent
if str(_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS))

from centroid import analyze, format_human  # noqa: E402


def parse_viewbox(svg_text: str) -> dict | None:
    """Extract viewBox as min-x, min-y, width, height if present."""
    m = re.search(
        r'viewBox\s*=\s*["\']\s*([\d.+eE-]+)\s+([\d.+eE-]+)\s+([\d.+eE-]+)\s+([\d.+eE-]+)\s*["\']',
        svg_text,
        re.IGNORECASE,
    )
    if not m:
        return None
    min_x, min_y, vb_w, vb_h = (float(m.group(i)) for i in range(1, 5))
    return {
        "min_x": min_x,
        "min_y": min_y,
        "width": vb_w,
        "height": vb_h,
        "center": {"x": min_x + vb_w / 2.0, "y": min_y + vb_h / 2.0},
    }


def parse_root_size_attrs(svg_text: str) -> dict:
    """Best-effort width/height attributes on root <svg>."""
    out: dict = {}
    open_tag = re.search(r"<svg\b[^>]*>", svg_text, re.IGNORECASE | re.DOTALL)
    if not open_tag:
        return out
    tag = open_tag.group(0)
    for attr in ("width", "height"):
        m = re.search(
            rf'\b{attr}\s*=\s*["\']([^"\']+)["\']',
            tag,
            re.IGNORECASE,
        )
        if m:
            out[attr] = m.group(1).strip()
    return out


def rasterize_svg(svg_bytes: bytes, size: int, background_rgba: tuple | None = None) -> "Image.Image":
    """
    Render SVG to an RGBA PIL image of size×size pixels.
    Transparent background by default (correct for icon mass).
    """
    try:
        import cairosvg
    except ImportError as e:
        raise SystemExit(
            "cairosvg is required for SVG rasterization:\n"
            "  pip install cairosvg pillow\n"
            "On some systems you also need cairo system libs.\n"
            f"Original error: {e}"
        ) from e

    try:
        from PIL import Image
    except ImportError as e:
        raise SystemExit(
            "Pillow is required: pip install pillow\n"
            f"Original error: {e}"
        ) from e

    # output_width/height force the pixel grid agents care about in UI
    png_bytes = cairosvg.svg2png(
        bytestring=svg_bytes,
        output_width=size,
        output_height=size,
        background_color=None if background_rgba is None else None,
    )

    im = Image.open(io.BytesIO(png_bytes))
    if im.mode != "RGBA":
        im = im.convert("RGBA")

    # Ensure exact size (cairosvg should already match)
    if im.size != (size, size):
        im = im.resize((size, size), Image.Resampling.NEAREST)

    if background_rgba is not None:
        bg = Image.new("RGBA", (size, size), background_rgba)
        bg.alpha_composite(im)
        im = bg

    return im


def format_svg_header(meta: dict) -> str:
    lines = [
        f"Source SVG:        {meta.get('source')}",
        f"Raster size:       {meta.get('raster_size')}×{meta.get('raster_size')} px",
    ]
    vb = meta.get("viewBox")
    if vb:
        lines.append(
            f"viewBox:           {vb['min_x']:g} {vb['min_y']:g} "
            f"{vb['width']:g} {vb['height']:g}  "
            f"(center {vb['center']['x']:g}, {vb['center']['y']:g})"
        )
    else:
        lines.append("viewBox:           (not found)")
    attrs = meta.get("svg_size_attrs") or {}
    if attrs:
        lines.append(
            f"SVG width/height:  {attrs.get('width', '—')} × {attrs.get('height', '—')}"
        )
    lines.append("")
    return "\n".join(lines) + "\n"

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Rasterize SVG at target UI size and compute alpha-weighted centroid. "
            "Diagnostic only — not perceptual center."
        )
    )
    parser.add_argument("svg", type=Path, help="Path to .svg file")
    parser.add_argument(
        "--size",
        type=int,
        default=24,
        metavar="PX",
        help="Raster box size in CSS pixels (default: 24)",
    )
    parser.add_argument(
        "--threshold",
        type=int,
        default=1,
        metavar="A",
        help="Min alpha 0-255 for ink bbox (default: 1)",
    )
    parser.add_argument(
        "--write-png",
        type=Path,
        default=None,
        metavar="PATH",
        help="Save the rasterized RGBA PNG for inspection",
    )
    parser.add_argument("--json", action="store_true", help="Print JSON only")
    parser.add_argument("--verbose", "-v", action="store_true", help="Extra hints")
    args = parser.parse_args(argv)

    if not args.svg.is_file():
        print(f"File not found: {args.svg}", file=sys.stderr)
        return 1
    if args.size < 1:
        print("--size must be >= 1", file=sys.stderr)
        return 1
    if not (0 <= args.threshold <= 255):
        print("--threshold must be 0-255", file=sys.stderr)
        return 1

    svg_bytes = args.svg.read_bytes()
    try:
        svg_text = svg_bytes.decode("utf-8")
    except UnicodeDecodeError:
        svg_text = svg_bytes.decode("utf-8", errors="replace")

    viewbox = parse_viewbox(svg_text)
    size_attrs = parse_root_size_attrs(svg_text)

    im = rasterize_svg(svg_bytes, args.size)

    if args.write_png:
        args.write_png.parent.mkdir(parents=True, exist_ok=True)
        im.save(args.write_png)

    data = analyze(im, args.threshold)
    data["source"] = str(args.svg)
    data["source_type"] = "svg"
    data["raster_size"] = args.size
    data["viewBox"] = viewbox
    data["svg_size_attrs"] = size_attrs or None
    if args.write_png:
        data["raster_png"] = str(args.write_png)

    # Heuristic flag: ink far from canvas center often means viewBox/padding issue
    if data.get("ok") and data.get("offset_from_canvas"):
        ox = abs(data["offset_from_canvas"]["x"])
        oy = abs(data["offset_from_canvas"]["y"])
        # > 8% of size is a strong signal to inspect export
        data["likely_viewbox_or_padding_issue"] = (ox > args.size * 0.08) or (
            oy > args.size * 0.08
        )

    if args.json:
        print(json.dumps(data, indent=2))
    else:
        meta = {
            "source": str(args.svg),
            "raster_size": args.size,
            "viewBox": viewbox,
            "svg_size_attrs": size_attrs,
        }
        print(format_svg_header(meta), end="")
        print(format_human(data, args.verbose), end="")
        if data.get("ok") and data.get("likely_viewbox_or_padding_issue"):
            print(
                "\nFlag: large offset vs canvas — inspect viewBox / empty padding "
                "before applying optical CSS nudges."
            )
        if args.write_png:
            print(f"\nWrote raster: {args.write_png}")

    return 0 if data.get("ok") else 2


if __name__ == "__main__":
    raise SystemExit(main())
