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

mycursor = mydb.cursor ()



"""""
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
    
    
    
    def addapartment(self):
        # Create table Apartment if there is no existing table
        mycursor.execute("""
            CREATE TABLE IF NOT EXISTS Apartment (
                Apartment_ID INT AUTO_INCREMENT PRIMARY KEY,
                Apartment_No INT NOT NULL,
                Floor_level INT NOT NULL,
                Rental_bill INT NOT NULL
            )
        """)
        mydb.commit()
        
        # Get input of the user in creating an apartment
        ApartmentNumber = self.ui.ApartNum_line_edit.text()
        FloorLevel = self.ui.FloorLvl_comboBox.currentText()
        RentalBill = self.ui.RentalBill_line_edit.text()

        insert_apartment_sql = "INSERT INTO Apartment (Apartment_No, Floor_level, Rental_bill) VALUES (%s, %s, %s)"
        
        try:
            # Insert the new apartment data
            mycursor.execute(insert_apartment_sql, (ApartmentNumber, FloorLevel, RentalBill))
            mydb.commit()
            QMessageBox.information(self, "Success", "Apartment inserted successfully.")
            
             # Update the table widget with data from Apartment table
            update_table_widget_sql = "SELECT * FROM Apartment"
            mycursor.execute(update_table_widget_sql)
            apartment_data = mycursor.fetchall()
            
            self.ui.Apartment_tableWidget_3.setRowCount(len(apartment_data))
            for row, apartment in enumerate(apartment_data):
                for column, value in enumerate(apartment):
                    item = QTableWidgetItem(str(value))
                    self.ui.Apartment_tableWidget_3.setItem(row, column, item)
                
            self.ui.ApartNum_line_edit.setText("")
            self.ui.FloorLvl_comboBox.setCurrentIndex(0)
            self.ui.RentalBill_line_edit.setText("")
            
        except Error as e:
            print(e)

      
