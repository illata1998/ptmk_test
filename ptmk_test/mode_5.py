import time
from tabulate import tabulate


def select_f_male_employees(database):
    """
    Fetches male employees whose names start with the letter 'F'
    from the 'employees' table. Measures the execution time of
    this operation. Prints out the found employees in the form
    of tabular data.
    """
    start_time = time.time()
    employees = database.fetch_employees_by_first_letter(first_letter='F')
    run_time = "--- %s seconds ---" % (time.time() - start_time)
    headers = ["Full Name", "Date of Birth", "Sex", "Age"]
    print(tabulate(employees, headers=headers, tablefmt="fancy_grid"))
    print(run_time)
