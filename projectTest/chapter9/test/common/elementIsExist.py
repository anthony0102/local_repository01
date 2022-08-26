# -*-coding:utf-8-*-
# 判断元素是否存在，存在返回True,不存在返回False
"""
self用于在成员方法的情况下表示类的调用实例。
这是必需的，以便类的成员方法作用于正确的对象。
这与Selenium没有任何关系，但它是语言的一个基本特性。
"""


class ElementIsExist(object):
    def __init__(self, driver):
        self.driver = driver

    def is_exist(self, element):
        flag = True
        try:
            self.driver.find_element_by_css_selector(element)
            return flag
        except:
            flag = False
            return flag

