from common.getKeyword_forResult import GetKeyword
from common.log import MyLog
from common.sendMethod import  SendMeth
from common.opreationExcel import  OperationExcel
import  unittest
import  ddt

exlData = OperationExcel('./data/TestName.xls', 'auth')
testData = exlData.getDataByDict()

@ddt.ddt()
class TestAuth(unittest.TestCase):
    @ddt.data(*testData)
    def testAuth(self, data):
        url = data['requestUrl']
        method = data['requestMethod']
        auth = data['requestParams']
        if  auth == "":
            pass
        else:
            auth = eval(auth) #将字符串转换成元组
        res = SendMeth.sendMethod(method, url, auth = auth)
        resCode = GetKeyword.getKeyWord(res, "code")
        resMsg = GetKeyword.getKeyWord(res, 'message')
        if resMsg == 'Authorization success!':
            MyLog.info('auth验证成功')
        else:
            MyLog.info(resMsg)
        self.assertEqual(resCode, data['code'])
        self.assertEqual(resMsg, data ['expectedResult'])

if __name__ == "__main__":
    unittest.main()