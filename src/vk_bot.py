import vk_api
from vk_api.longpoll import VkEventType, VkLongPoll

from src import consts, lab_state
from src.config import Configs
from src.vk_keyboards import get_keyboard


def main() -> None:
    TOKEN = Configs().vk_bot_token
    vk_session = vk_api.VkApi(token=TOKEN)
    vk = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            response: str | None = None
            match event.text:
                case consts.BEGIN_TEXT:
                    response = consts.START_TEXT
                case consts.IS_OPEN_TEXT:
                    response = lab_is_open()
                case consts.OPEN_TEXT:
                    response = lab_switch(True, user_id=event.user_id)
                case consts.CLOSE_TEXT:
                    response = lab_switch(False, user_id=event.user_id)
                case _:
                    return
            if response:
                vk.messages.send(
                    user_id=event.user_id,
                    message=response,
                    keyboard=get_keyboard(event.user_id),
                    random_id=0
                )


def lab_is_open() -> str:
    if lab_state.LabState.get_state():
        return consts.IS_OPENED_TEXT
    else:
        return consts.IS_CLOSED_TEXT


def lab_switch(open: bool, user_id: int) -> str | None:
    if user_id not in consts.COUNCIL_MEMBERS_VK_IDS:
        return consts.ACCESS_DENIED_TEXT

    opened = lab_state.LabState.get_state()
    if open and opened:
        return consts.OPENED_ALREADY_TEXT
    elif open and not opened:
        lab_state.LabState.set_state(open)
        return consts.OPENED_TEXT
    elif not open and opened:
        lab_state.LabState.set_state(open)
        return consts.CLOSED_TEXT
    if not open and not opened:
        return consts.CLOSED_ALREADY_TEXT
    return None


if __name__ == "__main__":
    main()
