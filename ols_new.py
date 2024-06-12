import pandas as pd
import statsmodels.api as sm

# Read the data from the CSV file
controlled_data = pd.read_csv("controlled_poultry_shed_data.csv")

# Function to perform OLS regression and return summary
def ols_regression(dependent_var, independent_var, data):
    X = data[independent_var]
    Y = data[dependent_var]
    X = sm.add_constant(X)  # Add a constant term for the intercept
    model = sm.OLS(Y, X).fit()
    return model.summary()

# Perform OLS regression for each specified pair
temperature_vs_gas = ols_regression("Gas Level", "Temperature", controlled_data)
temperature_vs_humidity = ols_regression("Humidity", "Temperature", controlled_data)
humidity_vs_gas = ols_regression("Gas Level", "Humidity", controlled_data)

# Save the summaries to a text file
with open("img/ols_regression_summaries.txt", "w") as file:
    file.write("OLS Regression Analysis: Temperature vs Gas Level\n")
    file.write(temperature_vs_gas.as_text())
    file.write("\n\n")
    
    file.write("OLS Regression Analysis: Temperature vs Humidity\n")
    file.write(temperature_vs_humidity.as_text())
    file.write("\n\n")
    
    file.write("OLS Regression Analysis: Humidity vs Gas Level\n")
    file.write(humidity_vs_gas.as_text())
