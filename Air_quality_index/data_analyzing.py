
import pandas as pd

# Load cleaned dataset
df = pd.read_csv("Cleaned_AirQuality.csv")

# Convert date
df["Date"] = pd.to_datetime(df["Date"])

# 1. Basic information
print("\n--- DATASET SUMMARY ---")
print(df.describe())

# 2. Pollutant analysis
print("\n--- POLLUTANT COUNTS ---")
print(df["Pollutant"].value_counts())

# 3. Average pollution by pollutant
print("\n--- AVERAGE POLLUTION ---")
print(df.groupby("Pollutant")["Value"].mean())

# 4. Highest pollution locations
print("\n--- TOP 10 LOCATIONS ---")
print(
    df.groupby("Location")["Value"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

# 5. Monthly analysis
df["Month"] = df["Date"].dt.month

print("\n--- MONTHLY POLLUTION ---")
print(df.groupby("Month")["Value"].mean())

print("\nData analysis completed!")
