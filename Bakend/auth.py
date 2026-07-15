# JWT library import
from jose import jwt, JWTError
import os

# Date & Time ke liye
from datetime import datetime, timedelta, timezone

# FastAPI modules
from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer

# Secret key jo token ko sign karne ke liye use hoti hai
SECRET_KEY = os.getenv("SECRET_KEY")

# JWT algorithm
ALGORITHM = "HS256"

# Token kitne minutes valid rahega
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# OAuth2 scheme
# Login endpoint se token milega
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


# Create JWT Token
def create_token(data: dict):

    # Original dictionary ki copy banate hain
    to_encode = data.copy()

    # Token expiry time
    expire = datetime.now(timezone.utc) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    # Expiry time token me add karte hain
    to_encode.update({"exp": expire})

    # JWT token generate karte hain
    token = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return token


# Verify JWT Token
def verify_token(token: str = Depends(oauth2_scheme)):
    try:

        # Token decode karte hain
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        return payload

    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )