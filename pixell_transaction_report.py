"""
Description: A program that reads through transaction records and reports the results.
Author: ACE Faculty
Edited by: Manuel Bolado
Date: 2024-02-29
Usage: This program will read transaction data from a .csv file, summarize and 
report the results.
"""
import csv
import os
 
valid_transaction_types = ['deposit', 'withdraw']
customer_data = {}
rejected_records = []
transaction_count = 0
transaction_counter = 0
total_transaction_amount = 0
valid_record = True
error_message = ''

os.system('cls' if os.name == 'nt' else 'clear')

try:
    with open('bank_data.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        # We can add the line of code below to skip the header. Though, it might be outside of the instructions.
        # next(reader, None)
        for row in reader:
            # Reset valid record and error message for each iteration
            valid_record = True
            error_message = ''

            # Extract the customer ID from the first column
            customer_id = row[0]
            
            # Extract the transaction type from the second column
            transaction_type = row[1]
            ### VALIDATION 1 ###
            if transaction_type not in valid_transaction_types:
                valid_record = False
                error_message += "Not a valid transaction type."

            # Extract the transaction amount from the third column
            ### VALIDATION 2 ###
            try:
                transaction_amount = float(row[2])
            except ValueError as e:
                valid_record = False
                if len(error_message) > 0: error_message += " "
                error_message += "Non-numeric transaction amount."

            if valid_record:
                transaction_counter += 1
                # Initialize the customer's account balance if it doesn't already exist
                if customer_id not in customer_data:
                    customer_data[customer_id] = {'balance': 0, 'transactions': []}

                # Update the customer's account balance based on the transaction type
                if transaction_type == valid_transaction_types[0]:
                    customer_data[customer_id]['balance'] += transaction_amount
                    transaction_count += 1
                    total_transaction_amount += transaction_amount
                elif transaction_type == valid_transaction_types[1]:
                    customer_data[customer_id]['balance'] -= transaction_amount
                    transaction_count += 1
                    total_transaction_amount += transaction_amount
                    
                # Record  transactions in the customer's transaction history
                customer_data[customer_id]['transactions'].append((transaction_amount, transaction_type))
            else:
                ### COLLECT INVALID RECORDS ###
                rejected_records.append((row, error_message))

except FileNotFoundError as e:
    print("File does not exist", e)
except Exception as e:
    print("General exception", e)

# Syntax for two decimals money format - ${value:,.2f}

print("PiXELL River Transaction Report\n===============================\n")
# Print the final account balances for each customer
for customer_id, data in customer_data.items():
    balance = data['balance']

    print(f"\nCustomer {customer_id} has a balance of ${balance:,.2f}.")
    # Print the transaction history for the customer
    print("Transaction History:")
    for transaction in data['transactions']:
        amount, type = transaction
        print(f"\t{type.capitalize()}: ${amount:,.2f}")

# Can cause an error if there was no transactions
try:
    print(f"\nAVERAGE TRANSACTION AMOUNT: ${(total_transaction_amount / transaction_counter):,.2f}")
except ZeroDivisionError as e:
    print("Cannot get average transaction amount as ", e)
except Exception as e:
    print("General error, ", e)

print("\nREJECTED RECORDS\n================")
for record in rejected_records:
    print("REJECTED:", record)
