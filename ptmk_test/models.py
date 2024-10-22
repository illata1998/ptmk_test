from dataclasses import dataclass
from typing import Optional
from datetime import date


@dataclass
class Employee:
    """
    Dataclass representing an employee entity.

    Attributes:
        full_name (str): The full name of the employee.
        date_of_birth (date): The date of birth of the employee.
        sex (str): The sex of the employee.
        age (Optional[int]): The age of the employee.
                             Defaults to None if not provided.
    """
    full_name: str
    date_of_birth: date
    sex: str
    age: Optional[int] = None
