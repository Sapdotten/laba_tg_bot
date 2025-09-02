from aiogram import F, types
from aiogram.dispatcher.router import Router
from aiogram.filters import Command

# from . import consts, keyboards, lab_state
import consts
import keyboards
import lab_state

router = Router()


@router.message(Command(commands=["start"]))
async def start(msg: types.Message):
    if msg.from_user.id in consts.COUNCIL_MEMBERS_TG_IDS:
        keyboard = keyboards.admin_keyboard()
    else:
        keyboard = keyboards.user_keyboard()
    await msg.answer(consts, reply_markup=keyboard)


@router.message(F.text == consts.OPEN_TEXT)
async def open_lab(msg: types.Message):
    if msg.from_user.id in consts.COUNCIL_MEMBERS_TG_IDS:
        # answer = await lab_state.LabState.change_status(True)
        current_state = lab_state.LabState.get_state()
        if current_state:
            await msg.answer(consts.OPENED_ALREADY_TEXT)
        else:
            answer = lab_state.LabState.set_state(True)
            answer = (
                consts.OPENED_TEXT
                if answer
                else consts.CLOSED_TEXT
            )
            await msg.answer(answer)
    else:
        await msg.answer(consts.ACCESS_DENIED_TEXT)


@router.message(F.text == consts.CLOSE_TEXT)
async def close_lab(msg: types.Message):
    if msg.from_user.id in consts.COUNCIL_MEMBERS_TG_IDS:
        # answer = await lab_state.LabState.change_status(True)
        current_state = lab_state.LabState.get_state()
        if not current_state:
            await msg.answer(consts.CLOSED_ALREADY_TEXT)
        else:
            answer = lab_state.LabState.set_state(False)
            answer = (
                consts.OPENED_TEXT
                if answer
                else consts.CLOSED_TEXT
            )
            await msg.answer(answer)
    else:
        await msg.answer(consts.ACCESS_DENIED_TEXT)


@router.message(F.text == consts.IS_OPEN_TEXT)
async def get_lab_state(msg: types.Message):
    answer = lab_state.LabState.get_state()
    answer = consts.IS_OPENED_TEXT if answer else consts.IS_CLOSED_TEXT
    await msg.answer(answer)
