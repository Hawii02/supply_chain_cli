from models import Supplier, sessionmaker, Customer, engine

session = sessionmaker(bind=engine)
createsession = session()

def find_supplier_by_name():
    supplier_name = input("Enter the supplier's name: ")
    supplier = createsession.query(Supplier).filter_by(supplier_name=supplier_name).first()
    if supplier:
        print(f"Supplier Name: {supplier.supplier_name}")
        if supplier.supplier_location:
            print(f"Supplier Location: {supplier.supplier_location}")
        else:
            print("Supplier Location: Not available")
        if supplier.supplier_contact:
            print(f"Supplier Contact: {supplier.supplier_contact}")
        else:
            print("Supplier Contact: Not available")
    else:
        print(f'Supplier "{supplier_name}" not found')

def find_product_by_name():
    product = input("Enter the product name:")
    product = createsession.query(Supplier).filter_by(product = product).first()
    if product.product:
        print(f'Product found: {product.product}')
    else:
        print(f'Product "{product.product}" not found')

def delete_customer():
    customer_name = input("Enter the customer's name:")
    delete_customer = createsession.query(Customer).filter_by(customer_name=customer_name).first()
    if delete_customer:
        createsession.delete(delete_customer)
        createsession.commit()
        print(f'Customer "{customer_name}" deleted successfully 🚮')
    else:
        print(f'Customer "{customer_name}" not found') 

def get_suppliers():
    suppliers = createsession.query(Supplier).all()
    for supplier in suppliers:
        print(supplier.supplier_name)
          
# def create_customer():
#     name = input("Enter the customer's name:")
#     contact = input("Enter the customer's contact:")
#     location = input("Enter the customer's location:")
#     try:
#         customer = Customer(customer_name=name,customer_contact=contact, customer_location=location)
#         print(f'Success: {customer.customer_name} on registering')
#     except Exception as exc:
#         print("Error adding customer:", exc)


def add_customer():
    name = input("Enter the customer's name:")
    contact = input("Enter the customer's contact:")
    location = input("Enter customer's location:")
    customer = Customer(customer_name = name, customer_contact = contact, customer_location = location)
    createsession.add(customer)
    createsession.commit()
    print(f'Success: {customer.customer_name} on registering 🎉')
   