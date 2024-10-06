class Responses:
    ON_START = \
"""
Вітаю! 👋🏻 
Я - староста бот!
Не зареєстровані? /reg

Зареєстровані?
Щоб переглянути список доступних команд, натисніть /list
"""
    ON_NOTIFY_FAIL = 'Нема доступу'
    ON_LIST = \
"""
Список команд:
/dz - 📕 Надіслати Д/з, або будь-який інший файл
При надсиланні файлу перегляньте інструкцію. Файли зберігаються на комп'ютері старости.

/deadline - ‼️ Список дедлайнів
Цією командою можна переглянути список наявних дедлайнів з датами, темою та П.І.Б. викладача

/contacts - 🪪 Контакти викладачів
Всі важливі контакти викладачів за наявності та доступності (номер телефону, тег, імейл та через який месенджер зв'язуватись)

/rozklad - 📅 Розклад занять
Розклад занять на сьогодні

/document - 🖨️ Замовити документ
Замовити документ в деканаті через старосту. Напишіть ваш ПІБ та яку довідку потрібно
"""
    ON_DZ = \
"""

"""
    ON_DEADLINE = \
"""

"""
    ON_ROZKLAD = 'Натисніть на кнопку знизу, щоб отримати розклад на відповідний день.'
    ON_DOCUMENT = 'Для того, щоб надіслати запит на отримання документу, вкажіть інформацію про нього'
    ON_LINKS = \
"""

"""

    ON_REG = 'Окей! Очікуйте підтвердження'
    ON_REQUEST_GENERIC = 'Хоче отримати доступ до функціональності бота.\n Дозволити?'
    ON_ACCEPT_GENERIC = 'Вас додано до бота'
    ON_REJECT_GENERIC = 'Вас обеженно у використанні бота'
    BY_ID = 'Користувач з id `{0}` '
    WITH_USE = 'Користувач:\nID: {0}\nUse: {1}\n` '
    FULL_INFO = 'Користувач:\nID: {0}\nUse: {1}\nІмя: {2}\n'

    ON_REQUEST_BY_ID = BY_ID + ON_REQUEST_GENERIC
    ON_REQUEST_WITH_USE = WITH_USE + ON_REQUEST_GENERIC
    ON_REQUEST_FULL_INFO = FULL_INFO + ON_REQUEST_GENERIC

    ON_ACCEPT_BY_ID = BY_ID + ON_ACCEPT_GENERIC
    ON_ACCEPT_WITH_USE = WITH_USE + ON_ACCEPT_GENERIC
    ON_ACCEPT_FULL_INFO = FULL_INFO + ON_ACCEPT_GENERIC

    ON_REJECT_BY_ID = BY_ID + ON_REJECT_GENERIC
    ON_REJECT_WITH_USE = WITH_USE + ON_REJECT_GENERIC
    ON_REJECT_FULL_INFO = FULL_INFO + ON_REJECT_GENERIC

    ON_ACCEPTED_DOCUMENT_REQUEST = 'Дякуємо за звернення, очікуйте повідомлення про підтвердження!'

    ON_DOCUMENT_REQUEST_GENERIC = \
"""
Новий запит на документ!
"{0}"
Від користувача з ID {1}
"""

    ON_DOCUMENT_REQUEST_WITH_USE = (ON_DOCUMENT_REQUEST_GENERIC +
"""
Нік: {2}
""")

    ON_DOCUMENT_REQUEST_WITH_NAME = (ON_DOCUMENT_REQUEST_WITH_USE +
"""
Імʼя: {3}
""")

    ON_NOT_LOGGED_IN = 'Ти не зареєстрований!\nВикористай команду /reg'
    ON_NOT_ADMIN = 'Ти ніхто, щоб використовувати цю команду'
    IN_PROGRESS = 'Дана команда в розробці'

    ON_ACCEPT = 'Вас було додано до функціоналу бота!\nСкористайтесь командою /list'
    ON_REJECT = 'У доступі відмовлено.'

    ON_ALREADY_REGISTERED = 'Ви вже зареєстровані!'

    ON_INFO = \
"""

"""

    ON_ONLINE = \
"""

"""

    ON_SCHEDULE = {
            "Понеділок":
    """

""",
        "Вівторок":
"""

""",
        "Середа":
"""

""",
        "Четвер":
"""

""",
        "Пʼятниця":
"""

""",
        "Субота":
"""

"""
    }

    NO_DAY = 'Вибраного дня не існує'
