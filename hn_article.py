import requests
import json

#执行api调用并查看响应
url = 'https://hacker-news.firebaseio.com/v0/item/31353677.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

#探索数据结构
response_dict = r.json()
response_str = json.dumps(response_dict, indent=4)
print(response_str)