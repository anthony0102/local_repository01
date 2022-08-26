# -*-coding:utf-8-*-

import pytest


@pytest.fixture(scope='session')
def session_fixture():
    pass

@pytest.fixture(scope='module')
def module_fixture():
    pass

@pytest.fixture(scope='class')
def class_fixture():
    pass

@pytest.fixture(scope='function')
def func_fixture():
    pass

def test_fixture(session_fixture, module_fixture, class_fixture, func_fixture):
    pass

# @pytest.mark.usefixtures('func_fixture')
# class TestFixture():
#     def test_fixture1(self):
#         pass
#
#     def test_fixture2(self):
#         pass

if __name__ == '__main__':
    pytest.main(['--setup-show', 'fixture_scope.py'])
