import requests
import json
class SendMeth:
     #根据不同的请求方法，返回请求结果
        @staticmethod
        def sendMethod(method, url,  params = None, data= None, headers = None, auth = None, files = None, stream = None):
            #定义请求方法
                if method == 'get' or method == 'delete':
                    #构造一个基础请求方法
                    response = requests.request(method = method, url = url, params = params, stream = stream)
                elif method == 'post' or method == 'put':
                     response = requests.request(method = method, url = url, data = data, headers=headers, auth = auth, files = files)
                else:
                    print('请求方式不对')
                    return None
                return response.json()

        #将json数据转换成json字符串
        @staticmethod
        def jsonToPython(res):
            result = json.dumps(res, indent=2,  ensure_ascii= False)
            return result

if __name__ =="__main__":
    method = "post"
    url = "http://www.testingedu.com.cn:8000/index.php?m=Home&c=User&a=do_login&t=0.2700815916074655"
    data = {
        'appid':95395338,
        "appsecret":'wOhi3R3x',
        "cityid":118387
      }
    header = {"Content-Type": "application/x-www-form-urlencoded"}
    json1 = { "username: ": "845809908@qq.com", "password": "123456", "verify_code: ": "1"}
    res = SendMeth.sendMethod(method,  url, data=json1,headers = header)
    print(SendMeth.jsonToPython(res))



