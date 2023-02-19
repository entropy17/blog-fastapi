from fastapi import FastAPI, Depends, status, Response, HTTPException

from blog import schemas, models
from blog.database import engine
from blog.routers import blog, user, login

app = FastAPI()

app.include_router(login.router)
app.include_router(blog.router)
app.include_router(user.router)


models.Base.metadata.create_all(bind=engine)




