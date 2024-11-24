from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Пустой список пользователей
users = []


# Определяем класс User, наследуемый от BaseModel
class User(BaseModel):
    id: int
    username: str
    age: int


@app.get("/")
async def get_main_page():
    return "Главная страница"


# GET запрос по маршруту '/users'
@app.get("/users", response_model=List[User])
async def get_users():
    return users


# POST запрос по маршруту '/user/{username}/{age}'
@app.post("/user/{username}/{age}", response_model=User)
async def create_user(username: str, age: int):
    user_id = (users[-1].id + 1) if users else 1
    new_user = User(id=user_id, username=username, age=age)
    users.append(new_user)
    return new_user


# PUT запрос по маршруту '/user/{user_id}/{username}/{age}'
@app.put("/user/{user_id}/{username}/{age}", response_model=User)
async def update_user(user_id: int, username: str, age: int):
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail="User was not found")


# DELETE запрос по маршруту '/user/{user_id}'
@app.delete("/user/{user_id}", response_model=User)
async def delete_user(user_id: int):
    for index, user in enumerate(users):
        if user.id == user_id:
            deleted_user = users.pop(index)
            return deleted_user
    raise HTTPException(status_code=404, detail="User was not found")
