from model.student import StudentDB

class StudentService():
    def __init__(self):
        self.student_db = StudentDB()

    def get_student(self):
        return [{'id': s[0], 'number': s[1], 'name': s[2], 'gender': s[3]} for s in self.student_db.get_student()]

    def add_student(self, number, name, gender):
        return self.student_db.add_student(number, name, gender)