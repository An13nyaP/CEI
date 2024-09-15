import requests

url = "http://api.open-notify.org/iss-now.json"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Failed to retrieve data. HTTP Status code: {response.status_code}")
