# -*-coding:utf-8-*-

import pytest


@pytest.mark.xfail(reason="运算错误")
def test_xfail1():
    assert 1 + 1 == 1

@pytest.mark.xfail
def test_xfail2():
    assert 1 + 1 == 2

