from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class UserBase(BaseModel):
   username: str
   email: str
   password: str
   avatar_url: str


class UserDisplay(BaseModel):
   username: str
   email: str
   avatar_url : str
   subscribers: int
   class Config():
      orm_mode = True



class PostBase(BaseModel):
   image_url: str
   #image_url_type: str
   caption: str
   #creator_id: int

#For PostDisplay:
class User(BaseModel):
   username: str
   avatar_url: str
   class Config():
      orm_mode = True

#For PostDisplay
class CommentDisplay(BaseModel):
   id: int
   text: str
   user: User
   timestamp: datetime
   class Config():
      orm_mode = True

class PostDisplay(BaseModel):
   id: int
   image_url: str
   caption: str
   timestamp: datetime
   likes: int
   user: User
   comments: List[CommentDisplay]
   class Config():
      orm_mode = True

class UserAuth(BaseModel):
   id: int
   username: str
   email: str

class CommentBase(BaseModel):
   #user_id: int
   text: str
   post_id: int
   

class UpdateProfile(BaseModel):
   username: str
   email: str
   password: str
   avatar_url: str
   
class UserPostDisplay(BaseModel):
   username: str
   email: str
   avatar_url : str
   subscribers: int
   items: List[PostDisplay]
   class Config():
      orm_mode = True