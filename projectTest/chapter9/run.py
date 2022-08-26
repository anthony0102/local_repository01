# -*-coding:utf-8-*-


"""
Created on 2022-01-24
Project: TYNAM后台管理系统
@Author: AnAn
"""

import sys
from projectTest.chapter9.test.runner.Main import Main

sys.path.append('./../../')  # 不执行不影响结果。 意思？  ./ 代表当前文件所在目录下的某个文件夹或文件 ； ../ 代表当前文件所在目录的父目录下的某个文件夹或文件
if __name__ == '__main__':
    Main().run_case()
