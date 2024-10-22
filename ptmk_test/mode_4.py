from ptmk_test.fake_employee_generator import generate_fake_employee


# The number of employee entities to add to the database.
EMPLOYEES_COUNT = 1000000

# The number of male employees whose names start with
# the letter 'F' to add to the database.
MALE_F_EMPLOYEES_COUNT = 100


def fill_employees_table(database):
    """
    Generates fake Employee objects, extracts data from
    those objects and bulk inserts it to the 'employees'
    table.
    """
    # Simple fake employees
    employees = ((emp.full_name, emp.date_of_birth, emp.sex)
                 for emp in generate_fake_employee(EMPLOYEES_COUNT))
    database.bulk_insert_employees(employees)
    print(f'{EMPLOYEES_COUNT} fake employees were inserted successfully.')

    # Male employees with 'F...'-like last name
    employees = ((emp.full_name, emp.date_of_birth, emp.sex)
                 for emp in generate_fake_employee(MALE_F_EMPLOYEES_COUNT,
                                                   first_letter='F',
                                                   predefined_sex='Male'))
    database.bulk_insert_employees(employees)
    print(f'{MALE_F_EMPLOYEES_COUNT} '
          f'fake male employees whose names start with '
          f'"F" were inserted successfully.')
