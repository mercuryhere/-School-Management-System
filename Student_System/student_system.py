import tkinter as tk
from tkinter import ttk
from database_connection import DatabaseConnection

class StudentSystem:
    def __init__(self, student_id: str):
        self.student_id = student_id
        self.db = DatabaseConnection()
        
    def create_dashboard(self, parent):
        dashboard = tk.Toplevel(parent)
        self.db.cursor.execute(
            "SELECT name FROM students WHERE student_id = ?", 
            (self.student_id,)
        )
        student_name = self.db.cursor.fetchone()[0]
        dashboard.title(f"Student Dashboard - {student_name}")
        dashboard.geometry("1200x700")
        
        notebook = ttk.Notebook(dashboard)
        notebook.pack(fill="both", expand=True, padx=10, pady=10)
        
        self._create_routine_tab(notebook)
        self._create_attendance_tab(notebook)
        self._create_contacts_tab(notebook)
        
        return dashboard
    
    def _create_routine_tab(self, notebook):
        routine_frame = ttk.Frame(notebook)
        notebook.add(routine_frame, text="Class Routine")
        
        routine_tree = ttk.Treeview(
            routine_frame, 
            columns=("Time", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"), 
            show="headings"
        )
        
        for col in routine_tree["columns"]:
            routine_tree.heading(col, text=col)
            routine_tree.column(col, width=150)

        routine_data = [
            ("10:30 AM", "Python", "Python", "Python", "Python", "Python"),
            ("12:30 PM", "Math", "Math", "Math", "Math", "Math"),
            ("2:30 PM", "Software Design", "Software Design", "Software Design", "Software Design", "Software Design")
        ]
        for item in routine_data:
            routine_tree.insert("", "end", values=item)
        
        routine_tree.pack(fill="both", expand=True, padx=10, pady=10)
    
    def _create_attendance_tab(self, notebook):
        attendance_frame = ttk.Frame(notebook)
        notebook.add(attendance_frame, text="Attendance")
        
        attendance_label = tk.Label(
            attendance_frame, 
            text="Attendance Record", 
            font=("Arial", 16, "bold")
        )
        attendance_label.pack(pady=20)
        
        attendance_tree = ttk.Treeview(
            attendance_frame, 
            columns=("Date", "Subject", "Status"), 
            show="headings"
        )
        attendance_tree.heading("Date", text="Date")
        attendance_tree.heading("Subject", text="Subject")
        attendance_tree.heading("Status", text="Status")
        
        self.db.cursor.execute("""
            SELECT date, subject, status 
            FROM attendance 
            WHERE student_id = ?
        """, (self.student_id,))
        
        for row in self.db.cursor.fetchall():
            attendance_tree.insert("", "end", values=row)
        
        attendance_tree.pack(fill="both", expand=True, padx=10, pady=10)
    
    def _create_contacts_tab(self, notebook):
        contacts_frame = ttk.Frame(notebook)
        notebook.add(contacts_frame, text="Teacher Contacts")
        
        contacts_label = tk.Label(
            contacts_frame, 
            text="Teacher Contact Information", 
            font=("Arial", 16, "bold")
        )
        contacts_label.pack(pady=20)
        
        self.db.cursor.execute("SELECT name, subject FROM teachers")
        for teacher in self.db.cursor.fetchall():
            contact_frame = tk.Frame(contacts_frame, relief="solid", bd=1)
            contact_frame.pack(fill="x", padx=20, pady=5)
            
            teacher_info = f"{teacher[0]} - {teacher[1]}"
            tk.Label(
                contact_frame, 
                text=teacher_info, 
                font=("Arial", 12, "bold")
            ).pack(side="left", padx=10, pady=5)