# -*-coding:utf-8-*-
from time import sleep

from projectTest.chapter9.test.common.elementIsExist import ElementIsExist


class TabOperation(object):
    """Tab操作"""

    def __init__(self, driver):
        self.driver = driver

    def get_all_tab(self):
        """获取所有tab"""

        sleep(1)

        # 获取所有的tab元素，元素定位默认取css定位
        fathers_tabs = [
            # ['.tabs1', 'a2'],  # 该列表不显示也可以正常执行 像是为了让列表不孤单，充当该列表里的一个子元素
                        ['.tabs', 'a'],  # 该列表不显示无法执行
                        ]

        # 获取页面显示父节点下的所有tab
        for fathers_tab in fathers_tabs:
            father_exist = ElementIsExist(self.driver).is_exist(fathers_tab[0])

            # 父节点存在，则进行以下操作
            if father_exist:
                # 通过css之class属性查找定位
                father = self.driver.find_element_by_css_selector(fathers_tab[0])
                # 通过css之标签名(tab)查找定位   tabs: 子元素们
                tabs = father.find_elements_by_css_selector(fathers_tab[1])  # element后加s!!!
                return tabs

    def switch_tab(self, tab_text):
        """
        切换tab
        :param tab_text: 需要切换到的tab的内容
        :return:
        """
        tabs = self.get_all_tab()
        for tab in tabs:
            if tab.text == tab_text:
                tab.click()
                return


if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.get("D:\JetBrains\PycharmProjects\projectAutoTest\projectHtml\chapter9\period4-2\\tabVerif.html")
    sleep(1)
    tab = TabOperation(driver)
    tab.switch_tab('Tab2')
    sleep(3)
    driver.quit()
