(The file `/home/md-asraful-molla/D_Drive/Hacktoberfest/hacktoberfest/Python/JPG_to_Pdf_converter/README.md` exists, but is empty)
# JPG/PNG to PDF Converter

Small CLI tool to convert images (JPG, PNG, WEBP) into PDF files using Pillow.

Installation

1. Create a virtualenv (recommended) and install requirements:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Usage

Convert multiple images into a single PDF:

```bash
python main.py images/*.jpg -o album.pdf
```

Create one PDF per image:

```bash
python main.py -d ./photos --single -O ./pdfs
```

Help:

```bash
python main.py --help
```

Notes

- The script requires Pillow. It converts images to RGB before writing to PDF to avoid alpha/CMYK issues.
- By default the combined PDF is written to `out.pdf` and individual PDFs to `./pdfs`.

