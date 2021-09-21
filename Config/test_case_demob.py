import pytest
# import os
# path = os.path.abspath(__file__)
# dirpath = os.path.dirname(os.path.abspath(__file__))
# print(dirpath)
import time
from parameterized import parameterized

class TestDemo(object):

    def setup_class(self):
        print("\n开始测试")
        assert 1 == 1


    def teardown_class(self):
        print("测试结束")

    @parameterized.expand([(10,20),(2,3),(9,3)])
    def test_aaa(self,a,b):
        print('111111')
        c = a + b
        print("c等于",c)
        time.sleep(1)
        assert 1 == 1

    @pytest.mark.parametrize("a,b",[("我","你"),(10,2)])
    def test_bbb(self,a,b):
        d = a + b
        print('d',d)
        time.sleep(0.5)
        assert 1 == 1