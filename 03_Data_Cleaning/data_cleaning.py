import pandas as pd
import numpy as np

# Load the raw dataset
df = pd.read_csv("bangalore_traffic_timely_data.csv")

# Display basic dataset information
print("Original Dataset Shape:")
print(df.shape)

print("\nFirst 5 Rows:")
print(df.head())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check duplicate rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Convert Date column to datetime format
df["Date"] = pd.to_datetime(df["Date"])

# Display data types after conversion
print("\nData Types:")
print(df.dtypes)

# Check for invalid numeric values
print("\nInvalid Numeric Values:")

numeric_columns = [
    "Traffic Volume",
    "Average Speed",
    "Travel Time Index",
    "Congestion Level",
    "Road Capacity Utilization",
    "Incident Reports",
    "Environmental Impact",
    "Public Transport Usage",
    "Traffic Signal Compliance",
    "Parking Usage",
    "Pedestrian and Cyclist Count"
]

for column in numeric_columns:
    if column == "Congestion Level":
        continue
    print(f"{column}: {(pd.to_numeric(df[column], errors='coerce').isna()).sum()} non-numeric values")

print("\nNegative Values in Numeric Columns:")
for column in numeric_columns:
    if column == "Congestion Level":
        continue
    values = pd.to_numeric(df[column], errors="coerce")
    print(f"{column}: {(values < 0).sum()} negative values")

# Remove duplicate rows if any
df = df.drop_duplicates()

# Save the cleaned dataset
df.to_csv("bangalore_traffic_cleaned.csv", index=False)

print("\nData Cleaning Completed Successfully!")
print("Cleaned dataset saved as: bangalore_traffic_cleaned.csv")

print("\nFinal Dataset Shape:")
print(df.shape)

