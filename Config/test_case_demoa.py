import pytest
# import os
# path = os.path.abspath(__file__)
# dirpath = os.path.dirname(os.path.abspath(__file__))
# print(dirpath)


class TestCase(object):
    def setup_class(self):
        print(1)


    def teardown_class(self):
        print(2)

    def test_case(self):
        a = 1
        b = 2
        c = a + b
        print(c)
        assert 1 == 1
