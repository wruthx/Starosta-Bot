class MessageDecorator:
    def __init__(self, message):
        self.__message = message

    @property
    def content(self) -> str:
        return self.__message.message
