import unittest
from process_data import process_data, write_report


class TestProcessData(unittest.TestCase):
    """
        Unit test class for processing data in the `process_data` function.

        Tests the correctness of the `process_data` function by verifying
        the structure and contents of the processed data against expected
        IDs and attributes.
    """

    def test_process_data(self):
        """
         Test the `process_data` function for valid IDs and attributes.

         This method verifies that the output of the `process_data` function
         is structured correctly. It checks that the result is a list of
         dictionaries, each containing an 'id' field that matches one of
         the expected IDs, and includes all specified attributes.

         It also writes the result to a report file for further inspection.
         """
        ids = ["9RkDT3JtSgqV", "NjDI9dg1J9Uq", "k1y0dQpRIWrU"]
        attributes = ["val_0", "val_1", "val_3"]
        result = process_data(ids, attributes)
        write_report(result)

        # Assuming we know some IDs in the generated data
        self.assertIsInstance(result, list)
        for item in result:
            self.assertIn('id', item)
            self.assertIn(item['id'], ids)
            for attr in attributes:
                self.assertIn(attr, item)


if __name__ == '__main__':
    unittest.main()
