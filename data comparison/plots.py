import pandas as pd
import matplotlib.pyplot as plt

# Read the data from the CSV files
traditional_data = pd.read_csv("traditional_poultry_shed_data.csv")
controlled_data = pd.read_csv("controlled_poultry_shed_data.csv")


# Function to plot comparisons
def plot_comparison(parameter, ylabel, filename):
    plt.figure(figsize=(14, 6))  # Wider figure

    # Plot traditional data
    for day in traditional_data["Day_Number"].unique():
        day_data = traditional_data[traditional_data["Day_Number"] == day]
        plt.plot(
            day_data["Hour"],
            day_data[parameter],
            color="blue",
            label=f"Traditional Shed{day}" if day == 1 else "",
        )

    # Plot controlled data
    for day in controlled_data["Day_Number"].unique():
        day_data = controlled_data[controlled_data["Day_Number"] == day]
        plt.plot(
            day_data["Hour"],
            day_data[parameter],
            color="green",
            label=f"Controlled Shed {day}" if day == 1 else "",
        )

    # Customize plot
    plt.title(f"Hourly {parameter} for 35 Days: Traditional vs Controlled Environment")
    plt.xlabel("Hour")
    plt.ylabel(ylabel)
    plt.xticks(range(0, 24, 2))  # Customizing x-axis ticks every 2 hours
    plt.legend(loc="upper right", bbox_to_anchor=(1.15, 1))
    plt.savefig(f"img/{filename}.png", dpi=300)  # Save the figure with high quality
    plt.close()


# Plot Temperature Comparison
plot_comparison("Temperature", "Temperature (°C)", "temperature_comparison")

# Plot Humidity Comparison
plot_comparison("Humidity", "Humidity (%)", "humidity_comparison")

# Plot Gas Level Comparison
plot_comparison("Gas Level", "Gas Level", "gas_level_comparison")
