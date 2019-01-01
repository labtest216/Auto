from requests import post
import json
import requests

# App run on IOT device.
# Report data to server every time interval.
url = "http://127.0.0.1:5000/"
data = {"ph": 999}
r = requests.post(url, data)
print(r.status_code, r.reason)