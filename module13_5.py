from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio

api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(resize_keyboard=True)
button1 = KeyboardButton(text='Рассчитать')
button2 = KeyboardButton(text="Информация")
kb.row(button1, button2)

class UserState(StatesGroup):
    name = State()
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(commands=['start'])
async def consol_command(messeage):
    await messeage.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb)

@dp.message_handler(text= 'Рассчитать')
async def client_name(message):
    await message.answer('Введите своё имя')
    await UserState.name.set()

@dp.message_handler(state= UserState.name)
async def client_age(message, state):
    await state.update_data(name=message.text)
    data = await state.get_data()
    await message.answer(f'Добрый день, {data["name"]}. Введите свой возраст.')
    await UserState.age.set()

@dp.message_handler(state= UserState.age)
async def client_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост.')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def client_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес.')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def client_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    calories = 10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age']) + 5
    await message.answer(f'{data["name"]}, ваша дневная норма калорий - {calories}.')
    await state.finish()




@dp.message_handler()
async def other_message(message):
    await message.answer('Введите команду /start, чтобы начать общение.')




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)