import pymysql

class StudentDB():
    def __init__(self):
        self.db = pymysql.connect(host='localhost', user='root', password='1234', db='choi_study')
        self.cur = self.db.cursor()
        print("connect db")
        sql = '''
        create table if not exists student(
            id int auto_increment primary key,
            number int, 
            name varchar(50), 
            gender varchar(50)
        );
        '''
        self.cur.execute(sql)
        self.db.commit()
        print('connect ok')

    def get_student(self):
        sql = "select * from student;"
        self.cur.execute(sql)
        result = self.cur.fetchall()
        return result

    def add_student(self, number, name, gender):
        sql = f"insert into student(number, name, gender) values({number}, '{name}', '{gender}');"
        self.cur.execute(sql)
        self.db.commit()

