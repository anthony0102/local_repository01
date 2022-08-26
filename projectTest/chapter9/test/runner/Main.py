# -*-coding:utf-8-*-
import os.path
import time
import unittest
from HTMLTestRunner import HTMLTestRunner


class Main:

    def get_all_case(self):
        """导入所有的用例"""
        current_path = os.path.abspath(os.path.dirname(__file__))
        case_path = current_path + '/../case/'
        discover = unittest.defaultTestLoader.discover(case_path, pattern="test*.py")
        print(discover)
        return discover

    def set_report(self, all_case, report_path=None):
        """设置生成报告"""
        if report_path is None:
            current_path = os.path.abspath(os.path.dirname(__file__))
            report_path = current_path + '/../../report/'
        else:
            report_path = report_path

        # 获取当前时间
        now = time.strftime('%Y{y}%m{m}%d{d}%H{h}%M{M}%S{s}').format(y="year", m="month", d="day", h="hour", M="minute", s="second")

        # 报告标题
        title = u"TYNAM后台管理系统"

        # 设置报告存放的路径和路径命名
        report_abspath = os.path.join(report_path, title + now + ".html")

        # 写入测试报告
        with open(report_abspath, "wb") as fp:
            runner = HTMLTestRunner(stream=fp, title=title)
            runner.run(all_case)
        return

    def run_case(self, report_path=None):
        all_case = self.get_all_case()
        self.set_report(all_case, report_path)


if __name__ == '__main__':
    Main().run_case()

