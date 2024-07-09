import json

def generate_report():
    # Load MSE from file
    with open('mse.json', 'r') as f:
        mse_data = json.load(f)
        mse = mse_data['mse']
        model_name = "Neural Network"

    with open('project_report.txt', 'w', encoding='utf-8') as file:
        file.write("Project Report on Public Transport Usage Analysis in Switzerland\n")
        file.write("=============================================================\n\n")
        
        file.write("Project Description:\n")
        file.write("Project Goal: Analyze and forecast public transport usage in various regions of Switzerland.\n\n")
        
        file.write("Data and Processing:\n")
        file.write("We used data on public transport users in different regions and transport types.\n")
        file.write("The data was cleaned, transformed, and saved in the file 'public_transport_usage_cleaned.csv'.\n\n")
        
        file.write("Dependency Analysis:\n")
        file.write("We analyzed the dependency of public transport usage on weather conditions.\n\n")
        
        file.write("User Segmentation:\n")
        file.write("We performed user segmentation based on usage patterns.\n\n")
        
        file.write("Demand Prediction:\n")
        file.write(f"The {model_name} model showed the best performance with a Mean Squared Error (MSE) of {mse:.2f}.\n\n")
        
        file.write("Forecasting and Results:\n")
        file.write(f"Forecasting of the number of users for the future was done using the optimized {model_name} model.\n")
        file.write("The forecasting results were saved and visualized.\n\n")
        
        file.write("End of Report.\n")

generate_report()
