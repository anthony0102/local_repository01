# -*-coding:utf-8-*-
import unittest
from time import sleep

from projectTest.chapter9.test.pages.loginPage import LoginPage


class TestLogout(unittest.TestCase):
    """测试 ’退出登录‘ 功能"""

    @classmethod
    def setUpClass(cls):
        cls.login = LoginPage()
        cls.login.login()

    @classmethod
    def tearDownClass(cls):
        cls.login.quit_driver()

    def test_logout01(self):
        """测试 ‘退出登录’"""
        self.login.log_out()
        sleep(3)


if __name__ == '__main__':
    unittest.main()

