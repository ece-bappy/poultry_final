import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the data from the CSV files
traditional_data = pd.read_csv("traditional_poultry_shed_data.csv")
controlled_data = pd.read_csv("controlled_poultry_shed_data.csv")

# Function to create heatmaps
def create_heatmap(data, parameter, ax, title):
    # Pivot the data to get Hours as columns and Days as rows
    pivot_data = data.pivot_table(values=parameter, index="Day_Number", columns="Hour")
    
    # Create a heatmap
    sns.heatmap(pivot_data, ax=ax, cmap="YlGnBu", cbar_kws={'label': parameter})
    
    # Customize plot
    ax.set_title(title)
    ax.set_xlabel("Hour")
    ax.set_ylabel("Day Number")

# Create a figure with subplots
fig, axs = plt.subplots(2, 2, figsize=(20, 12))  # 2x2 layout, with overall figure size

# Plot Traditional Temperature Heatmap
create_heatmap(traditional_data, "Temperature", axs[0, 0], "Traditional Shed Temperature")

# Plot Controlled Temperature Heatmap
create_heatmap(controlled_data, "Temperature", axs[0, 1], "Controlled Shed Temperature")

# Plot Traditional Humidity Heatmap
create_heatmap(traditional_data, "Humidity", axs[1, 0], "Traditional Shed Humidity")

# Remove the empty subplot (bottom right)
fig.delaxes(axs[1, 1])

# Adjust layout
plt.tight_layout()

# Save the figure with high quality
plt.savefig("img/heatmap_comparison.png", dpi=300)
plt.close()
