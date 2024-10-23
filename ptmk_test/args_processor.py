from ptmk_test.cli import parse_arguments

def process_arguments() -> dict[str, str | None]:
    """
    Processes and validates the command-line arguments.

    Returns:
        dict: A dictionary containing validated arguments.

    Raises:
        ValueError: If the arguments are invalid for the selected mode.
    """
    args = parse_arguments()
    mode = args.mode
    full_name = args.full_name
    date_of_birth = args.date_of_birth
    sex = args.sex

    if mode == '2':
        if full_name is None:
            raise ValueError("'Full Name' argument must be provided for mode 2.")
        if date_of_birth is None:
            raise ValueError("'Date of Birth' argument must be provided for mode 2.")
        if sex is None:
            raise ValueError("'Sex' argument must be provided for mode 2.")
        if sex not in ['Male', 'Female']:
            raise ValueError("'Sex' argument must be either 'Male' or 'Female'.")
    else:
        if any((full_name, date_of_birth, sex)):
            raise ValueError("All arguments apart from 'mode' must be None for this mode.")

    return {'mode': mode, 'full_name': full_name, 'date_of_birth': date_of_birth, 'sex': sex}
