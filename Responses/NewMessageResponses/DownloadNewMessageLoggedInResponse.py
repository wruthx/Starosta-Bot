from Responses.NewMessageResponses.OnNewMessageResponse import OnNewMessageResponse
from Responses.ValidationResponses.LoggedInResponse import LoggedInResponse
from telethon.tl.types import InputPeerUser


class DownloadNewMessageLoggedInResponse(LoggedInResponse, OnNewMessageResponse):

    def __init__(self):
        super().__init__('.*')

    async def on_valid(self, event):
        if event.is_group and event.chat_id == "group_id":
            return

        if event.media:
            target_user = InputPeerUser(user_id="admin_id", access_hash=0)
            await event.client.send_file(target_user, event.media)
            await event.reply('Файл надіслано старості!')
