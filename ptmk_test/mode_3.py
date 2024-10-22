from tabulate import tabulate


def find_and_show_unique_employees(database):
    """
    Fetches employees with unique full_name and
    date_of_birth fields from the 'employees' table.
    Prints out the found employees in the form of tabular data
    or a message if no entities were found.
    """
    employees = database.find_unique_employees()
    if employees:
        headers = ["Full Name", "Date of Birth", "Sex", "Age"]
        print(tabulate(employees, headers=headers, tablefmt="fancy_grid"))
    else:
        print('No entities were found.')
