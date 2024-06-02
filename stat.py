import csv
import numpy as np
import pandas as pd

# Load the data from the CSV file
data = pd.read_csv('temperature_humidity_gas_data.csv')

# List to store the statistical analysis results
results = []

# Function to calculate statistical measures for a given parameter (temperature, humidity, or gas level)
def calculate_statistics(parameter):
    stats = {}
    stats['Mean'] = np.mean(parameter)
    stats['Std Deviation'] = np.std(parameter)
    stats['Minimum'] = np.min(parameter)
    stats['Maximum'] = np.max(parameter)
    return stats

# Iterate over each day
for day in range(1, 36):
    # Filter data for the current day
    day_data = data[data['Day_Number'] == day]
    
    # Extract temperature, humidity, and gas level data for the current day
    temperatures = day_data['Temperature']
    humidities = day_data['Humidity']
    gas_levels = day_data['Gas Level']
    
    # Calculate statistics for temperature, humidity, and gas level
    temp_stats = calculate_statistics(temperatures)
    humidity_stats = calculate_statistics(humidities)
    gas_level_stats = calculate_statistics(gas_levels)
    
    # Add day number to statistics
    temp_stats['Day_Number'] = day
    humidity_stats['Day_Number'] = day
    gas_level_stats['Day_Number'] = day
    
    # Append statistics to the results list
    results.append(temp_stats)
    results.append(humidity_stats)
    results.append(gas_level_stats)

# Define the header for the CSV file
header = ['Day_Number', 'Parameter', 'Mean', 'Std Deviation', 'Minimum', 'Maximum']

# Write the results to a CSV file
with open('statistical_analysis.csv', mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=header)
    
    # Write the header
    writer.writeheader()
    
    # Write the statistics for each parameter for each day
    for result in results:
        writer.writerow(result)

print("Statistical analysis saved in statistical_analysis.csv.")
