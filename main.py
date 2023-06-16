from aiogram import executor
import logging
from config import dp
from Handlers import Commands, Callback, Extra, Admin


Commands.register_handlers_commands(dp)
Callback.register_handlers_callback(dp)
Admin.register_handlers_admin(dp)
Extra.register_handlers_extra(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
