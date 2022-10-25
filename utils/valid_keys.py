from accounts.exceptions import InvalidFieldsException


def is_valid_keys(invalid_keys: set, request_data: dict) -> None:
    invalid_fields = invalid_keys.intersection(request_data)

    if invalid_fields:
        error_fields = [
            {f'{field}': f'You can not update {field} property.'}
            for field in invalid_fields
        ]
        raise InvalidFieldsException(error_fields)
