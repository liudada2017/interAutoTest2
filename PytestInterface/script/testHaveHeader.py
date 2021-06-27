import json

from common.getKeyword_forResult import GetKeyword
from common.log import MyLog
from common.sendMethod import  SendMeth
from common.opreationExcel import  OperationExcel
import  unittest
import  ddt

exlData = OperationExcel('./data/testName.xls', 'header')
testData = exlData.getDataByDict()

@ddt.ddt()
class TestHaveHeader(unittest.TestCase):
    @ddt.data(*testData)
    def testHaveHeader(self, data):
        url = data['requestUrl']
        method = data['requestMethod']
        if  data['requestParams'] == "":
             header = data['requestParams']
        else:
            header = json.loads(data['requestParams'])
        res = SendMeth.sendMethod(method , url ,headers=header)
        resCode = GetKeyword.getKeyWord(res, 'code')
        conType = GetKeyword.getKeyWord(res,'data')['Content-Type']
        if conType == 'application/json' :
            MyLog.info('有头部信息，请求成功！')
        elif conType is None:
            MyLog.info('请求缺少头部信息！')
        self.assertEqual(resCode, data['code'])
        self.assertEqual(str(conType), data['expectedResult'])

if __name__ == "__main__":
    unittest.main()



