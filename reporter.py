from requests import post
import json
import requests


url = "http://127.0.0.1:5000/"
data = json.dumps({"ph": 7.0})
r = requests.post(url, data)
print(r.status_code, r.reason)