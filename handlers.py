from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery

import application.keyboards as kb

router = Router() 

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply(f'Доброго времени суток, {message.from_user.first_name}, я бот по скорингу строительных подрядчиков!\n',
                         reply_markup=kb.main)

@router.callback_query(F.data == 'begin')
async def beginned(callback: CallbackQuery):
    await callback.answer("Вы выбрали Начать")
    await callback.message.edit_text('Пришлите мне файл в формате .csv с информацией полной информацией о подрядчике')


