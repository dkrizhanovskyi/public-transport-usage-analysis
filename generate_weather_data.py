import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(0)

# Dates over 3 years
dates = pd.date_range(start='2021-01-01', end='2023-12-31')

# Weather data generation
weather_data = {
    'date': dates,
    'temperature': np.random.normal(loc=15, scale=10, size=len(dates)),  # Average temperature with variation
    'precipitation': np.random.uniform(low=0, high=10, size=len(dates))  # Amount of precipitation
}

# Create DataFrame
df_weather = pd.DataFrame(weather_data)

# Save to CSV
df_weather.to_csv('weather_data.csv', index=False)

# Log message to file with correct encoding
with open('log.txt', 'a', encoding='utf-8') as f:
    f.write("Weather data successfully generated and saved in 'weather_data.csv'.\n")
