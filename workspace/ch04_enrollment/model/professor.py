import pymysql

class ProfessorDB:
    def __init__(self):
        self.db = pymysql.connect(host='localhost', user='root', password='1234', db='choi_study')
        self.cur = self.db.cursor()
        print("connect db")
        sql = '''
        create table if not exists professor(
            id int auto_increment primary key,
            name varchar(50),
            major varchar(50),
            email varchar(50)
        );
        '''
        self.cur.execute(sql)
        self.db.commit()
        print('connect ok')

    def add_professor(self, name, major, email):
        sql = f"insert into professor(name, major, email) values('{name}', '{major}', '{email}')"
        self.cur.execute(sql)
        self.db.commit()

    def get_professor(self):
        sql = f"select * from professor"
        self.cur.execute(sql)
        result = self.cur.fetchall()
        print(result)
        return result