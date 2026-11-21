import requests
import pandas as pd

# Enter your OpenAQ API key
API_KEY = "4f6056b9f122344d8a8060b65928c3b38205a3dc72af3a2987d316d591caaeb8"

# OpenAQ API endpoint
url = "https://api.openaq.org/v3/locations"

headers = {
    "X-API-Key": API_KEY
}

params = {
    "iso": "IN",
    "limit": 100
}

response = requests.get(
    url,
    headers=headers,
    params=params
)

if response.status_code == 200:
    data = response.json()

    df = pd.json_normalize(data["results"])

    df.to_csv("AirQuality.csv", index=False)

    print("Dataset downloaded successfully!")
    print(df.head())

else:
    print("Error:", response.status_code)
    print(response.text)