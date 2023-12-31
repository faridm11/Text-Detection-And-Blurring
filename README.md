# Text Detection and Blurring Model

## Overview
This project presents a Python-based model for detecting text in images and blurring it. This tool is particularly useful for maintaining privacy and confidentiality in screen-shared images or videos. The model combines the power of OpenCV for image processing and Tesseract OCR for text detection.

## Features
- Detect text regions in images using Tesseract OCR.
- Automatically blur identified text areas, maintaining privacy.
- Process images in batch from a specified directory.
- Fast and efficient, suitable for real-time applications.

## How to Use
1. Install dependencies: OpenCV, Tesseract OCR, and Python.
2. Set `TESSDATA_PREFIX` environment variable to your Tesseract-OCR installation path.
3. Run the script with a folder path as an argument to process all images in the folder.
4. View results with text regions blurred.

## Requirements
- Python 3.x
- OpenCV
- Tesseract OCR

## Performance
- CPU : Ryzen 5 5600x
- CPU Usage: Under 10%
- 5 frames per second
