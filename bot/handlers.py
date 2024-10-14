from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from states import Form
from response import get_weather
from utils import send_weather_message

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await message.answer("Привет, напишите название города")
    await state.set_state(Form.city)


@router.message(Form.city)
async def answer(message: Message, state: FSMContext):
    try:
        city = message.text
        weather_data  = await get_weather(city)
        
        if weather_data:
            await send_weather_message(message, weather_data)
        else:
            await message.answer("Проверьте написание города")
    finally:
        await state.clear()