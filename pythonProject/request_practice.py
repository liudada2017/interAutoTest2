
########天气测试接口##########
# import  json
# import  requests
#
# url = "https://spot.yiketianqi.com/?"
# data ={
#     'appid': 95395338,
#     "appsecret": 'wOhi3R3x',
#     "cityid": 118387
# }
# response = requests.get(url,params = data)
# print(json.dumps(response.json(), indent=2,ensure_ascii=False))


##########传送正文方式为Content-Type = application/x-www-form-urlencoded，参数为字典############
# import  requests
# import json
#
# url = 'http://httpbin.org/post'
# data = {
#     "dep_id": "T01",
#     "dep_name": "Test学院",
#     "master_name": "Test-Master",
#     "slogan": "Here is Slogan"
# }
# response = requests.post(url = url , data = data)
# result = json.dumps(response.json(), indent=2, ensure_ascii = False )
# print(result)


############传送正文方式为raw，Content-Type= text\xml格式文本##########
#
# url = "http://httpbin.org/post"
# data = '<sites>' \
#             '<site>' \
#                 '<name>菜鸟教程</name>' \
#                 '<url>www.runoob.com</url>' \
#             '</site>' \
#             '<site>' \
#                 '<name>Google</name>' \
#                 '<url>www.google.com</url>' \
#             '</site>' \
#        '</sites>'
# headers = {'Content-Type':  'text/xml'}
# response = requests.post(url=url, json=data, headers = headers)
# result = json.dumps(response.json(),  indent=2, ensure_ascii=False)
# print(result)


###########传送正文方式为raw，Content-Type= application/json格式文本##########
# import  requests
# url = 'http://httpbin.org/post'
# data =  {
#     "data": [
#         {
#             "dep_id": "T01",
#             "dep_name": "Test学院",
#             "master_name": "Test-Master",
#             "slogan": "Here is Slogan"
#         }
#     ]
# }
#
# response = requests.post(url = url ,json = data)
# print(response.text)

###########传送正文方式为binary，Content-Type= multipart/form-data格式文本,多用于文件上传##########
# import  requests
# url = 'http://httpbin.org/post'
# data = {"files": open("test.txt", "rb")}
# response = requests.post(url =url, files = data)
# print(response.text)


###########Content-Type= multipart/form-data格式文本,多个文件上传,多个参数上传##########
# import  requests
# url ='http://httpbin.org/post'
# data ={
#              "name":'dada',
#              "age":18
# }
# files =[
#             ('files1',("1.jpeg", open('logo1.jpeg','rb'),'image/jpeg')),
#             ("files2",("2.jpeg",open('logo2.jpeg','rb'),'image/jpeg'))
#           ]
# response = requests.post(url = url, files = files, data = data)
# print(response.text)

###########Content-Type= multipart/form-data格式文本,流式上传大文件##########
# import requests
# from  requests_toolbelt import  MultipartEncoder
# url = 'http://httpbin.org/post'
# data = {
#     "username": "Jerry",
#     "password": "1232456",
#     "sex": "男"
# }
# m = MultipartEncoder(fields = data)
# headers = {'Content-type': m.content_type}
# response = requests.post(url = url,data = m, headers = headers)
# print(response.text)