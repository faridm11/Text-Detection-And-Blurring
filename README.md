#Text Detection and Blurring Model 

Overview
This project presents a Python-based model for detecting text in images and blurring it. This tool is particularly useful for maintaining privacy and confidentiality in screen-shared images or videos. The model combines the power of OpenCV for image processing and Tesseract OCR for text detection.

Features
Detect text regions in images using Tesseract OCR.
Automatically blur identified text areas, maintaining privacy.
Process images in batch from a specified directory.
Fast and efficient, suitable for real-time applications.
How to Use
Install dependencies: OpenCV, Tesseract OCR, and Python.
Set TESSDATA_PREFIX environment variable to your Tesseract-OCR installation path.
Run the script with a folder path as an argument to process all images in the folder.
View results with text regions blurred.
Requirements
Python 3.x
OpenCV
Tesseract OCR
