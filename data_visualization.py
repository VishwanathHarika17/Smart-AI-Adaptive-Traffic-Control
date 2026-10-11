import pandas as pd
import matplotlib.pyplot as plt
import os

# Create a folder to save the graphs
output_folder = "visualizations"
os.makedirs(output_folder, exist_ok=True)

# 1. Traffic volume by area
traffic_volume = pd.read_csv("traffic_volume_by_area.csv")

plt.figure(figsize=(10, 6))
plt.bar(traffic_volume.iloc[:, 0], traffic_volume.iloc[:, 1])
plt.title("Average Traffic Volume by Area")
plt.xlabel("Area")
plt.ylabel("Average Traffic Volume")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig(os.path.join(output_folder, "traffic_volume_by_area.png"))
plt.close()

# 2. Average speed by time block
average_speed = pd.read_csv("average_speed_by_timeblock.csv")

plt.figure(figsize=(9, 5))
plt.bar(average_speed.iloc[:, 0], average_speed.iloc[:, 1])
plt.title("Average Traffic Speed by Time Block")
plt.xlabel("Time Block")
plt.ylabel("Average Speed")
plt.tight_layout()
plt.savefig(os.path.join(output_folder, "average_speed_by_timeblock.png"))
plt.close()

# 3. Traffic situation counts
situation_counts = pd.read_csv("traffic_situation_counts.csv")

plt.figure(figsize=(8, 5))
plt.bar(situation_counts.iloc[:, 0], situation_counts.iloc[:, 1])
plt.title("Traffic Situation Counts")
plt.xlabel("Traffic Situation")
plt.ylabel("Number of Records")
plt.tight_layout()
plt.savefig(os.path.join(output_folder, "traffic_situation_counts.png"))
plt.close()

print("All visualizations created successfully!")
print("Check the visualizations folder for the three graphs.")

