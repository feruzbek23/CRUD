# Task Management

A simple **Task Management API** built with **FastAPI**, SQLite, and SQLAlchemy.

---
## Project Structure
```bash
📂 crud/
 ├── 📂 .github/             
 │   ├── 📂 workflows/       
 ├── 📂 alembic/             
 ├── 📂 models/              
 ├── 📂 routes/              
 ├── 📂 tests/               
 ├── main.py                 
 ├── database.py             
 ├── requirements.txt        
 ├── README.md               
 ├── .gitignore              
 ├── alembic.ini             

```
## Technology Used
Python – Programming language

FastAPI – Web framework for building APIs

SQLAlchemy & Alembic – Database ORM & migrations

Pydantic – Data validation & serialization

SQLite – Lightweight database

Pytest & HTTPX – Testing framework & API client

GitHub Actions – Automated testing & deployment




## 1️⃣ Setup Instructions

### 🔹 Prerequisites
- Python 3.10+
- pip (Python package manager)
- Virtual environment (recommended)

### 🔹 Installation Steps

1. **Clone the repository:**
```bash
git clone https://github.com/feruzbek23/CRUD.git
```
2. **Create a virtual environment:** 
```bash
python -m venv env
source env/bin/activate  # Mac/Linux
env\Scripts\activate  # Windows
```
3. **Upgrade pip:**
```bash
pip install --upgrade pip
```
4. **Install dependencies:**
```bash
pip install -r requirements.txt
```
5. **Apply database migrations:**
```bash
alembic upgrade head
```
6. **Run the FastAPI server**
```bash
uvicorn main:app --port 8080
```
---
## 2️⃣ API Documentation

Swagger UI: http://localhost:8080/docs

ReDoc: http://localhost:8080/redoc


Endpoint: GET /tasks 

Description: Returns a list of all tasks.

Response Example:
```bash
{
    "id": 1,
    "title": "Buy groceries",
    "description": "Milk, Eggs, Bread",
    "completed": false
}
```

Endpoint: POST /tasks

Description: Creates a new task.

Request Example:
```bash
{
  "title": "Read a book",
  "description": "Finish reading a novel",
  "completed": false
}
```
Response Example:
```bash
{
  "id": 2,
  "title": "Read a book",
  "description": "Finish reading a novel",
  "completed": false
}
```

Endpoint: GET /tasks/{id}

Description: Fetches a specific task by its id.

Request Example:
```bash
{
  "id": 2,
  "title": "Read a book",
  "description": "Finish reading a novel",
  "completed": false
}
```
Error Handling Example: (If Task Not Found):
```bash
{
  "detail": "Task not found"
}
```

Endpoint: PUT /tasks/{id}

Description: Updates an existing task by id.

Request Example:
```bash
{
  "title": "Read a book",
  "description": "Finish two chapters",
  "completed": true
}
```
Response Example:
```bash
{
  "id": 2,
  "title": "Read a book",
  "description": "Finish two chapters",
  "completed": true
}
```
Error Handling Example: (If Task Not Found):
```bash
{
  "detail": "Task not found"
}
```

Endpoint: DELETE /tasks/{id}

Description: Removes a task by id.

Response Example:
```bash
{
  "message": "Task deleted successfully"
}
```
Error Handling Example: (If Task Not Found)
```bash
{
  "detail": "Task not found"
}
```
---
## 3️⃣ CI/CD Pipeline
This project uses GitHub Actions:

✔ Run tests automatically on every push

✔ Deploy the API to a cloud platform (e.g., Heroku, AWS)

🔹 CI/CD Steps:
1. Install dependencies
2. Run tests (pytest)
3. Deploy (optional)








