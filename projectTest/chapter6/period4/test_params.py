# -*-coding:utf-8-*-

import pytest


@pytest.fixture(params=[(1, 3, 4),
                        (2, 4, 6),
                        (12, 23, 34)])
def test_params(request):
    return request.param

def test_add(test_params):
    assert test_params[2] == test_params[0] +test_params[1]

if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_params.py'])
