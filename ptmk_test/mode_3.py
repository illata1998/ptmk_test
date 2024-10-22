from tabulate import tabulate
from ptmk_test.db import EmployeeDB


def find_and_show_unique_employees(database: EmployeeDB):
    """
    Fetches and displays unique employees from the database.

    This function retrieves employees with unique combinations of full name and
    date of birth from the 'employees' table in the database. It then displays
    the results in a formatted table or prints a message if no employees are
    found.

    Args:
        database (EmployeeDB): An instance of the EmployeeDB class representing
                               the connection to the employee database.
    """
    employees = database.fetch_unique_employees()
    if employees:
        headers = ["Full Name", "Date of Birth", "Sex", "Age"]
        print(tabulate(employees, headers=headers, tablefmt="fancy_grid"))
    else:
        print('No entities were found.')
