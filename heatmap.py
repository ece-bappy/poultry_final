import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read the data from the CSV files
traditional_data = pd.read_csv("traditional_poultry_shed_data.csv")
controlled_data = pd.read_csv("controlled_poultry_shed_data.csv")

# Function to plot correlation heatmap
def plot_correlation_heatmap(data, title, drop_column):
    # Drop the specified column and select only numeric columns
    numeric_data = data.drop(columns=[drop_column]).select_dtypes(include=[float, int])
    plt.figure(figsize=(10, 8))
    corr_matrix = numeric_data.corr()
    sns.heatmap(corr_matrix, annot=True, cmap='viridis', vmin=-1, vmax=1)
    plt.title(title)
    plt.show()

# Plot correlation heatmap for traditional environment
plot_correlation_heatmap(traditional_data, "Correlation Matrix: Traditional Shed", "Day_Number")

# Plot correlation heatmap for controlled environment
plot_correlation_heatmap(controlled_data, "Correlation Matrix: Controlled Shed", "Day_Number")
