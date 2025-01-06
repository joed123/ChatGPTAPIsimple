import unittest
from check_pwd import check_pwd

class TestPWD(unittest.TestCase):

    def test1(self):
        string = "hi"                                   
        self.assertFalse(check_pwd(string))

    def test2(self):
        string = "gjkglskgjhsj"                                   
        self.assertTrue(check_pwd(string))

if __name__ == '__main__':
    unittest.main()