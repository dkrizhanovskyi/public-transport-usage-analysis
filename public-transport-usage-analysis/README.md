# Public Transport Usage Analysis

This project analyzes and forecasts public transport usage in various regions of Switzerland.

## Project Structure

1. Data Generation:
    - `generate_data.py`: Generates public transport usage data.
    - `generate_weather_data.py`: Generates weather data.

2. Data Preparation:
    - `01_data_preparation.py`: Merges and prepares the data for analysis.

3. Dependency Analysis:
    - `02_dependency_analysis.py`: Analyzes the dependency of transport usage on weather conditions.

4. User Segmentation:
    - `03_user_segmentation.py`: Segments users based on transport usage patterns.

5. Demand Prediction:
    - `04_demand_prediction.py`: Trains a neural network model to forecast transport usage.

6. Visualization:
    - `05_visualization.py`: Visualizes the forecasted number of users.

7. Documentation:
    - `06_documentation.py`: Generates a project report.

8. Automation:
    - `run_project.py`: Automates the execution of all project steps.

9. Dashboard:
    - `dashboard.py`: Streamlit dashboard for interactive visualization.

## How to Run

1. Install the necessary libraries:
   ```bash
   pip install seaborn scikit-learn joblib streamlit tensorflow
2. Run the automated script:
   ```bash
   python run_project.py
3. Launch the Streamlit application:
   ```bash
   streamlit run dashboard.py

## Results
The project provides insights into public transport usage and forecasts future demand based on historical data and weather conditions.


## Authors
Daniil Krizhanovskyi