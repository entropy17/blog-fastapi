
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from blog import models, schemas
from blog.database import SessionLocal

def fetch(db: Session, id: int):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"Blog with the id {id} is unavailable")
    return blog

def fetch_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs

def create(request: schemas.Blog, db: Session, user_id):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=user_id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def delete(db: Session, id: int):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Blog with the id {id} is unavailable")

    blog.delete(synchronize_session=False)
    db.commit()
    return {"Deleted successfully"}

def update(id: int, request: schemas.Blog, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Blog with the id {id} is unavailable")

    blog.update({models.Blog.title: request.title, models.Blog.body: request.body})
    db.commit()
    return {'data': "Updated successfully"}