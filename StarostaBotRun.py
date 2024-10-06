import os

from telethon.events import NewMessage, CallbackQuery
from Decorators import EventDecorator
from Constants.Responses import Responses
from StarostaBot import MonitorBot


bot = MonitorBot()

if __name__ == '__main__':
    bot.main()
