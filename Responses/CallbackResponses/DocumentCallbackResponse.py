from Constants.Buttons import Buttons
from Decorators.EventDecorator import EventDecorator
from Responses.CallbackResponses.CallBackResponse import CallbackResponse


class DocumentCallbackResponse(CallbackResponse):
    def __init__(self):
        super().__init__('^Опрацювання|^Готово')

    async def handle(self, event):
        params = event.data.decode('utf-8').split(',')
        user_id = int(params[1])
        message_id = int(params[2])
        if params[0] == 'Опрацювання':
            await self.bot.client.edit_message(
                event.sender_id,
                event.message_id,
                'Запит опрацьовується',
                buttons=Buttons.document_proceed(user_id, message_id)
            )
            await self.bot.client.send_message(
                user_id,
                'Запит опрацьовується. Очікуйте інформацію про готовність документу',
                reply_to=message_id,
            )
        else:
            await self.bot.client.edit_message(
                event.sender_id,
                event.message_id,
                'Запит опрацьовано',
            )
            await self.bot.client.send_message(
                user_id,
                'Ваш документ готовий. Зверніться до старости, щоб отримати його або перевірте пошту',
                reply_to=message_id,
            )
