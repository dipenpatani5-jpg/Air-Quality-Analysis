import requests
import pandas as pd

API_KEY = "4f6056b9f122344d8a8060b65928c3b38205a3dc72af3a2987d316d591caaeb8"

BASE_URL = "https://api.openaq.org/v3"

headers = {"X-API-Key": API_KEY}

# Read downloaded location data
locations = pd.read_csv("AirQuality.csv")

all_data = []

for _, location in locations.iterrows():

    location_id = location["id"]

    # Get sensors
    url = f"{BASE_URL}/locations/{location_id}/sensors"

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        continue

    sensors = response.json()["results"]

    for sensor in sensors:

        sensor_id = sensor["id"]
        parameter = sensor["parameter"]["name"]

        # Get daily measurements
        url = f"{BASE_URL}/sensors/{sensor_id}/days"

        params = {
            "date_from": "2025-01-01",
            "date_to": "2026-11-20",
            "limit": 1000
        }

        response = requests.get(
            url,
            headers=headers,
            params=params
        )

        if response.status_code != 200:
            continue

        measurements = response.json()["results"]

        for item in measurements:

            all_data.append({
                "Location_ID": location_id,
                "Location": location.get("name"),
                "Sensor_ID": sensor_id,
                "Pollutant": parameter,
                "Value": item.get("value"),
                "Date": item.get("period", {})
                          .get("datetimeFrom", {})
                          .get("utc")
            })

df = pd.DataFrame(all_data)

df.to_csv("AirQuality_Measurements.csv", index=False)

print("Measurements downloaded successfully!")
print(df.head())
print("Total records:", len(df))