from datetime import date
from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy import Integer, String, Date, JSON, Float, ForeignKey


from app.database import Base, db_engine

class Account_Type(Base):
    __tablename__ = "account_type"
    type_code = mapped_column(Integer, primary_key=True)
    type_description = mapped_column(String(125))

class Customer_Type(Base):
    __tablename__ = "customer_type"
    type_code = mapped_column(Integer, primary_key=True)
    type_description = mapped_column(String(125))

class Transaction_Type(Base):
    __tablename__ = "transaction_type"
    type_code = mapped_column(Integer, primary_key=True)
    type_description = mapped_column(String(125))

class Customer(Base):
    __tablename__ = "customer"
    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String(125))
    email  = mapped_column(String(125))
    created_on = mapped_column(Date, default=date.today)
    other_details = mapped_column(JSON)
    customer_type_id = mapped_column(Integer, ForeignKey("customer_type.type_code"))

    # customer_type = relationship("Customer_Type", back_populates="customer_type")

class Party(Base):
    __tablename__ = "party"
    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String(125))
    phone = mapped_column(String(25))
    email  = mapped_column(String(125))
    other_details = mapped_column(JSON)


class Account(Base):
    __tablename__ = "account"
    id = mapped_column(Integer, primary_key=True)
    account_name = mapped_column(String(125))
    date_opened = mapped_column(Date, default=date.today)
    date_closed = mapped_column(Date)
    current_balance = mapped_column(Float(6, 2))
    other_details = mapped_column(JSON)
    account_type_id = mapped_column(Integer)
    customer_id = mapped_column(Integer)
    
class Transaction(Base):
    __tablename__ = "transaction"
    message_number = mapped_column(Integer, primary_key=True)
    counterparty_role = mapped_column(String(125))
    currency_code = mapped_column(String(125))
    iban_number = mapped_column(String(125))
    transaction_date = mapped_column(Date, default=date.today)
    amount = mapped_column(Float(6, 2))
    balance = mapped_column(Float(6, 2))
    location = mapped_column(String(125))
    party_role = mapped_column(String(125))
    account_id =  mapped_column(Integer)
    counterparty_id = mapped_column(Integer)
    party_id = mapped_column(Integer)
    transaction_type_id = mapped_column(Integer)

class User(Base):
    __tablename__ = "user"
    userid = mapped_column(Integer, primary_key=True)
    username = mapped_column(String(125), nullable=False)
    password = mapped_column(String(255), nullable=False)
    role = mapped_column(String(255))
    email = mapped_column(String(255))
    
Base.metadata.create_all(bind=db_engine)
