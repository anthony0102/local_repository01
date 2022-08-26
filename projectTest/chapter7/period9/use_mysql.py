# -*-coding:utf-8-*-
# pip install mysql
# 命令行必须开启mysql服务 net start mysql
# SQL 发音：sequel  [ˈsiːkwəl]

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

# 创建游标对象
cursor = db.cursor()

# SQL语句
sql = "select * from student where sex='女'"
# sql = "select * from student where sex='女';"  # SQL语句加分号不影响

# 执行SQL语句
try:
    cursor.execute(sql)

    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        id = row[0]
        name = row[1]
        sex = row[2]
        age = row[3]
        grade = row[4]

        print(id, name, sex, age, grade, end='\n')

except:
    print("获取数据失败")

# 关闭游标
cursor.close()

# 断开连接
db.close()

