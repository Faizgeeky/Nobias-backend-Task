'''
Code written By : Faizmohammad N
email : nandoliyafaiz429@gmail.com
github : https://github.com/Faizgeeky/Nobias-backend-Task
Date : 12/09/2024
'''

from fastapi import APIRouter, Depends, HTTPException, status, Query
from api.schema import ArticleSchema, NewsCategory, ArticleAddSchema, AddCommentSchema, ArticlePaginationResponse
from api.models import Articles, Comments
from api.database import get_db
from sqlalchemy.orm import Session
from typing import List , Optional

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
    # check article exist else return 404
    article = db.query(Articles).filter(Articles.id == article_id).first()
    if not article:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Artice with {article_id} does not exist!")
    # add commente to article 
    db_comment = Comments(
        article_id = article_id,
        comment = comment.comment,
        commented_by = comment.author
    )
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    #return comment object
    return db_comment

# get all articel
@router.get('/articles', response_model=ArticlePaginationResponse)
def get_all_articles(
    author : Optional[str] = None,
    category : Optional[str] = None,
    page: int = Query(1, ge=1),         # Default page is 1, must be >= 1
    page_size: int = Query(10, ge=1),
    db: Session = Depends(get_db)):
    query = db.query(Articles)

    if author :
        query = query.filter(Articles.author == author)
    if category :
        query = query.filter(Articles.category == category)

    article_count = query.count()
    total_pages = (article_count + page_size -1) // page_size

    if page > total_pages:
        raise HTTPException(status_code=404, detail="Page not found")
    all_articles = (query.offset((page-1) * page_size).limit(page_size).all())

    return {
        "page":page,
        "page_size":page_size,
        "total_articles": article_count,
        "total_pages": total_pages,
        "articles": all_articles
    }


#update article
@router.put('/articles/{article_id}')
def update_article(article_id:int, article : ArticleAddSchema ,db: Session = Depends(get_db)):
    db_article =  db.query(Articles).filter(Articles.id == article_id).first()

    #  Check if article with id exists!
    if db_article is None:
        raise HTTPException( status_code=status.HTTP_404_NOT_FOUND,detail=f"Article with id {article_id} not found" ) 
    # change all parameters 
    db_article.title=article.title
    db_article.content=article.content
    db_article.author=article.author
    db_article.category="sports"
        
    db.commit()
    db.refresh(db_article)
    #return refreshed updated article
    return db_article

#delete article
@router.delete('/articles/{article_id}',response_model=ArticleSchema)
def delete_article(article_id:int,db: Session = Depends(get_db)):
    db_article =  db.query(Articles).filter(Articles.id == article_id).first()

    if db_article is None:
        raise HTTPException( status_code=status.HTTP_404_NOT_FOUND,detail=f"Article with id {article_id} not found" ) 
    
    db.delete(db_article)
    db.commit()
    return db_article
