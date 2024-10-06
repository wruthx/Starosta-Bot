from Responses.NewMessageResponses.OnNewMessageResponse import OnNewMessageResponse


class NewMessageGuestResponse(OnNewMessageResponse):
    def __init__(self, pattern: str, message: str):
        super().__init__(pattern)
        self.message = message

    async def handle(self, event):
        await event.reply(self.message)
