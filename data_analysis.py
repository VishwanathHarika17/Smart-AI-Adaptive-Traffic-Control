
import pandas as pd

# Load the cleaned traffic dataset
df = pd.read_csv("bangalore_traffic_cleaned.csv")

print("SMART TRAFFIC FLOW - DATA ANALYSIS")
print("=" * 40)

# 1. Dataset information
print("\n1. Dataset Information")
print("Number of records:", df.shape[0])
print("Number of columns:", df.shape[1])

# 2. Traffic situation counts
print("\n2. Traffic Situation Counts")
print(df["TrafficSituation"].value_counts())

# 3. Average traffic volume by area
print("\n3. Average Traffic Volume by Area")
print(
    df.groupby("Area Name")["Traffic Volume"]
    .mean()
    .sort_values(ascending=False)
    .round(2)
)

# 4. Average speed by area
print("\n4. Average Speed by Area")
print(
    df.groupby("Area Name")["Average Speed"]
    .mean()
    .sort_values(ascending=False)
    .round(2)
)

# 5. Traffic situations by time block
print("\n5. Traffic Situations by Time Block")
print(pd.crosstab(df["TimeBlock"], df["TrafficSituation"]))

# 6. Average traffic volume by time block
print("\n6. Average Traffic Volume by Time Block")
print(
    df.groupby("TimeBlock")["Traffic Volume"]
    .mean()
    .sort_values(ascending=False)
    .round(2)
)

# 7. Average speed by time block
print("\n7. Average Speed by Time Block")
print(
    df.groupby("TimeBlock")["Average Speed"]
    .mean()
    .sort_values(ascending=False)
    .round(2)
)


# 8. Save analysis results for future visualization

# Average traffic volume by area
df.groupby("Area Name")["Traffic Volume"].mean().round(2).reset_index().to_csv(
    "traffic_volume_by_area.csv", index=False
)

# Average speed by area
df.groupby("Area Name")["Average Speed"].mean().round(2).reset_index().to_csv(
    "average_speed_by_area.csv", index=False
)

# Traffic situation counts
df["TrafficSituation"].value_counts().rename_axis("Traffic Situation").reset_index(
    name="Count"
).to_csv("traffic_situation_counts.csv", index=False)

# Average traffic volume by time block
df.groupby("TimeBlock")["Traffic Volume"].mean().round(2).reset_index().to_csv(
    "traffic_volume_by_timeblock.csv", index=False
)

# Average speed by time block
df.groupby("TimeBlock")["Average Speed"].mean().round(2).reset_index().to_csv(
    "average_speed_by_timeblock.csv", index=False
)

# Traffic situations by time block
pd.crosstab(df["TimeBlock"], df["TrafficSituation"]).to_csv(
    "traffic_situations_by_timeblock.csv"
)
print("Analysis results saved to CSV files.")
print("Analysis completed successfully.")



