from common.sendMethod import SendMeth

class GetLoginMsg:
    def __init__(self, url, method):
        self.url = url
        self.method = method

    def postLoginData(self, data):
        """
        根据参数返回登录结果
        """
        return SendMeth.sendMethod(method=self.method, url = self.url ,json = data)
