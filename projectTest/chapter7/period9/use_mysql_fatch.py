# -*-coding:utf-8-*-
# fetchone() fetchmany(n) fetchall()
# fetch不能重复查询数据，查询过的数据不会再被下一个fetch查询

from projectTest.chapter7.period9.common.Use_ConnectDB import ConnectDB


# 连接database
db = ConnectDB()
db.get_connect()

# SQL语句
sql = "select * from student;"

# 执行SQL语句
db.cursor.execute(sql)

# row_first = db.cursor.fetchone()
# print(row_first)
#
row_n = db.cursor.fetchmany(3)
print(row_n)

# row_all = db.cursor.fetchall()
# print(row_all)  # 只有把上面两对语句注释掉，才能完整显示row_all
# for row in row_all:
#     print(row)

# 关闭游标，断开链接
db.close_connect()

