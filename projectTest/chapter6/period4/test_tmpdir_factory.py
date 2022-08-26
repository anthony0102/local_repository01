# -*-coding:utf-8-*-
# directory 目录
# temporary 临时
# factory 工厂

import pytest


@pytest.fixture(scope='module')
def test_tmpdir_factory(tmpdir_factory):
    # 创建临时目录
    tmp_dir = tmpdir_factory.mktemp('testdir')

    tmp_file = tmp_dir.join('tmpfile.txt')

    tmp_file.write('this is a temporary file')

    return tmp_file

def test_tempdir1(test_tmpdir_factory):
    with test_tmpdir_factory.open() as f:
        assert f.read() == 'this is a temporary file'

def test_tempdir2(test_tmpdir_factory):
    assert 'a temporary file' in test_tmpdir_factory.read()

if __name__ == '__main__':
    pytest.main(['-v', 'test_tmpdir_factory.py'])
