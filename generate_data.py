import os
import json
import random
import string

from schema import schema


def generate_random_id(length=12):
    """
        Generate a random ID string of specified length.

        Args:
            length (int): Length of the generated ID. Default is 12.

        Returns:
            str: A random string of alphanumeric characters.
        """
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


def generate_random_attributes():
    """
        Generate a dictionary of random attributes.

        Returns:
            dict: A dictionary with keys 'val_0' to 'val_9' and random string values.
        """
    return {f"val_{i}": generate_random_id(8) for i in range(10)}


def validate_record(record):
    """
        Validate a record against the defined schema.

        Args:
            record (dict): The record to validate.

        Returns:
            bool: True if the record is valid, False otherwise.
        """
    # Validate ID
    if not isinstance(record.get("id"), str):
        return False
    if not (1 <= len(record["id"]) <= 64):
        return False

    # Validate attributes
    attributes = record.get("attributes")
    if not isinstance(attributes, dict):
        return False

    # Check required attributes
    for key in schema["properties"]["attributes"]["required"]:
        if key not in attributes or not isinstance(attributes[key], str):
            return False

    return True


def generate_data_for_day(day, num_files=40, records_per_file=500000):
    """
       Generate data files for a specified day with random records.

       Args:
           day (str): The day for which to generate data (used as a directory name).
           num_files (int): Number of files to create. Default is 40.
           records_per_file (int): Number of records per file. Default is 500,000.

       Creates:
           A directory named after the specified day, containing the generated data files.
    """
    os.makedirs(f"days/{day}", exist_ok=True)
    for i in range(1, num_files + 1):
        with open(f"days/{day}/file{i}.txt", "w") as f:
            for _ in range(records_per_file):
                record = {
                    "id": generate_random_id(),
                    "attributes": generate_random_attributes()
                }
                if validate_record(record):
                    f.write(json.dumps(record) + "\n")
                else:
                    print("Invalid registration:", record)


def main():
    """
        Generate data files for a predefined list of days.

        Iterates over a list of day strings and calls `generate_data_for_day`
        for each day to create the corresponding data files.
    """
    days = ['220402', '220403', '220404', '220405', '220406',
            '220407', '220408', '220409', '220410', '220411']
    for day in days:
        generate_data_for_day(day)


if __name__ == "__main__":
    main()
