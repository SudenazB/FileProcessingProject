# File Processing Project

## Description
This project aims to develop a Python program to efficiently extract key-value data from JSON format files located in directories created every day.
Each day's directory contains files identified by keys that are unique for that day. 
The program aims to extract data from these files based on certain criteria for the last 10 days.

## Structure
- `generate_data.py`: Creates test data. It is configured to contain 40 files for each day and 500,000 records in each file.
- `'schema.py'`:  The schema.py file is a Python module used to define the structure of the JSON data to be used within the scope of the project.This module contains the necessary functions to check whether the JSON data conforms to the specified schema.
- `process_data.py`: It reads files, processes JSON data, and searches with parameters received from the user.
- `test_process_data.py`: Creates test cases using unittest framework to verify functionality.
- `days/`: Directory containing daily data.
- `output/`: Directory for report files.

## Data Generation And Processing
The first command creates the data and the second command processes the data:
```bash
python generate_data.py

python process_data.py --ids S2VgWYt2RC2c TdmKvf86G97y TdmKvf86G97y 2OXS6gLzRHNh S2VgWYt2RC2c TdmKvf86G97y TdmKvf86G97y 2OXS6gLzRHNh S2VgWYt2RC2c TdmKvf86G97y TdmKvf86G97y 2OXS6gLzRHNh --attributes val_4 val_7 val_0 val_1 val_8 val_2 val_3
