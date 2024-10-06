from MessageFormatter import MessageFormatter
from Decorators.UserDecorator import UserDecorator
from Responses.CallbackResponses.CallBackResponse import CallbackResponse
from Constants.Responses import Responses


class RegistrationCallbackResponse(CallbackResponse):
    def __init__(self, pattern: str, message: str):
        super().__init__(pattern)
        self.message = message

    async def handle(self, event):
        params = event.data.decode('utf-8').split(',')
        user_id = int(params[1])
        await self.bot.client.edit_message(
            event.sender_id,
            event.message_id,
            Responses.ON_ACCEPT_GENERIC if params[0] == 'Accept'
            else Responses.ON_REJECT_GENERIC
        )
        await self.bot.client.send_message(user_id,
                                           Responses.ON_ACCEPT if params[0] == 'Accept' else Responses.ON_REJECT)
        if params[0] == 'Accept':
            self.bot.register(user_id)




