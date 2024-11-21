from fastapi import FastAPI
app = FastAPI(swagger_ui_parameters={"tryItOutEnablet": True})

@app.get("/")
async def get_main_page():
    return "Главная страница"

@app.get("/user/admin")
async def get_main_page():
    return "Вы вошли как администратор"

@app.get("/user/{user_id}")
async def get_main_page(user_id: int = 125):
    return f"Вы вошли как пользователь № {user_id}"

@app.get("/user")
async def get_main_page(username: str = "Serg", age: int = 55):
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"
