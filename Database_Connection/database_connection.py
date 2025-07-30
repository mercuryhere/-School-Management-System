import sqlite3
from typing import Optional

class DatabaseConnection:
    _instance: Optional['DatabaseConnection'] = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.conn = sqlite3.connect("python.db")
            cls._instance.cursor = cls._instance.conn.cursor()
            cls._instance._create_tables()
        return cls._instance
    
    def _create_tables(self):
        # Create students table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                student_id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                password TEXT NOT NULL
            )
        """)
        
        # Create teachers table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS teachers (
                teacher_id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                password TEXT NOT NULL,
                subject TEXT NOT NULL
            )
        """)
        
        # Create attendance table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS attendance (
                date TEXT NOT NULL,
                subject TEXT NOT NULL,
                student_id TEXT NOT NULL,
                status TEXT NOT NULL,
                PRIMARY KEY (date, subject, student_id)
            )
        """)
        
        # Insert default data if tables are empty
        self._insert_default_data()
        
    def _insert_default_data(self):
        self.cursor.execute("SELECT COUNT(*) FROM students")
        if self.cursor.fetchone()[0] == 0:
            self.cursor.execute("INSERT INTO students VALUES (?, ?, ?)", 
                              ("240265", "Aagaman Koirala", "aagaman"))
        
        self.cursor.execute("SELECT COUNT(*) FROM teachers")
        if self.cursor.fetchone()[0] == 0:
            self.cursor.executemany("INSERT INTO teachers VALUES (?, ?, ?, ?)", [
                ("240240", "Ram Nepali", "teacher123", "Math"),
                ("240241", "Chris Brown", "teacher123", "Python"),
                ("240242", "Shyam Pandit", "teacher123", "Software Design")
            ])
        
        self.conn.commit()
    
    def get_connection(self):
        return self.conn
    
    def get_cursor(self):
        return self.cursor