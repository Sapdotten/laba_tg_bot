from aiogram import F, types
from aiogram.dispatcher.router import Router
from aiogram.filters import Command

# from . import consts, keyboards, lab_state
import consts
import keyboards
import lab_state

router = Router()


@router.message(Command(commands=["start"]))
async def start(msg: types.Message) -> None:
    if msg.from_user.id in consts.COUNCIL_MEMBERS_TG_IDS:
        keyboard = keyboards.admin_keyboard()
    else:
        keyboard = keyboards.user_keyboard()
    await msg.answer(consts.START_TEXT, reply_markup=keyboard)


@router.message(F.text == consts.OPEN_TEXT)
async def open_lab(msg: types.Message) -> None:
    if msg.from_user.id in consts.COUNCIL_MEMBERS_TG_IDS:
        if lab_state.LabState.get_state():
            await msg.answer(consts.OPENED_ALREADY_TEXT)
        else:
            await msg.answer(
                text=(
                    consts.OPENED_TEXT
                    if lab_state.LabState.set_state(True)
                    else consts.CLOSED_TEXT
                )
            )
    else:
        await msg.answer(consts.ACCESS_DENIED_TEXT)


@router.message(F.text == consts.CLOSE_TEXT)
async def close_lab(msg: types.Message) -> None:
    if msg.from_user.id in consts.COUNCIL_MEMBERS_TG_IDS:
        if not lab_state.LabState.get_state():
            await msg.answer(consts.CLOSED_ALREADY_TEXT)
        else:
            await msg.answer(
                text=(
                    consts.OPENED_TEXT
                    if lab_state.LabState.set_state(False)
                    else consts.CLOSED_TEXT
                )
            )
    else:
        await msg.answer(consts.ACCESS_DENIED_TEXT)


@router.message(F.text == consts.IS_OPEN_TEXT)
async def get_lab_state(msg: types.Message) -> None:

    await msg.answer(
        text=consts.IS_OPENED_TEXT if lab_state.LabState.get_state() else consts.IS_CLOSED_TEXT
    )
