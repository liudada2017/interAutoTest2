"""
getKeyword_forResult.py文件说明：
1.作用
    在接口返回值中，通过关键获取获取对应字段内容
paramsGet.json，前提：需要安装一个库：jsonpath库
    安装jsonpath ： pip install jsonpath
    使用jsonpath模块进行处理更加方便

"""
# 导入jsonpath模块
import  jsonpath

#封装获取接口返回值方法
class GetKeyword:
    @staticmethod
    def getKeyWord(response:dict, keyword):
        """
             通过关键字获取对应返回值,如果有多个值,只返回第一个,
             如果关键字不存在,返回False。
             :param:response 数据源  字典格式
             :param:keyword 要获取的字段
             :return:
             """
        try:
            return jsonpath.jsonpath(response, f"$..{keyword}")[0]
            """
            # 其中："$"表示最外层的{}，
            # ".."表示模糊匹配，
            # 当传入不存在的key_nane时，程序会返回false。
            """
        except:
            print('关键字不存在')
    @staticmethod
    def getKeyWords(response:dict, keyword):
        try:
            return jsonpath.jsonpath(response, f"$..{keyword}")
        except:
            print('关键字不存在')

if __name__ == "__main__":
    response = {
        "count": 2,
        "next": "下一页",
        "previous": None,
        "results": [
            {
                "dep_id": "10",
                "dep_name": "tester_10",
                "master_name": "master_10",
                "slogan": "随便"
            },
            {
                "dep_id": "11",
                "dep_name": "tester_11",
                "master_name": "master_11",
                "slogan": "随便"
            }
        ]
    }
    keyword = "dep_id"
    print(GetKeyword.getKeyWord(response,keyword)) #返回10
    print(GetKeyword.getKeyWords(response, keyword)) #返回10,11