import unittest

def div(x,y):
    return x-y

class TestDiv(unittest.TestCase):
    def test_div001(self):
        self.assertEqual(div(3,3),0)
    def test_div002(self):
        self.assertEqual(div(4,5),0)
    def test_div003(self):
        self.assertEqual(div(3,2),1)
