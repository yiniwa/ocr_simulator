# OCR Simulator

This library for simulating OCR (Optical Character Recognition) effects by converting text to images with various degradation conditions. This library helps generate synthetic OCR training data or test OCR systems under different text conditions.

## Features

### Multiple Text Effects
- **Minimal Noise**: Clean text rendering
- **BlackLetter**: Historical font simulation
- **Scanned Distorted Noise**: Geometric distortions and skewing
- **Salt and Pepper**: Some pixels in the image randomly turn black (pepper) or white (salt)

### Flexible Input Formats
- Single text strings
- CSV files
- Text files in folders
- Pandas DataFrames
- Lists of texts

### Customization Options
- Font size and style
- Image dimensions
- DPI settings
- Multiple languages (English, German, French, Luxembourgish...)
- Parallel processing support

## Installation and Setup

### macOS
1. Install Tesseract:
```
brew install tesseract
```
2. Check which languages you have 
 ```
tesseract --list-langs
 ```
3. Add the new languages
 ```
sudo curl -L https://github.com/tesseract-ocr/tessdata/raw/main/fra.traineddata -o /opt/homebrew/share/tessdata/fra.traineddata
(Change the language name)
 ```
## Run Demo
1. Clone the Repository:
 ```
git clone https://github.com/yiniwa/ocr_simulator.git
 ```
2. Navigate to the Directory:
 ```
cd ocr-simulator
 ```
3. Run Demo
 ```
python -m ocr_simulator.examples.demo
 ```
## Quick Start
 ```
from ocr_simulator import OCRSimulator

# Initialize simulator
simulator = OCRSimulator(condition='Minimal Noise')

# Process single text
result = simulator.process_single_text(
    "Your text here",
    save_image=True,
    image_filename="output.png"
)
 ```
 
##  Language Support
Currently supported languages:

English (eng)
German (deu)
French (fra)
Luxembourgish (ltz)
