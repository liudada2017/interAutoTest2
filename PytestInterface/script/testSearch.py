from common.getKeyword_forResult import GetKeyword
from common.log import MyLog
from common.sendMethod import  SendMeth
from common.opreationExcel import  OperationExcel
import  unittest
import  ddt
exlData = OperationExcel('./data/TestName.xls','search')
testData = exlData.getDataByDict()

@ddt.ddt()
class TestSearch(unittest.TestCase):
    @ddt.data(*testData)
    def testSearch(self, data):

            url = data['requestUrl']
            params = data['requestParams']
            res = SendMeth.sendMethod(data['requestMethod'], url, params = params)
            resMsg = GetKeyword.getKeyWord(res, 'message')
            resCode = GetKeyword.getKeyWord(res, 'code')
            if resMsg:
                MyLog.info('搜索成功')
            else:
                MyLog.info('搜索失败')
            self.assertEqual(resMsg, data['expectedResult'])
            self.assertEqual(resCode, data['code'])
