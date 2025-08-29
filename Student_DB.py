
import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# _____________ Database funcions _____________
def database_creation():
    conn = sqlite3.connect("student.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS students(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, grade TEXT)")
    conn.commit()
    conn.close()

def insert_student(name,grade):
    conn = sqlite3.connect("student.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO students(name, grade) VALUES(?,?)",(name,grade))
    conn.commit()
    conn.close()

def delete_student(student_id):
    conn = sqlite3.connect("student.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM students WHERE id=?",(student_id,))
    conn.commit()
    conn.close()

def fetch_student_data():
    conn = sqlite3.connect("student.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")
    row = cur.fetchall()
    conn.close()
    return row

# _____________ Treeview Functions _____________ 
def load_Treeview():
    for row in tree.get_children():
        tree.delete(row)
        
    for row in fetch_student_data():
        tree.insert("",tk.END, values=row)

def add_student():
    name = name_entry.get()
    grade = grade_entry.get()
    if not name or not grade:
        messagebox.showwarning("Input Error", "Please fill all the fields!")
        return
    
    insert_student(name, grade)
    load_Treeview()
    name_entry.delete(0,tk.END)
    grade_entry.delete(0,tk.END)

def remove_student():
    selection = tree.selection()
    if not selection:
        messagebox.showwarning("Selection Error", "Please select the student you want to remove.")
        return
    
    student_id = tree.item(selection[0])["values"][0]
    delete_student(student_id)
    load_Treeview()

# _____________ GUI _____________
root = tk.Tk()
root.title("Student Management System")
root.geometry("600x450")

tk.Label(root,text="Name:").pack(pady=2)
name_entry = ttk.Entry(root)
name_entry.pack(pady=2)

tk.Label(root,text="Grade:").pack(pady=2)
grade_entry = ttk.Entry(root)
grade_entry.pack(pady=2)

columns = ("ID", "Name", "Grade")
tree = ttk.Treeview(root, columns=columns, show="headings")
for i in columns:
    tree.heading(i, text=i)
    tree.column(i, anchor="center")
tree.pack(fill="both", expand=True, pady=10)

ttk.Button(root, text="Add Student", command=add_student).pack()
ttk.Button(root, text="Remove Student", command=remove_student).pack(pady=2)


database_creation()
load_Treeview()

root.mainloop()