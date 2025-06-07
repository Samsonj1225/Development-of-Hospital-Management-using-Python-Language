# Development-of-Hospital-Management-using-Python-Language

This project is a Hospital Management System GUI built using Python’s tkinter library and MySQL. It allows the user to add, view, modify, and delete patient records through a clean and adaptive user interface. Patient details such as Name, DOB, Age, Gender, Phone, Patient ID, Admission Date, Disease, and Referred By are stored persistently in a MySQL database.

The interface displays records in a scrollable table and provides detailed previews of each entry. The system ensures data retention across sessions and supports real-time operations on hospital records, ideal for administrative staff or hospital reception setups.

1. Set Up the MySQL Database
Install MySQL Server on your system.

Open MySQL Workbench or Terminal.

Ensure these credentials are correct in the script:

Host: localhost

User: root

Password: admin

The script will automatically:

Create a database named hospitaldemo (if it doesn't exist).

Create a table patients with fields like name, DOB, age, gender, phone, patient ID, admission date, disease, and referred by.
