# test_files.py
import time
from datetime import datetime
import os

def create_test_log_files():
    while True:  # Run infinitely
        try:
            # Get current timestamp
            current_time = datetime.now()
            date_str = current_time.strftime("%Y%m%d")
            
            # Create test log files
            apps = ['app1', 'app2', 'app3']  # You can add more apps
            
            for app in apps:
                # Create filename with current date
                filename = f"{app}_logs_{date_str}.logs"
                filepath = os.path.join('Source', filename)
                
                # Create file with timestamp content
                with open(filepath, 'w') as f:
                    f.write(f"Test log content created at: {current_time}")
                
                print(f"Created log file: {filename}")
            
            # Wait for 60 seconds before creating next set of files
            print("Waiting 60 seconds before creating next set of files...")
            time.sleep(60)  # Adjust this time as needed
            
        except Exception as e:
            print(f"Error creating log files: {e}")
            time.sleep(10)  # Wait before retrying if there's an error

if __name__ == "__main__":
    # Create Source directory if it doesn't exist
    os.makedirs('Source', exist_ok=True)
    
    print("Starting continuous log file creation...")
    create_test_log_files()