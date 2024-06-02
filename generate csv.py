import csv
import random

# Define the header
header = ["Hour", "Temperature", "Humidity", "Gas Level", "Day_Number"]

# Function to generate temperature trend across multiple steps
def generate_group_temperatures(start_temp, end_temp, steps):
    step = (start_temp - end_temp) / (steps - 1)
    return [round(start_temp - step * i, 2) for i in range(steps)]

# Create the data
data = []
minutes_increments = [0, 15, 30, 45]
hours_per_day = 24
days = 35
total_steps_per_day = len(minutes_increments) * hours_per_day * days

# Define temperature ranges for each group of hours
temperature_ranges = [
    (22.99, 22.55),  # 0 to 3
    (22.55, 22.45),  # 3 to 6
    (22.45, 22.60),  # 6 to 9
    (22.60, 23.45),  # 9 to 11
    (23.60, 25.40),  # 11 to 15
    (25.20, 24.80),  # 15 to 19
    (24.00, 23.20)   # 19 to 23
]

# Generate temperatures for each hour segment and repeat for each day
adjusted_temperatures = []
for start_temp, end_temp in temperature_ranges:
    group_temps = generate_group_temperatures(start_temp, end_temp, len(minutes_increments) * 3)
    adjusted_temperatures.extend(group_temps)

# Extend the temperature list to cover all days
while len(adjusted_temperatures) < total_steps_per_day:
    adjusted_temperatures *= 2

# Truncate the list if it exceeds the required length
adjusted_temperatures = adjusted_temperatures[:total_steps_per_day]

# Fill the data for each day
index = 0
for day in range(1, days + 1):
    for hour in range(hours_per_day):
        for minute in minutes_increments:
            time = f"{hour}:{minute:02d}"
            temperature = adjusted_temperatures[index]
            data.append([time, f"{temperature:.2f}", "", "", day])
            index += 1

# Create and write to the CSV file
with open('data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(data)

print("data.csv has been created with the specified headings and data.")
