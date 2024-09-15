import requests
import pandas as pd
import time

url = "http://api.open-notify.org/iss-now.json"

iss_data = []

for i in range(100):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # Extracting required info 
        timestamp = data["timestamp"]
        latitude = data["iss_position"]["latitude"]
        longitude = data["iss_position"]["longitude"]

        # Appending the data to the list
        iss_data.append({"timestamp": timestamp, "latitude": latitude, "longitude": longitude})
        time.sleep(1)
    else:
        print(f"Failed to retrieve data.")
        break

# Creating a DataFrame
df = pd.DataFrame(iss_data)

# Writing the DataFrame to CSV file
df.to_csv("iss_location_data.csv", index=False)
print("Data has been written to 'iss_location_data.csv'.")
