import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load merged data
data = pd.read_csv('public_transport_usage_cleaned.csv')

# Convert 'date' column to datetime
data['date'] = pd.to_datetime(data['date'])

# Dependency analysis
plt.figure(figsize=(14, 7))
sns.scatterplot(data=data, x='temperature', y='users', hue='region')
plt.title('Dependency of Number of Users on Temperature')
plt.xlabel('Temperature')
plt.ylabel('Number of Users')
plt.show()

# Select only numerical columns for correlation calculation
numeric_data = data.select_dtypes(include=[float, int])

# Correlation between weather conditions and transport usage
correlation_matrix = numeric_data.corr()
print(correlation_matrix['users'])
