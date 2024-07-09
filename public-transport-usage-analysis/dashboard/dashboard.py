import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Load forecast data
data = pd.read_csv('predicted_future_data.csv')

# Application title
st.title("Public Transport Usage Forecast Dashboard")

# Data filters
region = st.selectbox("Select Region", ['Zurich', 'Geneva', 'Basel', 'Bern', 'Lausanne'])
transport_type = st.selectbox("Select Transport Type", ['Train', 'Bus', 'Tram', 'Boat'])

# Prepare filters
region_col = f'region_{region}'
transport_col = f'transport_type_{transport_type}'

# Check for column existence
if region_col not in data.columns or transport_col not in data.columns:
    st.error(f"Data for {region} and {transport_type} is not available.")
else:
    # Filter data
    filtered_data = data[(data[region_col] == 1) & (data[transport_col] == 1)]

    if filtered_data.empty:
        st.warning(f"No data available for {region} and {transport_type}.")
    else:
        # Visualize data
        st.subheader(f"Predicted Number of Users for {transport_type} in {region}")

        fig, ax = plt.subplots()
        ax.plot(filtered_data['date'], filtered_data['predicted_users'])
        ax.set_title(f"Predicted Users of {transport_type} in {region}")
        ax.set_xlabel("Date")
        ax.set_ylabel("Number of Users")

        # Adjust tick frequency and rotation
        plt.xticks(ticks=plt.xticks()[0][::30], rotation=45)  # Set ticks every 30 days

        st.pyplot(fig)

        # Display data table
        st.subheader("Data Table")
        st.write(filtered_data[['date', 'predicted_users']])

        # Add download button for data
        csv = filtered_data[['date', 'predicted_users']].to_csv(index=False)
        st.download_button(
            label="Download data as CSV",
            data=csv,
            file_name='predicted_users.csv',
            mime='text/csv',
        )
