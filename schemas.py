from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str


class ContentCreate(BaseModel):
    title: str
    body: str
    user_id: int