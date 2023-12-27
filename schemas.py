from pydantic import BaseModel
from datetime import datetime
from typing import List
# from fastapi import Body


class UserBase(BaseModel):
    username: str
    email: str
    password: str


class UserDisplay(BaseModel):
    username: str
    email: str

    class Config:
        from_attributes = True


class CommentBase(BaseModel):
    text: str
    timestamp: datetime
    user_id: int
    post_id: int


# user in post display and comment display
class User(BaseModel):
    username: str

    class Config:
        from_attributes = True

class CommentDisplay(BaseModel):
    id: int
    user: User
    post_id: int
    timestamp: datetime
    text: str

    class Config:
        from_attributes = True



class PostBase(BaseModel):
    image_url: str
    image_url_type: str
    caption: str
    creator_id: int




class PostDisplay(BaseModel):
    id: int
    image_url: str
    image_url_type: str
    caption: str
    timestamp: datetime
    user: User
    comment: List[CommentDisplay]

    class Config:
        from_attributes = True


class UserAuth(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        orm_mode = True
