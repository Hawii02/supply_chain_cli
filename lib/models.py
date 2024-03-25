from sqlalchemy.orm import declarative_base, sessionmaker,relationship,backref
from sqlalchemy import create_engine, Column, Integer, String,ForeignKey


Base = declarative_base()

class Supplier(Base):
    __tablename__ = "suppliers"
    
    id = Column(Integer(), primary_key= True)
    supplier_name = Column(String())
    supplier_contact = Column(String())
    supplier_location = Column(String())
    product = Column(String()) 

    customers = relationship("Customer", backref=backref("supplier"))


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer(), primary_key = True)
    customer_name = Column(String())
    customer_contact = Column(String(4))
    customer_location = Column(String())
    supplier_id = Column(Integer(), ForeignKey("suppliers.id"))

engine = create_engine("sqlite:///supplier_database.db")   
Base.metadata.create_all(engine) 

session = sessionmaker(bind=engine)
createsession = session()