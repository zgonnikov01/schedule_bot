from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from config import ADMIN_IDS

router = Router()
router.message.filter(lambda message: message.from_user.id in ADMIN_IDS)

@router.message(CommandStart())
async def process_command_start(message: Message):
    await message.answer(("Hello, admin"))

