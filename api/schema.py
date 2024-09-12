'''
Code written By : Faizmohammad N
email : nandoliyafaiz429@gmail.com
github : https://github.com/Faizgeeky/Nobias-backend-Task
Date : 12/09/2024
'''

from pydantic import BaseModel
from enum import Enum

class NewsCategory(Enum):
    SPORTS="sports"
    CURRENT_AFFAIRS="current_affairs"
    ECONOMY="economy"

class ArticleSchema(BaseModel):
    title: str
    content: str
    author: str
    category : NewsCategory

