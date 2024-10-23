def validate_full_name(full_name_arg: str) -> str:
    """
    Validates the full name argument.

    Args:
        full_name_arg (str): The full name to validate.

    Returns:
        str: The validated full name.

    Raises:
        ValueError: If the full name argument is not provided.
    """
    if not full_name_arg:
        raise ValueError("'Full Name' argument must be provided.")
    return full_name_arg


def validate_sex(sex_arg: str) -> str:
    """
    Validates the sex argument.

    Args:
        sex_arg (str): The sex to validate.

    Returns:
        str: The validated sex.

    Raises:
        ValueError: If the sex argument is not provided or is not 'Male' or 'Female'.
    """
    if not sex_arg:
        raise ValueError("'Sex' argument must be provided.")
    if sex_arg not in ['Male', 'Female']:
        raise ValueError("'Sex' argument must be either 'Male' or 'Female'")
    return sex_arg


def validate_dob(dob_arg: str) -> str:
    """
    Validates the date of birth argument.

    Args:
        dob_arg (str): The date of birth to validate.

    Returns:
        str: The validated date of birth.

    Raises:
        ValueError: If the date of birth argument is not provided.
    """
    if not dob_arg:
        raise ValueError("'Date of Birth' argument must be provided.")
    return dob_arg
