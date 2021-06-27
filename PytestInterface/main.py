#coding = utf-8
import unittest
from BeautifulReport import BeautifulReport
from common.sendEmail import SendEmail
#测试用列路径
casePath = './script/'

#获取所有测试用例
def getAllCase():
    discover = unittest.defaultTestLoader.discover(casePath, pattern= "test*.py")
    suite = unittest.TestSuite()
    suite.addTest(discover)
    return suite

if __name__ == "__main__":
     # runner = unittest.TextTestRunner(verbosity=2)
     # runner.run(getAllCase())
    runner = BeautifulReport(getAllCase())  # => tests是通过discover查找并构建的测试套件
    runner.report(
        description='测试报告',  # => 报告描述
        filename='report.html',  # => 生成的报告文件名
        log_path='./reports/'  # => 报告路径
   )
#将测试报告发送到邮箱
#SendEmail().sendOneEmail('接口测试','天气api、helloAccumulator、登录、搜索、根据id查询用户信息','./reports/report.html')

