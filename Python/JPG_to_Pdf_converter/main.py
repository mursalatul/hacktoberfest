#!/usr/bin/env python3
"""Minimal JPG/PNG -> PDF converter.

Usage: python main.py /abs/path/to/image.png -o /abs/path/to/out.pdf
"""
import sys
from pathlib import Path


def main():
    args = sys.argv[1:]
    if not args:
        print("Usage: main.py <input.png> -o <output.pdf>")
        return 2

    try:
        inp = Path(args[0])
        if "-o" in args:
            o_index = args.index("-o")
            out = Path(args[o_index + 1])
        else:
            out = inp.with_suffix('.pdf')
    except Exception as e:
        print("Invalid arguments", e)
        return 2

    try:
        from PIL import Image
    except Exception:
        print("Pillow is required. Install with: pip install Pillow")
        return 3

    if not inp.exists():
        print(f"Input file not found: {inp}")
        return 1

    im = Image.open(inp).convert('RGB')
    im.save(out, format='PDF')
    print(f"Saved PDF: {out}")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
