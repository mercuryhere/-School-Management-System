import tkinter as tk
from tkinter import ttk, messagebox
from database_connection import DatabaseConnection

class AdminAdd:
    def __init__(self):
        self.db = DatabaseConnection()
    
    def create_student_form(self, parent, tree):
        form_frame = tk.Frame(parent)
        form_frame.pack(fill="x", padx=10, pady=10)
        
        tk.Label(
            form_frame, 
            text="Add New Student", 
            font=("Arial", 14, "bold")
        ).pack(pady=10)
        
        entries = {}
        for field in ["Student ID", "Name", "Password"]:
            tk.Label(form_frame, text=f"{field}:").pack()
            entry = tk.Entry(form_frame)
            entry.pack()
            entries[field] = entry
        
        def add_student():
            values = [entry.get() for entry in entries.values()]
            if not all(values):
                messagebox.showerror("Error", "Please fill all fields")
                return
            
            student_id = values[0]
            self.db.cursor.execute(
                "SELECT student_id FROM students WHERE student_id = ?", 
                (student_id,)
            )
            if self.db.cursor.fetchone():
                messagebox.showerror("Error", "Student ID already exists")
                return
            
            self.db.cursor.execute(
                "INSERT INTO students VALUES (?, ?, ?)", 
                tuple(values)
            )
            self.db.conn.commit()
            tree.insert("", "end", values=tuple(values))
            
            for entry in entries.values():
                entry.delete(0, tk.END)
            
            messagebox.showinfo("Success", "Student added successfully!")
        
        tk.Button(
            form_frame, 
            text="Add Student", 
            command=add_student
        ).pack(pady=10)
    
    def create_teacher_form(self, parent, tree):
        form_frame = tk.Frame(parent)
        form_frame.pack(fill="x", padx=10, pady=10)
        
        tk.Label(
            form_frame, 
            text="Add New Teacher", 
            font=("Arial", 14, "bold")
        ).pack(pady=10)
        
        entries = {}
        for field in ["Teacher ID", "Name", "Subject", "Password"]:
            tk.Label(form_frame, text=f"{field}:").pack()
            entry = tk.Entry(form_frame)
            entry.pack()
            entries[field] = entry
        
        def add_teacher():
            values = [entry.get() for entry in entries.values()]
            if not all(values):
                messagebox.showerror("Error", "Please fill all fields")
                return
            
            teacher_id = values[0]
            self.db.cursor.execute(
                "SELECT teacher_id FROM teachers WHERE teacher_id = ?", 
                (teacher_id,)
            )
            if self.db.cursor.fetchone():
                messagebox.showerror("Error", "Teacher ID already exists")
                return
            
            self.db.cursor.execute(
                "INSERT INTO teachers VALUES (?, ?, ?, ?)", 
                tuple(values)
            )
            self.db.conn.commit()
            tree.insert("", "end", values=tuple(values))
            
            for entry in entries.values():
                entry.delete(0, tk.END)
            
            messagebox.showinfo("Success", "Teacher added successfully!")
        
        tk.Button(
            form_frame, 
            text="Add Teacher", 
            command=add_teacher
        ).pack(pady=10)