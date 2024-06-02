import csv
import numpy as np

# Define the header
header = ["Hour", "Temperature", "Humidity", "Gas Level", "Day_Number"]


# Function to generate the temperature for a given hour
def generate_temperature(hour):
    if 6 <= hour <= 15:  # Increasing temperature from 6:00 to 15:00
        base_temp = 18 + (2 * (hour - 6) / 10)
    elif 16 <= hour <= 23:  # Decreasing temperature from 16:00 to 23:00
        base_temp = 20 - (2 * (hour - 16) / 8)
    elif 0 <= hour <= 5:  # Decreasing temperature from 0:00 to 5:00
        base_temp = 20 - (2 * (hour + 8) / 14)
    else:
        base_temp = 18  # Default in case of error

    # Add some random variation with a standard deviation of 0.3
    temperature = np.random.normal(base_temp, 0.9)
    return round(temperature, 2)


# Function to generate the humidity for a given hour
# Function to generate the humidity for a given hour
def generate_humidity(hour):
    # Define the parameters for the sine function
    amplitude = 8  # Amplitude of the sine wave
    period = 24  # Period of the sine wave (in hours)
    phase_shift = 0  # Phase shift of the sine wave (in hours) to peak at 6 AM
    base_humidity = 55  # Base humidity level

    # Calculate humidity using a sine function
    humidity = base_humidity + amplitude * np.sin(
        2 * np.pi * (hour - phase_shift) / period
    )

    # Add some random variation with a standard deviation of 2.5
    humidity = np.random.normal(humidity, 4)

    # Ensure humidity is within reasonable bounds (0 to 100)
    humidity = max(0, min(100, humidity))

    return round(humidity, 2)


# Function to generate the gas level for a given hour
def generate_gas_level(hour):
    if 6 <= hour <= 15:  # Increasing gas level from 6:00 to 15:00
        base_gas = 20 + (16 * (hour - 6) / 10)
    elif 16 <= hour <= 23:  # Decreasing gas level from 16:00 to 23:00
        base_gas = 36 - (16 * (hour - 16) / 8)
    elif 0 <= hour <= 5:  # Decreasing gas level from 0:00 to 5:00
        base_gas = 36 - (16 * (hour + 8) / 14)
    else:
        base_gas = 20  # Default in case of error

    # Add some random variation with a standard deviation of 1
    gas_level = np.random.normal(base_gas, 4)
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
with open("traditional_poultry_shed_data.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(data)

print(
    "traditional_poultry_shed_data.csv has been created with the specified headings and data."
)
