# -*-coding:utf-8-*-

import pytest


@pytest.fixture()
def fixture_prepare():
    print('\nthis is fixture prepare')

def test_fixture1(fixture_prepare):
    print('test_fixture1')

def test_fixture2(fixture_prepare):
    print('test_fixture2')

if __name__ == '__main__':
    # -s 显示测试函数中的print()输出
    pytest.main(['-s', 'test_fixture.py'])
