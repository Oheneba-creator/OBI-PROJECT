from fastapi import APIRouter, Depends

from app.database import db_session
from app.serializer.account_serializer import AccountInSerializer
from app.controller.account_controller import add_account_data, fetch_all_accounts

account_router = APIRouter()

@account_router.post("/account/")
def insert_account(data: AccountInSerializer, db=Depends(db_session)):
    new_account = add_account_data(db, data)
    return new_account


@account_router.get("/accounts")
def get_all_accounts(db=Depends(db_session)):
    all_accounts = fetch_all_accounts(db)
    return all_accounts