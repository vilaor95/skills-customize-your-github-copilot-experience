# Starter code for FastAPI assignment

# main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to your FastAPI assignment!"}

# Add your resource model and CRUD endpoints below
