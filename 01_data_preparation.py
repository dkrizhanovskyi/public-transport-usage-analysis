import pandas as pd

def load_and_prepare_data():
    # Load data
    transport_data = pd.read_csv('public_transport_usage.csv')
    weather_data = pd.read_csv('weather_data.csv')

    # Convert 'date' column to datetime
    transport_data['date'] = pd.to_datetime(transport_data['date'])
    weather_data['date'] = pd.to_datetime(weather_data['date'])

    # Merge data by date
    merged_data = pd.merge(transport_data, weather_data, on='date')

    # Save merged data
    merged_data.to_csv('public_transport_usage_cleaned.csv', index=False)
    # Log message to file with correct encoding
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write("Data successfully merged and saved in 'public_transport_usage_cleaned.csv'.\n")

load_and_prepare_data()
