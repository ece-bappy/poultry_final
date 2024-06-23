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

# Create a figure with 1x2 grid layout
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

# Plot the traditional shed correlation heatmap
sns.heatmap(traditional_corr_matrix, annot=True, fmt=".2f", cmap="coolwarm", cbar_kws={'label': 'Correlation Coefficient'}, ax=axes[0])
axes[0].set_title("Correlation Heatmap: Traditional Shed")

# Plot the controlled shed correlation heatmap
sns.heatmap(controlled_corr_matrix, annot=True, fmt=".2f", cmap="coolwarm", cbar_kws={'label': 'Correlation Coefficient'}, ax=axes[1])
axes[1].set_title("Correlation Heatmap: Controlled Shed")

# Save the combined figure
plt.tight_layout()
plt.savefig("img/combined_shed_correlation_heatmap.jpg", dpi=600)
plt.close()
