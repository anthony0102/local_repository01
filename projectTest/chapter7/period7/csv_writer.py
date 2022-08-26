# -*-coding:utf-8-*-


import csv


def csv_writer():
    """csv写入文本"""

    # 准备数据
    headers = ['code', 'name', 'ranking']
    rows = [
        (1, 'Python', 'first'),
        (2, 'Java', 'second'),
        (3, 'C', 'third')
    ]

    # 写入数据
    with open('data.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        # 写入表头数据
        writer.writerow(headers)

        # 写入内容数据
        # writer.writerows(rows)

        # 循环分条写入内容数据
        for row in rows:
            writer.writerow(row)

def csv_reader():
    """csv读取文本"""
    with open('data.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        print(list(reader))

if __name__ == '__main__':
    csv_writer()
    csv_reader()
