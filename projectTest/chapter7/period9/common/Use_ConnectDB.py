# -*-coding:utf-8-*-
# 封装连接数据库的方法

import pymysql

class ConnectDB(object):


    def __init__(self):
        pass

    # 初始化连接数据库
    def get_connect(self):

        # 连接database
        self.db = pymysql.connect(
            host="localhost",
            port=3306,
            user="root",
            password="",
            database="TynamManagement",
            charset="utf8",
        )

        # 创建游标对象
        self.cursor = self.db.cursor()

    def close_connect(self):

        # 关闭游标
        self.cursor.close()
        # 断开连接
        self.db.close()

