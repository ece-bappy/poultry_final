import csv
import matplotlib.pyplot as plt
import pandas as pd

# Read the data from the CSV file
data = pd.read_csv("traditional_poultry_shed_data.csv")

# Plot Temperature
plt.figure(figsize=(14, 6))  # Wider figure
for day in data["Day_Number"].unique():
    day_data = data[data["Day_Number"] == day]
    plt.plot(day_data["Hour"], day_data["Temperature"], label=f"Day {day}")
plt.title("Hourly Temperature for 35 Days")
plt.xlabel("Hour")
plt.ylabel("Temperature (°C)")
plt.xticks(range(0, 24, 2))  # Customizing x-axis ticks every 2 hours
plt.legend(loc="upper right", bbox_to_anchor=(1.15, 1))
plt.savefig("img_t/temperature_plot.png", dpi=300)  # Save the figure with high quality
plt.close()

# Plot Humidity
plt.figure(figsize=(14, 6))  # Wider figure
for day in data["Day_Number"].unique():
    day_data = data[data["Day_Number"] == day]
    plt.plot(day_data["Hour"], day_data["Humidity"], label=f"Day {day}")
plt.title("Hourly Humidity for 35 Days")
plt.xlabel("Hour")
plt.ylabel("Humidity (%)")
plt.xticks(range(0, 24, 2))  # Customizing x-axis ticks every 2 hours
plt.legend(loc="upper right", bbox_to_anchor=(1.15, 1))
plt.savefig("img_t/humidity_plot.png", dpi=300)  # Save the figure with high quality
plt.close()
plt.show


# Plot Gas Level
plt.figure(figsize=(14, 6))  # Wider figure
for day in data["Day_Number"].unique():
    day_data = data[data["Day_Number"] == day]
    plt.plot(day_data["Hour"], day_data["Gas Level"], label=f"Day {day}")
plt.title("Hourly Gas Level for 35 Days")
plt.xlabel("Hour")
plt.ylabel("Gas Level")
plt.xticks(range(0, 24, 2))  # Customizing x-axis ticks every 2 hours
plt.legend(loc="upper right", bbox_to_anchor=(1.15, 1))
plt.savefig("img_t/gas_level_plot.png", dpi=300)  # Save the figure with high quality
plt.close()
