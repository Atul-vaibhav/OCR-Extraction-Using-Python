import pytesseract
from pdf2image import convert_from_path

# Define the PDF file path
pdf_path = "oaksoldata.pdf"

# Convert PDF pages to images
images = convert_from_path(pdf_path)

# Extract text using OCR from the first page
ocr_text = pytesseract.image_to_string(images[0], lang="eng")

# Save extracted text to a file
with open("extracted_text.txt", "w") as file:
    file.write(ocr_text)

print("Text extraction complete. Saved to extracted_text.txt.")
