def handle_error_serializer(errors: dict):
    for key, value in errors.items():
        if key == "non_field_errors":
            return value
        if isinstance(value, dict):
            errors[key] = handle_error_serializer(value)
    return errors
