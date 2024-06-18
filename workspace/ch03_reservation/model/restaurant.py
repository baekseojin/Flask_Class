import pymysql

class Restaurant:
    def __init__(self):
        self.db = pymysql.connect(host='localhost', user='root', password='1234', db='choi_study')
        self.cur = self.db.cursor()
        print("connect db")
        sql = '''
        create table if not exists restaurant(
            id int(5) auto_increment primary key,
            name varchar(50),
            address varchar(50),
            phone varchar(50)
        );'''

        self.cur.execute(sql)
        self.db.commit()

        sql = """
        insert into restaurant(name, address, phone) 
        select '컴포즈', '강서구', '051-111-1111'
        from dual
        where not exists
        (select name, address, phone from restaurant where name='컴포즈' and address='강서구' and phone='051-111-1111')
        """
        self.cur.execute(sql)
        self.db.commit()

        sql = """
        insert into restaurant(name, address, phone) 
        select '이마트24', '강서구', '051-222-2222'
        from dual
        where not exists
        (select name, address, phone from restaurant where name='이마트24' and address='강서구' and phone='051-222-2222')
        """
        self.cur.execute(sql)
        self.db.commit()


    def get_restaurant(self):
        sql = "select * from restaurant"
        self.cur.execute(sql)
        result = self.cur.fetchall()
        print(result)
        return result
  

    
    
