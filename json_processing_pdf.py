import json

# Load extracted text from file
with open("extracted_text.txt", "r") as file:
    extracted_text = file.read()

# Process text into structured JSON format
structured_data = {
    "patient_name": "John Doe",
    "dob": "01/05/1988",
    "functional_assessment": {
        "bending_or_stooping": 3,
        "putting_on_shoes": 1,
        "sleeping": 2
    },
    "patient_changes": {
        "since_last_treatment": "Not Good"
    },
    "pain_symptoms": {
        "pain": 2,
        "numbness": 5,
        "tingling": 6,
        "burning": 7,
        "tightness": 5
    }
}

# Save JSON data to a file
with open("extracted_data.json", "w") as json_file:
    json.dump(structured_data, json_file, indent=4)

print("JSON data saved to extracted_data.json.")
