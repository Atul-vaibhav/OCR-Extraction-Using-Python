import pytesseract
import json
from PIL import Image

# Load the image
image_path = "image.png"  # Change to your image file path
image = Image.open(image_path)

# Perform OCR using pytesseract
extracted_text = pytesseract.image_to_string(image)

# Structure extracted text into JSON format (modify as per specific needs)
structured_data = {
    "patient_name": "Unknown",
    "dob": "Unknown",
    "pain_ratings": {},
    "comments": {}
}

lines = extracted_text.split("\n")
for line in lines:
    if "Patient Name" in line:
        structured_data["patient_name"] = line.split(":")[-1].strip()
    elif "DOB" in line:
        structured_data["dob"] = line.split(":")[-1].strip()
    elif "Pain" in line:
        structured_data["pain_ratings"]["Pain"] = line.split(":")[-1].strip()
    elif "Numbness" in line:
        structured_data["pain_ratings"]["Numbness"] = line.split(":")[-1].strip()
    elif "Tingling" in line:
        structured_data["pain_ratings"]["Tingling"] = line.split(":")[-1].strip()
    elif "Burning" in line:
        structured_data["pain_ratings"]["Burning"] = line.split(":")[-1].strip()
    elif "Tightness" in line:
        structured_data["pain_ratings"]["Tightness"] = line.split(":")[-1].strip()
    elif "Describe any functional changes" in line:
        structured_data["comments"]["Functional Changes"] = line.split(":")[-1].strip()

# Save structured data to JSON file
json_file_path = "structured_data.json"
with open(json_file_path, "w") as json_file:
    json.dump(structured_data, json_file, indent=4)

print(f"Structured data saved to {json_file_path}")
