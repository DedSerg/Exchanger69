from fastapi import FastAPI, Path, HTTPException
from pydantic import BaseModel
from typing import Annotated
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
@app.post("/user/{username}/{age}")
async def create_user(
        username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example='UrbanUser')],
        age: Annotated[int, Path(ge=18, le=120, description="Enter age", example='24')]
):
    user_id = (users[-1].id + 1) if users else 1
    new_user = User(id=user_id, username=username, age=age)
    users.append(new_user)
    return new_user


# PUT запрос по маршруту '/user/{user_id}/{username}/{age}'
@app.put("/user/{user_id}/{username}/{age}")
async def update_user(
        user_id: Annotated[int, Path(ge=1, le=100, description='Enter user id', example='1')],
        username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example='UrbanProfi')],
        age: Annotated[int, Path(ge=18, le=120, description="Enter age", example='28')]
):
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail="User was not found")


# DELETE запрос по маршруту '/user/{user_id}'
@app.delete("/user/{user_id}", response_model=User)
async def delete_user(
        user_id: Annotated[int, Path(ge=1, le=100, description='Enter user id', example='1')]
):
    for index, user in enumerate(users):
        if user.id == user_id:
            deleted_user = users.pop(index)
            return deleted_user
    raise HTTPException(status_code=404, detail="User was not found")
