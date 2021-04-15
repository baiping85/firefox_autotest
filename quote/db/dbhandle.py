# -*- coding: utf-8 -*-
# @Time : 2021-04-13 14:45
# @Author : bai ping
# @QQ : 376706275
import pymysql

class DbHandle:

    def __init__(self,host,port,username,password,database):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.database = database

    #获取数据库连接
    def get_connect(self):
        try:
            conn = pymysql.connect(host=self.host,port=self.port,user=self.username,
                            password=self.password,database=self.database)
            return conn
        except Exception as e:
            print(e,'connect failed')

    #查询数据
    def sql_search(self,sql,para):
        res = None
        try:
            conn = self.get_connect()
            cursor = conn.cursor()
            cursor.execute(sql,para)
            res = cursor.fetchall()
            conn.commit()
        except Exception as e:
            conn.rollback()
            print(e,'sql operation error~')
        finally:
            cursor.close()
            conn.close()

        return res

    #修改sql
    def sql_modify(self,sql,para):
        try:
            conn = self.get_connect()
            cursor = conn.cursor()
            cursor.execute(sql,para)
            conn.commit()
        except Exception as e:
            conn.rollback()
            print(e, 'sql operation error~')
        finally:
            cursor.close()
            conn.close()
