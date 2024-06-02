import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read CSV file into a pandas DataFrame
df = pd.read_csv("temperature_humidity_gas_data.csv")

# Convert 'Time' column to datetime format
df["Hour"] = pd.to_datetime(df["Hour"], format="%H:%M")

# Group by day and extract data for box plots
grouped_df = (
    df.groupby("Day_Number")
    .agg({"Temperature": "mean", "Humidity": "mean", "Gas Level": "mean"})
    .reset_index()
)

# Create individual box plots for each variable
variables = ["Temperature", "Humidity", "Gas Level"]
for variable in variables:
    plt.figure(figsize=(10, 6))
    sns.boxplot(x="Day_Number", y=variable, data=df)
    plt.title(f"Box Plot for {variable} Between Days")
    plt.xlabel("Day")
    plt.ylabel(variable)
    plt.savefig(f"{variable}_box_plots_all_days.png", dpi=300)
    plt.close()
