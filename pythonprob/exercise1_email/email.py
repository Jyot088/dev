import re

def is_valid_email(email):
    # Regular expression to match the email format
    pattern = r'^\w+@\w+\.\w{2,}$'
    
    # Match the input string with the pattern
    match = re.match(pattern, email)
    
    return bool(match)

def main():
    # Prompt the user to enter an email address
    email_input = input("Enter an email address: ")

    # Check if the input email address is valid
    if is_valid_email(email_input):
        print("Valid email address")
    else:
        print("Invalid email address")

if __name__ == "__main__":
    main()
