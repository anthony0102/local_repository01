# -*-coding:utf-8-*-
# 多个线程同时工作，不会一个结束另一个才开始

import datetime
import threading
import time


def do_thing(name):
    """线程运行的方法"""
    print('start doing thing:' + str(name), datetime.datetime.now())
    time.sleep(5)

    print('end doing thing:' + str(name), datetime.datetime.now())


names = ["第一条线程", "第二条线程", "第三条线程"]

for name in names:
    # 创建线程
    t = threading.Thread(target=do_thing, args=(name,))
    # 启动线程
    t.start()
    time.sleep(1)
