from common.getKeyword_forResult import GetKeyword
from common.log import MyLog
from common.sendMethod import  SendMeth
from common.opreationExcel import  OperationExcel
import  unittest
import  ddt

exlData = OperationExcel('./data/TestName.xls', 'dataJson')
testData = exlData. getDataByDict()

@ddt.ddt()
class TestJsonData(unittest.TestCase):
    @ddt.data(*testData)
    def testJsonData(self, data):
        url = data['requestUrl']
        method = data ['requestMethod']
        params = data['requestParams']
        res = SendMeth.sendMethod(method,url, data = params)
        resCode = GetKeyword.getKeyWord(res, 'code')
        resMsg  = GetKeyword.getKeyWord(res, 'message')
        if resMsg == "add success":
            MyLog.info(
                '添加成功'
            )
        else:
            MyLog.info('添加失败')
        self.assertEqual(resCode, data['code'])
        self.assertEqual(resMsg, data['expectedResult'])
