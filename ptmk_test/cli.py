import argparse


def parse_arguments() -> argparse.Namespace:
    """
    Parses command line arguments for the employee database management tool.

    This function sets up an ArgumentParser to handle the following arguments:
    - mode: Required. Choices are '1', '2', '3', '4', or '5', representing
            different operating modes.
    - full_name: Optional. The employee's full name (only used in mode 2).
    - date_of_birth: Optional. The employee's date of birth (only used in
                     mode 2).
    - sex: Optional. The employee's sex (only used in mode 2).

    Returns:
        argparse.Namespace: An object containing the parsed
                            arguments as attributes.
    """
    parser = argparse.ArgumentParser(
        prog='ptmk_test',
        description='Tool for managing the employee database.')

    # Operating mode of the application:
    parser.add_argument('mode', choices=['1', '2', '3', '4', '5'],
                        metavar='MODE', help="Set the app's operating mode",
                        type=str)

    # Full Name argument
    parser.add_argument('full_name', nargs='?',
                        metavar='FULL NAME',
                        help="Employee's full name (required for mode 2)",
                        type=str)

    # Date of Birth argument
    parser.add_argument('date_of_birth', nargs='?',
                        metavar='DATE OF BIRTH',
                        help="Employee's date of birth (required for mode 2)",
                        type=str)

    # Sex argument
    parser.add_argument('sex', nargs='?',
                        metavar='SEX',
                        help="Employee's sex (required for mode 2)",
                        type=str)

    return parser.parse_args()
