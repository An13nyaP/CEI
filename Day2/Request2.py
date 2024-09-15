import requests

url = "http://api.open-notify.org/iss-now.json"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    
    timestamp = data["timestamp"]
    latitude = data["iss_position"]["latitude"]
    longitude = data["iss_position"]["longitude"]
    
    print(f"Timestamp: {timestamp}")
    print(f"Latitude: {latitude}")
    print(f"Longitude: {longitude}")
else:
    print(f"Failed to retrieve data.")
