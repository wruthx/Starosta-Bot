from Constants.Responses import Responses
from Decorators.EventDecorator import EventDecorator
from Decorators.UserDecorator import UserDecorator
from Responses.NewMessageResponses.OnNewMessageResponse import OnNewMessageResponse


class RegistrationResponse(OnNewMessageResponse):
    def __init__(self, pattern: str):
        super().__init__(pattern)

    async def handle(self, event):
        e = EventDecorator(self.bot.client, event)
        user = await UserDecorator(event).load()
        if self.bot.is_logged(user.id):
            await event.reply(Responses.ON_ALREADY_REGISTERED)
        else:
            await e.request()
            await event.reply(Responses.ON_REG)
