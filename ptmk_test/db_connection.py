import os
from dotenv import load_dotenv
from ptmk_test.db import EmployeeDB


def get_db_connection():
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
