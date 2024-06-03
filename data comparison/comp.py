import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import seaborn as sns

# Read the data from the CSV files
traditional_data = pd.read_csv("traditional_poultry_shed_data.csv")
controlled_data = pd.read_csv("controlled_poultry_shed_data.csv")


# Function to print descriptive statistics
def print_descriptive_stats(data, label):
    print(f"Descriptive statistics for {label}:")
    print(data.describe())
    print("\n")


# Descriptive statistics
print_descriptive_stats(traditional_data, "Traditional Environment")
print_descriptive_stats(controlled_data, "Controlled Environment")

# T-tests
parameters = ["Temperature", "Humidity", "Gas Level"]
for parameter in parameters:
    t_stat, p_value = stats.ttest_ind(
        traditional_data[parameter], controlled_data[parameter], equal_var=False
    )
    print(f"T-test for {parameter}:")
    print(f"t-statistic: {t_stat}, p-value: {p_value}")
    print("\n")

# Box plots
plt.figure(figsize=(14, 6))
for i, parameter in enumerate(parameters):
    plt.subplot(1, 3, i + 1)
    sns.boxplot(
        data=[traditional_data[parameter], controlled_data[parameter]],
        palette=["blue", "green"],
    )
    plt.title(f"Box Plot of {parameter}")
    plt.xticks([0, 1], ["Traditional", "Controlled"])
plt.tight_layout()
plt.savefig("img_t/box_plots.png", dpi=300)
plt.close()

# Histograms
plt.figure(figsize=(14, 6))
for i, parameter in enumerate(parameters):
    plt.subplot(1, 3, i + 1)
    sns.histplot(
        traditional_data[parameter],
        color="blue",
        label="Traditional",
        kde=True,
        stat="density",
    )
    sns.histplot(
        controlled_data[parameter],
        color="green",
        label="Controlled",
        kde=True,
        stat="density",
    )
    plt.title(f"Histogram of {parameter}")
    plt.legend()
plt.tight_layout()
plt.savefig("img/histograms.png", dpi=300)
plt.close()
