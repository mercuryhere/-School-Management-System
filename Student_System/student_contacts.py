import tkinter as tk
from tkinter import ttk
from database_connection import DatabaseConnection

class StudentContacts:
    def __init__(self):
        self.db = DatabaseConnection()
    
    def create_contacts_tab(self, notebook):
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