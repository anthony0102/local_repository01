# -*-coding:utf-8-*-
import pymysql


# 连接database
db = pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    password="",
    database="TynamManagement",
    charset="utf8",
)

cursor = db.cursor(cursor=pymysql.cursors.DictCursor)

sql = "select * from student;"

cursor.execute(sql)
row_all = cursor.fetchall()
print(row_all)

# 关闭游标
cursor.close()

# 断开连接
db.close()
