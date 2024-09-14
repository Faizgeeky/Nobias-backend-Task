# Nobias-backend-Task

###  News Features

- **Adding News**: Add News article
- **Adding Comments**: Add Comments on particular article
- **Fethcing Article**: Users can easily access all the Article
- **Filter Article**: Users can easily filer the Article
- **Update Article**: Users can easily update the Article
- **Delete Article**: Users can delete filer the Article

### API Endpoints 

1. Fetch and filter all articles in pagination filters(author , category):
    ```sh
    GET
    /articles
    ```
2. Update the article:
    ```sh
    PUT
    /articles/{article_id}
    ```
3. Delete the article:
    ```sh
    DELETE
    /articles/{article_id}
    ```
4. Adding Article
    ```sh
    POST
    /articles
    ```
5. Adding Comment
    ```sh
    POST
    /comments/{article_id}
    ```

### Enhancement
- **Adding News category
- **Users Auth 
- **Authorized loggedIn users to add articles
- **Limit no of comments
- **Sub comments or reply comments feature
- **Adding asyn db session with db like postgres
- **Adding failed and more testcases in unit testing

## Setup Instructions

### Clone the Repository

To get started, clone the repository to your local machine:

```sh
git clone https://github.com/Faizgeeky/Nobias-backend-Task
cd Nobias-backend-Task
```

### Setting Up the News Rest API's


1. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

###   Use alembic migrations to migrate data

2. Run API testing :
    ```sh
    alembic init 
    alembic revision --autogenerate -m "Migration or model chnaged message"
    alembic upgrade head
    ```
   

###   🚀🚀 Ready to launch your API Endpoints

3. Run uvicorn server:
    ```sh
    uvicorn api.main:app --reload 
    ```

###   🚀🚀 Test all API's using pytest

4. Run API testing :
    ```sh
    pytest 
    ```

   

### API's Documentation

An enpoint http://localhost:8000/docs will have list of schema and api endpoints. Swagger OpenAPI Document

     

### API Documentations 

- It can be downloaded and test live while running the api's on webbrowser 

    <!-- API Testing -->
    http://127.0.0.0:8000/docs 

    <!-- API Documentation -->
    http://127.0.0.0:8000/redoc
