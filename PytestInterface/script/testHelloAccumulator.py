from common.getKeyword_forResult import GetKeyword
from common.log import MyLog
from common.sendMethod import  SendMeth
from common.opreationExcel import  OperationExcel
import  unittest
import  ddt
exlData = OperationExcel('./data/TestName.xls','name')
testData = exlData.getDataByDict()
@ddt.ddt()
class TestHelloAccumulator(unittest.TestCase):

    def setUp(self) -> None:
        self.urlHello = 'http://127.0.0.1:5000'
        self.urlAcc = 'http://127.0.0.1:5000/add_one'

    def testHello(self):
        res = SendMeth.sendMethod( 'get', self.urlHello)
        resMsg = GetKeyword.getKeyWord(res, 'message')
        resCode = GetKeyword.getKeyWord(res, 'code')
        if resMsg:
            MyLog.info('获取到hello信息！')
        else:
            MyLog.error('获取hello信息失败')
        self.assertEqual(10200,resCode)
        self.assertEqual('Welcome to API testing',resMsg)

    def testAccumulator(self):
        res = SendMeth.sendMethod('get', self.urlAcc)
        resMsg = GetKeyword.getKeyWord(res, 'message')
        resCode = GetKeyword.getKeyWord(res,'code')
        resNum = GetKeyword.getKeyWord(res, 'data').get('number')
        if  resMsg == "success":
            MyLog.info('增长1成功')
        else:
            MyLog.error('增长1失败')
        self.assertEqual(resCode, 10200)
        self.assertEqual(resNum, 1)

    @ddt.data(*testData)
    def testName(self, data):
            url = data['requestUrl'] + data['requestParams']
            res = SendMeth.sendMethod(data['requestMethod'], url)
            resMsg = GetKeyword.getKeyWord(res, 'message')
            resCode = GetKeyword.getKeyWord(res, 'code')
            if resMsg:
                MyLog.info('获取名字成功！')
            else:
                MyLog.error('获取名字失败！')
            self.assertEqual(resCode, data['code'])
            self.assertEqual(resMsg, data['expectedResult'])



    def tearDown(self) -> None:
        pass


