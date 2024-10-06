import os
import json
import argparse
from datetime import datetime, timedelta


def get_last_n_days(n):
    """
        Retrieve a list of the last n days in the format 'yymmdd'.

        Args:
            n (int): The number of days to retrieve.

        Returns:
            list: A list of strings representing the last n days.
    """
    today = datetime.now()
    return [(today - timedelta(days=i)).strftime("%y%m%d") for i in range(n)]


def process_data(ids, attributes):
    """
        Process and filter records from JSON files based on specified IDs and attributes.

        This function scans through a predefined set of directories (named with date codes)
        to retrieve records from JSON files. It filters these records to include only those
        with IDs that match the provided list and extracts specified attributes from each record.

        Args:
            ids (list): A list of IDs to filter the records. Only records with IDs in this list will be processed.
            attributes (list): A list of attribute names to extract from each record. If an attribute
                               is not found in a record, a warning is printed.

        Returns:
            list: A list of dictionaries, each containing the 'id' and selected attributes from
                  the matching records. If no records match the provided IDs, an empty list is returned.

        Notes:
            - The function checks for the existence of directories formatted as 'YYMMDD' within
              the 'days_test/' directory.
    """
    output_data = []

    days = ['220402', '220403', '220404', '220405', '220406',
            '220407', '220408', '220409', '220410', '220411']

    for day in days:
        day_path = f"days/{day}"
        if not os.path.exists(day_path):
            continue

        for filename in os.listdir(day_path):
            with open(os.path.join(day_path, filename), 'r') as file:
                for line in file:
                    record = json.loads(line)
                    if record['id'] in ids:
                        selected_attributes = {}
                        for attr in attributes:
                            if attr in record['attributes']:

                                selected_attributes[attr] = record['attributes'][attr]
                            else:
                                print(f"Warning: Attribute '{attr}' not found in record.")

                        output_data.append({**{'id': record['id']}, **selected_attributes})

    return output_data


def write_report(output_data):
    """
        Write the output data to a text file in JSON format.

        Args:
            output_data (list): A list of dictionaries to be written to the report file.

        The report file is saved in the 'output' directory with a timestamped filename.
    """
    output_filename = f"output/report_file_{datetime.now().strftime('%y%m%d%H%M%S')}.txt"
    with open(output_filename, 'w') as report_file:
        for item in output_data:
            report_file.write(json.dumps(item) + "\n")


def main():
    """
        Parse command-line arguments and process key-value data.

        Requires a list of IDs (max 10) and attributes (max 5) to search for and include.
        Processes the data and writes the output to a report file.
    """
    parser = argparse.ArgumentParser(description='Process key-value data.')
    parser.add_argument('--ids', type=str, nargs='+', help='List of IDs to search for (max 10)', required=True)
    parser.add_argument('--attributes', type=str, nargs='+', help='List of attribute IDs to include (max 5)',
                        required=True)

    args = parser.parse_args()

    # Limit arguments
    ids = args.ids[:10]
    if len(ids) > 5:
        print("Max ID limit is 5.")
        return
    attributes = args.attributes[:5]

    print("IDs:", ids)
    print("Attributes:", attributes)
    print("File scan started.")
    output_data = process_data(ids, attributes)
    write_report(output_data)
    print("Report File created.")

if __name__ == "__main__":
    main()
