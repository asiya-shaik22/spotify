from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
from database import Settings, get_db 
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session  

import models

settings = Settings()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")




# 🔒 Hash password
def hash_password(password: str):
    return pwd_context.hash(str(password))


# 🔍 Verify password
def verify_password(plain, hashed):
    return pwd_context.verify(str(plain), hashed)


# 🎟️ Create JWT token
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)




oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        user_id = int(payload.get("sub"))
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

    user = db.query(models.User).filter_by(id=user_id).first()
    return user