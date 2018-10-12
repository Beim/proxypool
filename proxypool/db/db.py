# -*- coding: utf-8 -*-
import pymysql

# db = pymysql.connect('119.29.160.85', 'root', '112223334', 'modemo')
# cursor = db.cursor()
#
# cursor.execute('insert into actor(name, doubanId) values ("what", 123)')
# db.commit()

# cursor.execute('select * from actor')
# data = cursor.fetchall()
# print(data)

class DbCursor(object):

    def __init__(self):
        self.db = pymysql.connect('119.29.160.85', 'root', '112223334', 'proxypool')

    def insert(self, sql_list):
        db = self.db
        cursor = db.cursor()
        try:
            for sql in sql_list:
                cursor.execute(sql)
            db.commit()
        except:
            db.rollback()
            return False
        return True

    def update(self, sql_list):
        return self.insert(sql_list)

    def delete(self, sql_list):
        return self.insert(sql_list)

    def query(self, sql):
        cursor = self.db.cursor()
        cursor.execute(sql)
        return cursor.fetchall()

dbCursor = DbCursor()