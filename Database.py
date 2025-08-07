# DB setup and functions
import psycopg2
from Config import DB_NAME, DB_USER, DB_HOST, DB_PASSWORD, DB_PORT

# Establishing a connection to the Database
def connect_db():
    
    ''' Creating a connection using the credential from Config.py'''
    try:
        connection = psycopg2.connect (
        dbname = DB_NAME,
        user = DB_USER, 
        password = DB_PASSWORD,
        host = DB_HOST,
        port = DB_PORT   
    )
        print("Successfully Connected to PostgreSQL!")
        return connection
    except psycopg2.ERROR as e:
        print("Failed to connect to PostgreSQL!")
        print("ERROR:", e)
        return None
    
# initializing the table creation if not exist
def init_db():
    '''Calling the connect_db() function'''
    connection = connect_db()
    cursor = connection.cursor()
    
    # create table query
    create_table_query = """
    CREATE TABLE IF NOT EXISTS weather (
        id SERIAL PRIMARY KEY,
        city TEXT,
        temperature REAL,
        condition TEXT,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """
    cursor.execute(create_table_query) # send the command
    connection.commit() # save change
    cursor.close() # clean up
    connection.close() # Close the db connection after used
    
# Function to save the data into the database table
def save_weather(city, temp, cond):
    connection = connect_db()
    cursor = connection.cursor()
    
    '''Sql query to insert data into the db table '''
    insert_into_table = """INSERT INTO weather (city, temperature, condition)
    VALUES (%s, %s, %s) 
    """
    # excuting the sql query
    cursor.execute(insert_into_table, (city, temp, cond))
    connection.commit()
    cursor.close()
    connection.close()