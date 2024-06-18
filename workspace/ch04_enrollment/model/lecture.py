import pymysql

class LectureDB:
    def __init__(self):
        self.db = pymysql.connect(host='localhost', user='root', password='1234', db='choi_study')
        self.cur = self.db.cursor()
        sql = """
        create table if not exists lecture(
            id int auto_increment primary key,
            professor_id int, 
            course_id int,
            day varchar(50), 
            start_time time,
            foreign key(professor_id) references professor(id),
            foreign key(course_id) references course(id)
        );
        """
        self.cur.execute(sql)
        self.db.commit()
        print('connect ok')

    def get_lecture(self):
        sql = "select * from lecture"
        self.cur.execute(sql)
        result = self.cur.fetchall()
        return result


    def get_lectureList(self):
        sql = """
        select c.name, p.name, p.major, c.credit, l.day, l.start_time, s.name, adddate(l.start_time, interval c.credit hour)
        from professor p, course c, lecture l, enrollment e, student s
        where e.student_id = s.id and e.lecture_id = l.id and e.course_id = c.id and l.professor_id = p.id 
        """
        self.cur.execute(sql)
        result = self.cur.fetchall()
        return result

    def add_lecture(self, professor_id, course_id, day, start_time):
        sql = f"insert into lecture(professor_id, course_id, day, start_time) values({professor_id}, {course_id}, '{day}', '{start_time}')"
        self.cur.execute(sql)
        self.db.commit()