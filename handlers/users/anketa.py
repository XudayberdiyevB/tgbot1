from os import fsdecode, stat
from aiogram import types
from aiogram.dispatcher.filters.builtin import Command
from aiogram.dispatcher.storage import FSMContext
# from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from states.personalData import PersonalData

@dp.message_handler(Command('anketa'))
async def enter_anketa(message: types.Message):
    await message.answer("Assalom alaykum, to'liq ism familyangizni kiriting:")
    await PersonalData.fullname.set()

@dp.message_handler(state=PersonalData.fullname)
async def answer_fullname(message: types.Message, state: FSMContext):
    fullname = message.text

    await state.update_data(
        {
            "name": fullname
        }
    )

    await message.answer("Email manzilingizni kiriting:")

    # await PersonalData.next()
    await PersonalData.email.set()


@dp.message_handler(state=PersonalData.email)
async def answer_email(message: types.Message, state:FSMContext):
    email = message.text

    await state.update_data(
        {
            "email": email
        }
    )

    await message.answer("Telefon raqamingizni kiriting:")

    await PersonalData.next()

@dp.message_handler(state=PersonalData.phone)
async def answer_phone(message: types.Message, state: FSMContext):
    phone = message.text

    await state.update_data(
        {
            "phone": phone
        }
    )

    data = await state.get_data()
    name = data.get('name')
    email = data.get('email')
    phone = data.get('phone')

    msg = "Quyidagi ma'lumotlar qabul qilindi:\n"
    msg += f"Ism Familyangiz - {name}\n"
    msg += f"Email manzilingiz - {email}\n"
    msg += f"Telefon raqamingiz - {phone}\n"

    await message.answer(msg)

    # await state.finish()
    await state.reset_state(with_data=False)


