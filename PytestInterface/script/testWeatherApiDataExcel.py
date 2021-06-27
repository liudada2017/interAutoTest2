from common.opreationExcel import OperationExcel
from interface.getWeatherApi import GetWeather
from common.getKeyword_forResult import GetKeyword
import unittest
import ddt

oper = OperationExcel('./data/TestWeater.xls','weather')
testData = oper.getDataByDict()

@ddt.ddt()
class TestWeatherApiExcel(unittest.TestCase):
    def setUp(self) -> None:
        self.url = 'https://spot.yiketianqi.com/'
        self.weather = GetWeather(self.url, 'get')

    @ddt.data(*testData)  # 使用元组或者列表，ddt会自动把元组或者列表对应到多个参数上
    def testWeatherApi(self, data):
        reqData = {"appid": data['appid'], 'appsecret': data['appsecret'], 'cityid': data['cityid']}
        apiResponse = self.weather.getWeatherParams(reqData)
        response = GetKeyword.getKeyWords(apiResponse, 'cityid')
        self.assertEqual(response[0], str(data['expect']))

if __name__ == "__main__":
    unittest.main()
