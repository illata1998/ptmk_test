from ptmk_test.db import EmployeeDB
from ptmk_test.config import DB_USER, DB_NAME, DB_PORT, DB_HOST, DB_PASSWORD


def get_db_connection() -> EmployeeDB:
    """
    Establishes and returns a connection to the employee database.

    This function loads environment variables from an .env file,
    retrieves database connection parameters, and creates an
    EmployeeDB instance with these parameters.

    Returns:
        EmployeeDB: An instance of the EmployeeDB class representing
                    the connection to the employee database.

    Environment Variables:
        DB_SERVER: The database server address.
        DB_USER: The username for database access.
        DB_PASSWORD: The password for database access.
        DB_NAME: The name of the database.
        DB_PORT: The port number for the database connection.
    """
    database = EmployeeDB(dbname=DB_NAME, user=DB_USER,
                          password=DB_PASSWORD, host=DB_HOST,
                          port=DB_PORT)
    return database
