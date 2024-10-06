from abc import ABC
from telethon.events import NewMessage
from Responses.BaseResponse import BaseResponse


class OnNewMessageResponse(BaseResponse, ABC):
    def __init__(self, pattern: str):
        super().__init__(pattern)

    def bind(self):
        self.bot.client.add_event_handler(
            self.handle,
            NewMessage(pattern=self.pattern)
        )