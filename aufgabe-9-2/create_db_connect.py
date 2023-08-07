import mariadb
from mariadb import *

def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mariadb.connect(
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


db_connection = create_server_connection("lernumgebung_mariadb-server", "root", "mariadb")
create_database(db_connection, "quiz")
