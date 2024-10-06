# File Processing Project

## Description
This project aims to develop a Python program to efficiently extract key-value data from JSON format files located in directories created every day.
Each day's directory contains files identified by keys that are unique for that day. 
The program aims to extract data from these files based on certain criteria for the last 10 days.

## Structure
- `generate_data.py`: Generates test data.
- `'schema.py'`:  The schema.py file is a Python module used to define the structure of the JSON data to be used within the scope of the project.This module contains the necessary functions to check whether the JSON data conforms to the specified schema.
- `process_data.py`: Processes the generated data.
- `test_process_data.py`: Contains tests for the data processing functionality.
- `days/`: Directory containing daily data.
- `output/`: Directory for report files.

## Data Generation And Processing
The first command creates the data and the second command processes the data:
```bash
python generate_data.py

python process_data.py --ids fEg5U5OuNNMk 1UTIOOiUfg4h jUdoakFx9tPY 79CE3Hzda8E4 NB7DM0xP0NIk --attributes val_4 val_7 val_5
