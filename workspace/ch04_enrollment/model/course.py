import pymysql

class CourseDB():
    def __init__(self):
        self.db = pymysql.connect(host='localhost', user='root', password='1234', db='choi_study')
        self.cur = self.db.cursor()
        print("connect db")
        sql = '''
        create table if not exists course(
            id int auto_increment primary key, 
            name varchar(50),
            credit int
        );
        '''
        self.cur.execute(sql)
        self.db.commit()
        print('connect ok')

    def get_course(self):
        sql = "select * from course"
        self.cur.execute(sql)
        result = self.cur.fetchall()
        return result

    def add_course(self, name, credit):
        sql = f"insert into course(name, credit) values('{name}', {credit});"
        self.cur.execute(sql)
        self.db.commit()