import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load the data from the uploaded CSV file
file_path = "controlled_poultry_shed_data.csv"
data = pd.read_csv(file_path)

# Set up the plotting environment
sns.set(style="whitegrid")

# Create a figure with two rows and two columns
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(14, 10))

# Scatter plot for Temperature vs. Humidity with regression line
ax = axes[0, 0]
sns.scatterplot(x="Temperature", y="Humidity", hue="Day_Number", palette="tab10", data=data, legend=False, ax=ax)
sns.regplot(x="Temperature", y="Humidity", data=data, scatter=False, color="blue", ax=ax)
ax.set_title("Temperature vs. Humidity")
ax.set_xlabel("Temperature")
ax.set_ylabel("Humidity")

# Scatter plot for Temperature vs. Gas Level with regression line
ax = axes[0, 1]
sns.scatterplot(x="Temperature", y="Gas Level", hue="Day_Number", palette="tab10", data=data, legend=False, ax=ax)
sns.regplot(x="Temperature", y="Gas Level", data=data, scatter=False, color="blue", ax=ax)
ax.set_title("Temperature vs. Gas Level")
ax.set_xlabel("Temperature")
ax.set_ylabel("Gas Level")

# Scatter plot for Humidity vs. Gas Level with regression line
ax = axes[1, 0]
sns.scatterplot(x="Humidity", y="Gas Level", hue="Day_Number", palette="tab10", data=data, legend=False, ax=ax)
sns.regplot(x="Humidity", y="Gas Level", data=data, scatter=False, color="blue", ax=ax)
ax.set_title("Humidity vs. Gas Level")
ax.set_xlabel("Humidity")
ax.set_ylabel("Gas Level")

# Remove the unused subplot
fig.delaxes(axes[1, 1])

# Adjust spacing between subplots
plt.tight_layout()

# Save the figure
plt.savefig("combined_plots.png", dpi=300)

# Show the plot
plt.show()