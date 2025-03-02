from fastapi import FastAPI
from routers import task_router
from database import Base, engine


Base.metadata.create_all(bind=engine)


app = FastAPI()
# Register the task router
app.include_router(task_router.router)


  