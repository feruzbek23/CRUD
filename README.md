# 🚀 Tasks

A simple **Task Management API** built with **FastAPI**, SQLite, and SQLAlchemy.

---

## 📌 1️⃣ Setup Instructions

### 🔹 Prerequisites
- Python 3.10+
- pip (Python package manager)
- Virtual environment (recommended)

### 🔹 Installation Steps

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/yourproject.git
cd yourproject
```
2. **Create a virtual environment:** 
```bash
python -m venv env
source env/bin/activate  # Mac/Linux
env\Scripts\activate  # Windows
```
3. **Install dependencies:**
```bash
pip install -r requirements.txt
```
4. **Apply database migrations:**
```bash
alembic upgrade head
```
5. **Run the FastAPI server**
```bash
uvicorn main:app --reload
```
