from ptmk_test.models import Employee
from ptmk_test.db import EmployeeDB
import datetime


def create_and_save_employee(database: EmployeeDB, **kwargs: dict) -> None:
    """
    Creates an Employee object and saves it to the database.

    This function creates an Employee object using the provided parameters,
    converts the date_of_birth string to a datetime.date object,
    and then inserts the employee data into the database.

    Args:
        database (EmployeeDB): An instance of the EmployeeDB class
                               representing the database connection.
        full_name (str): The full name of the employee.
        sex (str): The sex of the employee.
        date_of_birth (str): The date of birth of the employee
                             in the format "YYYY-MM-DD".
    """
    try:
        employee = Employee(
            full_name=kwargs['full_name'],
            date_of_birth=datetime.date.fromisoformat(kwargs['date_of_birth']),
            sex=kwargs['sex']
        )
        database.insert_employee(employee)
        print(f'Employee {kwargs["full_name"]} was inserted into the '
              f'database successfully.')
    except Exception as e:
        print(f'An error occurred while saving the employee: {e}')
