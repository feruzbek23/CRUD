import pytest
from fastapi.testclient import TestClient
from main import app
from database import get_db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.task_model import Base

SQLALCHEMY_DATABASE_URL = "sqlite:///./test_tasks.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


@pytest.fixture(scope="function", autouse=True)
def setup_database():
    Base.metadata.create_all(bind=engine)  # Create tables
    yield
    Base.metadata.drop_all(bind=engine)


# Test GET (should be empty at the start)
def test_get_tasks_empty():
    response = client.get("/tasks")
    assert response.status_code == 200
    assert response.json() == []  # No tasks should exist initially

# Test POST (Create a new task)
def test_create_task():
    task_data = {"title": "Buy Milk", "description": "From the store"}
    response = client.post("/tasks", json=task_data)
    
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Buy Milk"
    assert data["description"] == "From the store"
    assert "id" in data

# Test GET (after adding a task)
def test_get_tasks():
    task_data = {"title": "Go Running", "description": "Morning run"}
    client.post("/tasks", json=task_data) 

    response = client.get("/tasks")
    assert response.status_code == 200
    assert len(response.json()) > 0  # At least 1 task should exist

# Test GET (Retrieve a specific task)
def test_get_task_by_id():
    task_data = {"title": "Read a Book", "description": "Fiction novel"}
    post_response = client.post("/tasks", json=task_data)
    task_id = post_response.json()["id"]

    response = client.get(f"/tasks/{task_id}")
    assert response.status_code == 200
    assert response.json()["title"] == "Read a Book"

# Test GET (Fail when task not found)
def test_get_task_not_found():
    response = client.get("/tasks/9999")  # Assuming this ID does not exist
    assert response.status_code == 404
    assert response.json() == {"detail": "Task not found"}

# Test PUT (Update an existing task)
def test_update_task():
    task_data = {"title": "Write Code", "description": "FastAPI project"}
    post_response = client.post("/tasks", json=task_data)
    task_id = post_response.json()["id"]

    update_data = {"title": "Write Tests", "description": "Using pytest", "completed": True}
    response = client.put(f"/tasks/{task_id}", json=update_data)
    
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Write Tests"
    assert data["description"] == "Using pytest"
    assert data["completed"] == True

# Test PUT (Fail when task does not exist)
def test_update_task_not_found():
    response = client.put("/tasks/9999", json={"title": "Updated Title"})
    assert response.status_code == 404
    assert response.json() == {"detail": "Task not found"}

# Test DELETE (Delete an existing task)
def test_delete_task():
    task_data = {"title": "Go Running", "description": "Morning run"}
    post_response = client.post("/tasks", json=task_data)
    task_id = post_response.json()["id"]

    response = client.delete(f"/tasks/{task_id}")
    assert response.status_code == 200
    assert response.json() == {"message": "Task deleted successfully"}

    # Ensure the task is actually deleted
    response = client.get(f"/tasks/{task_id}")
    assert response.status_code == 404

# Test DELETE (Fail when task not found)
def test_delete_task_not_found():
    response = client.delete("/tasks/9999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Task not found"}
