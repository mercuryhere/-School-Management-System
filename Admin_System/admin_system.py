import tkinter as tk
from tkinter import ttk
from database_connection import DatabaseConnection
from admin_add import AdminAdd
from admin_remove import AdminRemove

class AdminSystem:
    def __init__(self):
        self.db = DatabaseConnection()
        self.admin_add = AdminAdd()
        self.admin_remove = AdminRemove()
    
    def create_dashboard(self, parent):
        dashboard = tk.Toplevel(parent)
        dashboard.title("Admin Dashboard")
        dashboard.geometry("1200x700")
        
        notebook = ttk.Notebook(dashboard)
        notebook.pack(fill="both", expand=True, padx=10, pady=10)
        
        self._create_students_tab(notebook)
        self._create_teachers_tab(notebook)
        
        return dashboard
    
    def _create_students_tab(self, notebook):
        students_frame = ttk.Frame(notebook)
        notebook.add(students_frame, text="Manage Students")
        
        list_frame = tk.Frame(students_frame)
        list_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        tk.Label(
            list_frame, 
            text="Current Students", 
            font=("Arial", 16, "bold")
        ).pack(pady=10)
        
        students_tree = ttk.Treeview(
            list_frame, 
            columns=("ID", "Name", "Password"), 
            show="headings"
        )
        students_tree.heading("ID", text="Student ID")
        students_tree.heading("Name", text="Name")
        students_tree.heading("Password", text="Password")
        
        self.db.cursor.execute("SELECT student_id, name, password FROM students")
        for row in self.db.cursor.fetchall():
            students_tree.insert("", "end", values=row)
        
        students_tree.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Add remove functionality
        self.admin_remove.create_student_remove(list_frame, students_tree)
        
        # Add new student form
        self.admin_add.create_student_form(students_frame, students_tree)
    
    def _create_teachers_tab(self, notebook):
        teachers_frame = ttk.Frame(notebook)
        notebook.add(teachers_frame, text="Manage Teachers")
        
        list_frame = tk.Frame(teachers_frame)
        list_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        tk.Label(
            list_frame, 
            text="Current Teachers", 
            font=("Arial", 16, "bold")
        ).pack(pady=10)
        
        teachers_tree = ttk.Treeview(
            list_frame, 
            columns=("ID", "Name", "Subject", "Password"), 
            show="headings"
        )
        teachers_tree.heading("ID", text="Teacher ID")
        teachers_tree.heading("Name", text="Name")
        teachers_tree.heading("Subject", text="Subject")
        teachers_tree.heading("Password", text="Password")
        
        self.db.cursor.execute("SELECT teacher_id, name, subject, password FROM teachers")
        for row in self.db.cursor.fetchall():
            teachers_tree.insert("", "end", values=row)
        
        teachers_tree.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Add remove functionality
        self.admin_remove.create_teacher_remove(list_frame, teachers_tree)
        
        # Add new teacher form
        self.admin_add.create_teacher_form(teachers_frame, teachers_tree)