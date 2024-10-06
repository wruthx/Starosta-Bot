from telethon import Button
from telethon.tl.types import KeyboardButtonCallback


class Buttons:
    @staticmethod
    def register(user_id: int) -> [KeyboardButtonCallback]:
        return [
            Button.inline("👍", f'Accept,{user_id}'),
            Button.inline("👎", f'Decline,{user_id}')
        ]

    @staticmethod
    def schedule() -> [[KeyboardButtonCallback]]:
        return [
            [
                Button.inline("Понеділок"),
                Button.inline("Вівторок")
            ],
            [
                Button.inline("Середа"),
                Button.inline("Четвер")
            ],
            [
                Button.inline("Пʼятниця"),
                Button.inline("Субота")
            ]
        ]

    @staticmethod
    def document(user_id: int, message_id: int) -> [KeyboardButtonCallback]:
        return [
            Button.inline('Опрацювання', f'Опрацювання,{user_id},{message_id}')
        ]

    @staticmethod
    def document_proceed(user_id: int, message_id: int) -> [KeyboardButtonCallback]:
        return [
            Button.inline('Готово', f'Готово,{user_id},{message_id}')
        ]