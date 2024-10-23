from ptmk_test.db import EmployeeDB


def create_employees_table(database: EmployeeDB, **kwargs: dict) -> None:
    """
    Creates the 'employees' table in the database.

    This function attempts to create the 'employees' table using the provided
    database connection. If successful, it prints a success message. If an
    exception occurs during the process, it catches the exception and prints
    an error message.

    Args:
        database (EmployeeDB): An instance of the EmployeeDB class
                               representing the database connection.
    """
    try:
        database.create_employees_table()
        print('Table "employees" was successfully created.')
    except Exception as e:
        print(f'An error occurred while creating the "employees" table: {e}')
