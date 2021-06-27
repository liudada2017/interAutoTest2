import xlrd
from xlrd import xldate_as_tuple
from datetime import  datetime

class OperationExcel:
    def __init__(self, filepath, model):
        book = xlrd.open_workbook(filename= filepath)
        self.sheet = book.sheet_by_index(0)
        self.model = model

    def readExcel(self):
        rows = self.sheet.nrows #获取所有行的值
        clos = self.sheet.ncols #获取所有列的值
        allDataList = []
        for row in range(1, rows):
            dataList = []
            for col in range(clos):
                ctype = self.sheet.cell(row,col).ctype
                cell = self.sheet.cell_value(row,col)
                #ctype : 0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
                if ctype == 2 and cell %1 == 0:
                    cell = int(cell)
                elif ctype == 3:
                        #处理日期时间数据，时间基准（0代表以1900-01-01为基准，1代表以1904-01-01为基准）
                        #datetime(1998,1,paramsGet.json,12,12,12)---->1998-01-02 12:12:12
                    date = datetime(*xldate_as_tuple(cell, 0))
                    cell = date.strftime("%Y-%m-%d %H-%M-%S")
                elif ctype == 4:
                    cell = True if cell == 1 else  False # 三目云算法
                if self.sheet.cell_value(row,1) == self.model:
                   dataList.append(cell)
            if len(dataList)!=0:
                allDataList.append(dataList)
        return allDataList
    def getDataByDict(self):
        keys = self.sheet.row_values(0) #获取第0行的值,返回值为一个列表
        values = self.readExcel()
        dataList = []
        for value in values:
            tmp = zip(keys,value)
            dataList.append(dict(tmp))
        return dataList
if __name__ == "__main__":
    oper = OperationExcel('../data/TestWeater.xls')
    data = oper.getDataByDict()
    print(data)

