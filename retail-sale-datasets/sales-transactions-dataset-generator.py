import pandas as pd
import random
from faker import Faker

fake = Faker()

num_transactions = 1000  # Adjust as needed

transactions = []

for _ in range(num_transactions):
    transaction_id = _ + 1  
    date = fake.date_this_year()
    customer_id = fake.random_int(min=1000, max=9999)
    product_id = fake.random_element(['PROD456', 'PROD789'])
    quantity_sold = random.randint(1, 5)
    price_per_unit = random.uniform(10, 200)
    total_sales_amount = quantity_sold * price_per_unit
    transactions.append([transaction_id, date, customer_id, product_id, quantity_sold, price_per_unit, total_sales_amount])

transactions_df = pd.DataFrame(transactions, columns=['Transaction ID', 'Date of Sale', 'Customer ID', 'Product ID', 'Quantity Sold', 'Price per Unit', 'Total Sales Amount'])
transactions_df.to_csv('sales_transactions.csv', index=False)
