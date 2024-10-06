from Constants.BotData import BotData
from Decorators.EventDecorator import EventDecorator
from Responses.NewMessageResponses.OnNewMessageResponse import OnNewMessageResponse
from Responses.ValidationResponses.AdminResponse import AdminResponse


class PinNewMessageSpamAdminInResponse(AdminResponse, OnNewMessageResponse):
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
            for user in self.bot.logged_users:
                try:
                    msg = await self.bot.client.send_message(
                        user,
                        message
                    )

                    if self.pinned:
                        await self.bot.client.pin_message(
                            user,
                            msg.id,
                            notify=self.disable_notifications
                        )
                except Exception as e:
                    print(e)
