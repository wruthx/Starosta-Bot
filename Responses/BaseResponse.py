from abc import ABC, abstractmethod


class BaseResponse(ABC):
    def __init__(self, pattern: str):
        self.bot = None
        self.pattern = pattern

    @abstractmethod
    async def handle(self, event):
        pass

    @abstractmethod
    def bind(self):
        pass

    def add(self, bot):
        self.bot = bot
        self.bind()
