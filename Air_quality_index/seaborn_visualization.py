
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
df = pd.read_csv("Cleaned_AirQuality.csv")

# Select PM2.5 data
pm25 = df[
    df["Pollutant"].str.lower() == "pm25"
].copy()

if pm25.empty:
    print("PM2.5 data not found!")

else:
    # Calculate average PM2.5 by location
    location_data = (
        pm25.groupby("Location")["Value"]
        .mean()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    # Create chart
    plt.figure(figsize=(12, 6))

    sns.barplot(
        data=location_data,
        x="Value",
        y="Location"
    )

    plt.title("Top 10 Locations by Average PM2.5")
    plt.xlabel("Average PM2.5 Concentration")
    plt.ylabel("Monitoring Location")

    plt.tight_layout()

    plt.savefig(
        "PM25_Location_Comparison.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()

    print("Seaborn visualization completed!")
