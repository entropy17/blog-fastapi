from typing import List
from fastapi import APIRouter, Depends, status

from blog import schemas
from blog.database import get_db
from sqlalchemy.orm import Session
from blog.routers.oauth2 import get_current_active_user

from blog.utils.blog_crud import create, delete, fetch, fetch_all, update

router = APIRouter(
    prefix="/blog",
    tags=["Blogs"]
)

@router.get("/")
def get_all_blogs(db: Session = Depends(get_db), current_user: int = Depends(get_current_active_user)):
    return fetch_all(db)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Blog)
def create_blog(request: schemas.Blog, db: Session = Depends(get_db), current_user: int = Depends(get_current_active_user)):
    return create(request, db, current_user.id)

@router.get("/{id}", response_model=schemas.BlogResponse)
def get_single_blog(id: int, db: Session = Depends(get_db), current_user: int = Depends(get_current_active_user)):
    return fetch(db, id)

@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_blog(id: int, request: schemas.Blog, db: Session = Depends(get_db), current_user: int = Depends(get_current_active_user)):
    return update(id, request, db)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id: int, db: Session = Depends(get_db), current_user: int = Depends(get_current_active_user)):
    return delete(db, id)