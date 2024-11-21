from fastapi import FastAPI, Path
from typing import Annotated
app = FastAPI(swagger_ui_parameters={"tryItOutEnabled": True})


@app.get("/")
async def get_main_page():
    return "Главная страница"

@app.get("/user/admin")
async def get_admin_page():
    return "Вы вошли как администратор"

@app.get("/user/{user_id}")
async def get_id_page(user_id: Annotated[int,Path(ge=1, le=100, description='Enter User ID', example='1')]):
    return f'Вы вошли как пользователь № {user_id}'

@app.get("/user")
async def get_user_page(username: Annotated[str, Path(min_length=3, max_length=15,
                                      description='Enter username', example='DeD_Serg')],
                    age: Annotated[int,Path(ge=16, le=75, description='Enter age', example='55')]):
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"

