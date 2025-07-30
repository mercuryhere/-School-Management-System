import tkinter as tk
from tkinter import ttk

class StudentRoutine:
    def create_routine_tab(self, notebook):
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