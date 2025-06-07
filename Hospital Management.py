from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector

# Setup Database
def setup_database():
    try:
        con = mysql.connector.connect(host="localhost", user="root", password="admin")
        cursor = con.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS hospitaldemo")
        con.close()

        con = mysql.connector.connect(host="localhost", user="root", password="admin", database="hospitaldemo")
        cursor = con.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS patients (
                name VARCHAR(100),
                dob VARCHAR(20),
                age VARCHAR(10),
                gender VARCHAR(10),
                phone VARCHAR(15),
                patient_id VARCHAR(20) PRIMARY KEY,
                admission_date VARCHAR(20),
                disease VARCHAR(100),
                referred_by VARCHAR(100)
            )
        """)
        con.commit()
        con.close()
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")

setup_database()

# GUI
win = Tk()
win.title("Hospital Management System")
win.geometry(f"{win.winfo_screenwidth()}x{win.winfo_screenheight()}")
win.config(bg='black')

# Variables
nameofthepatient = StringVar()
dateofbirth = StringVar()
age = StringVar()
gender = StringVar()
phnum = StringVar()
patientid = StringVar()
dateofadd = StringVar()
disease = StringVar()
reff = StringVar()

# Functions
def pd():
    if not nameofthepatient.get().strip() or not patientid.get().strip():
        messagebox.showerror("Error", "Name and Patient ID are required")
        return
    try:
        con = mysql.connector.connect(host="localhost", user="root", password="admin", database="hospitaldemo")
        my_cursor = con.cursor()
        my_cursor.execute("INSERT INTO patients VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
            nameofthepatient.get().strip(), dateofbirth.get().strip(), age.get().strip(),
            gender.get().strip(), phnum.get().strip(), patientid.get().strip(),
            dateofadd.get().strip(), disease.get().strip(), reff.get().strip()
        ))
        con.commit()
        con.close()
        fetch_data()
        messagebox.showinfo("Success", "Patient data saved successfully.")
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"Database error:\n{e}")

def fetch_data():
    con = mysql.connector.connect(host="localhost", user="root", password="admin", database="hospitaldemo")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM patients")
    rows = cursor.fetchall()
    table.delete(*table.get_children())
    for row in rows:
        table.insert('', END, values=row)
    con.close()

def get_data(event=''):
    selected = table.focus()
    values = table.item(selected, 'values')
    if values:
        nameofthepatient.set(values[0])
        dateofbirth.set(values[1])
        age.set(values[2])
        gender.set(values[3])
        phnum.set(values[4])
        patientid.set(values[5])
        dateofadd.set(values[6])
        disease.set(values[7])
        reff.set(values[8])

def pre():
    txt_frame.delete(1.0, END)
    txt_frame.insert(END, f"""
Name of the Patient : {nameofthepatient.get()}
Date of Birth       : {dateofbirth.get()}
Age                 : {age.get()}
Gender              : {gender.get()}
Phone Number        : {phnum.get()}
Patient ID          : {patientid.get()}
Date of Admission   : {dateofadd.get()}
Disease/Issue       : {disease.get()}
Referred By         : {reff.get()}
    """.strip())

def delete():
    if not patientid.get().strip():
        messagebox.showerror("Error", "Please select a record to delete")
        return
    try:
        con = mysql.connector.connect(host="localhost", user="root", password="admin", database="hospitaldemo")
        cursor = con.cursor()
        cursor.execute("DELETE FROM patients WHERE patient_id=%s", (patientid.get(),))
        con.commit()
        con.close()
        fetch_data()
        clear()
        messagebox.showinfo("Deleted", "Patient record deleted successfully")
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"Database error:\n{e}")

def clear():
    for var in (nameofthepatient, dateofbirth, age, gender, phnum, patientid, dateofadd, disease, reff):
        var.set("")
    txt_frame.delete(1.0, END)

def exit():
    if messagebox.askyesno("Exit", "Do you really want to exit?"):
        win.destroy()

def modify():
    if not patientid.get().strip():
        messagebox.showerror("Error", "Please select a record to update")
        return
    try:
        con = mysql.connector.connect(host="localhost", user="root", password="admin", database="hospitaldemo")
        cursor = con.cursor()
        cursor.execute("""
            UPDATE patients SET name=%s, dob=%s, age=%s, gender=%s, phone=%s, 
            admission_date=%s, disease=%s, referred_by=%s WHERE patient_id=%s
        """, (
            nameofthepatient.get().strip(), dateofbirth.get().strip(), age.get().strip(),
            gender.get().strip(), phnum.get().strip(), dateofadd.get().strip(),
            disease.get().strip(), reff.get().strip(), patientid.get().strip()
        ))
        con.commit()
        con.close()
        fetch_data()
        messagebox.showinfo("Updated", "Patient record updated successfully")
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"Database error:\n{e}")

# GUI Layout
Label(win, text="HOSPITAL MANAGEMENT SYSTEM", font='algerian 33', bg='blue', fg='white').pack(fill=X)

top_frame = Frame(win)
top_frame.pack(fill=BOTH, expand=True)

# Left Frame for Entry Fields
input_frame = LabelFrame(top_frame, text="Patient Information", font='arial 15 bold', bg='pink', bd=10)
input_frame.pack(side=LEFT, fill=BOTH, expand=True)

fields = [
    ("Name of the Patient", nameofthepatient),
    ("Date of Birth", dateofbirth),
    ("Age", age),
    ("Gender", gender),
    ("Phone Number", phnum),
    ("Patient ID", patientid),
    ("Date of Admission", dateofadd),
    ("Disease/Issue", disease),
    ("Referred By", reff)
]

for idx, (label_text, var) in enumerate(fields):
    Label(input_frame, text=label_text, bg='pink', font='arial 12').grid(row=idx, column=0, sticky=W, padx=10, pady=5)
    Entry(input_frame, textvariable=var, width=30).grid(row=idx, column=1, padx=10, pady=5)

# Right Frame for Patient Summary
prescription_frame = LabelFrame(top_frame, text="Patient Details", font='arial 15 bold', bg='pink', bd=10)
prescription_frame.pack(side=LEFT, fill=BOTH, expand=True)
txt_frame = Text(prescription_frame, font=('Courier', 12), bg='light yellow')
txt_frame.pack(fill=BOTH, expand=True)

# Table Frame
table_frame = Frame(win, bd=10, relief=RIDGE)
table_frame.pack(fill=BOTH, expand=True)

scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
scroll_y = Scrollbar(table_frame, orient=VERTICAL)
scroll_x.pack(side=BOTTOM, fill=X)
scroll_y.pack(side=RIGHT, fill=Y)

columns = ('name', 'dob', 'age', 'gender', 'phone', 'patient_id', 'admission_date', 'disease', 'referred_by')
table = ttk.Treeview(table_frame, columns=columns, xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
scroll_x.config(command=table.xview)
scroll_y.config(command=table.yview)

for col in columns:
    table.heading(col, text=col.replace('_', ' ').title())
    table.column(col, width=150)

table['show'] = 'headings'
table.pack(fill=BOTH, expand=True)
table.bind("<ButtonRelease-1>", get_data)

# Button Frame
button_frame = Frame(win, bg='gray')
button_frame.pack(fill=X)

buttons = [
    ("Save Patient Data", pd, 'green'),
    ("Patient Details", pre, 'purple'),
    ("Modify", modify, 'orange'),
    ("Delete", delete, 'brown'),
    ("Clear", clear, 'blue'),
    ("Exit", exit, 'red')
]

for text, cmd, color in buttons:
    Button(button_frame, text=text, font='arial 12 bold', bg=color, fg='white', command=cmd).pack(side=LEFT, fill=X, expand=True, padx=2, pady=5)

fetch_data()
win.mainloop()
