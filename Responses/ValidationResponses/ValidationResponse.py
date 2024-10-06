from abc import ABC, abstractmethod
from Responses.BaseResponse import BaseResponse


class ValidationResponse(BaseResponse, ABC):
    @abstractmethod
    async def is_valid(self, event):
        pass

    @abstractmethod
    async def on_valid(self, event):
        pass

    @abstractmethod
    async def on_invalid(self, event):
        pass

    async def handle(self, event):
        if await self.is_valid(event):
            await self.on_valid(event)
        else:
            await self.on_invalid(event)
