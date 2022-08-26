# -*-coding:utf-8-*-

import unittest

class TestSuit(unittest.TestCase):

    @unittest.skip("无条件跳过test1测试用例")
    def test_1(self):
        print('test1')

    @unittest.skipIf(1 == 1, "如果1等于1跳过test2")
    def test_2(self):
        print('test2')

    @unittest.skipUnless(1 == 1, "如果1等于1不跳过test3,执行test3")
    def test_3(self):
        print('test3')

    @unittest.expectedFailure
    def test_4(self):
        self.assertEqual(2, 1)
        print('test4')

# if __name__ == '__main__':
    # 构造测试集
    # suit = unittest.TestSuite(map(TestSuit, ['test_3', 'test_1']))
    # suit = unittest.TestSuite()
    # suit.addTest(TestSuit("test_3"))
    # suit.addTest(TestSuit("test_2"))
    # suit.addTests(map(TestSuit, ['test_3', 'test_1']))
    # 执行测试用例
    # unittest.TextTestRunner().run(suit)
if __name__ == '__main__':
    unittest.main()
