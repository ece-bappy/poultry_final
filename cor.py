import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read the data from the CSV files
traditional_data = pd.read_csv("traditional_poultry_shed_data.csv")
controlled_data = pd.read_csv("controlled_poultry_shed_data.csv")


# Function to plot correlation heatmap and save correlation matrix to a text file
def plot_correlation_heatmap_and_save(data, title, drop_column, filename):
    # Drop the specified column and select only numeric columns
    numeric_data = data.drop(columns=[drop_column]).select_dtypes(include=[float, int])
    # Compute the correlation matrix
    corr_matrix = numeric_data.corr()

    # Save the correlation matrix to a text file
    with open(filename, "w") as f:
        f.write(f"Correlation Matrix: {title}\n")
        f.write(corr_matrix.to_string())

    # Plot the correlation heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap="viridis", vmin=-1, vmax=1)
    plt.title(title)
    plt.show()


# Plot correlation heatmap and save correlation matrix for traditional environment
plot_correlation_heatmap_and_save(
    traditional_data,
    "Correlation Matrix: Traditional Shed",
    "Day_Number",
    "traditional_shed_correlation.txt",
)

# Plot correlation heatmap and save correlation matrix for controlled environment
plot_correlation_heatmap_and_save(
    controlled_data,
    "Correlation Matrix: Controlled Shed",
    "Day_Number",
    "controlled_shed_correlation.txt",
)
