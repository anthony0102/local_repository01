# -*-coding:utf-8-*-

import pytest


def add_number(a, b):
    return a + b

@pytest.mark.done
def test_add1():
    assert add_number(2, 3) == 5

@pytest.mark.undo
def test_add2():
    assert add_number(2, 3) == 4

@pytest.mark.undo
def test_add3():
    assert add_number(2, 3) == 6
