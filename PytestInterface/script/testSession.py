import json

from common.getKeyword_forResult import GetKeyword
from common.log import MyLog
from common.opreationExcel import  OperationExcel
import  unittest
import  ddt
import  requests
exlData = OperationExcel('./data/TestName.xls','session')
testData = exlData.getDataByDict()

@ddt.ddt()
class TestSession(unittest.TestCase):
    @ddt.data(*testData)
    def testSession(self, data):
        url = data['requestUrl']
        urlTwo = data['requestUrlTwo']
        params = json.loads(data['requestParams'])
       #session必须在这里新建，才能保证两次请求都调用的同一个session
        # 如果是调用函数中的session，则每次调用的session都不一样
        s = requests.session()
        r = s.post(url, data=params)
        res = r.json()
        r2 = s.get(urlTwo)
        resTwo = r2.json()
        resCode = GetKeyword.getKeyWord(res, 'code')
        resTwoCode = GetKeyword.getKeyWord(resTwo, 'code')
        resMsg = GetKeyword.getKeyWord(res, 'message')
        resTwoMsg = GetKeyword.getKeyWord(resTwo, 'message')
        if resMsg == "login success":
            MyLog.info('登录成功')
        else:
            MyLog.error('登录失败')
        self.assertEqual(resCode, data['code'])
        self.assertEqual(resTwoCode, data['codeTwo'])
        self.assertEqual(resMsg, data['expectedResult'])
        self.assertEqual(resTwoMsg, data['expectedResultTwo'])


if __name__ == "__main__":
    unittest.main()