import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load the data from the uploaded CSV file
file_path = "temperature_humidity_gas_data.csv"
data = pd.read_csv(file_path)


# Set up the plotting environment
sns.set(style="whitegrid")

# Create histograms for Temperature, Humidity, and Gas Level
fig, axes = plt.subplots(1, 3, figsize=(18, 6))

# Histogram for Temperature
sns.histplot(data["Temperature"], kde=True, ax=axes[0], color="skyblue")
axes[0].set_title("Temperature Distribution")
axes[0].set_xlabel("Temperature")
axes[0].set_ylabel("Frequency")

# Histogram for Humidity
sns.histplot(data["Humidity"], kde=True, ax=axes[1], color="salmon")
axes[1].set_title("Humidity Distribution")
axes[1].set_xlabel("Humidity")
axes[1].set_ylabel("Frequency")

# Histogram for Gas Level
sns.histplot(data["Gas Level"], kde=True, ax=axes[2], color="limegreen")
axes[2].set_title("Gas Level Distribution")
axes[2].set_xlabel("Gas Level")
axes[2].set_ylabel("Frequency")

# Show the plot
plt.tight_layout()
plt.savefig("img/Distribution.png", dpi=300)  # Save the figure with high quality
plt.close()
