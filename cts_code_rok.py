
"""
Overview:
    This program helps automate the process of managing data from Excel files. 
    # It performs a series of tasks to ensure that the data is correctly opened, 
    filtered, and transferred into the CTS. The goal 
    is to save time and reduce manual errors.

Key Functions:
    - Set Up Logging: This function keeps track of what the program does. It 
      records important information, such as any errors that occur during 
      the process.
      
    - Check File: This function checks if the Excel file exists and if it 
      was created today. If the file is missing or outdated, the program will 
      not proceed.
      
    - Open Excel in Business Mode: This function opens the specified Excel 
      file and sets it to a business mode.
      
    - Apply Filter: This function applies a filter to the data in Excel. It 
      helps in narrowing down the information to what's needed for the task.
      
    - Copy Data: This function copies the relevant data from the Excel file, 
      making it ready for the next step.
      
    - Open CTS: This function opens the CTS where the data will be 
      transferred.
      
    - Get Credentials: This function retrieves the necessary login 
      information (username and password) needed to access the CTS system.
      
    - Insert Credentials: This function automatically inputs the login 
      information into the CTS system.
      
    - Copy Data to CTS: This function takes the copied data from Excel and 
      transfers it into the CTS system.

Usage:
    - Running the Program: When the program is started, it will go through 
      the above steps automatically. Users do not need to interact with it 
      once it begins.
      
    - Error Handling: If something goes wrong (like a missing file), the 
      program will log the issue for review.
"""
import pyautogui # For automating mouse clicks and keyboard inputs - https://pyautogui.readthedocs.io/en/latest/
import os # https://docs.python.org/3/library/os.html#os.getenv
import time
import pandas as pd
from datetime import datetime
import logging # https://docs.python.org/3/library/logging.html


# Set up logging 
def setup_logging(log_file = "file_check.log"):
    try:
        logging.basicConfig(filename=log_file,level=logging.INFO,
                        format="%(asctime)s - %(levelname)s - %(message)s") # Example : 2024-10-19 10:15:32,123 - INFO - Logging is set up.
        logging.info("Logging is set up.")
        
    except Exception as e:
        logging.error(f"Failed to set up logging. {e}")

# Checking if file exists and was created today
def check_file(file_path):
    try:
        if not os.path.exists(file_path):  # Insert file path
            logging.error("File does not exist.")
            return False  # Return False if file doesn't exist
                
        file_mod_time = datetime.fromtimestamp(os.path.getmtime(file_path))  # Insert file path
        today = datetime.now().date()
        
        if file_mod_time.date() != today:
            logging.error("File not from Today.")
            return False  # Return False if the file is not from today
            
        logging.info("File is valid and created today.")
        return True  # Return True if all checks pass
            
    except Exception as e:
        logging.error(f"Failed to check file existence or date. {e}")
        return False  # Return False if there's an exception

# Open Excel in Business Mode
def open_excel_in_business_mode(file_path):
    try:
        # Open the Excel file using pandas
        with pd.ExcelFile(file_path) as excel:
            # Load the specific sheet if needed (e.g., "Sheet1")
            df = pd.read_excel(excel, sheet_name="Sheet1")  # Replace with actual sheet name if different
            logging.info("Excel file opened successfully in read-only mode.")

        # Wait for a moment to ensure Excel is ready (if applicable)
        time.sleep(5)  
        
        # Simulate mouse clicks to select Business Mode
        business_mode_btn_x, business_mode_btn_y = 500, 300  
        pyautogui.click(x=business_mode_btn_x, y=business_mode_btn_y)
        logging.info("Business Mode selected.")
        
        return True  # Return True if business mode is selected successfully
        
    except Exception as e:
        logging.error(f"Failed to open Excel or select Business Mode. {e}")
        return False  # Return False if there's an exception
        
# Apply filter via mouse clicks
def apply_excel_filter():
    try:
        # Click on the filter dropdown button, column H
        filter_button_x, filter_button_y = 500, 300  # Replace with actual coordinates
        pyautogui.click(x=filter_button_x, y=filter_button_y)
        time.sleep(1)  # Wait 1 sec for the dropdown to open
        
        # Select in the dropdown menu
        checkbox_x, checkbox_y = 500, 400  # Replace with actual coordinates
        pyautogui.click(x=checkbox_x, y=checkbox_y)
        
        logging.info("Filter applied in Excel.")
        
    except Exception as e:
        logging.error(f"Failed to apply filter in Excel. {e}")

# Copy data from Excel
def copy_excel_data(file_path):
    try:
        # Context manager for opening the Excel file
        with pd.ExcelFile(file_path) as excel: # Insert file path
            df = pd.read_excel(excel, sheet_name="Sheet1", index = True, header= True)  # Assuming 'Sheet1' contains the data
            logging.info("Excel file loaded and data copied successfully.")
            
            return df  # Return the full DataFrame without filtering
            
    except Exception as e:
        logging.error(f"Failed to copy data from Excel. Error: {e}")
        
# Open CTS
def open_CTS():
    try:
        # Coordinates to the CTS (replace these with actual coordinates)
        system_icon_x, system_icon_y = 300, 400
        
        # Simulate a double-click 
        pyautogui.doubleClick(x=system_icon_x, y=system_icon_y)
        logging.info("CTS icon clicked.")

        # Wait for the system to load (adjust timing as needed)
        time.sleep(5)

    except Exception as e:
        logging.error(f"Failed to open CTS. {e}")

# Getting the username and password from separate file - check os documentation
def get_credentials_for_CTS():
    try:
        username = os.getenv("MY_USERNAME")
        password = os.getenv("MY_PASSWORD")
        server = os.getenv("SERVER")
        
        if username is None or password is None or server is None:
            logging.error("Username or Password not set up properly.")
               
        logging.info("Successfully retrieved username and password.")
        return username, password, server
    
    except Exception as e:
        logging.error(f"An error occurred, check your credentials.{e}")

# Inserting credentials
def insert_credentials_into_CTS(username,password,server):
    try:
      # Coordinates of the username field (replace with actual coordinates)
        username_field_x, username_field_y = 500, 400
        pyautogui.click(x=username_field_x, y=username_field_y)
        pyautogui.write(username)
        logging.info("Username entered.")

        # Coordinates of the password field (replace with actual coordinates)
        password_field_x, password_field_y = 500, 450
        pyautogui.click(x=password_field_x, y=password_field_y)
        pyautogui.write(password)
        logging.info("Password entered.")
        
        # Coordinates of the server field (replace with actual coordinates)
        server_field_x, server_field_y = 500, 450
        pyautogui.click(x=server_field_x, y=server_field_y)
        pyautogui.write(server)
        logging.info("Server entered.")

        # Coordinates of the login/submit button (replace with actual coordinates)
        login_btn_x, login_btn_y = 550, 500
        pyautogui.click(x=login_btn_x, y=login_btn_y)
        logging.info("Login button clicked.")

        # Wait for the system to log in
        time.sleep(5)
        
    except Exception as e:
        logging.error(f"An error occurred, check your inserted credentials.{e}")   
      
# Copy to CTS
def copy_excel_to_CTS(df):
    try:
        if df is None or df.empty:
            logging.warning("No data to copy to CTS.")
            
        # Iterate through each row in the DataFrame
        for index, row in df.iterrows():
            # Assume you need to click in a specific location for each field
            # Replace these coordinates with actual positions in the CTS interface
            
            # Example: Click on the field for the first data column
            field1_x, field1_y = 600, 400  # Replace with actual coordinates
            pyautogui.click(x=field1_x, y=field1_y)
            pyautogui.write(str(row['Column1']))  # Replace 'Column1' with the actual column name
            
            # Example: Click on the field for the second data column
            field2_x, field2_y = 600, 450  # Replace with actual coordinates
            pyautogui.click(x=field2_x, y=field2_y)
            pyautogui.write(str(row['Column2']))  # Replace 'Column2' with the actual column name
            
            # Example: Click the Submit or Next button to submit the row data
            submit_btn_x, submit_btn_y = 600, 500  # Replace with actual coordinates
            pyautogui.click(x=submit_btn_x, y=submit_btn_y)

            logging.info(f"Data from row {index + 1} copied to CTS.") # Start counting at 1

            # Wait for a moment before processing the next row
            time.sleep(1)  # Adjust time as needed

    except Exception as e:
        logging.error(f"Failed to copy data to CTS. Error: {e}")

def main():
    setup_logging()

    file_path = "your_file_path_here.xlsx"  # Specify actual file path
    logging.info("Starting the process...")

    # Check if the file exists and was created today
    if not check_file(file_path):
        logging.error("File check failed. Exiting the program.")
        return  # Exit if the file check fails

    if not open_excel_in_business_mode(file_path):
        logging.error("Failed to open Excel in Business Mode. Exiting the program.")
        return  # Exit if opening Excel fails
    
    apply_excel_filter()
    
    df = copy_excel_data(file_path)  # Capture the DataFrame returned by copy_excel_data
    if df is None:
        logging.error("Failed to copy data from Excel. Exiting the program.")
        return  # Exit if there's no data to work with

    open_CTS()

    username, password, server = get_credentials_for_CTS()  # Capture credentials
    if username is None or password is None or server is None:
        logging.error("Credentials retrieval failed. Exiting the program.")
        return  # Exit if credentials retrieval fails

    insert_credentials_into_CTS(username, password, server)

    copy_excel_to_CTS(df)  # Pass the DataFrame to the copy function

    logging.info("Process completed successfully.")


if __name__ == "__main__":
    main()
 