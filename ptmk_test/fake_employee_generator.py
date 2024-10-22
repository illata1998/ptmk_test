import random
import string
import datetime
from ptmk_test.models import Employee
from typing import Generator


def generate_fake_date(start_year: int, finish_year: int) -> datetime.date:
    """
    Generates a fake date between two specified years.

    Args:
        start_year (int): The lower bound year for the generated date.
        finish_year (int): The upper bound year for the generated date.

    Returns:
        datetime.date: A randomly generated date within the specified
                       year range.
    """
    year = random.randint(start_year, finish_year)
    month = random.randint(1, 12)
    if month == 2:
        # February has 28 days
        day = random.randint(1, 28)
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        # January, March, May, July, August, October, December
        # each have 31 days
        day = random.randint(1, 31)
    else:
        # other months have 30 days
        day = random.randint(1, 30)
    return datetime.date(year, month, day)


def generate_fake_sex() -> str:
    """
    Generates a random sex.

    Returns:
        str: Either 'Male' or 'Female', chosen randomly.
    """
    return random.choice(['Male', 'Female'])


def generate_fake_name(
        first_letter: str | None = None,
        length: int = 5) -> str:
    """
    Generates a fake name-like string.

    Args:
        first_letter (str | None, optional): The first letter of the name.
                                             If None, a random uppercase letter
                                             is used. Defaults to None.
        length (int, optional): The length of the name (excluding the first
                                letter). Defaults to 5.

    Returns:
        str: A generated name-like string.
    """
    first_letter = first_letter or random.choice(string.ascii_uppercase)
    return first_letter + ''.join(
        random.choices(string.ascii_lowercase, k=length)
    )


def generate_fake_employee(
        n: int,
        first_letter: str | None = None,
        predefined_sex: str | None = None) -> Generator[Employee, None, None]:
    """
    Creates a generator that yields a series of fake Employee objects.

    Args:
        n (int): The number of fake employees to generate.
        first_letter (str, optional): The first letter of the employee's
                                      full name. If None, a random letter
                                      is used. Defaults to None.
        predefined_sex (str, optional): The sex of the employee. If None,
                                        a random sex is generated. Defaults
                                        to None.

    Yields:
        Employee: A fake Employee object with randomly generated attributes.
    """
    for _ in range(n):
        sex = predefined_sex or generate_fake_sex()
        full_name = ' '.join([
            generate_fake_name(first_letter=first_letter),
            generate_fake_name(),
            generate_fake_name()
        ])
        date_of_birth = generate_fake_date(1924, 2006)
        yield Employee(full_name=full_name, sex=sex,
                       date_of_birth=date_of_birth)
