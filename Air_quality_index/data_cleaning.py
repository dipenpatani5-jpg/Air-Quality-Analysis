
import pandas as pd

# Load dataset
df = pd.read_csv("AirQuality_Measurements.csv")

# 1. Display dataset information
print("\n--- DATASET INFORMATION ---")
print(df.info())

# 2. Display first five rows
print("\n--- FIRST FIVE ROWS ---")
print(df.head())

# 3. Check missing values
print("\n--- MISSING VALUES ---")
print(df.isnull().sum())

# 4. Check duplicate records
print("\n--- DUPLICATE RECORDS ---")
print(df.duplicated().sum())

# 5. Check available pollutants
print("\n--- POLLUTANTS ---")
print(df["Pollutant"].value_counts())

# 6. Check available locations
print("\n--- LOCATIONS ---")
print(df["Location"].value_counts())

# 7. Remove duplicates and missing values
df = df.drop_duplicates()
df = df.dropna(subset=["Value", "Date", "Pollutant"])

# 8. Convert Date into datetime format
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

# Remove invalid dates
df = df.dropna(subset=["Date"])

# 9. Save cleaned dataset
df.to_csv("Cleaned_AirQuality.csv", index=False)

print("\nData cleaning completed!")
print("Total cleaned records:", len(df))
