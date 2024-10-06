from os import environ
from telethon import TelegramClient

from threading import Thread
from Constants.Buttons import Buttons
from Constants.Responses import Responses
from Responses.CallbackResponses.DocumentCallbackResponse import DocumentCallbackResponse
from Responses.CallbackResponses.ScheduleCallbackResponse import ScheduleCallbackResponse
from Responses.NewMessageResponses.DocumentNewMessageLoggedInResponse import DocumentNewMessageLoggedInResponse
from Responses.NewMessageResponses.DownloadNewMessageLoggedInResponse import DownloadNewMessageLoggedInResponse
from Responses.NewMessageResponses.NewMessageGuestResponse import NewMessageGuestResponse
from Responses.NewMessageResponses.DefaiultNewMessageLoggedInResponse import DefaultNewMessageLoggedInResponse
from Responses.NewMessageResponses.PinNewMessageAdminResponse import PinNewMessageAdminResponse
from Responses.NewMessageResponses.PinNewMessageSpamAdminInResponse import PinNewMessageSpamAdminInResponse
from Responses.NewMessageResponses.RegistrationResponse import RegistrationResponse
from Responses.CallbackResponses.RegistrationCallbackResponse import RegistrationCallbackResponse

ALL_RESPONSES = [
    RegistrationResponse('/reg'),
    RegistrationCallbackResponse('^Accept', Responses.ON_ACCEPT_GENERIC),
    RegistrationCallbackResponse('^Decline', Responses.ON_REJECT_GENERIC),
    NewMessageGuestResponse('/start', Responses.ON_START),
    DefaultNewMessageLoggedInResponse('/list', Responses.ON_LIST),
    DefaultNewMessageLoggedInResponse('/contacts', Responses.ON_INFO),
    DefaultNewMessageLoggedInResponse('/online', Responses.ON_ONLINE),
    DocumentNewMessageLoggedInResponse(),
    DocumentCallbackResponse(),
    PinNewMessageAdminResponse('^/notify'),
    PinNewMessageSpamAdminInResponse('^/spam'),
    DownloadNewMessageLoggedInResponse(),
    DefaultNewMessageLoggedInResponse('/dz', Responses.ON_DZ),
    DefaultNewMessageLoggedInResponse('/rozklad', Responses.ON_ROZKLAD, buttons=Buttons.schedule()),
    ScheduleCallbackResponse('Понеділок|Вівторок|Середа|Четвер|Пʼятниця|Субота'),
    DefaultNewMessageLoggedInResponse('/links', Responses.ON_LINKS),
    DefaultNewMessageLoggedInResponse('/deadline', Responses.ON_DEADLINE)
]


class MonitorBot:
    def __init__(self):
        self.client = TelegramClient('anon',
                                     int(environ['API_ID']),
                                     environ['API_HASH']).start(bot_token=environ['API_TOKEN'])
        self.logged_users = []
        self.__init_users()
        self.__init_replies()

    def __init_users(self):
        with open('registered.txt') as file:
            self.logged_users = [int(id) for id in file.readlines()]

    def register(self, user_id):
        if self.is_logged(user_id):
            return
        self.logged_users.append(user_id)
        with open('registered.txt', 'a') as file:
            file.write(str(user_id) + '\n')

    def __init_replies(self):
        for reply in ALL_RESPONSES:
            reply.add(self)

    def main(self):
        with self.client:
            self.client.loop.run_forever()

    def is_logged(self, user_id: int) -> bool:
        return user_id in self.logged_users
