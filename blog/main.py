from fastapi import FastAPI, Depends, status, Response, HTTPException

from . import schemas, models
from .database import engine
from .routers import blog, user, login

app = FastAPI()

app.include_router(login.router)
app.include_router(blog.router)
app.include_router(user.router)


models.Base.metadata.create_all(bind=engine)




