# Nobias-backend-Task

###  News Features

- **Adding News**: Add News article
- **Adding Comments**: Add Comments on particular article
- **Fethcing Article**: Users can easily access all the Article
- **Filter Article**: Users can easily filer the Article
- **Update Article**: Users can easily update the Article
- **Delete Article**: Users can delete filer the Article


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

 

# Docker Setup 

## Building and Running the Docker Container

### Docker Build and Run

1. **Build the Docker Image**

   Build the Docker image using the following command:

   ```sh
   docker build -t app .
   ```

2. **Run the Docker Container**

  Run the Docker container with the environment variables from the .env file and map port 8000 to your local machine:

    
    Copy code
    docker run --env-file .env -p 8000:8000 app
    <!-- Access the application at http://127.0.0.1:8000/. -->
    

### API Documentations 

- It can be downloaded and test live while running the api's on webbrowser 

    <!-- API Testing -->
    http://127.0.0.0:8000/docs 

    <!-- API Documentation -->
    http://127.0.0.0:8000/redoc
