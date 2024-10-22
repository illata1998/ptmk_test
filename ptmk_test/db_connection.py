import os
from dotenv import load_dotenv
from ptmk_test.db import EmployeeDB


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
    load_dotenv()
    db_server = os.getenv('DB_SERVER')
    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')
    db_name = os.getenv('DB_NAME')
    db_port = os.getenv('DB_PORT')
    database = EmployeeDB(dbname=db_name, user=db_user,
                          password=db_password, host=db_server,
                          port=db_port)
    return database
