from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from keyboards.default.menuStart import menustart


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!\n\n")
    await message.answer(f"Telefon va kontaktingizni yuboring!", reply_markup=menustart)
