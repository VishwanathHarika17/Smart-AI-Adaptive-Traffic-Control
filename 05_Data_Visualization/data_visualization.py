
import pandas as pd
import matplotlib.pyplot as plt
import os

# Load the cleaned traffic dataset
df = pd.read_csv("bangalore_traffic_cleaned.csv")

# Create a folder to save all five charts
output_folder = "visualizations"
os.makedirs(output_folder, exist_ok=True)

# Convert columns into appropriate data types
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
df["Traffic Volume"] = pd.to_numeric(df["Traffic Volume"], errors="coerce")
df["Average Speed"] = pd.to_numeric(df["Average Speed"], errors="coerce")

# Define traffic situation colours
situation_colors = {
    "HIGH": "red",
    "MEDIUM": "gold",
    "LOW": "green"
}

# --------------------------------------------------
# 1. Average Traffic Volume by Area
# --------------------------------------------------

traffic_volume = (
    df.groupby("Area Name")["Traffic Volume"]
    .mean()
    .sort_values(ascending=False)
)

plt.figure(figsize=(11, 6))
plt.bar(traffic_volume.index, traffic_volume.values, color="steelblue")
plt.title("Average Traffic Volume by Area")
plt.xlabel("Area")
plt.ylabel("Average Traffic Volume")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig(os.path.join(output_folder, "traffic_volume_by_area.png"))
plt.close()


# --------------------------------------------------
# 2. Traffic Situation Distribution
# --------------------------------------------------

situation_counts = df["TrafficSituation"].value_counts()

pie_colors = [
    situation_colors.get(str(label).upper(), "gray")
    for label in situation_counts.index
]

plt.figure(figsize=(8, 6))
plt.pie(
    situation_counts.values,
    labels=situation_counts.index,
    autopct="%1.1f%%",
    startangle=90,
    colors=pie_colors
)
plt.title("Traffic Situation Distribution")
plt.tight_layout()
plt.savefig(os.path.join(output_folder, "traffic_situation_distribution.png"))
plt.close()


# --------------------------------------------------
# 3. Monthly Traffic Volume Trend
# --------------------------------------------------

monthly_traffic = (
    df.dropna(subset=["Date"])
    .groupby(df["Date"].dt.to_period("M"))["Traffic Volume"]
    .mean()
)

plt.figure(figsize=(11, 6))
plt.plot(
    monthly_traffic.index.astype(str),
    monthly_traffic.values,
    marker="o",
    color="blue"
)
plt.title("Monthly Traffic Volume Trend")
plt.xlabel("Month")
plt.ylabel("Average Traffic Volume")
plt.xticks(rotation=45, ha="right")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(os.path.join(output_folder, "monthly_traffic_volume_trend.png"))
plt.close()


# --------------------------------------------------
# 4. Traffic Volume vs Average Speed
# --------------------------------------------------

plt.figure(figsize=(10, 6))

for situation, group in df.groupby("TrafficSituation"):
    plt.scatter(
        group["Average Speed"],
        group["Traffic Volume"],
        label=situation,
        color=situation_colors.get(str(situation).upper(), "gray"),
        alpha=0.5
    )

plt.title("Traffic Volume vs Average Speed")
plt.xlabel("Average Speed")
plt.ylabel("Traffic Volume")
plt.legend(title="Traffic Situation")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(os.path.join(output_folder, "traffic_volume_vs_average_speed.png"))
plt.close()


# --------------------------------------------------
# 5. Congestion by Area
# --------------------------------------------------

congestion_data = (
    df.groupby(["Area Name", "Congestion Level"])["Traffic Volume"]
    .mean()
    .unstack(fill_value=0)
)

# Sort areas by overall average traffic volume
area_order = (
    df.groupby("Area Name")["Traffic Volume"]
    .mean()
    .sort_values(ascending=False)
    .index
)

congestion_data = congestion_data.reindex(area_order)

# Define congestion colours
congestion_colors = {
    "HIGH": "red",
    "MEDIUM": "gold",
    "LOW": "green"
}

colors = [
    congestion_colors.get(str(level).upper(), "gray")
    for level in congestion_data.columns
]

congestion_data.plot(
    kind="bar",
    stacked=True,
    figsize=(11, 6),
    color=colors
)

plt.title("Congestion by Area")
plt.xlabel("Area")
plt.ylabel("Average Traffic Volume")
plt.xticks(rotation=45, ha="right")
plt.legend(title="Congestion Level")
plt.tight_layout()
plt.savefig(os.path.join(output_folder, "congestion_by_area.png"))
plt.close()


# --------------------------------------------------
# Completion message
# --------------------------------------------------

print("SMART AI ADAPTIVE TRAFFIC CONTROL")
print("=" * 45)
print("All five visualizations created successfully!")
print("Check the 'visualizations' folder.")

print("\nGenerated charts:")
print("1. Average Traffic Volume by Area")
print("2. Traffic Situation Distribution")
print("3. Monthly Traffic Volume Trend")
print("4. Traffic Volume vs Average Speed")
print("5. Congestion by Area")
