import mysql.connector
from mysql.connector import Error
from PySide6.QtWidgets import QTableWidgetItem, QComboBox, QHeaderView, QDialog, QVBoxLayout, QMessageBox, QInputDialog
from PySide6.QtCore import Qt
from datetime import date


mydb = mysql.connector.connect (

    host="localhost",
    user ="root",
    password="root",
    database="lsms_database"

)

"""""
mycursor = mydb.cursor ()

try:
    # Establish a connection to the MySQL server
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="lsms_database"
    )

except Error as e:
    # Handle connection errors
    print(f"Error connecting to MySQL server: {e}")
    exit()

# Create a cursor object
mycursor = mydb.cursor()


# Function to create the "lsms_database" schema if it doesn't exist
def create_lsms_database_schema():
    try:
        # Execute the SQL statement to create the schema
        mycursor.execute("CREATE SCHEMA IF NOT EXISTS lsms_database")
        print("lsms_database schema created successfully!")

    except Error as e:
        # Handle schema creation errors
        print(f"Error creating lsms_database schema: {e}")
        exit()


# Create the "lsms_database" schema if it doesn't exist
create_lsms_database_schema()

"""""

class appFunctions():
    def __init__(self, arg):
        super(appFunctions, self).__init__()
        self.arg = arg
    
