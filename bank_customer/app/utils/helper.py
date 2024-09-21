import jwt
from datetime import datetime, timedelta
from passlib.context import CryptContext
from fastapi import HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer


class Authenticator():
    
    security = HTTPBearer()
    secret = "nmvsdokpdfsnvofdshhgdytfvhjufvi"
    pwd_context = CryptContext(schemes="bcrypt", deprecated="auto")
    
    
    def encrypt_password(self, password):
        return self.pwd_context.hash(password)
    
    def verify_password(self, password, hashed_password):
        return self.pwd_context.verify(password, hashed_password)
    
    def generate_token(self, user_id):
        payload = {
            "exp": datetime.utcnow() + timedelta(days=0, minutes=1),
            "iat": datetime.utcnow(),
            "user": user_id
        }
        return jwt.encode(payload, self.secret, algorithm="HS256")
    
    def decode_token(self, token):
        try: 
            decoded_token = jwt.decode(token, self.secret, algorithms=["HS256"])
            return decoded_token["user"]
        except jwt.ExpiredSignatureError as e:
            raise HTTPException(status_code=401, detail="Credential expired")
        except jwt.InvalidSignatureError as e:
            raise HTTPException(status_code=401, detail="Invalid credential")
    
    def authwrapper(self, auth: HTTPAuthorizationCredentials = Security(security)):
        return self.decode_token(auth.credentials)