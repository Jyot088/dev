import re

def is_valid_date(date_str):
    # Regular expression to match the date format "YYYY-MM-DD"
    pattern = r'^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$'
    
    # Match the input string with the pattern
    match = re.match(pattern, date_str)
    
    if match:
        # Extract year, month, and day
        year, month, day = map(int, date_str.split('-'))
        
        # Check for valid month
        if month == 2:
            # Check for leap year
            if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                print(" This is a Leap year")
                return day <= 29
            else:
                return day <= 28
        elif month in {4, 6, 9, 11}:
            return day <= 30
        else:
            return day <= 31
    else:
        return False

def main():
    # Prompt the user to enter a date
    date_input = input("Enter a date (YYYY-MM-DD): ")

    # Check if the input date is valid
    if is_valid_date(date_input):
        print("Valid date")
    else:
        print("Invalid date")

if __name__ == "__main__":
    main()
