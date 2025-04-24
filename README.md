# Assignment 04
## Author
Manuel Bolado ID: 0408650

## Description
Module 04 - Exceptions, Logging and Debugging

## Code Modification:
- Wrapped a try-block around code that opens the bank_data.csv to check for a FileNotFoundError
- Added validation step for transaction_type using an if statement. change error message and valid_record accordingly.
- Added validation step for transaction_amount using try-except statement. change error message and valid_record accordingly.
## Code Modification:
- Fixed logical error in transaction_type comparisons
## Code Modification:
- added transaction_counter whenever valid_record is true
## Code Modification:
- else if valid_record, append row value and error message into rejected_records as a tuple
## Code Modification:
- Changed print formatting to match with expected output
## Code Modification:
- added error handling for average transaction amount as there could be no transactions.

# User story
As a Software Development Manager,

I want to ensure all programs are correct, accurate and use exception handling appropriately,

So that I can be assured of the quality of our software.