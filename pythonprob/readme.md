Prerequisites

- Python 3.x
- JSON module (included in Python standard library)

Description

This project contains solutions to 3 Python problems.
It provides a unified interface for users to understand and interact with the solutions.
Unit tests are included for each problem solution.

Usage

Clone the repository.
Navigate to the project directory.
Run the main script for each problem.

Problem 1

This Python script validates an email address using regular expressions.

# Functionality

The script contains the following functions:

1. `is_valid_email(email)`: This function takes an email address as input and uses a regular expression pattern to check if the email address is valid. It returns `True` if the email address is valid according to the pattern, otherwise it returns `False`.

2. `main()`: This function is the entry point of the script. It prompts the user to enter an email address, validates the input using `is_valid_email()`, and prints whether the entered email address is valid or invalid.

# Example

```bash
$ python email_validator.py
Enter an email address: example@email.com
Valid email address


Problem 2

This Python script validates a date string in the format "YYYY-MM-DD" using regular expressions and additional checks for leap years and valid month-day combinations.

# Functionality

The script contains the following functions:

1. `is_valid_date(date_str)`: This function takes a date string as input and validates it against a regular expression pattern for the format "YYYY-MM-DD". It also performs additional checks for leap years and valid month-day combinations. It returns `True` if the input date is valid, otherwise it returns `False`.

2. `main()`: This function is the entry point of the script. It prompts the user to enter a date in the specified format, validates the input using `is_valid_date()`, and prints whether the entered date is valid or invalid.

# Example

```bash
$ python date_validator.py
Enter a date (YYYY-MM-DD): 2022-02-29
Invalid date


Problem 3

This Python script allows users to load book data from a JSON file, search for books published in a specific year, and prompt users to enter a publication year.

# Functionality

The script contains the following functions:

1. `load_book_data(file_path)`: This function loads book data from a JSON file specified by the `file_path` argument. It returns a dictionary containing the loaded book data. If the file is not found or an error occurs while reading it, an empty dictionary is returned.

2. `search_books_by_year(data, publication_year)`: This function searches for books published in a specific year within the provided book data. It takes a dictionary `data` containing book data and an integer `publication_year` representing the year to search for. It prints the titles of books published in the specified year if any are found; otherwise, it prints a message indicating no books were found.

3. `get_publication_year()`: This function prompts the user to enter a publication year and returns the entered year as an integer. It handles input validation, ensuring that the entered value is a valid integer representing a year.

4. `main()`: This function serves as the entry point of the script. It first loads book data from a JSON file located at `./exercise3_books/books.json`. If data is successfully loaded, it prints the total number of books in the dataset. It then prompts the user to enter a publication year and searches for books published in that year using the `search_books_by_year()` function.

# Example

```bash
$ python book_data_loader.py
Total number of books: 3
Enter a publication year: 2000
Books published in 2000 :
- Book 1
- Book 2
