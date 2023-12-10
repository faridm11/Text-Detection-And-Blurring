import time
import cv2
import tesserocr
from PIL import Image
import numpy as np
import time
import os
import sys  

os.environ['TESSDATA_PREFIX'] = r'C:\Program Files\Tesseract-OCR'

def preprocess_image(image_path):
    img = cv2.imread(image_path)
    if img is None:
        print(f"Error: Unable to load image at {image_path}")
        return None

    final_image = img
    return final_image 

def perform_ocr_and_blur(original_img):
    with tesserocr.PyTessBaseAPI(path=r'C:\Program Files\Tesseract-OCR\tessdata') as api:
        api.SetImage(Image.fromarray(original_img))
        boxes = api.GetComponentImages(tesserocr.RIL.TEXTLINE, True)

        for _, (im, box, _, _) in enumerate(boxes):
            x, y, w, h = box['x'], box['y'], box['w'], box['h']
            roi = original_img[y:y+h, x:x+w]
            blurred_roi = cv2.GaussianBlur(roi, (15, 15), 0)
            original_img[y:y+h, x:x+w] = blurred_roi

    return original_img

def process_image(image_path):
    original_img = cv2.imread(image_path)  
    if original_img is None:
        print(f"Error: Unable to load image at {image_path}")
        return

    preprocessed_image = preprocess_image(image_path)
    if preprocessed_image is not None:
        result_image = perform_ocr_and_blur(original_img)
        result_path = f"result_{os.path.basename(image_path)}"
        cv2.imwrite(result_path, result_image)
        print(f"Processed image saved as {result_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <image_path>")
        sys.exit(1)

    image_path = sys.argv[1]  # Get the image path from the command line argument
    start_time = time.time()
    process_image(image_path)
    end_time = time.time()
    print(f"Processed  image in {end_time - start_time} seconds")