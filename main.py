from fastapi import FastAPI
from routers import task_router
from database import Base, engine
import uvicorn

Base.metadata.create_all(bind=engine)


app = FastAPI()
# Register the task router
app.include_router(task_router.router)

if __name__ == "__main__":
    # This block will only execute if the script is run directly, not when imported as a module
    uvicorn.run(app, host="0.0.0.0", port=8080)
  