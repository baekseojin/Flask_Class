from model.lecture import LectureDB

class LectureService:
    def __init__(self):
        self.lecture_db = LectureDB()

    def get_lecture(self):
        return [{'id':s[0], 'professor_id':s[1], 'course_id':s[2], 'day':s[3], 'start_time':s[4]} for s in self.lecture_db.get_lecture()]

    def get_lectuerList(self):
        results = [{'c_name':s[0], 'p_name':s[1], 'p_major':s[2], 'c_credit':s[3], 'l_day':s[4], 'l_time':s[5], 's_name':s[6], 'end_time':s[7]} for s in self.lecture_db.get_lectureList()]
        for result in results:
            result['l_time'] = str(result['l_time'])
            result['end_time'] = str(result['end_time'])
        return results

    def add_lecture(self, professor_id, course_id, day, start_time):
        self.lecture_db.add_lecture(professor_id, course_id, day, start_time)