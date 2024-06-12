import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the data from the CSV files
traditional_data = pd.read_csv("traditional_poultry_shed_data.csv")
controlled_data = pd.read_csv("controlled_poultry_shed_data.csv")

# Filter the data to include only relevant columns
relevant_columns = ["Temperature", "Humidity", "Gas Level"]
traditional_filtered = traditional_data[relevant_columns]
controlled_filtered = controlled_data[relevant_columns]

# Compute the correlation matrices
traditional_corr_matrix = traditional_filtered.corr()
controlled_corr_matrix = controlled_filtered.corr()

# Plot the traditional shed correlation heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(traditional_corr_matrix, annot=True, fmt=".2f", cmap="coolwarm", cbar_kws={'label': 'Correlation Coefficient'})
plt.title("Correlation Heatmap: Traditional Shed")
plt.savefig("img/traditional_shed_correlation_heatmap.png", dpi=300)
plt.close()

# Plot the controlled shed correlation heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(controlled_corr_matrix, annot=True, fmt=".2f", cmap="coolwarm", cbar_kws={'label': 'Correlation Coefficient'})
plt.title("Correlation Heatmap: Controlled Shed")
plt.savefig("img/controlled_shed_correlation_heatmap.png", dpi=300)
plt.close()
