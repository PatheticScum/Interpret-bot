import logging

from aiogram import executor

from loader import dp, db

from ADMIN.notify_admins import on_startup_notify
from keyboards.set_bot_commands import set_default_commands
import handlers

import ADMIN.notify_admins

logging.basicConfig(level=logging.INFO)


async def on_startup(dispatcher):

    db.create_table_users()

    await set_default_commands(dispatcher)

    await on_startup_notify(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
