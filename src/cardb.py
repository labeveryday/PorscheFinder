import sqlite3 as sql
# from contextlib import closing
import os.path
from sqlite3.dbapi2 import Connection, Cursor, connect
from typing import List


class CarsDb:
    def __init__(self, db_name: str='car-db.db') -> None:
        self.db_name = db_name
        self.conn = None
        self._connect()

    def _connect(self) -> Connection:
        """Connection to database"""
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR + '/db', self.db_name)
        self.conn =  sql.connect(db_path)
        self.cursor = self.conn.cursor()
    
    def create_table(self) -> None:
        """Create CAR db TABLE"""
        try:
            self.cursor.execute("CREATE TABLE IF NOT EXISTS CAR (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL, price real NOT NULL, url TEXT NOT NULL, location TEXT, datelisted TEXT, unique(title));")
        except sql.OperationalError as e:
            print(e)
        
    def add_cars(self, car_dict: dict) -> None:
        """Add latest cars to dictionary"""
        car_sql = "INSERT INTO CAR (title, price, url, location,"\
                  "datelisted) values(?, ?, ?, ?, ?)"
        try:
            self.cursor.execute((car_sql), (car_dict['title'].strip(),
                                            car_dict['price'], car_dict['url'],
                                            car_dict['location'], car_dict['datelisted']))
        except sql.IntegrityError:
            # print(f"Duplicate: {car_dict['title']}, {car_dict['url']}")
            pass
    
    def get_cars(self, location='') -> list:
        """GET list of 10 cars from db"""
        if location:
            self.cursor.execute("SELECT * FROM CAR WHERE location=?", (location,))
        else:
            self.cursor.execute("SELECT * FROM (SELECT * FROM CAR ORDER BY id DESC)Var1 ORDER BY cast(ltrim(price, '$') as numeric) DESC;")
        results = self.cursor.fetchall()
        return results
    
    def commit(self):
        """Commit db changes"""
        self.conn.commit()
        
    def close(self) -> None:
        """Close db Connection"""
        self.cursor.close()
        self.conn.close()


if __name__ == "__main__":
    pass
