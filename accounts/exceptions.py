from rest_framework.exceptions import ValidationError


class InvalidFieldsException(ValidationError):
    status_code = 403
