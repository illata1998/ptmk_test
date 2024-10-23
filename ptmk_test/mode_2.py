from ptmk_test.models import Employee
from ptmk_test.db import EmployeeDB
from ptmk_test.args_validator import (validate_dob, validate_sex,
                                      validate_full_name)
import datetime


def create_and_save_employee(
        database: EmployeeDB,
        full_name: str,
        sex: str,
        date_of_birth: str) -> None:
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
        full_name = validate_full_name(full_name)
        date_of_birth = datetime.date.fromisoformat(validate_dob(date_of_birth))
        sex = validate_sex(sex)
        employee = Employee(
            full_name=full_name,
            date_of_birth=date_of_birth,
            sex=sex
        )
        database.insert_employee(employee)
        print(f'Employee {full_name} was inserted into the database successfully.')
    except Exception as e:
        print(f'Something went wrong: {e}')

