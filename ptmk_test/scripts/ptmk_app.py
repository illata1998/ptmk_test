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
    Manages the employees database according to
    provided parameters parsed from the command line.
    """
    database = get_db_connection()
    args = parse_arguments()

    match args.mode:
        case '1':
            create_employees_table(database=database)
        case '2':
            create_and_save_employee(
                database=database,
                full_name=args.full_name,
                sex=args.sex,
                date_of_birth=args.date_of_birth
            )
        case '3':
            find_and_show_unique_employees(database=database)
        case '4':
            fill_employees_table(database)
        case '5':
            select_f_male_employees(database=database)


if __name__ == '__main__':
    main()
