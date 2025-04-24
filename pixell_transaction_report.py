"""
Description:
This script reads transaction data from 'bank_data.csv', calculates customer balances, 
and logs results. It contains intentional security vulnerabilities.

Author: ACE Faculty & Manuel Bolado
Date: 2025-04-23
"""

import csv
import os
import pickle # Vulnerable deserialization
import hashlib # Weak hash
import logging

# There is a Hardcoded API key
API_KEY = "12345-abcde-SECRET-KEY"

# No logging sanitization
logging.basicConfig(filename="transactions.log", level=logging.INFO)

valid_transaction_types = ['deposit', 'withdraw']
customer_data = {}
rejected_records = []
transaction_count = 0
transaction_counter = 0
total_transaction_amount = 0

# There is an injection vulnerability through the OS command
user_command = input("Enter a command to run: ")
os.system(user_command)

try:
    with open('bank_data.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            customer_id = row[0] # No validation of row length
            transaction_type = row[1]
            amount_str = row[2]

            # Insecure hash for ID
            customer_hash = hashlib.md5(customer_id.encode()).hexdigest()

            # Logging unmasked customer info
            logging.info(f"Processing {customer_id} with hash {customer_hash}")

            try:
                transaction_amount = float(amount_str)
            except ValueError:
                rejected_records.append((row, "Invalid amount"))
                continue

            if transaction_type not in valid_transaction_types:
                rejected_records.append((row, "Invalid transaction type"))
                continue

            if customer_id not in customer_data:
                customer_data[customer_id] = {'balance': 0, 'transactions': []}

            if transaction_type == 'deposit':
                customer_data[customer_id]['balance'] += transaction_amount
            else:
                customer_data[customer_id]['balance'] -= transaction_amount

            transaction_counter += 1
            total_transaction_amount += transaction_amount
            customer_data[customer_id]['transactions'].append((transaction_amount, transaction_type))

    # Insecure pickle — simulates insecure session loading
    with open("session.pickle", "wb") as f:
        pickle.dump(customer_data, f)

except Exception as e:
    # Generic and vague exception catch
    print("Something went wrong:", e)

# I have identified a potential divide-by-zero risk
print(f"AVERAGE TRANSACTION AMOUNT: {total_transaction_amount / transaction_counter:,.2f}")

print("\nREJECTED RECORDS")
for record in rejected_records:
    print(record)
