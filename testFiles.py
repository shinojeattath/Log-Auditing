# test_files.py
import time
from datetime import datetime
import os

def create_test_log_files():
    while True: 
        try:
            current_time = datetime.now()
            date_str = current_time.strftime("%Y%m%d%H%M%S")
            

            # Create test log files
            apps = ['app1', 'app2', 'app3']
            for app in apps:
                filename = f"{app}_logs_{date_str}.logs"
                filepath = os.path.join('Source', filename)
                
                with open(filepath, 'w') as f:
                    f.write(f"Test log content created at: {current_time}")
                
                print(f"Created log file: {filename}")
            
            print("Waiting 60 seconds before creating next set of files...")
            time.sleep(60) 
            
        except Exception as e:
            print(f"Error creating log files: {e}")
            time.sleep(10) 

if __name__ == "__main__":
    os.makedirs('Source', exist_ok=True)
    create_test_log_files()