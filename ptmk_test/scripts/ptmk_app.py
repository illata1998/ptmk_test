from ptmk_test.cli import parse_arguments
from ptmk_test.db_connection import get_db_connection
from ptmk_test.modes.mode_selector import get_mode_function
from ptmk_test.args_processor import process_arguments


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


    try:
        database = get_db_connection()
        validated_args = process_arguments()
        mode_function = get_mode_function(validated_args['mode'])
        mode_function(database, **validated_args)
    except Exception as e:
        print(f'Something went wrong: {e}')


if __name__ == '__main__':
    main()
