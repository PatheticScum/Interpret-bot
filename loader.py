from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from sql.sqlite_db import Database
from ADMIN import config

bot = Bot(token=config.BOT_TOKEN, parse_mode='HTML')
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
db = Database('ADMIN/users.db')
