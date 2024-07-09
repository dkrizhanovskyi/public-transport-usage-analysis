import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv('public_transport_usage_cleaned.csv')

# Convert 'date' column to datetime
data['date'] = pd.to_datetime(data['date'])

# Add additional features
data['day_of_week'] = data['date'].dt.dayofweek
data['month'] = data['date'].dt.month
data['year'] = data['date'].dt.year

# Select features for clustering
features = ['users', 'day_of_week', 'month', 'year']
X = data[features]

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Clustering using KMeans
kmeans = KMeans(n_clusters=4, random_state=42)
data['cluster'] = kmeans.fit_predict(X_scaled)

# Visualize clusters
plt.figure(figsize=(14, 7))
sns.scatterplot(data=data, x='date', y='users', hue='cluster', palette='viridis')
plt.title('User Clusters Based on Transport Usage')
plt.xlabel('Date')
plt.ylabel('Number of Users')
plt.show()
