"""Module providing REST APIs for Get vehicle owner operations."""
import os
import psycopg2
from psycopg2.extras import RealDictCursor
from initdb import initdb, get_db_connection
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort

def get_vehicle_owner(vehicle_number):
    """ Function that gets vehicle for given vehicle number."""
    # Get connection to DB
    conn = get_db_connection('vehicles_db')
    
    # Get the cursor
    cur = conn.cursor(cursor_factory=RealDictCursor)
        
    # Get user information
    cur.execute("SELECT owner_name FROM vehicles WHERE vehicle_number = %s",
                (vehicle_number,))
               
    # Get result               
    owner = cur.fetchone()
    
    # Close the connection
    conn.close()
        
    # return user
    return owner

# Create Flask app
app = Flask(__name__)

# Home page
@app.route('/')
def index():
    return "OK"

# Vehicle page
@app.route('/vehicle')
def vehicle():
    """ Function that gets vehicle information."""

    # Get vehicle number from the request
    vehicle_number = request.args.get('vehicle_number')

    # Get vehicle owner information
    owner = get_vehicle_owner(vehicle_number)
    
    # return owner information
    if owner is not None:
        return owner['owner_name']
    
    # return N/A
    return "Not Available"

# Starts from here
if __name__ == "__main__":   
    # Initialize the database
    initdb()

    # Set the configuration
    app.config[os.getenv("FLASK_KEY")] = os.getenv("FLASK_KEY_VALUE")

    # Run the application
    app.run(host='0.0.0.0', port=8001)