import random
import string
import datetime
from ptmk_test.models import Employee


def generate_fake_date(start_year: int, finish_year: int) -> datetime.date:
    """
    Generates a fake date between two years
    which are passed as parameters.
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
    Generates a fake sex. Chooses between 'Male' and 'Female'.
    """
    return random.choice(['Male', 'Female'])


def generate_fake_name(
        first_letter: str | None = None,
        length: int = 5) -> str:
    """
    Generates a fake name-like string of the provided length starting with
    the provided first letter (else - with a random letter).
    """
    fake_name = first_letter if first_letter else random.choice(string.ascii_uppercase)
    return fake_name + ''.join(random.choice(string.ascii_lowercase)
                    for _ in range(length))


def generate_fake_employee(
        n: int,
        first_letter: str = None,
        predefined_sex: str = None):
    """
    Creates a generator iterator which produces a series of
    fake Employee objects. The first letter of
    the employee's full name and the employee's sex
    can be passes as parameters.
    """
    for _ in range(n):
        sex = predefined_sex if predefined_sex else generate_fake_sex()
        full_name = (generate_fake_name(first_letter=first_letter) + ' ' +
                     generate_fake_name() + ' ' + generate_fake_name())
        date_of_birth = generate_fake_date(1924, 2006)
        yield Employee(
            full_name=full_name,
            sex=sex,
            date_of_birth=date_of_birth
        )
