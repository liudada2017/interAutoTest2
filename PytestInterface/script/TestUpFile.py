from common.getKeyword_forResult import GetKeyword
from common.log import MyLog
from common.sendMethod import  SendMeth
from common.opreationExcel import  OperationExcel
import  unittest
import  ddt

exlData = OperationExcel('./data/TestName.xls', 'upFile')
testData = exlData.getDataByDict()
@ddt.ddt()
class TestUpFile(unittest.TestCase):

    @ddt.data(*testData)
    def testUpFile(self, data):
        url = data['requestUrl']
        method = data['requestMethod']
        filePath = data['requestParams']
        file = {'file': open(filePath, 'rb')}
        res = SendMeth.sendMethod(method, url, files = file)
        resCode = GetKeyword.getKeyWord(res, 'code')
        resMsg = GetKeyword.getKeyWord(res, 'message')
        if resMsg == 'upload success!':
            MyLog.info('文件上传成功')
        else:
            MyLog.info('文件上传失败')
        self.assertEqual(resCode, data['code'])
        self.assertEqual(resMsg, data['expectedResult'])


if __name__ =="__main__":
    unittest.main()
