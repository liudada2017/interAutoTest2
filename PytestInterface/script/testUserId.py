from common.getKeyword_forResult import GetKeyword
from common.log import MyLog
from common.sendMethod import  SendMeth
from common.opreationExcel import  OperationExcel
import  unittest
import  ddt
exlData = OperationExcel('./data/TestName.xls','nameId')
testData = exlData.getDataByDict()
@ddt.ddt()
class TestUserId(unittest.TestCase):
    @ddt.data(*testData)
    def testUserId(self, data):

            url = data['requestUrl'] +str(data['requestParams'])
            res = SendMeth.sendMethod(data['requestMethod'], url)
            resMsg = GetKeyword.getKeyWords(res, "message")[0]
            resCode = GetKeyword.getKeyWords(res, "code")[0]
            if resMsg :
                MyLog.info(data['expectedResult'])
            else:
                MyLog.error('根据用户Id查询信息失败')
            self.assertEqual(resMsg, data['expectedResult'])
            self.assertEqual(resCode, data['code'])


