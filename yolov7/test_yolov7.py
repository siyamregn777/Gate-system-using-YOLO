import torch
from PIL import Image
import cv2
import numpy as np

# Load YOLOv7 model
model = torch.hub.load('WongKinYiu/yolov7', 'custom', 'yolov7.pt', force_reload=True)

# Load an image (replace 'path_to_image' with your image path)
image_path = r'C:\Users\siyam\Documents\Gate-system-using-YOLO\images\train\download (1).jpeg'
img = Image.open(image_path)

# Convert the image to a NumPy array
img_np = np.array(img)

# Ensure the image is writable
img_np = img_np.copy()

# Perform detection
results = model(img_np)

# Print results
results.print()  # Print results to console

# Show results
results.show()   # This should now display the results correctly