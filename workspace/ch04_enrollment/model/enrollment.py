import pymysql

class EnrollmentDB:
    def __init__(self):
        self.db = pymysql.connect(host='localhost', user='root', password='1234', db='choi_study')
        self.cur = self.db.cursor()
        print("connect db")
        sql = '''
        create table if not exists enrollment(
            id int auto_increment primary key,
            student_id int, 
            course_id int,
            lecture_id int,
            foreign key(student_id) references student(id),
            foreign key(course_id) references course(id),
            foreign key(lecture_id) references lecture(id),
            unique index(student_id, course_id, lecture_id)
        );
        '''  

        self.cur.execute(sql)
        self.db.commit()
        print('connect ok')

    def get_enrollment(self):
        sql = """select e.id, s.number, s.name, c.name, c.credit from enrollment e
                    left join student s on s.id = e.student_id
                    left join course c on c.id = e.course_id
                    left join lecture l on l.id = e.lecture_id"""
        self.cur.execute(sql)
        result = self.cur.fetchall()
        return result


    def add_enrollment(self, student_id, course_id):
        sql = f"select id from lecture where course_id = {course_id}"
        self.cur.execute(sql)
        (lecture_id, ) = self.cur.fetchone()

        sql = f"insert into enrollment(student_id, course_id, lecture_id) values({student_id}, {course_id}, {lecture_id});"
        self.cur.execute(sql)
        self.db.commit()

    