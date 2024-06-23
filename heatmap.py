import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
traditional_data = pd.read_csv("traditional_poultry_shed_data.csv")
controlled_data = pd.read_csv("controlled_poultry_shed_data.csv")

# Function to create heatmap
def create_heatmap(data, title, environment, ax):
    # Pivot the data to create a heatmap
    hours = ['0:00', '1:00', '2:00', '3:00', '4:00', '5:00', '6:00', '7:00', '8:00', '9:00', 
             '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', 
             '19:00', '20:00', '21:00', '22:00', '23:00']
    pivoted_data = data.pivot_table(index="Day_Number", columns="Hour", values=title, dropna=False)
    pivoted_data = pivoted_data.reindex(columns=hours)
    
    # Create the heatmap
    sns.heatmap(pivoted_data, cmap="YlGnBu", annot=False, cbar_kws={'label': title}, ax=ax)
    ax.set_title(environment + " - " + title + " Heatmap")
    ax.set_xlabel("Hour")
    ax.set_ylabel("Day Number")

# Create a 2x3 grid for the plots
fig, axes = plt.subplots(3, 2, figsize=(16, 18))

# Create heatmaps for each parameter
parameters = ["Temperature", "Humidity", "Gas Level"]
environments = ["Traditional", "Controlled"]

for i, parameter in enumerate(parameters):
    for j, environment in enumerate(environments):
        if environment == "Traditional":
            create_heatmap(traditional_data, parameter, environment, axes[i, j])
        else:
            create_heatmap(controlled_data, parameter, environment, axes[i, j])

plt.tight_layout()

# Save the figure with 300 dpi
plt.savefig("poultry_heatmaps1.jpg", dpi=600)

