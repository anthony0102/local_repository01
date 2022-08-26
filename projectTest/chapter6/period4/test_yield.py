# test_yield.py
# -*-coding:utf-8-*-

import pytest


@pytest.fixture()
def fixture_yield():
    print('\n Test started')
    yield
    print('\n End of test')

def test_yield(fixture_yield):
    print('\n 数据销毁操作测试')


if __name__ == '__main__':
    pytest.main(['-s', '--setup-show', 'test_yield.py'])
