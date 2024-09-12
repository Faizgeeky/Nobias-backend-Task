'''
Code written By : Faizmohammad N
email : nandoliyafaiz429@gmail.com
github : https://github.com/Faizgeeky/Nobias-backend-Task
Date : 12/09/2024
'''

from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import mapped_column
from database import Base
import datetime


#  We can declare simply what elements should be there in new articele title, author, date, content, category 
class Article(Base):
    __tablename__ = 'articles'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    author = Column(String, nullable=False)
    date = Column(DateTime, default=datetime.datetime.now())
    category = Column(String, nullable=False)

# 
class Comments(Base):
    __tablename__ = 'comments'
    id = Column(Integer,primary_key=True)
    article_id =  mapped_column(ForeignKey("articles.id"))
    comment = Column(String, nullable=False)
    commented_by = Column(String, nullable=False)
    date = Column(DateTime, default=datetime.datetime.now())