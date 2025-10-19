from aiogram import Router, Bot, F
from aiogram.filters import Command, StateFilter, CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from config import ADMIN_IDS

router = Router()
router.message.filter(lambda message: message.from_user.id in ADMIN_IDS)

@router.message(CommandStart())
async def process_command_start(message: Message):
    await message.answer(("Hello, admin"))

