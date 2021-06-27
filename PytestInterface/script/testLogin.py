import json
from common.getKeyword_forResult import GetKeyword
from common.log import MyLog
from common.sendMethod import  SendMeth
from common.opreationExcel import  OperationExcel
import  unittest
import  ddt
exlData = OperationExcel('./data/TestName.xls','login')
testData = exlData.getDataByDict()

@ddt.ddt()
class TestLogin(unittest.TestCase):
    @ddt.data(*testData)
    def testLogin(self, data):
            url = data['requestUrl']
            """
            当data为dict类型时，会将dict解析为 key1=value1&key2=value2的形式。
            若data为字符串类型，requests会向请求体中直接传入该串，省去了解析的过程
            loads针对内存现象，load针对文件句柄
            """
            reParams = json.loads(data['requestParams'])#从excel中读取的值为字符串，不会解析，所以这里要转换成字典
            res = SendMeth.sendMethod(data['requestMethod'], url ,data = reParams)
            resMsg = GetKeyword.getKeyWord(res, 'message')
            resCode = GetKeyword.getKeyWord(res,'code')
            if resMsg:
                MyLog.info('登录接口请求成功！')
            else:
                MyLog.info('登录接口请求失败！')
            self.assertEqual(resMsg, data['expectedResult'])
            self.assertEqual(resCode, data['code'])

if __name__ == "__main__":
       unittest.main()

