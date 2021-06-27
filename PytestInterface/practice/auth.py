"""
自定义的身份验证机制是作为 requests.auth.AuthBase 的子类来实现的，
Requests 在 requests.auth 中提供了两种常见的的身份验证方案：
 HTTPBasicAuth 和 HTTPDigestAuth 。

"""
#示列一：使用明文提交用户名密码
# import requests
# baseUrl = "http://httpbin.org/get?username=xiaoming&password=123456"
# response = requests.get(baseUrl)
# if response.status_code == 200:
#     print(response.text)

"""
{
  "args": {
    "password": "123456", 
    "username": "xiaoming"
  }, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/paramsGet.json.25.1", 
    "X-Amzn-Trace-Id": "Root=1-60ac6728-2a1d75845cacdd180b1f49b4"
  }, 
  "origin": "125.70.79.238", 
  "url": "http://httpbin.org/get?username=xiaoming&password=123456"
}

"""

#示列2：使用requests库的Auth选项提交请求
# import  requests
# from requests.auth import  HTTPBasicAuth
# baseUrl = "http://httpbin.org"
# #身份验证
# response = requests.get(baseUrl+"/basic-auth/xiaoming/123456",auth = HTTPBasicAuth('xiaoming','123456'))
# if response.status_code == 200:
#     print(response.text)

"""
返回结果：
{
  "authenticated": true, 
  "user": "xiaoming"
}
"""

#示列3:请求一个实际的登录界面
import  requests
from requests.auth import  HTTPBasicAuth
url = 'http://sck.rjkflm.com:666/spider/auth/'
ah = HTTPBasicAuth('admin','admin')
response = requests.get(url = url, auth = ah)
if response.status_code == 200:
   print(response.text)