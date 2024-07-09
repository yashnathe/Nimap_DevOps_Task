from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
import os

app = FastAPI()

USERS_FILE_PATH = os.getenv('USERS_FILE_PATH', 'data/users.json')

class User(BaseModel):
    name: str
    age: int
    email: str

def read_users():
    if not os.path.exists(USERS_FILE_PATH):
        return []
    with open(USERS_FILE_PATH, 'r') as file:
        return json.load(file)

def write_users(users):
    with open(USERS_FILE_PATH, 'w') as file:
        json.dump(users, file, indent=4)

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/users")
def get_users():
    return read_users()

@app.post("/users")
def create_user(user: User):
    users = read_users()
    users.append(user.dict())
    write_users(users)
    return user
