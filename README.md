
# OCR to MySQL Data Pipeline

## Overview
This project extracts text from images using OCR (Tesseract), structures the extracted data into JSON format, and stores it into a MySQL database.

## Technologies Used
- Python
- OpenCV
- Tesseract OCR
- MySQL
- JSON

## Project Structure
```
📂 Your-GitHub-Repo
│── 📄 README.md             # Project documentation with setup instructions
│── 📄 extract_and_structure.py   # Python script for OCR and JSON structuring
│── 📄 store_to_mysql.py     # Python script for storing extracted data into MySQL
│── 📂 data
│   ├── sample_image.png     # Sample input image
│   ├── sample_output.json   # Sample extracted JSON output
│── 📂 sql
│   ├── schema.sql           # SQL schema for database tables
│   ├── insert_sample.sql    # Sample SQL insert statements
```

## Setup Instructions
### 1. Install Dependencies
Ensure you have Python installed. Install required libraries:
```sh
pip install pytesseract opencv-python mysql-connector-python
```
Install Tesseract OCR and add it to the system PATH:
- Windows: [Download Here](https://github.com/UB-Mannheim/tesseract/wiki)
- Linux:
  ```sh
  sudo apt install tesseract-ocr
  ```

### 2. Run OCR Script
To extract text and structure it as JSON:
```sh
python extract_and_structure.py
```

### 3. Setup MySQL Database
Create the database and tables using:
```sh
mysql -u root -p < sql/schema.sql
```

### 4. Insert Extracted Data
Run the MySQL storage script:
```sh
python store_to_mysql.py
```

## Sample JSON Output
```json
{
  "Patient Name": "John Doe",
  "DOB": "01/05/1980",
  "Pain Level": 6,
  "Comments": "Not good"
}
```

## Contributing
Feel free to fork and improve the project. Submit a pull request for any enhancements.

## License
This project is licensed under the MIT License.

