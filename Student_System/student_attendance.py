import tkinter as tk
from tkinter import ttk
from database_connection import DatabaseConnection

class StudentAttendance:
    def __init__(self, student_id: str):
        self.student_id = student_id
        self.db = DatabaseConnection()
    
    def create_attendance_tab(self, notebook):
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