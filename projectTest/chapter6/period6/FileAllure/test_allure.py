# -*-coding:utf-8-*-
# pip install pytest-allure-adaptor
# pip uninstall pytest-allure-adaptor
# pip install allure-pytest


import pytest


def add_number(a, b):
    return a + b

def test_add1():
    assert add_number(2, 3) == 5

def test_add2():
    assert add_number(2, 3) == 4

def test_add3():
    assert add_number(3, 3) == 6
