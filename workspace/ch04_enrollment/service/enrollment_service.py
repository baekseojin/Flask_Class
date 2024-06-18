from model.enrollment import EnrollmentDB

class EnrollmentService:
    def __init__(self):
        self.enrollment_db = EnrollmentDB()

    def get_enrollment(self):
        return [{'id':s[0], 'student_number':s[1], 'student_name':s[2], 'course_name':s[3], 'credit':s[4]} for s in self.enrollment_db.get_enrollment()]

    def add_enrollment(self, student_id, course_id):
       self.enrollment_db.add_enrollment(student_id, course_id)
      
       
