import pandas as pd
import scipy.stats as stats

# Read the data from the CSV files
traditional_data = pd.read_csv("traditional_poultry_shed_data.csv")
controlled_data = pd.read_csv("controlled_poultry_shed_data.csv")


# Function to return descriptive statistics as a string
def get_descriptive_stats(data, label):
    stats_str = f"Descriptive statistics for {label}:\n{data.describe()}\n\n"
    return stats_str


# Initialize a string to hold the entire summary
summary = ""

# Descriptive statistics
summary += get_descriptive_stats(traditional_data, "Traditional Environment")
summary += get_descriptive_stats(controlled_data, "Controlled Environment")

# T-tests
parameters = ["Temperature", "Humidity", "Gas Level"]
for parameter in parameters:
    t_stat, p_value = stats.ttest_ind(
        traditional_data[parameter], controlled_data[parameter], equal_var=False
    )
    summary += f"T-test for {parameter}:\n"
    summary += f"t-statistic: {t_stat}, p-value: {p_value}\n\n"

# Save the summary to a text file
with open("analysis_summary.txt", "w") as file:
    file.write(summary)
