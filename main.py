# Entry Point
from Database import connect_db, init_db, save_weather

# Testing DB Connection
connection = connect_db()
if connection:
    connection.close()
    
# Calling the Table init_db function
init_db()

# Calling the save weather function
save_weather()