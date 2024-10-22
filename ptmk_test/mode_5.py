import time
from tabulate import tabulate
from ptmk_test.db import EmployeeDB


def select_f_male_employees(database: EmployeeDB):
    """
    Fetches and displays male employees whose names start with
    the letter 'F' from the database.

    Args:
        database (EmployeeDB): An instance of the EmployeeDB class representing
                               the connection to the employee database.
    """
    start_time = time.time()
    employees = database.fetch_male_employees_by_first_letter(first_letter='F')
    run_time = "--- %s seconds ---" % (time.time() - start_time)
    headers = ["Full Name", "Date of Birth", "Sex", "Age"]
    print(tabulate(employees, headers=headers, tablefmt="fancy_grid"))
    print(run_time)
