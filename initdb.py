"""Module providing a function that initializes a database."""
import os
import psycopg2
from psycopg2.extras import RealDictCursor

def get_db_connection(db):
    """ Function that gets connection to the database."""
    # Connect to DB
    conn = psycopg2.connect(database=db, 
                            user=os.getenv("POSTGRES_USER"),
                            password=os.getenv("POSTGRES_PASSWORD"),
                            host=os.getenv("POSTGRES_SERVICE_HOST"),
                            port=os.getenv("POSTGRES_SERVICE_PORT"))
                            
    # Set autocommit to true
    conn.autocommit = True
    return conn
    
# inits database
def initdb():
    """Function that initializes a database."""
    # Connect to the database
    conn = get_db_connection('postgres')
                           
    # Get the cursor
    cur = conn.cursor(cursor_factory=RealDictCursor)
        
    # Check database vehicles_db exists or not
    cur.execute("SELECT COUNT(*) FROM pg_database WHERE datname = %s",
                ('vehicles_db',))
                         
    # Fetch result
    result = cur.fetchone()    
    
    # Not exist
    if(result['count'] == 0):
        # Create database vehicles_db
        cur.execute("CREATE DATABASE vehicles_db")
        
        # Close the connection
        conn.close()       
        
        # Connect to database vehicles_db
        conn = get_db_connection('vehicles_db')

        # Get the cursor
        cur = conn.cursor(cursor_factory=RealDictCursor)
        
        # Create the table vehicles
        cur.execute("CREATE TABLE vehicles (" +
                    "vehicle_number TEXT PRIMARY KEY," +
                    "owner_name TEXT NOT NULL" 
                    ")")

 
        # Insert vehicle
        cur.execute("INSERT INTO vehicles (vehicle_number, owner_name)"+
                     "VALUES (%s, %s)",
                    ('TS07HR9551', 'RAMAKRISHNA KUMMARI')
                    )

        # Insert vehicle
        cur.execute("INSERT INTO vehicles (vehicle_number, owner_name)"+
                     "VALUES (%s, %s)",
                    ('TS07HR9552', 'DILIP JAIN')
                )

        # Insert vehicle
        cur.execute("INSERT INTO vehicles (vehicle_number, owner_name)"+
                     "VALUES (%s, %s)",
                    ('TS07HR9553', 'DEEPA SHENOY')
                )
        
        # Insert vehicle
        cur.execute("INSERT INTO vehicles (vehicle_number, owner_name)"+
                     "VALUES (%s, %s)",
                    ('TS07HR9554', 'VEENA S')
                )
        
        # Insert vehicle
        cur.execute("INSERT INTO vehicles (vehicle_number, owner_name)"+
                     "VALUES (%s, %s)",
                    ('TS07HR9555', 'RADHIKA V')
                )
        
        # Close the connection
        conn.close()
    else:
        # Close the connection
        conn.close() 

if __name__ == "__main__":
    initdb()
