import tkinter as tk
from tkinter import ttk, messagebox
from database_connection import DatabaseConnection

class AdminRemove:
    def __init__(self):
        self.db = DatabaseConnection()
    
    def create_student_remove(self, parent, tree):
        remove_frame = tk.Frame(parent)
        remove_frame.pack(fill="x", padx=10, pady=5)
        
        def remove_student():
            selected_items = tree.selection()
            if not selected_items:
                messagebox.showerror("Error", "Please select a student to remove")
                return
            
            student_values = tree.item(selected_items[0])['values']
            student_id = student_values[0]
            student_name = student_values[1]
            
            if messagebox.askyesno("Confirm", f"Are you sure you want to remove student {student_name}?"):
                try:
                    # Remove from attendance table first (foreign key constraint)
                    self.db.cursor.execute("DELETE FROM attendance WHERE student_id = ?", (student_id,))
                    # Remove from students table
                    self.db.cursor.execute("DELETE FROM students WHERE student_id = ?", (student_id,))
                    self.db.conn.commit()
                    
                    # Remove from treeview
                    tree.delete(selected_items[0])
                    messagebox.showinfo("Success", f"Student {student_name} removed successfully!")
                except Exception as e:
                    self.db.conn.rollback()
                    messagebox.showerror("Error", f"Failed to remove student: {str(e)}")
        
        remove_btn = tk.Button(
            remove_frame,
            text="Remove Selected Student",
            command=remove_student,
            bg="red",
            fg="white",
            font=("Arial", 12)
        )
        remove_btn.pack(pady=5)
    
    def create_teacher_remove(self, parent, tree):
        remove_frame = tk.Frame(parent)
        remove_frame.pack(fill="x", padx=10, pady=5)
        
        def remove_teacher():
            selected_items = tree.selection()
            if not selected_items:
                messagebox.showerror("Error", "Please select a teacher to remove")
                return
            
            teacher_values = tree.item(selected_items[0])['values']
            teacher_id = teacher_values[0]
            teacher_name = teacher_values[1]
            
            if messagebox.askyesno("Confirm", f"Are you sure you want to remove teacher {teacher_name}?"):
                try:
                    # Remove the teacher
                    self.db.cursor.execute("DELETE FROM teachers WHERE teacher_id = ?", (teacher_id,))
                    self.db.conn.commit()
                    
                    # Remove from treeview
                    tree.delete(selected_items[0])
                    messagebox.showinfo("Success", f"Teacher {teacher_name} removed successfully!")
                except Exception as e:
                    self.db.conn.rollback()
                    messagebox.showerror("Error", f"Failed to remove teacher: {str(e)}")
        
        remove_btn = tk.Button(
            remove_frame,
            text="Remove Selected Teacher",
            command=remove_teacher,
            bg="red",
            fg="white",
            font=("Arial", 12)
        )
        remove_btn.pack(pady=5)