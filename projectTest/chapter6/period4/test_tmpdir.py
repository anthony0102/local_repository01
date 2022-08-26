# -*-coding:utf-8-*-

import pytest


def test_tmpdir(tmpdir):
    # 创建临时目录
    tmp_dir = tmpdir.mkdir('testdir')
    # 创建临时文件
    tmp_file = tmp_dir.join('tmpfile.txt')

    tmp_file.write('this is a temporary file')

    assert tmp_file.read() == 'this is a temporary file'

if __name__ == '__main__':
    pytest.main(['-v', 'test_tmpdir.py'])
