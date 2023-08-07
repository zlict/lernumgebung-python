import mariadb
from mariadb import *

def create_server_connection(host_name, user_name, user_password):

    #TODO: Add connection commands and error handling

    return connection

def create_server_and_db_connection(host_name, user_name, user_password, db_name):

    #TODO: Add connection commands and error handling

    return connection

db_connection = create_server_connection("lernumgebung_mariadb-server", "root", "mariadb")
db_connection = create_server_and_db_connection("lernumgebung_mariadb-server", "root", "mariadb", "quiz")
