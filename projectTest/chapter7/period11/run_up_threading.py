# -*-coding:utf-8-*-
# args: arguments 争论;争吵;争辩;辩论;论据;理由;论点  指不固定的参数 *元组 **字典
import datetime
import threading
import time


class MyThreading(threading.Thread):

    def __init__(self, func, args, name=""):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = name

    def run(self):
        self.func(*self.args)

def do_thing(name):
    """线程运行的方法"""
    print('start doing thing:' + str(name), datetime.datetime.now())
    time.sleep(5)

    print('end doing thing:' + str(name), datetime.datetime.now())


names = ["第一条线程", "第二条线程", "第三条线程"]

for name in names:
    # 创建线程
    t = MyThreading(do_thing, (name,))
    # 启动线程
    t.start()
    time.sleep(1)

