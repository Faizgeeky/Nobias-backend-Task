'''
Code written By : Faizmohammad N
email : nandoliyafaiz429@gmail.com
github : https://github.com/Faizgeeky/Nobias-backend-Task
Date : 12/09/2024
'''

from fastapi import APIRouter, Depends
from schema import ArticleSchema, NewsCategory
from models import Article
from database import get_db
from sqlalchemy.orm import Session
router = APIRouter()

# add article
@router.post("/api/article")
def add_article(article: ArticleSchema, db: Session = Depends(get_db) ):
    article = Article(
        title=article.title,
        content=article.content,
        author=article.author,
        category=article.category
    )
    db.add(article)
    db.commit
    db.refresh
    return article
# get all articel

#update article

#delete article


#filter article