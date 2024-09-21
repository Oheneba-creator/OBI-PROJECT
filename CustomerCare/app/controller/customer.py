from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models.customer import Customer 
#from app.db import db_session

class CustomerController:
    @staticmethod
    def create_customer(session: Session, data):
        new_customer = Customer(**data)
        session.add(new_customer)
        session.commit()
        return new_customer
    
    @staticmethod
    def fetch_customer():
        all_customers = select(Customer)
        return all_customers