
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("Cleaned_AirQuality.csv")

# Convert values to numeric
df["Value"] = pd.to_numeric(
    df["Value"], errors="coerce"
)

# Create pollutant comparison table
pivot_df = df.pivot_table(
    index="Date",
    columns="Pollutant",
    values="Value",
    aggfunc="mean"
)

# Calculate correlation
correlation = pivot_df.corr()

# Create heatmap
plt.figure(figsize=(10, 7))

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Air Pollution Correlation Heatmap")
plt.tight_layout()

plt.savefig(
    "AirQuality_Correlation_Heatmap.png",
    dpi=300
)

plt.show()

print("Correlation heatmap completed!")
