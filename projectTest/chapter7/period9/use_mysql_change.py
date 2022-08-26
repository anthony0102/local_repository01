# -*-coding:utf-8-*-

from projectTest.chapter7.period9.common.Use_ConnectDB import ConnectDB


db = ConnectDB()

db.get_connect()

cursor = db.db.cursor()
# cursor = db.cursor()  # 出错？？？

# 1 添加数据---------------------------------------------------
# sql = "insert into student(id, name, sex) values(20007, '刘当当', '女');"

# cursor.execute(sql)
# db.cursor.execute(sql)  # 也可执行

# db.db.commit()
# -----------------------------------------------------

# 2 修改数据----------------------------------------------
# sql_u = "update student set name='钱小芊' where id='30001';"
# cursor.execute(sql_u)
# db.db.commit()
# -----------------------------------------------------

# 3 删除数据--------------------------------------------
sql_d = "delete from student where id=40002;"
cursor.execute(sql_d)
db.db.commit()
# -----------------------------------------------------

# ----------------------以上增删改操作后，执行打印表数据---------------------------------------
# SQL语句
# sql_p = "select * from student;"

# 执行SQL语句
# db.cursor.execute(sql_p)  # 需要和row_all = db.cursor.fetchall()一致，或同时去掉"db."
# cursor.execute(sql_p)  # 出错？---需要和row_all = cursor.fetchall()一致，或同时为"db.cursor......"
# db.db.cursor.execute(sql_p)  # 出错？？？

# row_all = db.cursor.fetchall()
#
# print(row_all)
# ---------------------------------------------------------------------------------

db.close_connect()
