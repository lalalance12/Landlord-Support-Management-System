import mysql.connector
from mysql.connector import Error
from PySide6.QtWidgets import QTableWidgetItem, QComboBox, QHeaderView, QDialog, QVBoxLayout, QMessageBox, QInputDialog, QAbstractItemView
from PySide6.QtCore import Qt
from datetime import date


mydb = mysql.connector.connect (

    host="localhost",
    user ="root",
    password="root",
    database="lsms_database"

)

mycursor = mydb.cursor ()


class appFunctions():
    def __init__(self, arg):
        super(appFunctions, self).__init__()
        self.arg = arg
    
    
    def click_apart_page(self):
         # Update the table widget with data from Apartment table
            update_table_widget_sql = "SELECT * FROM Apartment"
            mycursor.execute(update_table_widget_sql)
            apartment_data = mycursor.fetchall()
            
            self.ui.Apartment_tableWidget_3.setRowCount(len(apartment_data))
            for row, apartment in enumerate(apartment_data):
                for column, value in enumerate(apartment):
                    item = QTableWidgetItem(str(value))
                    self.ui.Apartment_tableWidget_3.setItem(row, column, item)
                    
            self.ui.Apartment_tableWidget_3.verticalHeader().setVisible(False)
            self.ui.Apartment_tableWidget_3.setEditTriggers(QAbstractItemView.NoEditTriggers)
        
        
    def add_apartment(self):
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
        
        set_auto_increment_sql = "ALTER TABLE Apartment AUTO_INCREMENT = 1000"
        mycursor.execute(set_auto_increment_sql)
        mydb.commit()
        
        # Get input of the user in creating an apartment
        ApartmentNumber = self.ui.ApartNum_line_edit.text()
        FloorLevel = self.ui.FloorLvl_comboBox.currentText()
        RentalBill = self.ui.RentalBill_line_edit.text()
        
        
        # Check if any input is missing
        if not all((ApartmentNumber, FloorLevel, RentalBill)):
            QMessageBox.warning(self, "Missing Input", "Please enter all the necessary data.")
            return
        
        # Check if the apartment number already exists
        check_existing_sql = "SELECT COUNT(*) FROM Apartment WHERE Apartment_No = %s"
        mycursor.execute(check_existing_sql, (ApartmentNumber,))
        count = mycursor.fetchone()[0]
        if count > 0:
            QMessageBox.warning(self, "Duplicate Apartment Number", "Apartment number already exists.")
            return

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
                    
            self.ui.Apartment_tableWidget_3.verticalHeader().setVisible(False)
                
            self.ui.ApartNum_line_edit.setText("")
            self.ui.FloorLvl_comboBox.setCurrentIndex(0)
            self.ui.RentalBill_line_edit.setText("")
            
        except Error as e:
            print(e)
            
    def delete_apartment(self):
        # Get the selected row index from Apartment_tableWidget_3
        selected_row = self.ui.Apartment_tableWidget_3.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "No Selection", "Please select an apartment to delete.")
            return

        # Get the Apartment_ID value from the selected row
        apartment_id = self.ui.Apartment_tableWidget_3.item(selected_row, 0).text()

        # Prompt the user for confirmation before deleting
        confirm_delete = QMessageBox.question(self, "Confirm Deletion", "Are you sure you want to delete this apartment?",
                                            QMessageBox.Yes | QMessageBox.No)
        if confirm_delete == QMessageBox.Yes:
            try:
                # Delete the apartment from the database
                delete_apartment_sql = "DELETE FROM Apartment WHERE Apartment_ID = %s"
                mycursor.execute(delete_apartment_sql, (apartment_id,))
                mydb.commit()
                QMessageBox.information(self, "Success", "Apartment deleted successfully.")

                # Update the table widget with data from Apartment table
                update_table_widget_sql = "SELECT * FROM Apartment"
                mycursor.execute(update_table_widget_sql)
                apartment_data = mycursor.fetchall()

                self.ui.Apartment_tableWidget_3.setRowCount(len(apartment_data))
                for row, apartment in enumerate(apartment_data):
                    for column, value in enumerate(apartment):
                        item = QTableWidgetItem(str(value))
                        self.ui.Apartment_tableWidget_3.setItem(row, column, item)

                self.ui.Apartment_tableWidget_3.verticalHeader().setVisible(False)

            except Error as e:
                print(e)
        else:
            QMessageBox.information(self, "Deletion Canceled", "Deletion operation canceled.")
      
    def get_apartment(self):
        # Get the selected row index from Apartment_tableWidget_3
        selected_row = self.ui.Apartment_tableWidget_3.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "No Selection", "Please select an apartment to update.")
            return

        # Get the Apartment_ID value from the selected row
        apartment_id = self.ui.Apartment_tableWidget_3.item(selected_row, 0).text()

        try:
            # Fetch the apartment data from the database
            fetch_apartment_sql = "SELECT * FROM Apartment WHERE Apartment_ID = %s"
            mycursor.execute(fetch_apartment_sql, (apartment_id,))
            apartment_data = mycursor.fetchone()

            if apartment_data is not None:
                # Update the input fields with the apartment data
                self.ui.ApartNum_line_edit.setText(str(apartment_data[1]))
                self.ui.FloorLvl_comboBox.setCurrentText(str(apartment_data[2]))
                self.ui.RentalBill_line_edit.setText(str(apartment_data[3]))

            else:
                QMessageBox.warning(self, "Apartment Not Found", "Apartment ID does not exist.")

        except Error as e:
            print(e)

    def update_apartment(self):
        # Get the selected row index from Apartment_tableWidget_3
        selected_row = self.ui.Apartment_tableWidget_3.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "No Selection", "Please select an apartment to update.")
            return

        # Get the Apartment_ID value from the selected row
        apartment_id = self.ui.Apartment_tableWidget_3.item(selected_row, 0).text()

        # Get the input data from the input fields
        ApartmentNumber = self.ui.ApartNum_line_edit.text()
        FloorLevel = self.ui.FloorLvl_comboBox.currentText()
        RentalBill = self.ui.RentalBill_line_edit.text()
        
        
        # Check if any input is missing
        if not all((ApartmentNumber, FloorLevel, RentalBill)):
            QMessageBox.warning(self, "Missing Input", "Please enter all the necessary data.")
            return

        # Update the apartment data in the database
        try:
            update_apartment_sql = "UPDATE Apartment SET Apartment_No = %s, Floor_level = %s, Rental_bill = %s WHERE Apartment_ID = %s"
            mycursor.execute(update_apartment_sql, (ApartmentNumber, FloorLevel, RentalBill, apartment_id))
            mydb.commit()
            QMessageBox.information(self, "Success", "Apartment updated successfully.")

            # Update the table widget with updated data
            update_table_widget_sql = "SELECT * FROM Apartment"
            mycursor.execute(update_table_widget_sql)
            apartment_data = mycursor.fetchall()

            self.ui.Apartment_tableWidget_3.setRowCount(len(apartment_data))
            for row, apartment in enumerate(apartment_data):
                for column, value in enumerate(apartment):
                    item = QTableWidgetItem(str(value))
                    self.ui.Apartment_tableWidget_3.setItem(row, column, item)

            self.ui.Apartment_tableWidget_3.verticalHeader().setVisible(False)
            
            self.ui.ApartNum_line_edit.setText("")
            self.ui.FloorLvl_comboBox.setCurrentIndex(0)
            self.ui.RentalBill_line_edit.setText("")

        except Error as e:
            print(e)
            
############################################################################################################################################################       