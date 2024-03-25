from models import Supplier, createsession, Customer



def find_supplier_by_name():
    suppliername = input("Enter the supplier's name:")
    supplier = createsession.query(Supplier).filter_by(supplier_name=suppliername).first()
    print(supplier) if supplier else print(
        f'Supplier {suppliername} not found')

def find_product_by_name():
    product = input("Enter the product:")
    product = createsession.query(Supplier).filter_by(product=product).first()
    print(product) if product else print(
        f'Product {product} not found')

def delete_customer():
    customername = input("Enter the customer's name:")
    if customer := Customer.find_by_name(customername):
        customer.delete()
        print(f'Customer {customername} deleted')
    else:
        print(f'Customer {customername} not found')

def get_suppliers():
    suppliers = createsession.query(Supplier).all()
    for supplier in suppliers:
        print(supplier)


def create_customer():
    name = input("Enter the customer's name:")
    contact = input("Enter the customer's contact:")
    location = input("Enter the customer's location:")
    try:
        customer = Customer.create(name, contact, location)
        print(f'Success: {customer} on registering')
    except Exception as exc:
        print("Error adding customer:", exc)