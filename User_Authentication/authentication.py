from database_connection import DatabaseConnection

class Authentication:
    def __init__(self):
        self.db = DatabaseConnection()
        
    def verify_student(self, student_id: str, password: str) -> bool:
        self.db.cursor.execute(
            "SELECT password FROM students WHERE student_id = ?", 
            (student_id,)
        )
        result = self.db.cursor.fetchone()
        return bool(result and result[0] == password)
    
    def verify_teacher(self, teacher_id: str, password: str) -> bool:
        self.db.cursor.execute(
            "SELECT password FROM teachers WHERE teacher_id = ?", 
            (teacher_id,)
        )
        result = self.db.cursor.fetchone()
        return bool(result and result[0] == password)
    
    def verify_admin(self, admin_id: str, password: str) -> bool:
        return admin_id == "123" and password == "admin"