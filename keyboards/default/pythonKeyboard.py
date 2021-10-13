from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

pythonKeys = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1. Kirish1"),
            KeyboardButton(text="2. Kirish2"),
            KeyboardButton(text="3. Kirish3")
        ],
        [
            KeyboardButton(text="4. Kirish4"),
            KeyboardButton(text="5. Kirish5"),
            KeyboardButton(text="6. Kirish6")
        ],
    ],
    resize_keyboard=True
)