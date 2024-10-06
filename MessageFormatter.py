from Constants.Responses import Responses


class MessageFormatter:

    @staticmethod
    def generate_request(user_id: int, user_name: str = None, initials: str = None) -> str:
        if not user_name:
            return Responses.ON_REQUEST_BY_ID.format(user_id)

        if not initials:
            return Responses.ON_REQUEST_WITH_USE.format(user_id, user_name)

        return Responses.ON_REQUEST_FULL_INFO.format(user_id, user_name, initials)

    @staticmethod
    def generate_document_request(request: str, user_id: int, user_name: str = None, initials: str = None):
        if not user_name:
            return Responses.ON_DOCUMENT_REQUEST_GENERIC.format(request, user_id)

        if not initials:
            return Responses.ON_DOCUMENT_REQUEST_WITH_USE.format(request, user_id, user_name)

        return Responses.ON_DOCUMENT_REQUEST_WITH_NAME.format(request, user_id, user_name, initials)
