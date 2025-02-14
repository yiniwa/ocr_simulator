# ocr_simulator/examples/demo.py
import os
from pathlib import Path
import shutil
from ocr_simulator import OCRSimulator
import pandas as pd


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


def demo_minimal_noise_text():
    """Demo using single text input."""
    print("\n=== Demo 1: Minimal Noise Text Processing ===")

    output_dir = ensure_output_dir("ocr_output/Minimal_Noise")

    simulator = OCRSimulator(
        condition='Minimal Noise',
        language='eng',
        save_images=True,
        output_dir=output_dir
    )

    text = "This is a Minimal Noise text for OCR simulation."
    result = simulator.process_input(
        text,
        input_type='text',
        save_image=True,
        image_filename=os.path.join(output_dir, "Minimal_Noise.png")
    )

    print(f"Original text: {result['original_text']}")
    print(f"OCR output: {result['ocr_text']}")


def demo_blackletter():
    """Demo using blackletter font."""
    print("\n=== Demo 2: Blackletter Font Processing ===")

    output_dir = ensure_output_dir("ocr_output/Blackletter")

    simulator = OCRSimulator(
        condition='BlackLetter',  # Correct capitalization
        language='deu',
        font_path="/Library/Fonts/Canterbury.ttf",
        save_images=True,
        output_dir=output_dir
    )

    german_text = "Dies ist ein Beispieltext in deutscher Sprache."
    result = simulator.process_input(german_text, input_type='text')

    print(f"Original text: {result['original_text']}")
    print(f"OCR output: {result['ocr_text']}")


def demo_distorted():
    """Demo using distorted text."""
    print("\n=== Demo 3: Scanned Distorted Noise Text Processing ===")

    output_dir = ensure_output_dir("ocr_output/Scanned_Distorted_Noise")

    simulator = OCRSimulator(
        condition='Scanned Distorted Noise',
        language='eng',
        save_images=True,
        output_dir=output_dir,
        config={
            'skew_range': (-0.06, 0.06),
            'incomplete_prob': 0.15,
            'gap_range': (1, 3),
            'text_noise_range': (-30, 30),
            'bg_noise_prob': 0.05,
            'bg_noise_range': (-10, 10)
        }
    )

    # Create DataFrame from list
    texts = [
        "First sample text with distortion.",
        "Second sample text to process.",
        "Third text with different content."
    ]
    df = pd.DataFrame({'text': texts})

    results = simulator.process_dataframe(
        df,
        output_csv=os.path.join(output_dir, "results.csv"),
        image_prefix="Scanned_Distorted_Noise"
    )
    print("\nProcessed multiple texts with Scanned Distorted Noise:")
    print(results)


def demo_salt_and_pepper():
    """Demo using Salt and Pepper."""
    print("\n=== Demo 4: Salt and Pepper Processing ===")

    output_dir = ensure_output_dir("ocr_output/Salt_and_Pepper")

    simulator = OCRSimulator(
        condition='Salt and Pepper',
        language='eng',
        save_images=True,
        output_dir=output_dir,
        config={'dot_density': 0.0045},
        n_jobs=1
    )

    df = pd.DataFrame({
        'text': [
            "Sample text with noise.",
            "Another text to process.",
            "Testing noise effects."
        ]
    })

    results = simulator.process_dataframe(
        df,
        output_csv=os.path.join(output_dir, "results.csv"),
        image_prefix="Salt_and_Pepper"
    )
    print("\nProcessed DataFrame with Salt and Pepper:")
    print(results)


def main():
    """Run all demos."""
    try:
        demo_minimal_noise_text()
        demo_blackletter()
        demo_distorted()
        demo_salt_and_pepper()
    except Exception as e:
        print(f"\nError running demo: {e}")
        print("Please check disk space and permissions.")


if __name__ == "__main__":
    main()
