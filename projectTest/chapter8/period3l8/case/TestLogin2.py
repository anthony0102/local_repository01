# -*-coding:utf-8-*-
"""
处理获取的数据：
1、剔除header行和无用的数据
2、返回邮箱地址，密码，预期结果定位，预期结果
"""
import time
import unittest

from ddt import ddt, data, unpack
from selenium import webdriver
from projectTest.chapter8.period3l8.common.ExcelUtil import ExcelUtil
# period3-8换成period3l8,否则识别不了


class Case(object):

    def __init__(self):
        pass

    def get_case(self):
        """
        获取数据
        得到有用的数据，并且使数据以邮箱地址、密码、预期结果定位、预期结果的顺序返回
        :return:
        """

        # 获取excel中的文件数据
        sheet = 'Login'
        file = ExcelUtil(sheet_name=sheet)
        data = file.get_data()

        # 得到所需数据的索引，然后，根据索引获取相应顺序的数据
        email_index = data[0].index("邮箱地址")
        password_index = data[0].index("密码")
        expected_element_index = data[0].index("预期结果定位")
        expected_index = data[0].index("预期结果")

        # print(email_index, password_index, expected_element_index, expected_index)  # 2 3 4 5

        data_length = data.__len__()
        all_case = []

        # 筛选，不要header行和其他不需要的数据
        for i in range(1, data_length):
            case = []
            case.append(data[i][email_index])
            case.append(data[i][password_index])
            case.append(data[i][expected_element_index])
            case.append(data[i][expected_index])
            all_case.append(case)
        return all_case


class Login():

    def __init__(self, driver):
        self.driver = driver

    def login(self, email, password):

        # 把邮件地址传入页面
        time.sleep(1)
        if email != None:
            email_element = self.driver.find_element_by_id('ty-email')
            email_element.send_keys(email)
        time.sleep(1)

        # 把密码传入页面
        if password != None:
            password_element = self.driver.find_element_by_id('ty-pwd')
            password_element.send_keys(password)
        time.sleep(1)

        # 点击登录
        login_btn = self.driver.find_element_by_css_selector("input[value='登  录']")
        login_btn.click()

    def login_assert(self, assert_type, assert_message):
        """
        登录断言
        assert_type: 断言类型【邮箱地址错误email error, 密码错误password error, 】
        assert_message
        """

        time.sleep(1)

        if assert_type == 'email error':
            email_message = self.driver.find_element_by_id('ty-email-error').text
            assert email_message == assert_message
        elif assert_type == 'password error':
            password_message = self.driver.find_element_by_id('ty-pwd-error').text
            assert password_message == assert_message
        elif assert_type in ['login success', 'login fail']:
            login_message = self.driver.switch_to.alert.text
            assert login_message == assert_message
        else:
            print("输入的断言类型assert_type不正确")


@ddt
class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        # url = "http://localhost:63342/projectAutoTest\projectHtml\chapter8\index.html"
        url = "D:\JetBrains\PycharmProjects\projectAutoTest\projectHtml\chapter8\index.html"
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.driver.get(url=url)

    def tearDown(self):
        self.driver.quit()

    case = Case().get_case()

    @data(*case)
    @unpack
    def test_login(self, email, password, assert_type, assert_message):
        login = Login(driver=self.driver)
        login.login(email=email, password=password)
        login.login_assert(assert_type=assert_type, assert_message=assert_message)


if __name__ == '__main__':
    # print(Case().get_case())
    unittest.main()
