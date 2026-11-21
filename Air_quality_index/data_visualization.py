
import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("Cleaned_AirQuality.csv")

# Convert date
df["Date"] = pd.to_datetime(df["Date"], utc=True)

df["Date"] = df["Date"].dt.tz_convert(None)

# Select PM2.5 pollutant
pm25 = df[
    df["Pollutant"].str.lower() == "pm25"
].copy()

if pm25.empty:
    print("PM2.5 data not found!")
    print("Available pollutants:")
    print(df["Pollutant"].value_counts())

else:
    # Extract month and year
    pm25["Month"] = pm25["Date"].dt.to_period("M")

    # Calculate monthly average
    monthly_data = pm25.groupby(
        "Month"
    )["Value"].mean()

    # Create line chart
    plt.figure(figsize=(12, 6))

    plt.plot(
        monthly_data.index.astype(str),
        monthly_data.values,
        marker="o",
        linewidth=2
    )

    plt.title("Monthly Average PM2.5 Concentration Across Monitoring Locations")
    plt.xlabel("Month")
    plt.ylabel("Average PM2.5 Concentration")
    plt.xticks(rotation=45)

    plt.grid(True)
    plt.tight_layout()
    plt.savefig("Monthly Average PM2.5 Concentration Across Monitoring Locations", dpi=300, bbox_inches="tight")
    plt.show()
    print("Graph saved successfully!")
    print("Visualization completed!")
