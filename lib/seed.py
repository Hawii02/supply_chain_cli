from models import create_engine, sessionmaker, Base, Supplier, createsession, Customer
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from faker import Faker
from faker_commerce import faker
import random


# Base = declarative_base()

# fake = Faker()

# supplier_location = [
#     "Kisumu", "Mombasa", "Kericho", "Nakuru", "Kajiado", "Makueni", "Malindi", "Marsabit", "Kilimani", "Donholm", "Kayole", "Eastleigh", "Kitengela", "Syokimau", "Bamburi", "Mamotela", "Sugoi", "Kericho", "Eldoret", "Nandi hills", "Manyatta"
# ]
# product = [
#     "Furniture", "Watches", "Flour", "Vaseline", "Milk", "Jeans", "Sweatpants", "Swimming costumes", "Bracelets", "Vehicles", "Bikes", "Laptop", "Phones", "Jackets", "Umbrellas", "Tank", "Necklaces", "Flowers", "Guns", "Chairs", "Tv stands"
# ]

# for i in range(21):
#     supplier = Supplier(
#         supplier_name= fake.name(), 
#         supplier_contact = random.randint(500, 550),
#         supplier_location = fake.random_element(supplier_location),
#         product = fake.random_element(product)
#         )
    
#     createsession.add(supplier)
#     createsession.commit()


# customer_location = [
#     "Kisumu", "Mombasa", "Kericho", "Nakuru", "Kajiado", "Makueni", "Malindi", "Marsabit", "Kilimani", "Donholm", "Kayole", "Eastleigh", "Kitengela", "Syokimau", "Bamburi", "Mamotela", "Sugoi", "Kericho", "Eldoret", "Nandi hills", "Manyatta"
# ]

# for i in range(21):
#     customer = Customer(
#         customer_name= fake.name(), 
#         customer_contact = random.randint(1000, 2000),
#         customer_location = fake.random_element(customer_location),
#         supplier_id = 
#         )
    
#     createsession.add(customer)
#     createsession.commit()


def get_random_supplier_id():
    supplier_ids = [supplier.id for supplier in createsession.query(Supplier).all()]
    return random.choice(supplier_ids)

Base = declarative_base()
fake = Faker()
supplier_location = ["Kisumu", "Mombasa", "Kericho", "Nakuru", "Kajiado", "Makueni", "Malindi", "Marsabit", "Kilimani", "Donholm", "Kayole", "Eastleigh", "Kitengela", "Syokimau", "Bamburi", "Mamotela", "Sugoi", "Kericho", "Eldoret", "Nandi hills", "Manyatta"]

product = ["Furniture", "Watches", "Flour", "Vaseline", "Milk", "Jeans", "Sweatpants", "Swimming costumes", "Bracelets", "Vehicles", "Bikes", "Laptop", "Phones", "Jackets", "Umbrellas", "Tank", "Necklaces", "Flowers", "Guns", "Chairs", "Tv stands"]

for _ in range(21):
    supplier = Supplier(
        supplier_name=fake.name(), 
        supplier_contact=random.randint(500, 550),
        supplier_location=fake.random_element(supplier_location),
        product=fake.random_element(product)
    )
    createsession.add(supplier)
    createsession.commit()

customer_location = ["Kisumu", "Mombasa", "Kericho", "Nakuru", "Kajiado", "Makueni", "Malindi", "Marsabit", "Kilimani", "Donholm", "Kayole", "Eastleigh", "Kitengela", "Syokimau", "Bamburi", "Mamotela", "Sugoi", "Kericho", "Eldoret", "Nandi hills", "Manyatta"]

for _ in range(21):
    supplier_id = get_random_supplier_id() 
    customer = Customer(
        customer_name=fake.name(), 
        customer_contact=random.randint(1000, 2000),
        customer_location=fake.random_element(customer_location),
        supplier_id=supplier_id  
    )
    createsession.add(customer)
    createsession.commit()