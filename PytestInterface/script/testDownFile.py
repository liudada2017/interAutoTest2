from common.getKeyword_forResult import GetKeyword
from common.log import MyLog
from common.sendMethod import  SendMeth
from common.opreationExcel import  OperationExcel
import  unittest
import  ddt
import requests
import  os

exlData = OperationExcel('./data/TestName.xls', 'downFile')
testData =  exlData.getDataByDict()

@ddt.ddt()
class TestDownFile(unittest.TestCase):

    @ddt.data(*testData)
    def testDownFile(self, data):
        url = data['requestUrl']
        filePath = data['requestParams']
        res = requests.get(url, stream=True)
        with open(filePath, "wb") as f:
            for chunk in res.iter_content(chunk_size=512):
                f.write(chunk)
            f.close()

        if os.path.exists('./log.txt'):
            MyLog.info('文件下载成功')
        else:
            MyLog.error('文件下载失败')



if __name__ == "__main__":
    unittest.main()