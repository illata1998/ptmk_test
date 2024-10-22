import psycopg2
from psycopg2.extras import NamedTupleCursor, execute_values
from psycopg2.extensions import cursor
from ptmk_test.models import Employee


class EmployeeDB:
    """
    PostgreSQL employees database class.
    """
    def __init__(self, dbname: str, user: str, password: str,
                 host: str, port: str,
                 cursor_factory: cursor = NamedTupleCursor) -> None:
        """
        Initializes the database connection with provided
        connection parameters: the database name,
        username, user password, database host address,
        connection port number.
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
        Creates the 'employees' table and an index for it
        on the 'full_name' and 'sex' fields.
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
        Takes one Employee class object and
        inserts its data into the 'employees' table.
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
        Selects employees from the 'employees' table with
        the unique combination of 'full_name' and 'date_of_birth'
        fields and returns a list of Employee objects.
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

    def bulk_insert_employees(self, employees: tuple) -> None:
        """
        Takes a tuple of employees' data
        and inserts it the 'employees' table.
        """
        with self.conn.cursor() as cur:
            sql = """
            INSERT INTO employees (full_name, date_of_birth, sex) values %s
            """
            execute_values(cur, sql, employees)
            self.conn.commit()

    def fetch_employees_by_first_letter(self, first_letter: str) -> list[Employee]:
        """
        Fetches employees from the 'employees' table
        according to two criteria: first letter of their name
        and their sex, which are passed as parameters.
        Returns a list of Employee objects.
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
            cur.execute(sql, {'first_letter': first_letter + '%%',})
            for row in cur.fetchall():
                employees.append(Employee(
                    full_name=row.full_name,
                    date_of_birth=row.date_of_birth,
                    sex=row.sex,
                    age=row.age
                ))
        return employees
