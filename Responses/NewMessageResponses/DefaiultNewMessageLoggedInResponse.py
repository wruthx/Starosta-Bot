from telethon.tl.types import KeyboardButtonCallback

from Constants.Buttons import Buttons
from Responses.ValidationResponses.LoggedInResponse import LoggedInResponse
from Responses.NewMessageResponses.OnNewMessageResponse import OnNewMessageResponse


class DefaultNewMessageLoggedInResponse(LoggedInResponse, OnNewMessageResponse):
    def __init__(self, pattern: str, message: str, buttons: [[KeyboardButtonCallback]] = None):
        super().__init__(pattern)
        self.message = message
        self.buttons = buttons

    async def on_valid(self, event):
        if self.buttons:
            await event.reply(self.message, buttons=self.buttons)
        else:
            await event.reply(self.message)
