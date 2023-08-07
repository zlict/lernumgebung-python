import mariadb
from mariadb import *

def create_server_and_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mariadb.connect(
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

def execute_query(db_connection, query):
    
    #TODO: Add execution commands and error handling
    

create_table_question_query = """
CREATE TABLE question (
    id INT AUTO_INCREMENT,
    question VARCHAR(255) NOT NULL,
    difficulty TINYINT(1) NOT NULL,
    PRIMARY KEY (id)
);
"""

create_table_answer_query = """
CREATE TABLE answer (
    id INT AUTO_INCREMENT,
    fk_question_id INT NOT NULL,
    answer VARCHAR(255) NOT NULL,
    isCorrect BOOLEAN NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (fk_question_id) REFERENCES question(id)
);
"""

create_table_score_query = """
CREATE TABLE score (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  difficulty TINYINT(1) NOT NULL,
  result_percent DECIMAL(3,2) NOT NULL,
  playedAt DATETIME NOT NULL DEFAULT NOW(),
  
  PRIMARY KEY (id)
);
"""

db_connection = create_server_and_db_connection("lernumgebung_mariadb-server", "root", "mariadb", "quiz")
execute_query(db_connection, create_table_question_query)
execute_query(db_connection, create_table_answer_query)
execute_query(db_connection, create_table_score_query)