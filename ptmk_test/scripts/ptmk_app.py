#!/user/bin/env python3


from ptmk_test.cli import parse_arguments
from ptmk_test.db_connection import get_db_connection
from ptmk_test.mode_1 import create_employees_table
from ptmk_test.mode_2 import create_and_save_employee
from ptmk_test.mode_3 import find_and_show_unique_employees
from ptmk_test.mode_4 import fill_employees_table
from ptmk_test.mode_5 import select_f_male_employees


def main():
    """
    This function serves as the entry point for the application and coordinates
    the execution of various database operations based on user input.

    This function performs the following steps:
    1. Establishes a database connection using get_db_connection().
    2. Parses command-line arguments using parse_arguments().
    3. Executes the appropriate database operation based on the specified mode:
       - Mode 1: Creates the employees table.
       - Mode 2: Creates and saves a new employee record.
       - Mode 3: Finds and displays unique employees.
       - Mode 4: Fills the employees table with generated data.
       - Mode 5: Selects and displays male employees whose names start with 'F'.

    The specific operation is determined by the 'mode' argument passed via the
    command line. Additional arguments (full_name, sex, date_of_birth) are
    required for Mode 2.

    """
    database = get_db_connection()
    args = parse_arguments()

    mode_functions = {
        '1': lambda: create_employees_table(database=database),
        '2': lambda: create_and_save_employee(
            database=database,
            full_name=args.full_name,
            sex=args.sex,
            date_of_birth=args.date_of_birth
        ),
        '3': lambda: find_and_show_unique_employees(database=database),
        '4': lambda: fill_employees_table(database),
        '5': lambda: select_f_male_employees(database=database)
    }

    mode_function = mode_functions.get(args.mode)
    mode_function()


if __name__ == '__main__':
    main()
