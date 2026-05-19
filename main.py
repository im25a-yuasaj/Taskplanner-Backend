'''
In the main.py file, we have connected all the routes to the FastAPI application.
'''
from fastapi import FastAPI
from routes import user, task, category, priority, progress, material, file
app = FastAPI()
app.include_router(user.router)
app.include_router(task.router)
app.include_router(category.router)
app.include_router(priority.router)
app.include_router(progress.router)
app.include_router(material.router)
app.include_router(file.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}