import pandas as pd
import matplotlib.pyplot as plt

# Read the data from the CSV files
traditional_data = pd.read_csv("traditional_poultry_shed_data.csv")
controlled_data = pd.read_csv("controlled_poultry_shed_data.csv")

# Function to plot comparisons
def plot_comparison(parameter, ylabel, ax):
    # Plot traditional data
    for day in traditional_data["Day_Number"].unique():
        day_data = traditional_data[traditional_data["Day_Number"] == day]
        ax.plot(
            day_data["Hour"],
            day_data[parameter],
            color="blue",
            label=f"Traditional Shed {day}" if day == 1 else "",
        )

    # Plot controlled data
    for day in controlled_data["Day_Number"].unique():
        day_data = controlled_data[controlled_data["Day_Number"] == day]
        ax.plot(
            day_data["Hour"],
            day_data[parameter],
            color="green",
            label=f"Controlled Shed {day}" if day == 1 else "",
        )

    # Customize plot
    ax.set_title(f"Hourly {parameter} for 35 Days: Traditional vs Controlled Environment")
    ax.set_xlabel("Hour")
    ax.set_ylabel(ylabel)
    ax.set_xticks(range(0, 24, 2))  # Customizing x-axis ticks every 2 hours
    ax.legend(loc="upper right", bbox_to_anchor=(1.15, 1))

# Create a figure with subplots
fig, axs = plt.subplots(2, 2, figsize=(20, 12))  # 2x2 layout, with overall figure size

# Plot Temperature Comparison
plot_comparison("Temperature", "Temperature (°C)", axs[0, 0])

# Plot Humidity Comparison
plot_comparison("Humidity", "Humidity (%)", axs[0, 1])

# Plot Gas Level Comparison
plot_comparison("Gas Level", "Gas Level", axs[1, 0])

# Remove the empty subplot (bottom right)
fig.delaxes(axs[1, 1])

# Adjust layout
plt.tight_layout()

# Save the figure with high quality
plt.savefig("img/comparison_plots.png", dpi=300)
plt.close()
