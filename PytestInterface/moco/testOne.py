import requests
url ='http://127.0.0.1:12306/api/departments/T03/'
json = {
    "data":[
          {
            "dep_id": "T03",
            "dep_name": "C++",
            "master_name": "C++-Master",
            "slogan": "Here is Slogan"
          }
        ]
}
response = requests.put(url = url,json = json)
print(response.text)