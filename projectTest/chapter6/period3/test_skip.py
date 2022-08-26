# -*-coding:utf-8-*-

import pytest


@pytest.mark.skip()
def test_skip1():
    assert 1 == 2

@pytest.mark.skip(reason="跳过该条测试用例")
def test_skip2():
    assert 1 == 2
