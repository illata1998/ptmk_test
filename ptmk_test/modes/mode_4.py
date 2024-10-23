from ptmk_test.fake_employee_generator import generate_fake_employee
from ptmk_test.db import EmployeeDB


# The number of random employee entities to add to the database.
RANDOM_EMPLOYEES_COUNT = 1000000

# The number of male employees whose names start with
# the letter 'F' to add to the database.
MALE_F_NAME_EMPLOYEES_COUNT = 100


def fill_employees_table(database: EmployeeDB, **kwargs: dict) -> None:
    """
    Fills the 'employees' table with fake employee data.

    This function generates two sets of fake employee data and
    inserts them into the database:
    1. A large set of random employees
    2. A smaller set of male employees with names starting with 'F'

    Args:
        database (EmployeeDB): An instance of the EmployeeDB class
                               representing the database connection.
    """
    # Generate and insert random employees
    try:
        # Generate and insert random employees
        employees = ((emp.full_name, emp.date_of_birth, emp.sex)
                     for emp in generate_fake_employee(RANDOM_EMPLOYEES_COUNT))
        database.bulk_insert_employees(employees)
        print(f'{RANDOM_EMPLOYEES_COUNT} fake employees '
              f'were inserted successfully.')

        # Generate and insert male employees with names starting with 'F'
        employees = ((emp.full_name, emp.date_of_birth, emp.sex)
                     for emp in generate_fake_employee(MALE_F_NAME_EMPLOYEES_COUNT,
                                                       first_letter='F',
                                                       predefined_sex='Male'))
        database.bulk_insert_employees(employees)
        print(f'{MALE_F_NAME_EMPLOYEES_COUNT} '
              f'fake male employees whose names start with '
              f'"F" were inserted successfully.')
    except Exception as e:
        print(f'An error occurred while bulk inserting employees: {e}')
