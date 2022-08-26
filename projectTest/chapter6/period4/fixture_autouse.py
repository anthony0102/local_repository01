# -*-coding:utf-8-*-

import pytest


@pytest.fixture(autouse=True)
def autouse_fixture():
    print('this is autouse of fixture')

def test_fixture1():
    print('this is test_fixture1')

def test_fixture2():
    print('this is test_fixture2')


if __name__ == '__main__':
    pytest.main(['-s', '--setup-show', 'fixture_autouse.py'])
