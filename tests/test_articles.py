from fastapi.testclient import TestClient
from api.main import app
from sqlalchemy.orm import Session
from api.models import Articles
import pytest

# Create a pytest fixture for the FastAPI test client
@pytest.fixture(scope="module")
def client():
    with TestClient(app) as client:
        yield client


# Fixture to add a dummy article to the database for testing
@pytest.fixture(scope="function")
def add_article(client):
    response = client.post("/articles", json={
        "title": "Test Article",
        "content": "This is a test article content.",
        "author": "Test Author",
        "category": "SPORTS"
    })
    assert response.status_code == 200
    data = response.json()
    return data 


def test_create_article(client):
    #manullay add the data and check reponse
    response = client.post("/articles", json={
        "title": "Test Article",
        "content": "This is a test article content.",
        "author": "Test Author",
        "category": "SPORTS"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Article"
    assert data["author"] == "Test Author"



def test_get_articles(client):
    # simply check if response 200 and type is dict
    response = client.get("/articles")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)


def test_update_article(client, add_article):
    # use fixure created to get the added article and we can update it
    article_data = add_article  
    article_id = article_data["id"]

    response = client.put(f"/articles/{article_id}", json={
        "title": "Updated Test Article",
        "content": "Updated content",
        "author": "Updated Author",
        "category": "SPORTS"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Updated Test Article"
    assert data["content"] == "Updated content"


def test_delete_article(client, add_article):
    # use fixture to add data and get the article id
    article_data = add_article  
    article_id = article_data["id"]

    # Delete the article
    delete_response = client.delete(f"/articles/{article_id}")
    assert delete_response.status_code == 200
