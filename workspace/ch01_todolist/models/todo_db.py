import pymysql

class TodoDB:
    def __init__(self):
        self.db = pymysql.connect(host='localhost', user='root', password='1234')
        self.cur = self.db.cursor()
        print("connect ok")

    def add(self, task):
        sql = "insert into todos(task) values('{0}')".format(task['name'])
