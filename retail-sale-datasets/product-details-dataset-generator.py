import pandas as pd
import random
from faker import Faker

from product_details import Categories, Subcategories

categories = Categories
subcategories = Subcategories

fake = Faker()

num_products = 50  # Adjust as needed

products = []

for _ in range(num_products):
    product_id = f'PROD{"{:05d}".format(_)}' # Added leading zeros
    product_name = fake.word()
    # category = fake.random_element(['Electronics', 'Clothing', 'Furniture'])
    category = fake.random_element(categories)
    # subcategory = fake.random_element(['Computers', 'Shirts', 'Chairs'])
    subcategory = fake.random_element(subcategories[category])
    manufacturer = fake.company()
    unit_cost = random.uniform(50, 1000)
    products.append([product_id, product_name, category, subcategory, manufacturer, unit_cost])

products_df = pd.DataFrame(products, columns=['Product ID', 'Product Name', 'Category', 'Subcategory', 'Manufacturer', 'Unit Cost'])
products_df.to_csv('product_details.csv', index=False)
