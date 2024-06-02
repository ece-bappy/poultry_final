import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load the data from the uploaded CSV file
file_path = "temperature_humidity_gas_data.csv"
data = pd.read_csv(file_path)

# Set up the plotting environment
sns.set(style="whitegrid")

# Scatter plot for Temperature vs. Humidity with regression line
plt.figure(figsize=(10, 6))
sns.scatterplot(
    x="Temperature",
    y="Humidity",
    hue="Day_Number",
    palette="tab10",
    data=data,
    legend=False,
)
sns.regplot(x="Temperature", y="Humidity", data=data, scatter=False, color="blue")
plt.title("Temperature vs. Humidity")
plt.xlabel("Temperature")
plt.ylabel("Humidity")
plt.tight_layout()
plt.savefig("img/Temperature_vs_Humidity.png", dpi=300)
plt.show()

# Scatter plot for Temperature vs. Gas Level with regression line
plt.figure(figsize=(10, 6))
sns.scatterplot(
    x="Temperature",
    y="Gas Level",
    hue="Day_Number",
    palette="tab10",
    data=data,
    legend=False,
)
sns.regplot(x="Temperature", y="Gas Level", data=data, scatter=False, color="blue")
plt.title("img/Temperature vs. Gas Level")
plt.xlabel("Temperature")
plt.ylabel("Gas Level")
plt.tight_layout()
plt.savefig("img/Temperature_vs_Gas_Level.png", dpi=300)
plt.show()

# Scatter plot for Humidity vs. Gas Level with regression line
plt.figure(figsize=(10, 6))
sns.scatterplot(
    x="Humidity",
    y="Gas Level",
    hue="Day_Number",
    palette="tab10",
    data=data,
    legend=False,
)
sns.regplot(x="Humidity", y="Gas Level", data=data, scatter=False, color="blue")
plt.title("Humidity vs. Gas Level")
plt.xlabel("Humidity")
plt.ylabel("Gas Level")
plt.tight_layout()
plt.savefig("img/Humidity_vs_Gas_Level.png", dpi=300)
plt.show()
