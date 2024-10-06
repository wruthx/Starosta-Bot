from abc import ABC
from Responses.BaseResponse import BaseResponse
from telethon.events import CallbackQuery


class CallbackResponse(BaseResponse, ABC):
    def __init__(self, pattern: str):
        super().__init__(pattern)

    def bind(self):
        self.bot.client.add_event_handler(
            self.handle,
            CallbackQuery(pattern=self.pattern)
        )
