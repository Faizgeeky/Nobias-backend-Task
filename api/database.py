'''
Code written By : Faizmohammad N
email : nandoliyafaiz429@gmail.com
github : https://github.com/Faizgeeky/Nobias-backend-Task
Date : 12/09/2024
'''

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

DATABASE_URL = os.getenv('DATABASE_URL')
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base() 

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()