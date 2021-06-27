import unittest
import  pytest
from selenium import  webdriver
import time
# def  add (a,b):
#     return a+b
# def testAdd():
#     listn = [1,2,3,4]
#     assert  add(2,3) in listn
# testAdd()

class WebTest(unittest.TestCase):
        def setUp(self) :
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()
            time.sleep(10)
            self.driver.get("http://www.bing.com")

        def testBing001(self):
            self.assertEqual(self.driver.title,"微软 Bing 搜索 - 国内版")

        def testBing002(self):
            self.assertEqual(self.driver.current_url,'https://cn.bing.com/')

        def tearDown(self) :
            self.driver.quit()

pytest.main()


