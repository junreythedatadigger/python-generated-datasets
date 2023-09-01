import pandas as pd
import random
from faker import Faker

fake = Faker()

num_customers = 500  # Adjust as needed

customers = []

for _ in range(num_customers):
    customer_id = f'CUST{"{:05d}".format(_)}' # Added leading zeros
    age = random.randint(18, 70)
    gender = fake.random_element(['Male', 'Female'])
    location = fake.city()
    membership_type = fake.random_element(['Silver', 'Gold', 'Platinum'])
    customers.append([customer_id, age, gender, location, membership_type])

customers_df = pd.DataFrame(customers, columns=['Customer ID', 'Age', 'Gender', 'Location', 'Membership Type'])
customers_df.to_csv('customer_demographics.csv', index=False)
