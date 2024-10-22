from ptmk_test.models import Employee
import datetime


def create_and_save_employee(
        database,
        full_name: str,
        sex: str,
        date_of_birth: str) -> None:
    """
    Creates an Employee object from passed parameters.
    Inserts the employee data to the database.
    """
    employee = Employee(
        full_name=full_name,
        date_of_birth=datetime.datetime.strptime(
            date_of_birth, "%Y-%m-%d"
        ).date(),
        sex=sex
    )
    database.insert_employee(employee)
    print(f'Employee {full_name} was inserted into '
          f'the database successfully.')
