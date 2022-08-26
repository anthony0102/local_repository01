# -*-coding:utf-8-*-

import unittest
from HTMLTestRunner import HTMLTestRunner


if __name__ == '__main__':
    testLoader = unittest.TestLoader()
    discover = testLoader.discover(start_dir='/', pattern="test*.py")

    # 上层目录寻找test, 不会包含寻找./中的test*.py
    # discover = testLoader.discover(start_dir='../', pattern="test*.py")

    print(discover)
    runner = unittest.TextTestRunner()

    # verbosity 控制输出测试结果的详细程度，默认verbosity=1
    # runner = unittest.TextTestRunner(verbosity=0)
    # runner = unittest.TextTestRunner(verbosity=1)
    # runner = unittest.TextTestRunner(verbosity=2)

    # 生成HTML格式的测试报告:from HTMLTestRunner import HTMLTestRunner
    with open('TestReport01.html', 'wb') as f:
        runner = HTMLTestRunner(stream=f,    # 测试报告写入存储区域， 流
                                title="自动化测试报告01",
                                description="自动化测试")
        runner.run(discover)
    # runner.run(discover)