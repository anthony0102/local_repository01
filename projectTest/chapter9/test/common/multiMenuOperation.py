# -*-coding:utf-8-*-
from time import sleep

from projectTest.chapter9.test.common.elementIsExist import ElementIsExist


class MultiMenuOperation(object):
    """多级菜单操作"""

    def __init__(self, driver):
        self.driver = driver

    def get_all_menu(self):
        """获取所有菜单"""
        # 此处体现出__init__的作用
        driver = self.driver
        sleep(1)

        # 获取tab父元素 通过id属性定位（#nav），通过标签名tag/tab(ul li a......)定位，多层级之间用“>”
        fathers_menus = [['#nav', '#nav>ul>li>a', '#nav>ul>li ul>li>a'],
                         ['#nav1', 'a', 'div'],
                         ]

        # 获取父元素下的所有菜单
        menu_level = []
        for father_menu in fathers_menus:
            father_exist = ElementIsExist(driver).is_exist(father_menu[0])
            if father_exist:

                # 将第一级菜单添加到list中的第一个元素？？？？
                if ElementIsExist(driver).is_exist(father_menu[1]):
                    menu_level_1 = driver.find_elements_by_css_selector(father_menu[1])  # 商城 水果 家电 链接 外卖配送
                    menu_level.append(menu_level_1)

                    # 将第二级菜单添加到list中的第二个元素？？？？
                    if ElementIsExist(driver).is_exist(father_menu[2]):
                        menu_level_2 = driver.find_elements_by_css_selector(father_menu[2])
                        menu_level.append(menu_level_2)
                    return menu_level
                return menu_level

    def select_menu(self, menu_text=[]):
        """
        选择菜单
        :param menu_text: 必须是list
        :return:
        """
        menu_levels = self.get_all_menu()
        print(menu_levels)
        i = 0
        for menus in menu_levels:
            for menu in menus:
                if menu.text == menu_text[i]:
                    sleep(1)
                    menu.click()
                    i += 1
                    break


if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("D:\JetBrains\PycharmProjects\projectAutoTest\projectHtml\chapter9\period4-3\index.html")
    sleep(1)
    menu = MultiMenuOperation(driver)
    menu.select_menu(["链接", "必应"])
    sleep(3)
    driver.quit()
