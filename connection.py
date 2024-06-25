import pymysql

def create_connection():
    try:
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            database='test',
            cursorclass=pymysql.cursors.DictCursor
        )
        return connection
    except pymysql.MySQLError as error:
        print(f"Failed to connect to database: {error}")
        return None

def close_db(connection):
    if connection:
        connection.close()
    else:
        print("Database connection already closed")
