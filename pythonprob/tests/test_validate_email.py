import unittest
from unittest.mock import patch
import os
import sys

# Assuming is_valid_email function is implemented in main.py
sys.path.insert(1, r'C:\Users\JYOTHSNA\Desktop\Flask\pythonprob\exercise1_email')
from email import is_valid_email

class TestEmailValidator(unittest.TestCase):
 
    def test_valid_emails(self):
        # Get the absolute path to valid_emails.txt
        valid_emails_path = os.path.join(os.path.dirname(__file__), 'mocks', 'valid_emails.txt')
        with open(valid_emails_path, 'r') as file:
            valid_emails = file.readlines()
        
        # Initialize counters for passed and failed test cases
        passed_count = 0
        failed_count = 0

        for email in valid_emails:
            with patch('builtins.input', side_effect=[email.strip()]):
                # Call the is_valid_email function
                result = is_valid_email(email.strip())
                # Assert that the result is True, indicating a valid email
                if result:
                    passed_count += 1
                    print(f"Test passed: {email.strip()} (Expected: True, Actual: {result})")
                else:
                    failed_count += 1
                    print(f"Test failed: {email.strip()} (Expected: True, Actual: {result})")

        # Print summary of valid emails test results
        print(f"\nValid Emails Test Summary: Passed: {passed_count}, Failed: {failed_count}")

    def test_invalid_emails(self):
        # Get the absolute path to invalid_emails.txt
        invalid_emails_path = os.path.join(os.path.dirname(__file__), 'mocks', 'invalid_emails.txt')
        with open(invalid_emails_path, 'r') as file:
            invalid_emails = file.readlines()
        
        # Initialize counters for passed and failed test cases
        passed_count = 0
        failed_count = 0

        for email in invalid_emails:
            with patch('builtins.input', side_effect=[email.strip()]):
                # Call the is_valid_email function
                result = is_valid_email(email.strip())
                # Assert that the result is False, indicating an invalid email
                if not result:
                    passed_count += 1
                    print(f"Test passed: {email.strip()} (Expected: False, Actual: {result})")
                else:
                    failed_count += 1
                    print(f"Test failed: {email.strip()} (Expected: False, Actual: {result})")

        # Print summary of invalid emails test results
        print(f"\nInvalid Emails Test Summary: Passed: {passed_count}, Failed: {failed_count}")

if __name__ == "__main__":
    unittest.main()
