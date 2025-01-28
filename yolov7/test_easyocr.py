import easyocr
import cv2

# Initialize EasyOCR Reader
reader = easyocr.Reader(['en'])

# Load an image (replace 'path_to_image' with your image path)
image_path = r'C:\Users\siyam\Documents\Gate-system-using-YOLO\images\train\download (1).jpeg'
image = cv2.imread(image_path)

# Perform OCR
results = reader.readtext(image)

# Print results
for (bbox, text, prob) in results:
    print(f'Detected text: {text} with probability: {prob:.2f}')