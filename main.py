from fastapi import FastAPI
from database import SessionLocal, engine, Base
from models import User, Content
from schemas import UserCreate, ContentCreate
import models
app = FastAPI()
Base.metadata.create_all(bind=engine)
@app.post("/users")
def create_user(user: UserCreate):
    db = SessionLocal()
    new_user = User(
        name=user.name,
        email=user.email
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    user_id = new_user.id
    db.close()
    return {
        "message": "User created successfully",
        "user_id": user_id
    }
@app.post("/content")
def create_content(content: ContentCreate):
    db = SessionLocal()
    new_content = Content(
        title=content.title,
        body=content.body,
        user_id=content.user_id
    )
    db.add(new_content)
    db.commit()
    db.refresh(new_content)
    content_id = new_content.id
    title = new_content.title
    body = new_content.body
    db.close()
    return {
        "message": "Content added successfully",
        "content_id": content_id,
        "title": title,
        "body": body
    }