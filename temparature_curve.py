import csv
import matplotlib.pyplot as plt
import pandas as pd

# Read the data from the CSV file
data = pd.read_csv('temperature_humidity_gas_data.csv')

# Plot Temperature in a separate window
plt.figure(figsize=(10, 6))
for day in data['Day_Number'].unique():
    day_data = data[data['Day_Number'] == day]
    plt.plot(day_data['Hour'], day_data['Temperature'], label=f'Day {day}')
plt.title('Hourly Temperature for 35 Days')
plt.xlabel('Hour')
plt.ylabel('Temperature (°C)')
plt.legend(loc='upper right', bbox_to_anchor=(1.15, 1))
plt.show()

# Plot Humidity in a separate window
plt.figure(figsize=(10, 6))
for day in data['Day_Number'].unique():
    day_data = data[data['Day_Number'] == day]
    plt.plot(day_data['Hour'], day_data['Humidity'], label=f'Day {day}')
plt.title('Hourly Humidity for 35 Days')
plt.xlabel('Hour')
plt.ylabel('Humidity (%)')
plt.legend(loc='upper right', bbox_to_anchor=(1.15, 1))
plt.show()

# Plot Gas Level in a separate window
plt.figure(figsize=(10, 6))
for day in data['Day_Number'].unique():
    day_data = data[data['Day_Number'] == day]
    plt.plot(day_data['Hour'], day_data['Gas Level'], label=f'Day {day}')
plt.title('Hourly Gas Level for 35 Days')
plt.xlabel('Hour')
plt.ylabel('Gas Level')
plt.legend(loc='upper right', bbox_to_anchor=(1.15, 1))
plt.show()
