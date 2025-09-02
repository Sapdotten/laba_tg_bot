from src import consts
import vk_api
from vk_api.keyboard import VkKeyboard, VkKeyboardColor


def get_keyboard(id):
    if id in consts.COUNCIL_MEMBERS_VK_IDS:
        return create_keyboard_council().get_keyboard()
    else:
        return create_keyboard_user().get_keyboard()


def create_keyboard_user():
    keyboard = vk_api.keyboard.VkKeyboard(one_time=False)
    keyboard.add_button("Лаборатория открыта?", color=VkKeyboardColor.PRIMARY)
    return keyboard


def create_keyboard_council():
    keyboard = create_keyboard_user()
    keyboard.add_line()
    keyboard.add_button("Закрыть", color=VkKeyboardColor.NEGATIVE)
    keyboard.add_button("Открыть", color=VkKeyboardColor.POSITIVE)
    return keyboard
