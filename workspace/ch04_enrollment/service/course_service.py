from model.course import CourseDB

class CourseService:
    def __init__(self):
        self.course_db = CourseDB()

    def get_course(self):
        return [{'id':s[0], 'name':s[1], 'credit':s[2]} for s in self.course_db.get_course()]

    def add_course(self, name, credit):
        return self.course_db.add_course(name, credit)