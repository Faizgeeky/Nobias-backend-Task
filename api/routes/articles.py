'''
Code written By : Faizmohammad N
email : nandoliyafaiz429@gmail.com
github : https://github.com/Faizgeeky/Nobias-backend-Task
Date : 12/09/2024
'''

from fastapi import APIRouter, Depends, HTTPException, status
from api.schema import ArticleSchema, NewsCategory, List, ArticleAddSchema, AddCommentSchema
from api.models import Articles, Comments
from api.database import get_db
from sqlalchemy.orm import Session
router = APIRouter()

# add article
@router.post("/articles/")
def add_article(article: ArticleAddSchema, db: Session = Depends(get_db)):
    db_article = Articles(
        title=article.title,
        content=article.content,
        author=article.author,
        category='sports'
        # comments = []
    )
    db.add(db_article)
    db.commit()
    db.refresh(db_article)
    return db_article


@router.post('/comments/{article_id}')
def add_comment(article_id: int,comment :AddCommentSchema, db : Session = Depends(get_db)):

    article = db.query(Articles).filter(Articles.id == article_id).first()
    if not article:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Artice with {article_id} does not exist!")
        
    db_comment = Comments(
        article_id = article_id,
        comment = comment.comment,
        commented_by = comment.author
    )
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment

# get all articel
@router.get('/articles', response_model=List[ArticleSchema])
def get_all_articles(db: Session = Depends(get_db)):
    all_articles = db.query(Articles).all()
    return all_articles


#update article

#delete article
@router.delete('/articles/{article_id}',response_model=ArticleSchema)
def get_all_articles(article_id:int,db: Session = Depends(get_db)):
    db_article =  db.query(Articles).filter(Articles.id == article_id).first()

    if db_article is None:
        raise HTTPException( status_code=status.HTTP_404_NOT_FOUND,detail=f"Article with id {article_id} not found" ) 
    
    db.delete(db_article)
    db.commit()
    return db_article

#filter article