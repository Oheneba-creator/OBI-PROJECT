from typing import Optional
from pydantic import BaseModel

class AccountInSerializer(BaseModel):
    account_name: str
    current_balance: float
    account_type_id: int
    customer_id: Optional[int] =None
    name: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    customer_type_id: Optional[int] = None
    

# m = AccountInSerializer(account_name="ben savings account", current_balance=50, account_type_id=1, name="Bernard", customer_type_id=1)
# print(m.model_dump())