import pandas as pd
import numpy as np
from scipy.stats import pearsonr
import statsmodels.api as sm
import csv

# Load the data from the uploaded CSV file
file_path = 'controlled_poultry_shed_data.csv'
data = pd.read_csv(file_path)

# Function to perform linear regression and return the summary
def perform_regression(x, y):
    x = sm.add_constant(x)  # Adds a constant term to the predictor
    model = sm.OLS(y, x).fit()
    return model.summary()

# Calculate Pearson correlation coefficients
correlations = {
    'Temperature vs Humidity': pearsonr(data['Temperature'], data['Humidity']),
    'Temperature vs Gas Level': pearsonr(data['Temperature'], data['Gas Level']),
    'Humidity vs Gas Level': pearsonr(data['Humidity'], data['Gas Level'])
}

# Perform linear regressions
regression_summaries = {
    'Temperature vs Humidity': perform_regression(data['Temperature'], data['Humidity']),
    'Temperature vs Gas Level': perform_regression(data['Temperature'], data['Gas Level']),
    'Humidity vs Gas Level': perform_regression(data['Humidity'], data['Gas Level'])
}

# Save the correlation coefficients to a CSV file
correlation_file_path = 'correlations.csv'
with open(correlation_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Pair', 'Pearson Correlation', 'P-value'])
    for pair, (corr, p_value) in correlations.items():
        writer.writerow([pair, corr, p_value])

# Print correlation results
print(f"Correlation results saved to {correlation_file_path}")

# Save the regression summaries to text files
for pair, summary in regression_summaries.items():
    file_name = pair.replace(' ', '_').replace('vs', 'vs_') + '_regression_summary.txt'
    with open(file_name, 'w') as f:
        f.write(str(summary))
    print(f"Regression summary for {pair} saved to {file_name}")
