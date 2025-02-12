import json
import mysql.connector

# Load JSON Data
with open("structured_data.json", "r") as json_file:
    patient_record = json.load(json_file)

# Database Connection
conn = mysql.connector.connect(
    host="localhost",
    user="your_user",
    password="your_password",
    database="hospital_db"
)
cursor = conn.cursor()

# Create Tables (if not exists)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS patients (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        dob DATE
    );
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS forms_data (
        id INT AUTO_INCREMENT PRIMARY KEY,
        patient_id INT,
        form_json JSON,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (patient_id) REFERENCES patients(id)
    );
''')

# Insert Data into Tables
name = patient_record.get("patient_name", "Unknown")
dob = patient_record.get("dob", "2000-01-01")  # Default DOB if not available

# Insert into patients table
cursor.execute("INSERT INTO patients (name, dob) VALUES (%s, %s)", (name, dob))
patient_id = cursor.lastrowid

# Insert JSON into forms_data table
cursor.execute("INSERT INTO forms_data (patient_id, form_json) VALUES (%s, %s)", (patient_id, json.dumps(patient_record)))

# Commit and Close Connection
conn.commit()
cursor.close()
conn.close()

print("Data successfully inserted into MySQL database!")
