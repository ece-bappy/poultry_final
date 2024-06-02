import csv
import matplotlib.pyplot as plt

# Load data from CSV file
hours = []
temperatures = []
days = []

with open('data.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        hours.append(row['Hour'])
        temperatures.append(float(row['Temperature']))
        days.append(int(row['Day_Number']))

# Plot each day's temperature curve
unique_days = set(days)
for day in unique_days:
    day_temperatures = [temp for temp, d, h in zip(temperatures, days, hours) if d == day]
    day_hours = [h for d, h in zip(days, hours) if d == day]
    plt.plot(day_hours, day_temperatures, label=f"Day {day}")

# Add labels and legend
plt.xlabel('Hour')
plt.ylabel('Temperature')
plt.title('Temperature Variation by Day')
plt.legend()

# Use logarithmic scale for the y-axis
plt.yscale('log')

# Show plot
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()  # Adjust layout to prevent overlapping labels
plt.show()
