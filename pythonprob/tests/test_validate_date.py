import unittest
from unittest.mock import patch
import os
import sys

# Assuming validate_date function is implemented in main.py
sys.path.insert(1, r'C:\Users\JYOTHSNA\Desktop\Flask\pythonprob\exercise2_calender')
from date import is_valid_date

class TestDateValidator(unittest.TestCase):
 
    def test_valid_dates(self):
        # Get the absolute path to valid_dates.txt
        valid_dates_path = os.path.join(os.path.dirname(__file__), 'mocks', 'valid_dates.txt')
        with open(valid_dates_path, 'r') as file:
            valid_dates = file.readlines()
        
        # Initialize counters for passed and failed test cases
        passed_count = 0
        failed_count = 0

        for date_str in valid_dates:
            with patch('builtins.input', side_effect=[date_str.strip()]):
                # Call the validate_date function
                result = is_valid_date(date_str.strip())
                # Assert that the result is True, indicating a valid date
                if result:
                    passed_count += 1
                    print(f"Test passed: {date_str.strip()} (Expected: True, Actual: {result})")
                else:
                    failed_count += 1
                    print(f"Test failed: {date_str.strip()} (Expected: True, Actual: {result})")

        # Print summary of valid dates test results
        print(f"\nValid Dates Test Summary: Passed: {passed_count}, Failed: {failed_count}")

    def test_invalid_dates(self):
        # Get the absolute path to invalid_dates.txt
        invalid_dates_path = os.path.join(os.path.dirname(__file__), 'mocks', 'invalid_dates.txt')
        with open(invalid_dates_path, 'r') as file:
            invalid_dates = file.readlines()
        
        # Initialize counters for passed and failed test cases
        passed_count = 0
        failed_count = 0

        for date_str in invalid_dates:
            with patch('builtins.input', side_effect=[date_str.strip()]):
                # Call the validate_date function
                result = is_valid_date(date_str.strip())
                # Assert that the result is False, indicating an invalid date
                if not result:
                    passed_count += 1
                    print(f"Test passed: {date_str.strip()} (Expected: False, Actual: {result})")
                else:
                    failed_count += 1
                    print(f"Test failed: {date_str.strip()} (Expected: False, Actual: {result})")

        # Print summary of invalid dates test results
        print(f"\nInvalid Dates Test Summary: Passed: {passed_count}, Failed: {failed_count}")

if __name__ == "__main__":
    unittest.main()
