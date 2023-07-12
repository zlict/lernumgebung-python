import mysql.connector
from mysql.connector import Error

def create_server_and_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("[DEBUG] MariaDB Database-Server connection successful")
        print("[DEBUG] Database connection to {0} successful".format(db_name))
    except Error as err:
        print(f"[ERROR] '{err}'")

    return connection

def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"[ERROR] '{err}'")

db_connection = create_server_and_db_connection("mysql-server", "root", "root", "quiz")
questions_query = "SELECT * FROM question WHERE difficulty = 3;"
questions_query_results = read_query(db_connection, questions_query)

for question_query_result in questions_query_results:
      question_query_result = list(question_query_result)
      print("Id: {0}; Frage: {1}; Difficulty: {2}".format(question_query_result[0], question_query_result[1], question_query_result[2]))

      # TODO: Extend the code to show all Questions and it's possible Answers. If an answer is the correct one mark it with "*"