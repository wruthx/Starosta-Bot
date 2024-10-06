from Constants.Responses import Responses
from Decorators.EventDecorator import EventDecorator
from Decorators.UserDecorator import UserDecorator
from Responses.NewMessageResponses.OnNewMessageResponse import OnNewMessageResponse
from Responses.ValidationResponses.LoggedInResponse import LoggedInResponse


class DocumentNewMessageLoggedInResponse(LoggedInResponse, OnNewMessageResponse):

    def __init__(self):
        super().__init__('^/document')

    async def on_valid(self, event):
        ed = EventDecorator(self.bot.client, event)
        ud = await UserDecorator(event).load()
        message = ed.message.strip('/document').strip(' ')
        if not message:
            await event.reply(Responses.ON_DOCUMENT)
            return

        msg = await event.reply(Responses.ON_ACCEPTED_DOCUMENT_REQUEST)
        await ed.request_document(ud, msg.id, message)
