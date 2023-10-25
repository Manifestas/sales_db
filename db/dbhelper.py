import sqlite3


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("Successfully connected to the database")
    except sqlite3.Error as err:
        print(f"Error: '{err}'")

    return conn


def execute_query(connection, query):
    if connection is not None:
        cursor = connection.cursor()
        try:
            cursor.execute(query)
            connection.commit()
            print("Query successful")
        except sqlite3.DatabaseError as err:
            print(f"Error: '{err}'")
    else:
        print("Database is not connected")


def execute_read_query(connection, query):
    result = None
    if connection is not None:
        cursor = connection.cursor()
        try:
            cursor.execute(query)
            result = cursor.fetchall()
        except sqlite3.Error as e:
            print(f"The error '{e}' occurred")
    else:
        print("Database is not connected")

    return result

