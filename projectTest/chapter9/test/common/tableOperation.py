# -*-coding:utf-8-*-
from time import sleep

from projectTest.chapter9.test.common.elementIsExist import ElementIsExist


class TableOperation(object):
    """表格操作"""
    def __init__(self, driver):
        self.driver = driver

    def get_table(self):
        """
        获取table
        :return:返回table的headers body_rows body_rows_column
        """
        sleep(1)

        # 列表顺序：table header body_rows body_rows_columns
        tables_header_body = [['table #dataArea>table',
                               'table #dataArea>table>.header>td',
                               'table #dataArea>table>tr:not(.header)',
                               'table #dataArea>table>tr:not(.header)>td'
                               ],
                              ]

        # 获取画面显示的table
        for table_header_body in tables_header_body:
            #
            if ElementIsExist(self.driver).is_exist(table_header_body[0]):
                table = self.driver.find_element_by_css_selector(table_header_body[0])
                headers = table.find_elements_by_css_selector(table_header_body[1])
                body_rows = table.find_elements_by_css_selector(table_header_body[2])

                rows = []
                for body_row in body_rows:
                    body_row_column = body_row.find_elements_by_css_selector(table_header_body[3])
                    rows.append(body_row_column)

                return headers, rows
            else:
                print("table定位失败")
                return

    def select_row(self, header_text, row_text):
        """
        根据header中的列获取对应body中的行
        :param header_text:
        :param row_text:
        :return:
        """
        headers, rows = self.get_table()

        #
        idx = int()
        for header in headers:
            if header.text == header_text:
                idx = headers.index(header)

        #
        for row in rows:
            if row[idx].text == row_text:
                return row

    def row_click(self, header_text, row_text):
        """选择表格中的行并单击"""
        row = self.select_row(header_text, row_text)
        #
        #
        return row[0].click()


"""实现： 对选择行的单击操作"""
