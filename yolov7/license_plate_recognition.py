import cv2
import easyocr
import requests
import os

# Initialize EasyOCR reader globally
reader = easyocr.Reader(['en'])

def check_plate_in_database(plate):
    """
    Check if the license plate exists in the database by sending a request to the API.
    """
    try:
        response = requests.get(f"http://localhost:5000/check_plate?plate={plate}")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error checking plate in database: {e}")
        return {"registered": False}

def extract_license_plate(image_path):
    """
    Extract potential license plate text from an image using EasyOCR.
    """
    # Read the image
    frame = cv2.imread(image_path)
    if frame is None:
        print("Error: Could not read image.")
        return None

    # Perform OCR to get the text
    ocr_results = reader.readtext(frame)
    
    detected_texts = []
    for (bbox, text, prob) in ocr_results:
        if len(text) >= 3:  # Filter based on your needs
            detected_texts.append(text.strip())
    
    return detected_texts

def main(image_path):
    # Extract text from the provided image path
    detected_texts = extract_license_plate(image_path)

    if detected_texts:
        for text in detected_texts:
            print(f"Detected License Plate: {text}")

            # Check database
            result = check_plate_in_database(text)
            if result.get("registered"):
                print("Access Granted")
            else:
                print("Access Denied")
    else:
        print("No license plate detected.")

if __name__ == "__main__":
    
    image_path = r"C:\Users\siyam\Pictures\1faf1862-1b51-497c-8154-ab8a5e2ba955.png " 
    # image_path = r"C:\Users\siyam\Pictures\A_realistic_image_of_a_generic_license_plate_featuring_a_white_background_with_blue_letters_and_numbers_The_plate_should_display_the_fictional_license_plate_number_XYZ_5678_The_edges_of_the_plate_should_be_slightl.jpeg " 

    main(image_path)