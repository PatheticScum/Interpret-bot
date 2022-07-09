from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

inter = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='EN'),
            KeyboardButton(text='RU'),
            KeyboardButton(text='UZ')
        ]
    ],
    resize_keyboard=True
)
