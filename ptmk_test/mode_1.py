import psycopg2


def create_employees_table(database) -> None:
    """
    Creates the 'employees' table.
    Prints out a successful message or an error.
    """
    try:
        database.create_employees_table()
        print('Table "employees" was successfully created.')
    except Exception as e:
        print(f'Something went wrong: {e}')
