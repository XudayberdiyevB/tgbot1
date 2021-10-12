from aiogram.dispatcher.filters.state import State, StatesGroup


class PersonalData(StatesGroup):
    fullname = State()
    email = State()
    phone = State()
