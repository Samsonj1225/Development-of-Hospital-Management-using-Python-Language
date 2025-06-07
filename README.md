# Development-of-Hospital-Management-using-Python-Language

This project is a Hospital Management System GUI built using Python’s tkinter library and MySQL. It allows the user to add, view, modify, and delete patient records through a clean and adaptive user interface. Patient details such as Name, DOB, Age, Gender, Phone, Patient ID, Admission Date, Disease, and Referred By are stored persistently in a MySQL database.

The interface displays records in a scrollable table and provides detailed previews of each entry. The system ensures data retention across sessions and supports real-time operations on hospital records, ideal for administrative staff or hospital reception setups.

### 1. Set Up the MySQL Database

- Install MySQL Server on your system.
- Open MySQL Workbench or Terminal.
- Ensure these credentials are correct in the script:
  - **Host**: `localhost`
  - **User**: `root`
  - **Password**: `admin`
- The script will automatically:
  - Create a database named `hospitaldemo` (if it doesn't exist).
  - Create a table `patients` with fields like:
    - `name`
    - `dob`
    - `age`
    - `gender`
    - `phone`
    - `patient_id`
    - `admission_date`
    - `disease`
    - `referred_by`


2. Prepare the Python Environment
--> Make sure Python is installed.
--> Install the MySQL connector package:
      pip install mysql-connector-python
--> Save the provided code in a file named, for example, Hospital Management.py.

3. Run the Application
--> Open a terminal or IDE.
--> Run the script:
       Hospital Management.py
--> The application will open in full screen with a user-friendly GUI.

5. Using the GUI
--> Enter patient details in the left-side form fields.
--> Click “Save Patient Data” to store the record in the database.
--> Click “Patient Details” to view a formatted preview of the data.
--> Click “Modify” to update selected patient details using the Patient ID.
--> Click “Delete” to remove a record (requires Patient ID).
--> Click “Clear” to reset all input fields and preview.
--> Click “Exit” to close the application.

5. Viewing Patient Records
--> The lower section displays a scrollable table of all records.
--> Clicking a row will autofill the form for quick editing or deleting.

6. Persistent Data Storage
--> All data is stored in the MySQL database.
--> Records remain available even after restarting the program.
