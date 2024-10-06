from abc import ABC
from Constants.Responses import Responses
from Decorators.UserDecorator import UserDecorator
from Responses.ValidationResponses.ValidationResponse import ValidationResponse


class LoggedInResponse(ValidationResponse, ABC):
    async def is_valid(self, event):
        user = await UserDecorator(event).load()
        return self.bot.is_logged(user.id)

    async def on_invalid(self, event):
        await event.reply(Responses.ON_NOT_LOGGED_IN)
