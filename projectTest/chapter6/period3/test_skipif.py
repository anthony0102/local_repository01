# -*-coding:utf-8-*-

import pytest


@pytest.mark.skipif('sys.platform == "win32"',
                    reason="不适合在win32中运行")
def test_skipif1():
    assert 1 == 2

@pytest.mark.skipif('sys.platform != "win32"')
def test_skipif2():
    assert 1 == 1
