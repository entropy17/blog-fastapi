from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from blog import models
from blog.database import SessionLocal, get_db

from blog.utils.jwt_token import verify_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

def get_current_active_user(token: str = Depends(oauth2_scheme), db: SessionLocal = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code = status.HTTP_401_UNAUTHORIZED,
        detail = f"Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"}
    )
    token = verify_token(token, credentials_exception=credentials_exception)
    user = db.query(models.User).filter(models.User.id == token.id).first()
    return user
        
     