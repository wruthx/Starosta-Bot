from abc import ABC
from Constants.Responses import Responses
from Decorators.UserDecorator import UserDecorator
from Responses.ValidationResponses.ValidationResponse import ValidationResponse


class AdminResponse(ValidationResponse, ABC):
    async def is_valid(self, event):
        user = await UserDecorator(event).load()
        return user.is_admin

    async def on_invalid(self, event):
        await event.reply(Responses.ON_NOT_ADMIN)
