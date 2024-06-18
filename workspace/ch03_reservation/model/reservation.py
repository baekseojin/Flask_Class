import pymysql

class Reservation():
    def __init__(self):
        self.db = pymysql.connect(host='localhost', user='root', password='1234', db='choi_study')
        self.cur = self.db.cursor()
        print("connect db")
        sql = '''
        create table if not exists reservation(
            id int auto_increment primary key,
            name varchar(50) not null,
            email varchar(50) not null,
            phone varchar(50) not null,
            num_guest int not null,
            date_time datetime not null,
            restaurant_id int not null,
            foreign key (restaurant_id) references restaurant(id)
        );
        '''
        self.cur.execute(sql)
        self.db.commit()
        print('connect ok')

    def add_reservation(self, reservation):
        sql = "INSERT INTO reservation (name, email, phone, num_guest, date_time, restaurant_id) VALUES (%s, %s, %s, %s, %s, %s)"
        self.cur.execute(sql, (reservation.name, reservation.email, reservation.phone, reservation.num_guest, reservation.date_time, reservation.restaurant_id))
        self.db.commit()

    def get_reservation(self):
        sql = "select * from reservation"
        self.cur.execute(sql)
        result = self.cur.fetchall()
        print(result)
        return result
        

    def delete(self, index):
        sql = f"delete from reservation where id={index}"
        self.cur.execute(sql)
        self.db.commit()
