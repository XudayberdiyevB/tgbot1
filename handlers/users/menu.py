from aiogram import types
from aiogram.dispatcher.filters.builtin import Command

from loader import dp
from keyboards.default.menuKeyboards import menu
from keyboards.default.pythonKeyboard import pythonKeys


@dp.message_handler(Command("menu"))
async def show_menu(msg: types.Message):
    await msg.answer("Kerakli kurslarni tanlang", reply_markup=menu)


@dp.message_handler(text="Python")
async def get_python(msg: types.Message):
    await msg.answer("Mavzu tanlang", reply_markup=pythonKeys)
