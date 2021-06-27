# -*- coding: utf-8 -*-
import json

from common.getKeyword_forResult import GetKeyword
from common.log import MyLog
from common.sendMethod import  SendMeth
from common.opreationExcel import  OperationExcel
import  unittest
import  ddt

exlData = OperationExcel('./data/TestName.xls', 'requestMethod')
testData = exlData.getDataByDict()

@ddt.ddt()
class TestRequestMethods(unittest.TestCase):
    @ddt.data(*testData)
    def testRequestMethods(self, data):
        url = data['requestUrl']
        method = data['requestMethod']
        params = data['requestParams']
        if method == 'get' or method == 'delete':
            res = SendMeth.sendMethod(method, url, params=params)
        else:
            params = json.dumps(params) #请求参数带中文，要转车json字符串，否则报错
            res = SendMeth.sendMethod(method, url, data = params)
        resCode = GetKeyword.getKeyWord(res, 'code')
        resMsg = GetKeyword.getKeyWord(res, 'message')
        if resMsg == 'get success':
            MyLog.info('获取手机信息成功')
        elif resMsg == 'update success':
            MyLog.info('更新信息成')
        elif resMsg == "delete success":
            MyLog.info('删除手机信息成功')
        else:
            MyLog.error('获取、更新、删除手机信息失败')
        self.assertEqual(resCode, data['code'])
        self.assertEqual(resMsg, data['expectedResult'])

if __name__ == "__main__":
    unittest.main()
