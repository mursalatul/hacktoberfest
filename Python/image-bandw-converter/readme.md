# Image to Black and White Converter 🖼️➡️⚫⚪

A simple Python tool that converts your color images to beautiful black and white photos. Perfect for photographers, designers, and anyone who wants to create stunning monochrome images!

**Author:** Rasheduzzaman Rakib  
**Version:** 1.0.0

## ✨ What it does

- 🎨 **Convert single images** or **entire folders** to black and white
- 📁 **5 different styles** - from natural grayscale to artistic effects
- 🌐 **Works with all common formats** - JPEG, PNG, GIF, BMP, TIFF, WebP
- � **Fast and easy** - just one command and you're done!

## 🚀 Quick Start (3 steps!)

**What you need:** Python 3.6+ installed on your computer

### Step 1: Download the code
```bash
git clone https://github.com/rasheduzzamanrakib/hacktoberfest.git
cd hacktoberfest/Python/image-bandw-converter
```

### Step 2: Install the image library
```bash
pip install Pillow
```

### Step 3: Start converting!
```bash
python main.py your_photo.jpg black_white_photo.jpg
```

That's it! Your black and white image is ready 🎉

## 📖 How to Use

### Convert a Single Image
```bash
# Basic conversion (recommended for most photos)
python main.py my_photo.jpg my_photo_bw.jpg

# High contrast for documents/text
python main.py document.png document_bw.png -m 1

# Natural look for portraits
python main.py portrait.jpg portrait_bw.jpg -m weighted

# Artistic effect
python main.py artwork.jpg artwork_bw.jpg -m desaturate
```

### Convert Multiple Images at Once
```bash
# Convert all images in a folder
python main.py ./my_photos ./black_white_photos -d

# Include subfolders too
python main.py ./all_photos ./bw_photos -d -r
```

### Different Styles Available
- **Default** (`-m L`) - Good for most photos
- **High contrast** (`-m 1`) - Perfect for documents and text  
- **Natural** (`-m weighted`) - Best for portraits and people
- **Artistic** (`-m desaturate`) - Creative effect
- **With transparency** (`-m LA`) - For PNG images with transparent backgrounds

## 📝 Quick Reference

| What you want to do | Command |
|---------------------|---------|
| Convert one image | `python main.py input.jpg output.jpg` |
| Convert whole folder | `python main.py ./photos ./bw_photos -d` |
| High contrast (text/docs) | `python main.py input.jpg output.jpg -m 1` |
| Natural look (portraits) | `python main.py input.jpg output.jpg -m weighted` |
| See all options | `python main.py --help` |

## 🎨 Different Styles Explained

### 🔸 Default Style (`L`)
**When to use:** Most photos, quick conversions  
**Result:** Balanced black and white that works well for everything

### 🔸 High Contrast (`1`) 
**When to use:** Text documents, sketches, vintage look  
**Result:** Pure black and white pixels only - dramatic effect

### 🔸 Natural Style (`weighted`)
**When to use:** Portraits, professional photos  
**Result:** Most natural-looking conversion that mimics how your eyes see

### 🔸 Artistic Style (`desaturate`)
**When to use:** Creative projects, maintaining mood  
**Result:** Removes color but keeps the original lighting

### � With Transparency (`LA`)
**When to use:** PNG logos, graphics with transparent backgrounds  
**Result:** Black and white but keeps transparent areas

## 📁 Supported Image Types

**Works with all common formats:**
- JPEG (`.jpg`, `.jpeg`) - Most photos
- PNG (`.png`) - Screenshots, logos
- GIF (`.gif`) - Animated images (converts first frame)
- BMP (`.bmp`) - Windows bitmap files
- TIFF (`.tiff`, `.tif`) - Professional photos
- WebP (`.webp`) - Modern web format

Just use the same file extension for your output file!

## 💡 Examples

### For Photographers
```bash
# Convert wedding photos
python main.py ./wedding_photos ./wedding_bw -d -m weighted

# Quick batch conversion
python main.py ./photoshoot ./photoshoot_bw -d
```

### For Documents
```bash
# Make scanned documents crisp
python main.py scan.jpg clean_scan.jpg -m 1
```

### For Social Media
```bash
# Vintage Instagram effect
python main.py selfie.jpg vintage_selfie.jpg -m 1

# Artistic mood
python main.py landscape.jpg artistic_landscape.jpg -m desaturate
```

## ⚡ Performance

**It's fast!** 
- Small photos (1920×1080): Less than 1 second
- Large photos (4K): About 1-2 seconds  
- Batch processing: 50-200 images per minute

**Memory friendly:**
- Uses only the memory needed for one image at a time
- Works even with large photo collections

## � Common Issues & Solutions

### "pip install Pillow" doesn't work?
```bash
# Try this instead:
python -m pip install Pillow
```

### "No module named PIL" error?
```bash
# Make sure Pillow installed correctly:
pip install Pillow
```

### "File not found" error?
- Check your file path is correct
- Make sure the image file exists
- Try using the full path: `/home/user/photo.jpg`

### Image doesn't look right?
- For photos of people: `python main.py photo.jpg output.jpg -m weighted`
- For documents: `python main.py doc.jpg output.jpg -m 1`
- For artistic effect: `python main.py art.jpg output.jpg -m desaturate`

### Need more help?
Open an issue on GitHub with your error message and what command you used.

## 🤝 Want to Help?

This project is part of **Hacktoberfest 2025**! 🎃

**Easy ways to contribute:**
- Found a bug? [Report it here](https://github.com/rasheduzzamanrakib/hacktoberfest/issues)
- Have an idea? Share it in the issues
- Fix typos in this README
- Test it on your computer and let us know how it works

**For developers:**
1. Fork the repository
2. Make your improvements  
3. Test with different images
4. Submit a pull request

All skill levels welcome! 🙌

## 🙏 Credits

**Made by:** Rasheduzzaman Rakib  
**Built with:** Python + Pillow library  
**License:** MIT (free to use!)

## 🎉 Ready to Try It?

**Get started now:**
```bash
git clone https://github.com/rasheduzzamanrakib/hacktoberfest.git
cd hacktoberfest/Python/image-bandw-converter
pip install Pillow
python main.py your_photo.jpg black_white_photo.jpg
```

**Questions?** [Open an issue on GitHub](https://github.com/rasheduzzamanrakib/hacktoberfest/issues)  
**Like it?** Give it a ⭐ on GitHub!

**Happy Converting! �➡️⚫⚪**