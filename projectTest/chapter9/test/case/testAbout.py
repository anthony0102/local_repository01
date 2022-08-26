# -*-coding:utf-8-*_
import unittest

from projectTest.chapter9.test.pages.aboutPage import AboutPage


class TestAbout(unittest.TestCase):
    """测试 ‘关于我们’ 页面"""

    @classmethod
    def setUpClass(cls):
        cls.about = AboutPage()
        cls.about.login()

    @classmethod
    def tearDownClass(cls):
        cls.about.quit_driver()

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_about01(self):
        """测试 进入 ‘关于我们’ 页面"""
        self.about.select_menu("关于我们")
        about = self.about.about_element()
        self.assertEqual("关于我们", about.text)


if __name__ == '__main__':
    unittest.main()