# -*-coding:utf-8-*-

import pytest


# 默认scpoe作用域是function级别
@pytest.fixture()
def signin_signout():
    print('\n Successful signin to the system')
    yield
    print('\n Exit the system successfully')
