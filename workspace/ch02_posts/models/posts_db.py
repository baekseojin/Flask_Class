import pymysql

class PostsDB:
    def __init__(self):
        self.db = pymysql.connect(host='localhost', user='root', password='1234', db='choi_study')
        self.cur = self.db.cursor()
        print("connect db")

    def get_posts(self):
        sql = "select * from posts"
        self.cur.execute(sql)
        result = self.cur.fetchall()
        print(result)
        return result
    
    def get_one(self, id):
        sql = "select * from posts where id='{0}'".format(id)
        self.cur.execute(sql)
        result = self.cur.fetchone()
        print(result)
        return result

    def new_post(self, post):
        sql = "insert into posts(title, content, author) values(%s, %s, %s)"
        self.cur.execute(sql, post)
        self.db.commit()

    def update_post(self, post):
        sql = "update posts set title=%s, content=%s, author=%s where id=%s"
        self.cur.execute(sql, post)
        self.db.commit()

    def delete_post(self, id):
        sql = f"delete from posts where id={id}"
        self.cur.execute(sql)
        self.db.commit()

    
    
        