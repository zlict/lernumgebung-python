import mysql.connector
from mysql.connector import Error

def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("[DEBUG] MariaDB Database-Server connection successful")
    except Error as err:
        print(f"[ERROR] '{err}'")

    return connection

def create_database(db_connection, db_name):

    #TODO: Add connection commands and error handling


db_connection = create_server_connection("mysql-server", "root", "root")
create_database(db_connection, "quiz")
