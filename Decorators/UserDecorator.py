from Constants.BotData import BotData


class UserDecorator:
    def __init__(self, client):
        self.__client = client
        self.__user = None

    async def load(self) -> 'UserDecorator':
        if not self.__user:
            self.__user = await self.__client.get_sender()
        return self

    @property
    def id(self) -> int:
        return self.__user.id

    @property
    def is_admin(self):
        try:
            return self.id == BotData.ADMIN_ID
        except AttributeError:
            return False

    @property
    def is_allowed(self) -> bool:
        try:
            return self.id in BotData.ALLOWED_ID
        except AttributeError:
            return False

    @property
    def use(self):
        if not self.__user.username:
            return None
        return '@' + self.__user.username

    @property
    def initials(self):
        if not self.__user.first_name and self.__user.last_name:
            return None

        return ' '.join([str(item) for item in [self.__user.first_name, self.__user.last_name] if item is not None])
