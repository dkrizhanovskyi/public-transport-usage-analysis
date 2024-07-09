import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input
from tensorflow.keras.callbacks import EarlyStopping
from sklearn.metrics import mean_squared_error
import joblib
import json
import sys

# Set stdout encoding
sys.stdout.reconfigure(encoding='utf-8')

# Load data
data = pd.read_csv('public_transport_usage_cleaned.csv')

# Convert 'date' column to datetime
data['date'] = pd.to_datetime(data['date'])

# Add additional features
data['day_of_week'] = data['date'].dt.dayofweek
data['month'] = data['date'].dt.month
data['year'] = data['date'].dt.year

# Save original 'region' and 'transport_type' values
data['original_region'] = data['region']
data['original_transport_type'] = data['transport_type']

# Select features and target variable
features = ['day_of_week', 'month', 'year']
data = pd.get_dummies(data, columns=['region', 'transport_type'])
X = data[features + [col for col in data.columns if col.startswith('region_') or col.startswith('transport_type_')]]
y = data['users']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Create neural network model
model = Sequential()
model.add(Input(shape=(X_train_scaled.shape[1],)))
model.add(Dense(128, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(1))

model.compile(optimizer='adam', loss='mse')

# Train model with early stopping
early_stopping = EarlyStopping(patience=10, restore_best_weights=True)
history = model.fit(X_train_scaled, y_train, validation_split=0.2, epochs=100, callbacks=[early_stopping], verbose=1)

# Predict and evaluate model
y_pred = model.predict(X_test_scaled)
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

# Save model and scaler
model.save('demand_prediction_model.keras')
joblib.dump(scaler, 'scaler.pkl')

# Save MSE to file
with open('mse.json', 'w') as f:
    json.dump({'mse': mse}, f)

# Forecast future demand
future_dates = pd.date_range(start='2024-01-01', periods=365)
regions = ['Zurich', 'Geneva', 'Basel', 'Bern', 'Lausanne']
transport_types = ['Train', 'Bus', 'Tram', 'Boat']

future_data = []

for date in future_dates:
    for region in regions:
        for transport in transport_types:
            future_data.append([date, date.dayofweek, date.month, date.year, region, transport])

future_df = pd.DataFrame(future_data, columns=['date', 'day_of_week', 'month', 'year', 'region', 'transport_type'])
original_regions = future_df['region']
original_transport_types = future_df['transport_type']
future_df = pd.get_dummies(future_df, columns=['region', 'transport_type'])

# Align columns with training data
for col in X.columns:
    if col not in future_df.columns:
        future_df[col] = 0

# Scale future data for predictions
future_df_scaled = scaler.transform(future_df[X.columns])

# Predict
predictions = model.predict(future_df_scaled)
future_df['predicted_users'] = predictions
future_df['region'] = original_regions
future_df['transport_type'] = original_transport_types
future_df.to_csv('predicted_future_data.csv', index=False)
print(future_df[['date', 'region', 'transport_type', 'predicted_users']])
