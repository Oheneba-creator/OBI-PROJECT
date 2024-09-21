from app.models import Account, Customer
from app.serializer.account_serializer import AccountInSerializer

def add_account_data(db_session, data: AccountInSerializer):
    new_account = None
    # convert data which is an accountinserializer format to dictionary
    data = data.model_dump()
    with db_session as db:
        # check customer exists already
        if data.get("customer_id"):
            # find existing customer
            existing_customer = db.query(Customer).where(Customer.id==data["customer_id"]).first()
            
            print("\n\n", existing_customer, "\n\n")
            
            # create account for existing customer
            new_account = Account(account_name=data["account_name"], current_balance=data["current_balance"], account_type_id=data["account_type_id"], customer_id=existing_customer.id)
            db.add(new_account)
            db.commit()
        else:
            # create new customer
            new_customer = Customer(name=data["name"], phone=data["phone"], email=data["email"], customer_type_id=data["customer_type"])
            db.add(new_customer)
            db.commit()
            
            # create account for new customer
            new_account = Account(account_name=data["account_name"], current_balance=data["current_balance"], account_type_id=data["account_type_id"], customer_id=new_customer.id)
            db.add(new_account)
            db.commit()
            
    return new_account


def fetch_account_details():
    pass


def fetch_all_accounts(db_session) -> Account:
    all_accounts = []
    with db_session as db:
        all_accounts = db.query(Customer).all()
        print(all_accounts)
    return all_accounts
        
        