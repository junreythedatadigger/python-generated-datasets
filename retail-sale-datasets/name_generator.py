# Code to generate names
from faker import Faker

fake = Faker()

# number of names to generate
num_of_names = 17

# the code to generate names and print
for _ in range(num_of_names):
    print(fake.name())