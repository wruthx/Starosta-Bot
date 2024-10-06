from Constants.Responses import Responses
from Responses.CallbackResponses.CallBackResponse import CallbackResponse


class ScheduleCallbackResponse(CallbackResponse):
    def __init__(self, pattern: str):
        super().__init__(pattern)

    async def handle(self, event):
        day = event.data.decode('utf-8')
        await event.reply(Responses.ON_SCHEDULE[day] if day in Responses.ON_SCHEDULE else Responses.NO_DAY)
