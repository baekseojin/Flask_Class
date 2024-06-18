from model.professor import ProfessorDB

class ProfessorService:
    def __init__(self):
        self.professor_db = ProfessorDB()

    def add_professor(self, name, major, email):
        return self.professor_db.add_professor(name, major, email)

    def get_professor(self):
        return [{'id':s[0], 'name': s[1], 'major':s[2], 'email':s[3]} for s in self.professor_db.get_professor()]