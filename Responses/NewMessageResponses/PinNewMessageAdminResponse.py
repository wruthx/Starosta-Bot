from Constants.BotData import BotData
from Decorators.EventDecorator import EventDecorator
from Responses.NewMessageResponses.OnNewMessageResponse import OnNewMessageResponse
from Responses.ValidationResponses.AdminResponse import AdminResponse


class PinNewMessageAdminResponse(AdminResponse, OnNewMessageResponse):
    def __init__(self, pattern: str, pinned: bool = True, disable_notifications: bool = False):
        super().__init__(pattern)
        self.pinned = pinned
        self.disable_notifications = disable_notifications

    async def on_valid(self, event):
        ed = EventDecorator(self.bot.client, event)
        message = ed.message.strip(self.pattern).strip(' ')
        if not message:
            await event.reply('Потрібно додати повідомлення до команди')
        else:
            msg = await self.bot.client.send_message(
                BotData.GROUP_ID,
                message
            )

            if self.pinned:
                await self.bot.client.pin_message(
                    BotData.GROUP_ID,
                    msg.id,
                    notify=self.disable_notifications
                )
