from fastapi import FastAPI
from routes import user, task
app = FastAPI()

app.include_router(user.router)
app.include_router(task.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}