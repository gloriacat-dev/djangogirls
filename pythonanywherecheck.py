
import os
import requests

url = "https://www.pythonanywhere.com/api/v0/user/Gloria/webapps/"
headers = {"Authorization": "Token " + "fae413b829c9712c60e7f07ed282224326dd8ed2"}

response = requests.get(url, headers=headers, timeout=20)

print("HTTP status:", response.status_code)
print("Response:", response.text[:500])
PY