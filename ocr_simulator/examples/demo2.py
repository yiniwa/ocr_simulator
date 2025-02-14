# ocr_simulator/examples/demo2.py

import os
from pathlib import Path
import shutil
from ocr_simulator import OCRSimulator
from PIL import Image, ImageDraw, ImageFont


def ensure_output_dir(base_dir: str) -> str:
    """Create output directory with error handling."""
    try:
        output_dir = os.path.join(os.getcwd(), base_dir)
        os.makedirs(output_dir, exist_ok=True)
        print(f"Using output directory: {output_dir}")

        total, used, free = shutil.disk_usage(os.path.dirname(output_dir))
        if free < 1_000_000_000:  # Less than 1GB
            print("Warning: Low disk space available!")

        return output_dir
    except OSError as e:
        print(f"Error creating output directory: {e}")
        temp_dir = os.path.join(os.path.expanduser("~"), "temp_ocr_output")
        os.makedirs(temp_dir, exist_ok=True)
        print(f"Falling back to temporary directory: {temp_dir}")
        return temp_dir


def demo_with_custom_sizes():
    """Demo showing different size configurations."""
    print("\n=== Demo: Custom Size Configurations ===")

    output_dir = ensure_output_dir("ocr_output/custom_sizes")

    # Example 1: Large font with specific image size
    simulator_large = OCRSimulator(
        condition='Minimal Noise',
        language='eng',
        font_size=24,  # Larger font
        image_width=800,  # Fixed width
        image_height=400,  # Fixed height
        dpi=300,  # Standard DPI for testing
        save_images=True,
        output_dir=output_dir
    )

    test_text = "Testing custom size configurations for OCR simulation."

    font = ImageFont.truetype(
        simulator_large.font_path, simulator_large.font_size_px)
    image = Image.new('RGB', (800, 400), color="white")
    draw = ImageDraw.Draw(image)

    text_position = (50, 150)
    # Black text on white background
    draw.text(text_position, test_text, font=font, fill="black")

    image.save(os.path.join(output_dir, "large_font.png"))
    print(
        f"Image saved to: {os.path.join(output_dir, 'large_font.png')}")

    # Example 2: Custom margin with auto-sized image
    simulator_margin = OCRSimulator(
        condition='Minimal Noise',
        language='eng',
        font_size=12,
        margin=0.5,  # Standard margin
        save_images=True,
        output_dir=output_dir,
        dpi=300  # Standard DPI
    )

    result2 = simulator_margin.process_single_text(
        test_text,
        save_image=True,
        image_filename=os.path.join(output_dir, "large_margin.png")
    )

    print("\nLarge Margin Configuration:")
    print(f"Original text: {result2['original_text']}")
    print(f"OCR output: {result2['ocr_text']}")


def main():
    """Run the demo with error handling."""
    try:
        demo_with_custom_sizes()
    except Exception as e:
        print(f"\nError running demo: {e}")
        print("Please check disk space and permissions.")


if __name__ == "__main__":
    main()
