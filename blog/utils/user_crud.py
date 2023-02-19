from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from blog import models, schemas
from blog.hashing import encrypt

def create(request: schemas.User, db: Session):
    hashed_password = encrypt(request.password)
    new_user = models.User(
        name=request.name, 
        email=request.email, 
        password=hashed_password)
    if db.query(models.User).filter(models.User.email == request.email).first() != None:
        return {"User already exists. Please login"}
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"Profile created"}

def get(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with the id {id} not found"
        )
    
    return user