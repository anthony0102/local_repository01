# -*-coding:utf-8-*-

import pytest


list_one = [1, 2, 3, 4]
# list_two = [5, 6, 7, 8]

@pytest.mark.parametrize('number', list_one)
def test_parametrize(number):
    assert number in list_one
    # assert number in list_two

