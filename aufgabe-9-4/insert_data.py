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
    cursor = db_connection.cursor()
    try:
        cursor.execute(query)
        db_connection.commit()
        print("[DEBUG] Query successful")
    except Error as err:
        print(f"[ERROR] '{err}'")


insert_data_question_query = """
INSERT INTO question (question, difficulty) VALUES
    ('Wie alt ist die Schweiz', 1),
    ('Wie viele Bundesräte hat die Schweizer Eidgenossenschaft', 1),
    ('Welche ist die längste Autobahn?', 3),
    ('Wie viele Einwohner hat die Schweiz?', 2),
    ('Wie viele Quadratkilemter umfasst die Schweiz?', 3),
    ('Wie viele Landessprachen hat die Schweiz?', 2),
    ('Wie viele Kanton gibt es in der Schweiz?', 2),
    ('Wie viele Nachbarländer hat die Schweiz?', 3),
    ('Welcher ist der höchste Berg in der Schweiz?', 3);
"""

insert_data_answer_query = """
INSERT INTO answer (fk_question_id, answer, is_correct) VALUES
    (1, "732 Jahre", 1),
    (1, "300 Jahre", 0),
    (1, "100 Jahre", 0),
    (1, "632 Jahre", 0),
    (2, "7", 1),
    (2, "6", 0),
    (2, "5", 0),
    (2, "8", 0),
    (3, "A1", 1),
    (3, "A3", 0),
    (3, "A8", 0),
    (3, "A4", 0),
    (4, "8.7 Mio", 1),
    (4, "4.2 Mio", 0),
    (4, "10.4 Mio", 0),
    (4, "1.1 Mio", 0),
    (5, "41.285 km2", 1),
    (5, "11.567 km2", 0),
    (5, "150.912 km2", 0),
    (5, "53.277 km2", 0),
    (6, "4", 1),
    (6, "3", 0),
    (6, "2", 0),
    (6, "5", 0),
    (7, "26", 1),
    (7, "28", 0),
    (7, "20", 0),
    (7, "24", 0),
    (8, "5", 1),
    (8, "4", 0),
    (8, "3", 0),
    (8, "6", 0),
    (9, "Dufourspitze", 1),
    (9, "Mont-Fort", 0),
    (9, "Rigi", 0),
    (9, "Pilatus", 0);
"""

insert_data_score_query = """
INSERT INTO score (name, difficulty, result_percent, played_at) VALUES
  ("Hans Muster", 1, 0.99, "2023-07-12 11:33:12"),
  ("Leanra Müller", 3, 0.34, "2023-07-12 11:19:34"),
  ("Jasmin Känzig", 2, 0.67, "2023-07-12 11:15:29"),
  ("Andreas Richter", 1, 0.81, "2023-07-12 11:27:40");
"""

db_connection = create_server_and_db_connection("lernumgebung_mariadb-server", "root", "mariadb", "quiz")

# Rufen Sie die Funktion execute_query(...) mit den entsprechenden Variabeln um die Drei Tabellen mit Daten zu befüllen.