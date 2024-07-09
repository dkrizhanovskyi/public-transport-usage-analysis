import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(0)

# Dates over 3 years
dates = pd.date_range(start='2021-01-01', end='2023-12-31')

# Regions and transport types
regions = ['Zurich', 'Geneva', 'Basel', 'Bern', 'Lausanne']
transport_types = ['Train', 'Bus', 'Tram', 'Boat']

# Data generation
data = []
for date in dates:
    for region in regions:
        for transport in transport_types:
            # Ensure data for all combinations of regions and transport types
            users = np.random.poisson(lam=1000)  # Average number of users
            data.append([date, region, transport, users])

# Create DataFrame
df = pd.DataFrame(data, columns=['date', 'region', 'transport_type', 'users'])

# Save to CSV
df.to_csv('public_transport_usage.csv', index=False)

# Log message to file with correct encoding
with open('log.txt', 'a', encoding='utf-8') as f:
    f.write("Data successfully generated and saved in 'public_transport_usage.csv'.\n")
