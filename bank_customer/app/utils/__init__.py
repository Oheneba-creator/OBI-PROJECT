import jwt
from passlib.hash import bcrypt

SECRET = "jbsadlf;abdsfjlndanbkhdglahfa"
ALGORITHM = "HS256"

def encrypt_password(password):
    return bcrypt.using(rounds=13).hash(password)

def verify_password(hashed_password, password):
    return bcrypt.verify(password, hashed_password)

def create_token(username, email):
    return jwt.encode({"username": username, "email": email}, SECRET, algorithm=ALGORITHM)

def decrypt_token(token):
    return jwt.decode(token, SECRET, algorithm=ALGORITHM)

