from common.getKeyword_forResult import GetKeyword
from common.log import MyLog
from common.sendMethod import  SendMeth
from common.opreationExcel import  OperationExcel
import  unittest
import requests

class TestDependentInter(unittest.TestCase):
    def testDependentInter(self):
        #获取抽奖活动id
        r = requests.get("http://127.0.0.1:5000/get_activity")
        result = r.json()
        activity_id = result["data"]["id"]
        if result['message'] == "success":
            MyLog.info('获取活动ID成功')
            self.assertEqual(10200, result['code'])
            self.assertEqual('success', result['message'])
        else:
            MyLog.error('获取活动ID失败')

        # 获取用户id
        r = requests.get("http://127.0.0.1:5000/get_user")
        result = r.json()
        user_id = result["data"]["id"]
        if result['message'] == "success":
            MyLog.info('获取用户ID成功')
            self.assertEqual(10200, result['code'])
            self.assertEqual('success', result['message'])
        else:
            MyLog.error('获取用户ID出错')

        # 调用获取抽奖号码接口
        data = {"aid": 2, "uid": 1}
        r = requests.post("http://127.0.0.1:5000/lucky_number", data=data)
        result = r.json()
        if result['message'] == "Lucky draw number":
            MyLog.info('获取抽奖号码接口成功')
            self.assertEqual(10200, result['code'])
        elif result['message'] == 'activity id exist':
            MyLog.info('活动ID已经存在')
            self.assertEqual(10104, result['code'])
            self.assertEqual('activity id exist', result['message'])
        else:
            MyLog.error('获取抽奖号码接口失败')


if __name__ =="__main__":
    unittest.main()