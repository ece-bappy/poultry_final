import csv
import numpy as np

# Define the header
header = ["Hour", "Temperature", "Humidity", "Gas Level", "Day_Number"]

# Function to generate the temperature for a given hour
def generate_temperature(hour):
    if 7 <= hour <= 15:  # Increasing temperature from 7:00 to 15:00
        base_temp = 20.5 + (4 * (hour - 7) / 8)
    elif 16 <= hour <= 23:  # Decreasing temperature from 16:00 to 23:00
        base_temp = 24.5 - (4 * (hour - 16) / 8)
    elif 0 <= hour <= 6:  # Decreasing temperature from 0:00 to 6:00
        base_temp = 24.5 - (4 * (hour + 8) / 8)
    else:
        base_temp = 20.5  # Default in case of error

    # Add some random variation with a standard deviation of 0.7
    temperature = np.random.normal(base_temp, 0.7)
    return round(temperature, 2)

# Function to generate the humidity for a given hour
def generate_humidity(hour):
    if 0 <= hour <= 6:  # Decreasing humidity from 0:00 to 6:00
        base_humidity = 75 - (18 * hour / 6)
    elif 7 <= hour <= 15:  # Decreasing humidity from 7:00 to 15:00
        base_humidity = 75 - (18 * (hour - 6) / 8)
    elif 16 <= hour <= 23:  # Increasing humidity from 16:00 to 23:00
        base_humidity = 57 + (18 * (hour - 15) / 8)
    else:
        base_humidity = 57  # Default in case of error

    # Add some random variation with a standard deviation of 2.5
    humidity = np.random.normal(base_humidity, 2.5)
    return round(humidity, 2)

# Function to generate the gas level for a given hour
def generate_gas_level(hour):
    if 7 <= hour <= 15:  # Increasing gas level from 7:00 to 15:00
        base_gas = 17 + (3 * (hour - 7) / 8)
    elif 16 <= hour <= 23:  # Decreasing gas level from 16:00 to 23:00
        base_gas = 20 - (3 * (hour - 16) / 8)
    elif 0 <= hour <= 6:  # Decreasing gas level from 0:00 to 6:00
        base_gas = 20 - (3 * (hour + 8) / 8)
    else:
        base_gas = 17  # Default in case of error

    # Add some random variation with a standard deviation of 0.45
    gas_level = np.random.normal(base_gas, 0.45)
    return round(gas_level, 2)

# Create the data
data = []

for day in range(1, 36):
    for hour in range(24):
        time = f"{hour}:00"
        temperature = generate_temperature(hour)
        humidity = generate_humidity(hour)
        gas_level = generate_gas_level(hour)
        data.append([time, temperature, humidity, gas_level, day])

# Create and write to the CSV file
with open('temperature_humidity_gas_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(data)

print("temperature_humidity_gas_data.csv has been created with the specified headings and data.")
