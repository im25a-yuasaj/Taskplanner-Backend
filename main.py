'''
In the main.py file, we have connected all the routes to the FastAPI application.
'''

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import user, task, category, priority, progress, material, taskmaterial, file

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["0.0.0.0:8000", 'https://*.vercel.app'],  # Allow all origins for development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user.router)
app.include_router(task.router)
app.include_router(category.router)
app.include_router(priority.router)
app.include_router(progress.router)
app.include_router(material.router)
app.include_router(taskmaterial.router)
app.include_router(file.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}