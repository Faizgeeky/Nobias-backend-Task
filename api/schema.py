'''
Code written By : Faizmohammad N
email : nandoliyafaiz429@gmail.com
github : https://github.com/Faizgeeky/Nobias-backend-Task
Date : 12/09/2024
'''

from pydantic import BaseModel
from enum import Enum
from typing import List

class NewsCategory(Enum):
    SPORTS="sports"
    CURRENT_AFFAIRS="current_affairs"
    ECONOMY="economy"

class CommentSchema(BaseModel):
    id: int
    comment: str
    commented_by: str

    class Config:
        orm_mode = True
    
class AddCommentSchema(BaseModel):
    comment : str
    author : str
    

class ArticleSchema(BaseModel):
    id : int
    title: str
    content: str
    comments: List[CommentSchema] = []
    author: str
    category : NewsCategory

class ArticleAddSchema(BaseModel):
    title: str
    content: str
    author: str
    category : NewsCategory

#  Important schema to return data along with pagination details
class ArticlePaginationResponse(BaseModel):
    page: int
    page_size:int
    total_articles: int
    total_pages : int
    articles : List[ArticleSchema]