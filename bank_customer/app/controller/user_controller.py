import json

from app.models import User
from app.utils.helper import Authenticator
from app.serializer.user_serializer import UserInSerializer, UserOutSerializer


authenticator = Authenticator()

def add_user(db_session, data: UserInSerializer):
    response = {"message": "", "data": None}
    # verify email not in system
    with db_session as db:
        verify_email = db.query(User).where(User.email == data.email).first()
        
        if verify_email:
            response = {"message": "email already in use", "data": None} 
        else:
            hashed_password = authenticator.encrypt_password(data.password)
            new_user = User(username=data.username, email=data.email, password=hashed_password, role=data.role)
            db.add(new_user)
            db.commit()
            del new_user.password
            hashed_user = UserOutSerializer(**new_user)
            print("\n\n", hashed_user)
            response = {"message": "user created successfully", data: []}
    
    return response

def get_user(db_session, username):
    current_user = None
    with db_session as db:
        if username:
            current_user = db.query(User).where(User.username == username).first()
    return current_user


def signin(db_session, data: UserInSerializer):
    response = None
    print("\n\n", data)
    with db_session as db:
        current_user = get_user(db, data["username"])
        print(current_user, "\n\n")
        if current_user:
            is_password_correct = authenticator.verify_password(data["password"], current_user.password)
            if is_password_correct:        
                token = authenticator.generate_token(current_user.userid)
                print("\n\n", token, "\n\n")
                return {"message": "successfully logged in", "data": str(token)}
            return {"message": "username or password incorrect", "data": None}
        return {"message": "user does not exist", "data": None}
