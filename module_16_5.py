from fastapi import FastAPI, Path, HTTPException, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from typing import Annotated
from pydantic import BaseModel

app = FastAPI()

# Создаем объект Jinja2Templates
templates = Jinja2Templates(directory="templates")

# Словарь пользователей
users = {
    '1': {'username': 'UrbanUser', 'age': 24},
    '2': {'username': 'UrbanTest', 'age': 22},
    '3': {'username': 'Capybara', 'age': 60},
}

# Определяем класс User, наследуемый от BaseModel
class User(BaseModel):
    id: int
    username: str
    age: int


@app.get("/", response_class=HTMLResponse)
async def get_users(request: Request) -> HTMLResponse:
    return templates.TemplateResponse('users.html', {"request": request, "users": users})


# GET запрос по маршруту '/users/{user_id}'
@app.get('/users/{user_id}', response_class=HTMLResponse)
async def get_user(request: Request, user_id: str) -> HTMLResponse:
    user = users.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail='User was not found')
    return templates.TemplateResponse("users.html", {"request": request, "user": {'id': user_id, **user}, "users": users})


# POST запрос по маршруту '/user/'
@app.post("/user/")
async def create_user(
        username: str = Form(...),
        age: int = Form(...)
):
    user_id = str(len(users) + 1)  # Генерация нового ID
    new_user = {"username": username, "age": age}
    users[user_id] = new_user
    return {"id": user_id, **new_user}



# PUT запрос по маршруту '/user/{user_id}'
@app.put("/user/{user_id}")
async def update_user(
        user_id: Annotated[str, Path(description='Enter user id')],
        username: str,
        age: int
):
    user = users.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User was not found")
    user['username'] = username
    user['age'] = age
    return {"id": user_id, **user}


# DELETE запрос по маршруту '/user/{user_id}'
@app.delete("/user/{user_id}")
async def delete_user(
        user_id: Annotated[str, Path(description='Enter user id')]
):
    user = users.pop(user_id, None)
    if user is None:
        raise HTTPException(status_code=404, detail="User was not found")
    return {"id": user_id, **user}
