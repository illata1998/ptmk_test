import argparse


def parse_arguments():
    """
    Parses command line strings into Python objects.
    """
    parser = argparse.ArgumentParser(
        prog='ptmk_test',
        description='Tool for managing the employee database.')
    # Operating mode of the application:
    parser.add_argument('mode', choices=['1', '2', '3', '4', '5'],
                        metavar='MODE', help="set the app's operating mode")
    # Full Name argument
    parser.add_argument('full_name', nargs='?',
                        metavar='FULL NAME',
                        help="employee's full name FOR MODE 2 ONLY")
    # Date of Birth argument
    parser.add_argument('date_of_birth', nargs='?',
                        metavar='DATE OF BIRTH',
                        help="employee's date of birth FOR MODE 2 ONLY")
    # Sex argument
    parser.add_argument('sex', nargs='?',
                        metavar='SEX', help="employee's sex FOR MODE 2 ONLY")
    return parser.parse_args()
