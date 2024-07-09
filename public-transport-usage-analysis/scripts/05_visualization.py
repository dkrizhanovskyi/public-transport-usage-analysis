import pandas as pd
import matplotlib.pyplot as plt

# Load forecast data
future_data = pd.read_csv('predicted_future_data.csv')

# Visualize forecasted number of public transport users
plt.figure(figsize=(12, 6))
plt.plot(future_data['date'], future_data['predicted_users'])
plt.title('Forecasted Number of Public Transport Users')
plt.xlabel('Date')
plt.ylabel('Number of Users')
plt.grid(True)

# Adjust tick frequency and rotation
plt.xticks(ticks=plt.xticks()[0][::30], rotation=45)  # Set ticks every 30 days

plt.show()
