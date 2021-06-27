"""
getWeatherApi.py文件说明：
1、查询接口测试
paramsGet.json、获取查询接口返回值
"""
from common.sendMethod import SendMeth

class GetWeather:
    def __init__(self, url,  method):
        self.url = url
        self.method = method

    def getWeather(self, cityid):
        """
        根据单个id查询单个城市的天气
        """
        url = self.url + f"{cityid}" #功能类似format
        print(url)
        return SendMeth.sendMethod(method = self.method, url= url)
    def getWeatherParams(self, parames):
       """
              根据参数查询天气
        """
       return SendMeth.sendMethod(method= self.method, url = self.url, params= parames)

if __name__ == "__main__":
    url1 = 'https://spot.yiketianqi.com/'
    url2 = "https://spot.yiketianqi.com/?appid=95395338&appsecret=wOhi3R3x&cityid="
    method = "get"
    data = {"appid":95395338, 'appsecret':'wOhi3R3x','cityid':118387}
    cityid = 118387
    res = GetWeather(url2,method).getWeather(cityid)
    res2 = GetWeather(url1,method).getWeatherParams(data)
    print(res)
    print(res2)