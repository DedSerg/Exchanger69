from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

api = "7384131085:AAFXpA1nM_kCaDr_vvunxyOIjRUuVfpUDI4"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb2 = ReplyKeyboardMarkup(resize_keyboard=True)
button3 = KeyboardButton(text='Рассчитать')
button4 = KeyboardButton(text="Информация")
kb2.row(button3, button4)

kb1 = InlineKeyboardMarkup()
button1 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
button2 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
kb1.row(button1, button2)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=['start'])
async def consol_command(messeage):
    await messeage.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb2)


@dp.message_handler(content_types=['text'], text= 'Информация')
async def inform(message):
    await message.answer('Информация о боте!')


@dp.message_handler(content_types=['text'], text='Рассчитать')
async def client_menu(message):
    await message.answer('Выберите опцию:', reply_markup=kb1)


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) + 5')
    await call.answer()


@dp.callback_query_handler(text='calories')
async def client_age(call):
    await call.message.answer('Введите свой возраст')
    await call.answer()
    await  UserState.age.set()


@dp.message_handler(state=UserState.age)
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
    client_cal = 10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age']) + 5
    await message.answer(f'Ваша дневная норма калорий - {client_cal}.')
    await state.finish()


@dp.message_handler()
async def other_message(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
