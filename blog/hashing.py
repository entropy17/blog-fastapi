from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

def encrypt(password: str):
    return pwd_cxt.hash(password)

def verify_password(hashed_pwd, plain_pwd):
    return pwd_cxt.verify(plain_pwd, hashed_pwd)
