# -*-coding:utf-8-*-

"""
Created on 2021/11/22
Project: TYNAM后台管理系统 （学习用）
@Author: anan
"""

import os, time, unittest
import HTMLTestRunner


# 获取当前路径
# current_path = os.path.abspath(os.path.dirname(__file__))
# report_path = current_path + '/report/'
report_file = r'D:\JetBrains\PycharmProjects\projectAutoTest\projectTest\chapter8\period3l8\report\report.html'
# report_path = r'D:\JetBrains\PycharmProjects\projectAutoTest\projectTest\chapter8\period3l8\report'

# 获取当前时间
# now = time.strftime("%Y-%m-%d %H: %M", time.localtime(time.time()))

title = u"TYNAM后台管理系统"

# 报告存放路径
report_abspath = os.path.join(report_file)

def all_case():
    """导入所有用例"""
    # case_path= os.getcwd()
    case_path= r'D:\JetBrains\PycharmProjects\projectAutoTest\projectTest\chapter8\period3l8\case'
    print(case_path)
    discover = unittest.defaultTestLoader.discover(case_path, pattern="Test*.py")
    print(discover)
    return discover


if __name__ == "__main__":
    fp = open(report_file, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=title)
    runner.run(all_case())
    fp.close()
