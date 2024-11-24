from fastapi import FastAPI, Path, HTTPException
from typing import Annotated

app = FastAPI()

# Словарь пользователей
users = {'1': 'Имя: Example, возраст: 18'}


@app.get("/")
async def get_main_page():
    return "Главная страница"


@app.get("/users")
async def get_all_dict():
    return users


@app.post("/user/{username}/{age}")
async def create_user(
        username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example='UrbanUser')],
        age: Annotated[int, Path(ge=18, le=120, description="Enter age", example='24')]
):
    # Проверка на существование пользователя с таким же именем
    if any(user.startswith(f"Имя: {username}") for user in users.values()):
        raise HTTPException(status_code=400, detail="Username already exists")

    user_id = str(int(max(users, key=int)) + 1)  # Генерируем новый ID пользователя
    users[user_id] = f"Имя: {username}, возраст: {age}"  # Добавляем нового пользователя
    return f"User {user_id} is registered"


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(
        user_id: Annotated[str, Path(ge=1, le=100, description='Enter user id', example='1')],
        username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example='UrbanProfi')],
        age: Annotated[int, Path(ge=18, le=120, description="Enter age", example='28')]
):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")

    users[user_id] = f"Имя: {username}, возраст: {age}"  # Обновляем данные пользователя
    return f"User {user_id} has been updated"


@app.delete("/user/{user_id}")
async def delete_user(
        user_id: Annotated[int, Path(ge=1, le=100, description='Enter user id', example='1')]
):
    if str(user_id) not in users:
        raise HTTPException(status_code=404, detail="User not found")

    deleted_user = users.pop(str(user_id))
    return f"User {user_id} has been deleted: {deleted_user}"