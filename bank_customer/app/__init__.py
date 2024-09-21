from fastapi import FastAPI, Depends

from app.utils.helper import Authenticator
from app.routes.account_routes import account_router
from app.routes.user_routes import user_router


app = FastAPI()
authenticator = Authenticator()

@app.get("/")
def root():
    return {"message": "Welcome"}

app.include_router(user_router)   
app.include_router(account_router, dependencies=[Depends(authenticator.authwrapper)])
