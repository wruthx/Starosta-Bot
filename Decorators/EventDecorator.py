from telethon import TelegramClient
from Constants.Buttons import Buttons
from MessageFormatter import MessageFormatter
from Decorators.UserDecorator import UserDecorator
from Constants.BotData import BotData


class EventDecorator:
    def __init__(self, client: TelegramClient, source):
        self.__client = client
        self.__source = source

    @property
    def message(self) -> str:
        return self.__source.message.message

    async def send(self, message: str) -> None:
        await self.__client.send_message(
            BotData.ADMIN_ID,
            message
        )

    async def request(self) -> None:
        cd = await UserDecorator(self.__source).load()
        await self.__client.send_message(
            BotData.ADMIN_ID,
            MessageFormatter.generate_request(cd.id, cd.use, cd.initials),
            buttons=Buttons.register(cd.id)
        )

    async def test(self, message: str) -> None:
        await self.__client.send_message(
            BotData.TESTG_ID,
            message
        )

    async def request_document(self, user: UserDecorator, message_id: int, request: str):
        await self.__client.send_message(
            BotData.ADMIN_ID,
            MessageFormatter.generate_document_request(request, user.id, user.use, user.initials),
            buttons=Buttons.document(user.id, message_id)
        )