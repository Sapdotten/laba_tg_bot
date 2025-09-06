from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from src import consts


def user_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text=consts.IS_OPEN_TEXT)]
    ], resize_keyboard=True, one_time_keyboard=False)


def admin_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text=consts.IS_OPEN_TEXT)],
        [KeyboardButton(text=consts.OPEN_TEXT), KeyboardButton(text=consts.CLOSE_TEXT)]
    ], resize_keyboard=True, one_time_keyboard=False)
