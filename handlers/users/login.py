import sqlite3
from os import fsdecode, stat
from aiogram import types
from aiogram.dispatcher.filters.builtin import Command
from aiogram.dispatcher.storage import FSMContext
# from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from states.login import Login


@dp.message_handler(Command('login'))
async def login(message: types.Message):
    await message.answer("Email manzilingizni kiriting:")
    await Login.email.set()


@dp.message_handler(state=Login.email)
async def check_email(message: types.Message, state: FSMContext):
    email = message.text

    conn = sqlite3.connect("data.db")
    cur = conn.cursor()
    result_email = None

    try:
        query = f'SELECT email FROM user WHERE email="{email}"'
        cur.execute(query)
        result_email = cur.fetchone()[0]
        await message.answer("Parol kiriting:")
        await Login.password.set()
    except Exception as e:  # noqa
        await message.answer("Foydalanuvchi topilmadi! Qaytadan kiriting")
        await Login.email.set()

    await state.update_data(
        {
            "email": result_email
        }
    )

    await Login.password.set()


@dp.message_handler(state=Login.password)
async def check_email(message: types.Message, state: FSMContext):
    password = message.text

    conn = sqlite3.connect("data.db")
    cur = conn.cursor()
    data = await state.get_data()
    email = data.get('email')
    try:
        query = f'SELECT password FROM user WHERE email="{email}"'
        cur.execute(query)
        result_password = cur.fetchone()[0]
        if password != result_password:
            await message.answer("Parol noto'g'ri! Qaytadan kiriting:")
            await Login.password.set()
        else:
            await message.answer("Tizimga muvaffaqiyatli kirildi! ")
            await state.reset_state(with_data=False)
    except Exception as e:  # noqa
        await message.answer("Foydalanuvchi topilmadi! Qaytadan kiriting")
        await Login.email.set()
