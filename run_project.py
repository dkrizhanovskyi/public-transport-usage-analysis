import subprocess
import sys

# Set stdout encoding
sys.stdout.reconfigure(encoding='utf-8')

def run_command(command):
    """Function to execute a command in the command line."""
    print(f"Running command: {command}")
    result = subprocess.run(command, shell=True, text=True, capture_output=True, encoding='utf-8')
    print(result.stdout)
    if result.returncode != 0:
        print(result.stderr)
        raise Exception(f"Command '{command}' returned non-zero exit status {result.returncode}.")
    print("Command executed successfully.\n")

def main():
    try:
        # Install necessary libraries if not already installed
        run_command("pip install seaborn scikit-learn joblib streamlit tensorflow")

        # Project steps
        run_command("python generate_data.py")
        run_command("python generate_weather_data.py")
        run_command("python 01_data_preparation.py")
        run_command("python 02_dependency_analysis.py")
        run_command("python 03_user_segmentation.py")
        run_command("python 04_demand_prediction.py")
        run_command("python 05_visualization.py")
        run_command("python 06_documentation.py")

        # Read and print the log file
        with open('log.txt', 'r', encoding='utf-8') as f:
            print(f.read())

        print("Project execution completed successfully.")

    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    main()
