import mysql.connector
from mysql.connector import Error

def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Connection to MariaDB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection


def transform_db(connection, query_sql):
    cursor = connection.cursor()
    try:
        cursor.execute(query_sql)
        connection.commit()
        print("Query successfully")
    except Error as e:
        print(f"The error '{e}' occurred")
        
def write_to_db(connection, query, data):
    cursor = connection.cursor()
    try:
        cursor.execute(query, data)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def read_from_db(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")
        return None

# Example usage
if __name__ == "__main__":
    connection = create_connection("maria-db", "admin", "admin", "metastore_db")
    
    # Create table
    create_table_query = """
    CREATE TABLE IF NOT EXISTS potencial_clients (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        surname VARCHAR(255) NOT NULL
    )
    """
    transform_db(connection, create_table_query)
    
    # Write to DB
    insert_query = """
    INSERT INTO potencial_clients (name, surname) VALUES (%s, %s)
    """
    data_to_insert = ("Vanesa", "Ropero")
    #write_to_db(connection, insert_query, data_to_insert)

    # Read from DB
    select_query = "SELECT * FROM potencial_clients"
    rows = read_from_db(connection, select_query)
    for row in rows:
        print(row)
