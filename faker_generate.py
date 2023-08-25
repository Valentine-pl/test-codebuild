import csv
from faker import Faker
import uuid
import random

# Initialize the Faker library
fake = Faker()

# Define how many records you want
num_records = 100

# Define some additional data like product categories, payment methods, and shipment methods
product_categories = ['Electronics', 'Fashion', 'Home & Kitchen', 'Books', 'Toys & Games', 'Tools & Home Improvement', 'Health & Personal Care']
payment_methods = ['Credit Card', 'Debit Card', 'PayPal', 'Cash On Delivery', 'Gift Card']
shipment_methods = ['Standard Delivery', 'Express Delivery', 'Same-day Delivery', 'In-store Pickup']

# Set to track used transaction IDs
used_ids = set()

# Generate a unique transaction ID
def generate_unique_id():
    while True:
        potential_id = fake.random_int(min=10000000, max=99999999)
        if potential_id not in used_ids:
            used_ids.add(potential_id)
            return potential_id

# Define a function to generate a single record
def generate_record():
    return [
        generate_unique_id(),  # Generate unique transaction IDs
        fake.random_number(digits=5),
        fake.bs(),
        fake.random_element(elements=product_categories),
        round(random.randint(100, 999) * 1.1, 2),
        fake.random_int(min=1, max=5),
        fake.random_number(digits=5),
        fake.random_element(elements=['Male', 'Female']),
        fake.random_int(min=18, max=90),
        fake.country(),
        round(random.randint(100, 999) * 1.1, 2),
        fake.date_time_this_decade().timestamp(),
        fake.random_element(elements=payment_methods),
        fake.random_element(elements=shipment_methods),
        fake.random_int(min=1, max=7),
    ]

# Generate the data
data = [generate_record() for _ in range(num_records)]

# Define CSV file path
csv_file_path = "fake_data.csv"

# Write data to CSV file
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    # Write header
    csv_writer.writerow([
        'transaction_id', 'product_id', 'product_name', 'product_category', 'product_price',
        'quantity_purchased', 'user_id', 'user_gender', 'user_age', 'user_country',
        'purchase_amount', 'transaction_date', 'payment_method', 'shipment_method', 'shipment_duration'
    ])
    # Write data rows
    csv_writer.writerows(data)

print(f"CSV data has been written to {csv_file_path}")
