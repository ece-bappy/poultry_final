import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the data from the CSV files
traditional_data = pd.read_csv("traditional_poultry_shed_data.csv")
controlled_data = pd.read_csv("controlled_poultry_shed_data.csv")

# Ensure that both datasets have an 'Hour' column
if 'Hour' not in traditional_data.columns or 'Hour' not in controlled_data.columns:
    raise ValueError("Both dataframes must include an 'Hour' column")

# Function to compute std vs hour
def std_vs_hour(data):
    return data.groupby('Hour').std()

# Compute std vs hour for both environments
std_traditional = std_vs_hour(traditional_data)
std_controlled = std_vs_hour(controlled_data)

# Parameters to plot
parameters = ["Temperature", "Humidity", "Gas Level"]

# Create plots
plt.figure(figsize=(15, 10))
for i, parameter in enumerate(parameters):
    plt.subplot(2, 2, i + 1)
    plt.plot(std_traditional.index, std_traditional[parameter], label='Traditional', color='blue')
    plt.plot(std_controlled.index, std_controlled[parameter], label='Controlled', color='green')
    plt.xlabel('Hour')
    plt.ylabel(f'Standard Deviation of {parameter}')
    plt.title(f'Standard Deviation vs Hour for {parameter}')
    plt.legend()
    plt.xticks(np.arange(0, 24, step=2))  # Set x-axis ticks at intervals of 2 hours

plt.tight_layout()
plt.savefig("img/std_vs_hour_plot.png", dpi=300)
plt.close