#!/usr/bin/env python3
"""
Image to Black and White Converter

A Python application that converts color images to black and white using various methods.
Supports multiple image formats including JPEG, PNG, GIF, BMP, and TIFF.

Author: Rasheduzzaman Rakib
"""

import os
import sys
import argparse
from pathlib import Path
from PIL import Image, ImageEnhance
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class ImageConverter:
    """
    A class to handle image conversion to black and white using different methods.
    """
    
    SUPPORTED_FORMATS = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.tif', '.webp'}
    
    def __init__(self):
        """Initialize the ImageConverter."""
        pass
    
    def is_supported_format(self, file_path):
        """
        Check if the file format is supported.
        
        Args:
            file_path (str): Path to the image file
            
        Returns:
            bool: True if format is supported, False otherwise
        """
        return Path(file_path).suffix.lower() in self.SUPPORTED_FORMATS
    
    def convert_to_grayscale(self, input_path, output_path, method='L'):
        """
        Convert an image to grayscale/black and white.
        
        Args:
            input_path (str): Path to the input image
            output_path (str): Path where the converted image will be saved
            method (str): Conversion method ('L', 'LA', '1', 'weighted', 'desaturate')
            
        Returns:
            bool: True if conversion successful, False otherwise
        """
        try:
            # Validate input file
            if not os.path.exists(input_path):
                logger.error(f"Input file does not exist: {input_path}")
                return False
            
            if not self.is_supported_format(input_path):
                logger.error(f"Unsupported file format: {input_path}")
                return False
            
            # Open the image
            logger.info(f"Opening image: {input_path}")
            with Image.open(input_path) as img:
                # Convert based on method
                if method == 'L':
                    # Standard grayscale conversion
                    bw_img = img.convert('L')
                    
                elif method == 'LA':
                    # Grayscale with alpha channel
                    bw_img = img.convert('LA')
                    
                elif method == '1':
                    # Pure black and white (1-bit)
                    bw_img = img.convert('1')
                    
                elif method == 'weighted':
                    # Weighted average method (custom weights for RGB)
                    if img.mode != 'RGB':
                        img = img.convert('RGB')
                    
                    # Create a new grayscale image using weighted average
                    # Standard weights: R=0.299, G=0.587, B=0.114
                    width, height = img.size
                    bw_img = Image.new('L', (width, height))
                    
                    # Get pixel data
                    rgb_pixels = img.load()
                    bw_pixels = bw_img.load()
                    
                    # Apply weighted conversion pixel by pixel
                    for x in range(width):
                        for y in range(height):
                            r, g, b = rgb_pixels[x, y]
                            gray_value = int(r * 0.299 + g * 0.587 + b * 0.114)
                            bw_pixels[x, y] = gray_value
                    
                elif method == 'desaturate':
                    # Desaturation method
                    if img.mode != 'RGB':
                        img = img.convert('RGB')
                    
                    # Convert to HSV and set saturation to 0
                    enhancer = ImageEnhance.Color(img)
                    bw_img = enhancer.enhance(0)
                    
                else:
                    logger.warning(f"Unknown method '{method}', using default 'L' method")
                    bw_img = img.convert('L')
                
                # Create output directory if it doesn't exist
                output_dir = os.path.dirname(output_path)
                if output_dir and not os.path.exists(output_dir):
                    os.makedirs(output_dir, exist_ok=True)
                
                # Save the converted image
                logger.info(f"Saving converted image: {output_path}")
                bw_img.save(output_path)
                
                # Display image info
                logger.info(f"Original image size: {img.size}")
                logger.info(f"Original image mode: {img.mode}")
                logger.info(f"Converted image mode: {bw_img.mode}")
                
                return True
                
        except Exception as e:
            logger.error(f"Error converting image: {e}")
            return False
    
    def batch_convert(self, input_dir, output_dir, method='L', recursive=False):
        """
        Convert multiple images in a directory to black and white.
        
        Args:
            input_dir (str): Directory containing input images
            output_dir (str): Directory to save converted images
            method (str): Conversion method
            recursive (bool): Whether to process subdirectories recursively
            
        Returns:
            tuple: (success_count, total_count)
        """
        if not os.path.exists(input_dir):
            logger.error(f"Input directory does not exist: {input_dir}")
            return 0, 0
        
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        
        success_count = 0
        total_count = 0
        
        # Get all image files
        pattern = "**/*" if recursive else "*"
        input_path = Path(input_dir)
        
        for file_path in input_path.glob(pattern):
            if file_path.is_file() and self.is_supported_format(str(file_path)):
                total_count += 1
                
                # Create corresponding output path
                relative_path = file_path.relative_to(input_path)
                output_file = Path(output_dir) / relative_path
                
                # Add '_bw' suffix to filename
                output_file = output_file.with_name(
                    f"{output_file.stem}_bw{output_file.suffix}"
                )
                
                # Ensure output directory exists
                output_file.parent.mkdir(parents=True, exist_ok=True)
                
                if self.convert_to_grayscale(str(file_path), str(output_file), method):
                    success_count += 1
                    logger.info(f"Converted: {file_path} -> {output_file}")
                else:
                    logger.error(f"Failed to convert: {file_path}")
        
        return success_count, total_count


def main():
    """Main function to handle command-line interface."""
    parser = argparse.ArgumentParser(
        description="Convert images to black and white",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s input.jpg output.jpg
  %(prog)s input.png output.png -m weighted
  %(prog)s input.jpg output.jpg -m 1
  %(prog)s -d /path/to/images /path/to/output
  %(prog)s -d /path/to/images /path/to/output -r -m desaturate

Conversion methods:
  L          - Standard grayscale (default)
  LA         - Grayscale with alpha channel
  1          - Pure black and white (1-bit)
  weighted   - Weighted RGB average
  desaturate - HSV desaturation method
        """
    )
    
    parser.add_argument('input', nargs='?', help='Input image file')
    parser.add_argument('output', nargs='?', help='Output image file')
    
    parser.add_argument('-d', '--directory', action='store_true',
                       help='Process entire directory')
    parser.add_argument('-r', '--recursive', action='store_true',
                       help='Process directories recursively')
    parser.add_argument('-m', '--method', 
                       choices=['L', 'LA', '1', 'weighted', 'desaturate'],
                       default='L',
                       help='Conversion method (default: L)')
    parser.add_argument('-v', '--verbose', action='store_true',
                       help='Enable verbose logging')
    parser.add_argument('--version', action='version', version='%(prog)s 1.0.0')
    
    args = parser.parse_args()
    
    # Set logging level
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    
    # Validate arguments
    if not args.directory and (not args.input or not args.output):
        parser.error("Input and output files are required unless using --directory")
    
    if args.directory and (not args.input or not args.output):
        parser.error("Input and output directories are required when using --directory")
    
    if args.recursive and not args.directory:
        parser.error("--recursive can only be used with --directory")
    
    # Initialize converter
    converter = ImageConverter()
    
    try:
        if args.directory:
            # Batch processing
            logger.info(f"Starting batch conversion from {args.input} to {args.output}")
            success_count, total_count = converter.batch_convert(
                args.input, args.output, args.method, args.recursive
            )
            
            logger.info(f"Batch conversion completed: {success_count}/{total_count} images converted successfully")
            
            if success_count == total_count:
                print(f"✅ Successfully converted all {total_count} images!")
            elif success_count > 0:
                print(f"⚠️  Converted {success_count} out of {total_count} images.")
            else:
                print(f"❌ Failed to convert any images.")
                sys.exit(1)
        
        else:
            # Single file processing
            logger.info(f"Converting single image: {args.input} -> {args.output}")
            
            if converter.convert_to_grayscale(args.input, args.output, args.method):
                print(f"✅ Successfully converted {args.input} to {args.output}")
            else:
                print(f"❌ Failed to convert {args.input}")
                sys.exit(1)
    
    except KeyboardInterrupt:
        logger.info("Conversion interrupted by user")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()