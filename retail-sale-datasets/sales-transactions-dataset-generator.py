import pandas as pd
import random
from faker import Faker
import datetime

fake = Faker()

num_transactions = 100000  # Adjust as needed

# Get data from the product_details.csv
products_df1 = pd.read_csv('product_details.csv')                           # Used to create a list from a column
products_df2 = pd.read_csv('product_details.csv', index_col='ProductID')    # Used to access a data using the ProductID

# Get data from the customer_demogrphics.csv
customers_df = pd.read_csv('customer_demographics.csv')                     # Used to create a list from a column

date = fake.date_this_year()                                                # Generate a fake start date

transactions = []

for _ in range(num_transactions):
    transaction_id = _ + 1                                                  # Generate transaction ID
    date += datetime.timedelta(hours=random.randint(12, 24))                   # Generate date that increase
    customer_id = fake.random_element(customers_df.CustomerID.tolist())     # Get random customer ID
    product_id = fake.random_element(products_df1.ProductID.tolist())       # Get random product ID
    quantity_sold = random.randint(1, 1000)                                   # Generate random number of items
    price_per_unit = products_df2.UnitCost[product_id]                      # Get unit cost based on product ID
    total_sales_amount = quantity_sold * price_per_unit                     # Calculate total sales unit
    transactions.append([transaction_id, date, customer_id, product_id, quantity_sold, price_per_unit, total_sales_amount])

transactions_df = pd.DataFrame(transactions, columns=['TransactionID', 'DateOfSale', 'CustomerID', 'ProductID', 'QuantitySold', 'PricePerUnit', 'TotalSalesAmount'])
transactions_df.to_csv('sales_transactions.csv', index=False)
