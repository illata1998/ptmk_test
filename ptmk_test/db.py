import psycopg2
import datetime
from typing import Generator
from psycopg2.extras import NamedTupleCursor, execute_values
from ptmk_test.models import Employee


class EmployeeDB:
    """
    PostgreSQL employees database class.

    This class provides an interface for interacting with a PostgreSQL database
    containing employee information. It includes methods for creating tables,
    inserting and fetching employee data, and performing specialized queries.

    Attributes:
        conn (psycopg2.extensions.connection): The database connection object.
    """

    def __init__(
            self, dbname: str, user: str, password: str,
            host: str, port: str,
            cursor_factory: psycopg2.extensions.cursor = NamedTupleCursor
    ) -> None:
        """
        Initializes the database connection with provided connection parameters.

        Args:
            dbname (str): The name of the database.
            user (str): The username for database access.
            password (str): The password for database access.
            host (str): The database server address.
            port (str): The port number for the database connection.
            cursor_factory (cursor, optional): The cursor factory to use.
                                               Defaults to NamedTupleCursor.

        Raises:
            Exception: If the connection to the database fails.
        """
        try:
            self.conn = psycopg2.connect(
                dbname=dbname,
                user=user,
                password=password,
                host=host,
                port=port,
                cursor_factory=cursor_factory
            )
        except Exception as e:
            print(f'Something went wrong: {e}')

    def create_employees_table(self) -> None:
        """
        Creates the 'employees' table and a view for male employees.

        This method creates a table named 'employees' with columns for
        id, full_name, date_of_birth, and sex. It also creates a view
        named 'male_employees' that selects all male employees from
        the 'employees' table.
        """
        with self.conn.cursor() as cur:
            sql = """
            CREATE TABLE employees (
                id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
                full_name VARCHAR(100),
                date_of_birth DATE,
                sex VARCHAR(6)
            );
            CREATE VIEW male_employees AS
            SELECT
                id,
                full_name,
                date_of_birth,
                sex
            FROM employees
            WHERE sex = 'Male';
            """
            cur.execute(sql)
            self.conn.commit()

    def insert_employee(self, employee: Employee) -> None:
        """
        Inserts a single employee into the 'employees' table.

        Args:
            employee (Employee): An Employee object containing the data
                                 to be inserted.
        """
        with self.conn.cursor() as cur:
            cur.execute(
                "INSERT INTO employees (full_name, date_of_birth, sex)"
                "VALUES (%s, %s, %s) RETURNING id;",
                (employee.full_name, employee.date_of_birth, employee.sex)
            )
            self.conn.commit()

    def fetch_unique_employees(self) -> list[Employee]:
        """
        Fetches unique employees from the 'employees' table.

        This method selects employees with unique combinations of 'full_name'
        and 'date_of_birth', calculates their age, and returns them as a list
        of Employee objects.

        Returns:
            list[Employee]: A list of unique Employee objects.
        """
        employees = []
        with self.conn.cursor() as cur:
            sql = """
            SELECT DISTINCT ON (full_name, date_of_birth)
                full_name,
                date_of_birth,
                sex,
                DATE_PART('YEAR', AGE(NOW(), date_of_birth)) AS age
            FROM employees
            ORDER BY full_name;
            """
            cur.execute(sql)
            for row in cur.fetchall():
                employees.append(Employee(
                    full_name=row.full_name,
                    date_of_birth=row.date_of_birth,
                    sex=row.sex,
                    age=row.age
                ))
        return employees

    def bulk_insert_employees(self, employees: Generator[
        tuple[str, datetime.date, str], None, None
    ]) -> None:
        """
        Inserts multiple employees into the 'employees' table in a single
        operation.

        Args:
            employees (tuple): A tuple of employee data to be inserted.
        """
        with self.conn.cursor() as cur:
            sql = """
            INSERT INTO employees (full_name, date_of_birth, sex) values %s
            """
            execute_values(cur, sql, employees)
            self.conn.commit()

    def fetch_male_employees_by_first_letter(
            self, first_letter: str
    ) -> list[Employee]:
        """
        Fetches male employees whose names start with a specific letter.

        This method queries the 'male_employees' view to retrieve employees
        whose full names start with the specified letter. It also calculates
        their age.

        Args:
            first_letter (str): The first letter of the employee's name
                                to search for.

        Returns:
            list[Employee]: A list of Employee objects matching the criteria.
        """
        employees = []
        with self.conn.cursor() as cur:
            sql = """
            SELECT
                full_name,
                date_of_birth,
                sex,
                DATE_PART('YEAR', AGE(NOW(), date_of_birth)) AS age
            FROM male_employees
            WHERE full_name LIKE %(first_letter)s;
            """
            cur.execute(sql, {'first_letter': first_letter + '%%'})
            for row in cur.fetchall():
                employees.append(Employee(
                    full_name=row.full_name,
                    date_of_birth=row.date_of_birth,
                    sex=row.sex,
                    age=row.age
                ))
        return employees
