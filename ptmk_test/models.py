from dataclasses import dataclass
from typing import Optional
from datetime import date


@dataclass
class Employee:
    """
    Dataclass for an 'employee' entity.
    """
    full_name: str
    date_of_birth: date
    sex: str
    age: Optional[int] = None