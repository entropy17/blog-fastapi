from fastapi import APIRouter, Depends, HTTPException, Response, status

from blog import models, schemas
from blog.database import get_db
from sqlalchemy.orm import Session

from blog.utils.user_crud import create, get

router = APIRouter(
    prefix="/user",
    tags=['Users']
)

@router.post("/")
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return create(request, db)

@router.get("/{id}", response_model=schemas.UserResponse)
def get_user(id: int, db: Session = Depends(get_db)):
    return get(id, db)