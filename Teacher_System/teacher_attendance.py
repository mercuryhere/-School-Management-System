import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from database_connection import DatabaseConnection

class TeacherAttendance:
    def __init__(self, teacher_id: str):
        self.teacher_id = teacher_id
        self.db = DatabaseConnection()
    
    def create_attendance_tab(self, notebook, subject):
        attendance_frame = ttk.Frame(notebook)
        notebook.add(attendance_frame, text=f"Manage {subject} Attendance")
        
        tk.Label(
            attendance_frame, 
            text=f"Mark {subject} Attendance", 
            font=("Arial", 16, "bold")
        ).pack(pady=20)
        
        date_frame = tk.Frame(attendance_frame)
        date_frame.pack(fill="x", padx=20, pady=5)
        
        tk.Label(date_frame, text="Date:").pack(side="left", padx=5)
        date_entry = tk.Entry(date_frame)
        date_entry.insert(0, datetime.now().strftime("%Y-%m-%d"))
        date_entry.pack(side="left", padx=5)
        
        students_frame = tk.Frame(attendance_frame)
        students_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        tk.Label(
            students_frame, 
            text="Students", 
            font=("Arial", 14, "bold")
        ).pack(pady=10)
        
        self.db.cursor.execute("SELECT student_id, name FROM students")
        for student_id, student_name in self.db.cursor.fetchall():
            student_frame = tk.Frame(students_frame)
            student_frame.pack(fill="x", pady=5)
            
            tk.Label(
                student_frame, 
                text=f"{student_name} ({student_id})"
            ).pack(side="left", padx=5)
            
            status_var = tk.StringVar(value="Present")
            tk.Radiobutton(
                student_frame, 
                text="Present", 
                variable=status_var, 
                value="Present"
            ).pack(side="left", padx=5)
            tk.Radiobutton(
                student_frame, 
                text="Absent", 
                variable=status_var, 
                value="Absent"
            ).pack(side="left", padx=5)
            
            def mark_attendance(sid=student_id, status_v=status_var):
                date = date_entry.get()
                self.db.cursor.execute("""
                    INSERT OR REPLACE INTO attendance (date, subject, student_id, status)
                    VALUES (?, ?, ?, ?)
                """, (date, subject, sid, status_v.get()))
                self.db.conn.commit()
                messagebox.showinfo("Success", f"Attendance marked for {student_name}")
            
            tk.Button(
                student_frame, 
                text="Mark", 
                command=mark_attendance
            ).pack(side="right", padx=5)