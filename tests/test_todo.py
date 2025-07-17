from app import create_app
from app.models.todo import Todo
from app.repositories.todo_repository import TodoRepository
from app.services.todo_service import TodoService
import pytest

@pytest.fixture
def app():
    app = create_app()
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def init_database():
    # Setup code to initialize the database
    yield
    # Teardown code to clean up the database

def test_create_todo(client, init_database):
    response = client.post('/todos', json={'task': 'Test Todo'})
    assert response.status_code == 201
    assert response.json['task'] == 'Test Todo'

def test_get_todo(client, init_database):
    client.post('/todos', json={'task': 'Test Todo'})
    response = client.get('/todos/todo1')
    assert response.status_code == 200
    assert response.json['task'] == 'Test Todo'

def test_update_todo(client, init_database):
    client.post('/todos', json={'task': 'Test Todo'})
    response = client.put('/todos/todo1', json={'task': 'Updated Todo'})
    assert response.status_code == 200
    assert response.json['task'] == 'Updated Todo'

def test_delete_todo(client, init_database):
    client.post('/todos', json={'task': 'Test Todo'})
    response = client.delete('/todos/todo1')
    assert response.status_code == 204
    response = client.get('/todos/todo1')
    assert response.status_code == 404