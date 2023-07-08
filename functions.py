import mysql.connector
from mysql.connector import Error
from PySide6.QtWidgets import QTableWidgetItem, QComboBox, QHeaderView, QDialog, QVBoxLayout, QMessageBox, QInputDialog, QAbstractItemView, QCalendarWidget, QDialogButtonBox, QLabel, QDialogButtonBox
from PySide6.QtCore import Qt, QDate, QLocale
import datetime


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
        
############################################################################################################################################################
    
    def click_tenant_stat_list_page(self):
        # Update the table widget with data from Tenant and Payment tables
        update_table_widget_sql = """
            SELECT t.Tenant_ID, t.Name, t.Phone_no, COALESCE(p.Payment_Status, 'No Payment') AS Payment_Status, p.Payment_Date, p.Payment_ID
            FROM Tenant t
            LEFT JOIN (
                SELECT p1.*
                FROM Payment p1
                WHERE p1.Payment_ID = (
                    SELECT Payment_ID
                    FROM Payment
                    WHERE tenant_id = p1.tenant_id
                    ORDER BY
                        CASE
                            WHEN Payment_Status = 'overdue' THEN 0
                            WHEN Payment_Status = 'pending' THEN 1
                            WHEN Payment_Status = 'successful' THEN 2
                        END,
                        Payment_Status DESC,
                        Payment_Date DESC
                    LIMIT 1
                )
            ) p ON t.tenant_id = p.tenant_id
        """
        mycursor.execute(update_table_widget_sql)
        tenant_data = mycursor.fetchall()

        self.ui.Tenant_tableWidget_3.setRowCount(len(tenant_data))
        for row, data in enumerate(tenant_data):
            for column, value in enumerate(data):
                item = QTableWidgetItem(str(value))
                item.setTextAlignment(Qt.AlignCenter)
                self.ui.Tenant_tableWidget_3.setItem(row, column, item)

        self.ui.Tenant_tableWidget_3.verticalHeader().setVisible(True)
        self.ui.Tenant_tableWidget_3.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.Tenant_tableWidget_3.resizeColumnsToContents()
    


    def search_tenant_stat_list(self):
        # Update the table widget with data from Tenant and Payment tables
        update_table_widget_sql = """
            SELECT t.Tenant_ID, t.Name, t.Phone_no, COALESCE(p.Payment_Status, 'No Payment') AS Payment_Status, p.Payment_Date, p.Payment_ID
            FROM Tenant t
            LEFT JOIN (
                SELECT p1.*
                FROM Payment p1
                WHERE p1.Payment_ID = (
                    SELECT Payment_ID
                    FROM Payment
                    WHERE tenant_id = p1.tenant_id
                    ORDER BY
                        CASE
                            WHEN Payment_Status = 'overdue' THEN 0
                            WHEN Payment_Status = 'pending' THEN 1
                            WHEN Payment_Status = 'successful' THEN 2
                        END,
                        Payment_Status DESC,
                        Payment_Date DESC
                    LIMIT 1
                )
            ) p ON t.tenant_id = p.tenant_id
        """
        mycursor.execute(update_table_widget_sql)
        tenant_data = mycursor.fetchall()

        self.ui.Tenant_tableWidget_3.setRowCount(len(tenant_data))
        for row, data in enumerate(tenant_data):
            for column, value in enumerate(data):
                item = QTableWidgetItem(str(value))
                item.setTextAlignment(Qt.AlignCenter)
                self.ui.Tenant_tableWidget_3.setItem(row, column, item)

        self.ui.Tenant_tableWidget_3.verticalHeader().setVisible(True)
        self.ui.Tenant_tableWidget_3.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.Tenant_tableWidget_3.resizeColumnsToContents()

        # Find the data in the displayed table from click_tenant_stat_list_page
        search_text = self.ui.Search_lineEdit.text()

        table_widget = self.ui.Tenant_tableWidget_3

        if search_text != "":
            matching_rows = []

            for row in range(table_widget.rowCount()):
                matching_data = False
                for col in range(table_widget.columnCount()):
                    item = table_widget.item(row, col)
                    if item is not None and search_text in item.text():
                        matching_data = True
                        break
                if matching_data:
                    matching_rows.append(row)

            table_widget.clearSelection()
            table_widget.setRowCount(0)

            for row in matching_rows:
                table_widget.insertRow(table_widget.rowCount())
                for col in range(table_widget.columnCount()):
                    item = table_widget.item(row, col)
                    if item is not None:
                        new_item = QTableWidgetItem(item.text())
                        new_item.setTextAlignment(Qt.AlignCenter)
                        table_widget.setItem(table_widget.rowCount() - 1, col, new_item)

            table_widget.setSizeAdjustPolicy(QAbstractItemView.AdjustToContents)
            table_widget.resizeColumnsToContents()
                    

############################################################################################################################################################

    def click_CRUD_tenant_page(self):
        # Update the table widget with data from Tenant table
        update_table_widget_sql = "SELECT * FROM Tenant"
        mycursor.execute(update_table_widget_sql)
        tenant_data = mycursor.fetchall()
            
        self.ui.Tenant_tableWidget.setRowCount(len(tenant_data))
        for row, apartment in enumerate(tenant_data):
            for column, value in enumerate(apartment):
                item = QTableWidgetItem(str(value))
                item.setTextAlignment(Qt.AlignCenter)
                self.ui.Tenant_tableWidget.setItem(row, column, item)
                    
        self.ui.Tenant_tableWidget.verticalHeader().setVisible(False)
        self.ui.Tenant_tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.Tenant_tableWidget.resizeColumnsToContents()

    def add_tenant(self):
        # Create table Tenant if there is no existing table
        mycursor.execute("""
            CREATE TABLE IF NOT EXISTS Tenant (
                Tenant_ID INT AUTO_INCREMENT PRIMARY KEY,
                Name VARCHAR (90),
                Age INT,
                Sex VARCHAR(10),
                Phone_no BIGINT,
                Email VARCHAR(50),
                Apartment_ID INT,
                CONSTRAINT fk1 FOREIGN KEY (Apartment_ID) REFERENCES Apartment (Apartment_ID) ON DELETE CASCADE ON UPDATE CASCADE
            )
        """)
        mydb.commit()
        
         # Create table Lease if there is no existing table
        mycursor.execute("""
            CREATE TABLE IF NOT EXISTS Lease (
                Lease_ID INT AUTO_INCREMENT PRIMARY KEY,
                Date_Lease DATE,
                Tenant_ID INT,
                Apartment_ID INT,
                CONSTRAINT fk5 FOREIGN KEY (Tenant_ID) REFERENCES Tenant (Tenant_ID) ON DELETE CASCADE ON UPDATE CASCADE,
                CONSTRAINT fk6 FOREIGN KEY (Apartment_ID) REFERENCES Apartment (Apartment_ID) ON DELETE CASCADE ON UPDATE CASCADE
                )
        """)
        mydb.commit()
        
        set_auto_increment_sql = "ALTER TABLE Lease AUTO_INCREMENT = 4400"
        mycursor.execute(set_auto_increment_sql)
        mydb.commit()
        
         # Create table Occupy if there is no existing table
        mycursor.execute("""
            CREATE TABLE IF NOT EXISTS Occupy (
                Tenant_ID INT,
                Apartment_ID INT,
                PRIMARY KEY (Tenant_ID, Apartment_ID),
                CONSTRAINT fk7 FOREIGN KEY (Tenant_ID) REFERENCES Tenant (Tenant_ID) ON DELETE CASCADE ON UPDATE CASCADE,
                CONSTRAINT fk8 FOREIGN KEY (Apartment_ID) REFERENCES Apartment (Apartment_ID) ON DELETE CASCADE ON UPDATE CASCADE
            )
        """)
        mydb.commit()
        
        set_auto_increment_sql = "ALTER TABLE Tenant AUTO_INCREMENT = 5500"
        mycursor.execute(set_auto_increment_sql)
        mydb.commit()


        # Get input of the user in creating an apartment
        Name = self.ui.Name_line_edit.text()
        Age = self.ui.Age_line_edit.text()
        Sex = self.ui.Sex_comboBox.currentText()
        PhoneNum = self.ui.PhoneNum_line_edit.text()
        Email = self.ui.Email_line_edit.text()
        ApartmentID = self.ui.ApartNum_line_edit_3.text()
        
        
        # Check if any input is missing
        if not all((Name, Age, Sex, PhoneNum, Email, ApartmentID)):
            QMessageBox.warning(self, "Missing Input", "Please enter all the necessary data.")
            print("Error:", Name, Age, Sex, PhoneNum, Email, ApartmentID)
            return
        
        # Check if the Apartment_ID exists in the Apartment table
        apartment_exists_sql = "SELECT Apartment_ID FROM Apartment WHERE Apartment_ID = %s"
        mycursor.execute(apartment_exists_sql, (ApartmentID,))
        apartment_result = mycursor.fetchone()
        
        if not apartment_result:
            QMessageBox.warning(self, "Invalid Apartment ID", "The entered Apartment ID does not exist.")
            return
        
        
        try:
            # Insert the new tenant data into Tenant table
            insert_tenant_sql = "INSERT INTO Tenant (Name, Age, Sex, Phone_no, Email, Apartment_ID) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (Name, Age, Sex, PhoneNum, Email, ApartmentID)
            mycursor.execute(insert_tenant_sql, values)
            mydb.commit()
            
            # Get the generated Tenant_ID
            tenant_id = mycursor.lastrowid

            # Insert the new tenant data into the Occupy table
            insert_occupy_sql = "INSERT INTO Occupy (Tenant_ID, Apartment_ID) VALUES (%s, %s)"
            values = (tenant_id, ApartmentID)
            mycursor.execute(insert_occupy_sql, values)
            mydb.commit()
            
            # Check if the Apartment_ID exists in the Lease table
            apartment_leased_sql = "SELECT Apartment_ID FROM Lease WHERE Apartment_ID = %s"
            mycursor.execute(apartment_leased_sql, (ApartmentID,))
            apartment_leased_result = mycursor.fetchone()

            if not apartment_leased_result:
                # Create a dialog to enter the lease date
                lease_dialog = QDialog(self)
                lease_dialog.setWindowTitle("Lease Date")
                calendar_widget = QCalendarWidget()

                # Create a label
                label = QLabel("Enter the Lease Date:", lease_dialog)
                button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
                button_box.accepted.connect(lease_dialog.accept)
                button_box.rejected.connect(lease_dialog.reject)
                layout = QVBoxLayout(lease_dialog)
                layout.addWidget(label)
                layout.addWidget(calendar_widget)
                layout.addWidget(button_box)

                if lease_dialog.exec() == QDialog.Accepted:
                    selected_date = calendar_widget.selectedDate()
                    lease_date = selected_date.toString("yyyy-MM-dd")
                else:
                    QMessageBox.warning(self, "Lease Date", "Lease operation canceled.")
                    return

                # Insert the lease data into the Lease table
                insert_lease_sql = "INSERT INTO Lease (Date_Lease, Tenant_ID, Apartment_ID) VALUES (%s, %s, %s)"
                values = (lease_date, tenant_id, ApartmentID)
                mycursor.execute(insert_lease_sql, values)
                mydb.commit()

                QMessageBox.information(self, "Success", "Lease information inserted successfully.")
            
            QMessageBox.information(self, "Success", "Tenant inserted successfully.")
            
            # Update the table widget with data from Tenant table
            update_table_widget_sql = "SELECT * FROM Tenant"
            mycursor.execute(update_table_widget_sql)
            tenant_data = mycursor.fetchall()
            
            self.ui.Tenant_tableWidget.setRowCount(len(tenant_data))
            for row, tenant in enumerate(tenant_data):
                for column, value in enumerate(tenant):
                    item = QTableWidgetItem(str(value))
                    item.setTextAlignment(Qt.AlignCenter)
                    self.ui.Tenant_tableWidget.setItem(row, column, item)
                    
            self.ui.Tenant_tableWidget.verticalHeader().setVisible(False)
            
            # Reset to blank all line edit and combo box    
            self.ui.Name_line_edit.setText("")
            self.ui.Age_line_edit.setText("")
            self.ui.Sex_comboBox.setCurrentIndex(0)
            self.ui.PhoneNum_line_edit.setText("")
            self.ui.Email_line_edit.setText("")
            self.ui.ApartNum_line_edit_3.setText("")
            
        except Error as e:
            print("Error:", e)

    def delete_tenant(self):
        # Get the selected row index from Tenant_tableWidget
        selected_row = self.ui.Tenant_tableWidget.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "No Selection", "Please select a tenant to delete.")
            return

        # Get the Tenant_ID value from the selected row
        tenant_id = self.ui.Tenant_tableWidget.item(selected_row, 0).text()

        # Prompt the user for confirmation before deleting
        confirm_delete = QMessageBox.question(self, "Confirm Deletion", "Are you sure you want to delete this tenant?",
                                            QMessageBox.Yes | QMessageBox.No)
        if confirm_delete == QMessageBox.Yes:
            try:
                # Delete the tenant from the database
                delete_tenant_sql = "DELETE FROM Tenant WHERE Tenant_ID = %s"
                mycursor.execute(delete_tenant_sql, (tenant_id,))
                mydb.commit()
                QMessageBox.information(self, "Success", "Tenant deleted successfully.")

                # Update the table widget with data from tenant table
                update_table_widget_sql = "SELECT * FROM Tenant"
                mycursor.execute(update_table_widget_sql)
                tenant_data = mycursor.fetchall()

                self.ui.Tenant_tableWidget.setRowCount(len( tenant_data))
                for row, tenant in enumerate(tenant_data):
                    for column, value in enumerate(tenant):
                        item = QTableWidgetItem(str(value))
                        item.setTextAlignment(Qt.AlignCenter)
                        self.ui.Tenant_tableWidget.setItem(row, column, item)

                self.ui.Tenant_tableWidget.verticalHeader().setVisible(False)

            except Error as e:
                print(e)
        else:
            QMessageBox.information(self, "Deletion Canceled", "Deletion operation canceled.")
    
    def get_tenant(self):
        # Get the selected row index from Tenant_tableWidget
        selected_row = self.ui.Tenant_tableWidget.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "No Selection", "Please select a tenant to update.")
            return

        # Get the Tenant_ID value from the selected row
        tenant_id = self.ui.Tenant_tableWidget.item(selected_row, 0).text()

        try:
            # Fetch the tenant data from the database
            fetch_tenant_sql = "SELECT * FROM Tenant WHERE Tenant_ID = %s"
            mycursor.execute(fetch_tenant_sql, (tenant_id,))
            tenant_data = mycursor.fetchone()

            if tenant_data is not None:
                # Update the input fields with the tenant data
                self.ui.Name_line_edit.setText(str(tenant_data[1]))
                self.ui.Age_line_edit.setText(str(tenant_data[2]))
                self.ui.Sex_comboBox.setCurrentText(str(tenant_data[3]))
                self.ui.PhoneNum_line_edit.setText(str(tenant_data[4]))
                self.ui.Email_line_edit.setText(str(tenant_data[5]))
                self.ui.ApartNum_line_edit_3.setText(str(tenant_data[6]))

            else:
                QMessageBox.warning(self, "Tenant Not Found", "Tenant ID does not exist.")

        except Error as e:
            print(e)
            
            
    def update_tenant(self):
        # Get the selected row index from Tenant_tableWidget
        selected_row = self.ui.Tenant_tableWidget.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "No Selection", "Please select an tenant to update.")
            return

        # Get the Tenant_ID value from the selected row
        tenant_id = self.ui.Tenant_tableWidget.item(selected_row, 0).text()

        # Get the input data from the input fields
        Name = self.ui.Name_line_edit.text()
        Age = self.ui.Age_line_edit.text()
        Sex = self.ui.Sex_comboBox.currentText()
        PhoneNum = self.ui.PhoneNum_line_edit.text()
        Email = self.ui.Email_line_edit.text()
        ApartmentID = self.ui.ApartNum_line_edit_3.text()

        # Check if any input is missing
        if not all((Name, Age, Sex, PhoneNum, Email, ApartmentID)):
            QMessageBox.warning(self, "Missing Input", "Please enter all the necessary data.")
            print("Error:", Name, Age, Sex, PhoneNum, Email, ApartmentID)
            return
        
        # Check if the Apartment_ID exists in the Apartment table
        apartment_exists_sql = "SELECT Apartment_ID FROM Apartment WHERE Apartment_ID = %s"
        mycursor.execute(apartment_exists_sql, (ApartmentID,))
        apartment_result = mycursor.fetchone()
        
        if not apartment_result:
            QMessageBox.warning(self, "Invalid Apartment ID", "The entered Apartment ID does not exist.")
            return
        
        # Update the tenant data in the database
        try:
            update_tenant_sql = "UPDATE Tenant SET Name = %s, Age = %s, Sex = %s, Phone_no = %s, Email = %s, Apartment_ID = %s WHERE Tenant_ID = %s"
            mycursor.execute(update_tenant_sql, (Name, Age, Sex, PhoneNum, Email, ApartmentID, tenant_id))
            mydb.commit()
            QMessageBox.information(self, "Success", "Tenant updated successfully.")

            # Update the table widget with updated data
            update_table_widget_sql = "SELECT * FROM Tenant"
            mycursor.execute(update_table_widget_sql)
            tenant_data = mycursor.fetchall()

            self.ui.Tenant_tableWidget.setRowCount(len( tenant_data))
            for row, tenant in enumerate(tenant_data):
                for column, value in enumerate(tenant):
                    item = QTableWidgetItem(str(value))
                    item.setTextAlignment(Qt.AlignCenter)
                    self.ui.Tenant_tableWidget.setItem(row, column, item)

            self.ui.Tenant_tableWidget.verticalHeader().setVisible(False)
            
            # Reset to blank all line edit and combo box
            self.ui.Name_line_edit.setText("")
            self.ui.Age_line_edit.setText("")
            self.ui.Sex_comboBox.setCurrentIndex(0)
            self.ui.PhoneNum_line_edit.setText("")
            self.ui.Email_line_edit.setText("")
            self.ui.ApartNum_line_edit_3.setText("")

        except Error as e:
            print(e)


############################################################################################################################################################
    
    def click_tenant_info_page(self):
        # Clear all data in line edits
        self.ui.Search_line_edit.setText("")
        self.ui.Name_line_edit_2.setText("")
        self.ui.Age_line_edit_2.setText("")
        self.ui.Sex_line_edit_2.setText("")
        self.ui.PhoneNum_line_edit_2.setText("")
        self.ui.Email_line_edit_2.setText("")
        self.ui.ApartNum_line_edit_2.setText("")
        self.ui.Payment_Stat_line_edit.setText("")
        
        # Clear the table widget of data
        self.ui.PayHis_tableWidget_2.clearContents()
        self.ui.PayHis_tableWidget_2.setRowCount(0)
    
    def search_tenant(self):
        # Clear data from previous tenant in the table widget
        self.ui.PayHis_tableWidget_2.clearContents()
        self.ui.PayHis_tableWidget_2.setRowCount(0)
        
        # Get the Tenant ID from Search_line_edit
        tenant_id = self.ui.Search_line_edit.text()

        if not tenant_id:
            QMessageBox.warning(self, "No Input", "Please enter a Tenant ID.")
            return

        # Check if the Tenant_ID exists in the Tenant table
        tenant_exists_sql = "SELECT Tenant_ID FROM Tenant WHERE Tenant_ID = %s"
        mycursor.execute(tenant_exists_sql, (tenant_id,))
        tenant_result = mycursor.fetchone()
        
        if not tenant_result:
            QMessageBox.warning(self, "Invalid Tenant ID", "The entered Tenant ID does not exist.")
            return
        
        try:
            # Fetch the tenant data from the database
            fetch_tenant_sql = "SELECT * FROM Tenant WHERE Tenant_ID = %s"
            mycursor.execute(fetch_tenant_sql, (tenant_id,))
            tenant_data = mycursor.fetchone()

            if tenant_data is not None:
                # Update the input fields with the tenant data
                self.ui.Name_line_edit_2.setText(str(tenant_data[1]))
                self.ui.Name_line_edit_2.setAlignment(Qt.AlignCenter)
                self.ui.Name_line_edit_2.setReadOnly(True)

                self.ui.Age_line_edit_2.setText(str(tenant_data[2]))
                self.ui.Age_line_edit_2.setAlignment(Qt.AlignCenter)
                self.ui.Age_line_edit_2.setReadOnly(True)

                self.ui.Sex_line_edit_2.setText(str(tenant_data[3]))
                self.ui.Sex_line_edit_2.setAlignment(Qt.AlignCenter)
                self.ui.Sex_line_edit_2.setReadOnly(True)

                self.ui.PhoneNum_line_edit_2.setText(str(tenant_data[4]))
                self.ui.PhoneNum_line_edit_2.setAlignment(Qt.AlignCenter)
                self.ui.PhoneNum_line_edit_2.setReadOnly(True)

                self.ui.Email_line_edit_2.setText(str(tenant_data[5]))
                self.ui.Email_line_edit_2.setAlignment(Qt.AlignCenter)
                self.ui.Email_line_edit_2.setReadOnly(True)

                self.ui.ApartNum_line_edit_2.setText(str(tenant_data[6]))
                self.ui.ApartNum_line_edit_2.setAlignment(Qt.AlignCenter)
                self.ui.ApartNum_line_edit_2.setReadOnly(True)
             
            else:
                QMessageBox.warning(self, "Tenant Not Found", "Tenant ID does not exist.")

        
            # Fetch the payment data from the database
            fetch_payment_sql = "SELECT * FROM Payment WHERE Tenant_ID = %s"
            mycursor.execute(fetch_payment_sql, (tenant_id,))
            payment_data = mycursor.fetchall()
            
            if payment_data is not None:
                # Check for overdue payment
                for payment in payment_data:
                    if payment[1] == 'Overdue':
                        self.ui.Payment_Stat_line_edit.setText('Overdue')
                        self.ui.Payment_Stat_line_edit.setAlignment(Qt.AlignCenter)
                        self.ui.Payment_Stat_line_edit.setReadOnly(True)
                        break
                else:
                    # Check for pending payment
                    for payment in payment_data:
                        if payment[1] == 'Pending':
                            self.ui.Payment_Stat_line_edit.setText('Pending')
                            self.ui.Payment_Stat_line_edit.setAlignment(Qt.AlignCenter)
                            self.ui.Payment_Stat_line_edit.setReadOnly(True)
                            break
                    else:
                        self.ui.Payment_Stat_line_edit.setText('Successful')
                        self.ui.Payment_Stat_line_edit.setAlignment(Qt.AlignCenter)
                        self.ui.Payment_Stat_line_edit.setReadOnly(True)
            else:
                    self.ui.Payment_Stat_line_edit.setText("")
                    QMessageBox.warning(self, "Tenant Not Found", "There are no payments made by this Tenant.") 
                               
        except Error as e:
            print(e)
 
 
    def payment_history(self): 
        
        #Get the Tenant ID from Search_line_edit
        tenant_id = self.ui.Search_line_edit.text()

        if not tenant_id:
            QMessageBox.warning(self, "No Input", "Please enter a Tenant ID.")
            return

        # Check if the Tenant_ID exists in the Tenant table
        tenant_exists_sql = "SELECT Tenant_ID FROM Tenant WHERE Tenant_ID = %s"
        mycursor.execute(tenant_exists_sql, (tenant_id,))
        tenant_result = mycursor.fetchone()
        
        if not tenant_result:
            QMessageBox.warning(self, "Invalid Tenant ID", "The entered Tenant ID does not exist.")
            return
        
        try:          
            # Fetch the payment data from the database
            fetch_payment_sql = "SELECT * FROM Payment WHERE Tenant_ID = %s ORDER BY Payment_Date ASC"
            mycursor.execute(fetch_payment_sql, (tenant_id,))
            payment_data = mycursor.fetchall()
                        
            if payment_data is not None:
                # Clear the existing table widget data
                self.ui.PayHis_tableWidget_2.clearContents()
                self.ui.PayHis_tableWidget_2.setRowCount(0)

                # Populate the table widget with payment data
                for row, payment in enumerate(payment_data):
                    self.ui.PayHis_tableWidget_2.insertRow(row)
                    for column, value in enumerate(payment):
                        item = QTableWidgetItem(str(value))
                        item.setTextAlignment(Qt.AlignCenter)
                        self.ui.PayHis_tableWidget_2.setItem(row, column, item)
            else:
                    QMessageBox.warning(self, "Tenant Not Found", "There are no payments made by this Tenant.")
                    
        except Error as e:
            print(e)
 
        






























############################################################################################################################################################     
    
    def click_apart_info_page(self):
        
        # Update the table widget with data from Apartment table
        update_table_widget_sql = "SELECT * FROM Apartment"
        mycursor.execute(update_table_widget_sql)
        apartment_data = mycursor.fetchall()
        
        self.ui.Apartment_tableWidget_2.clear()
        column_count = 4  
        self.ui.Apartment_tableWidget_2.setRowCount(len(apartment_data))
        self.ui.Apartment_tableWidget_2.setColumnCount(column_count)
        
        self.ui.Apartment_tableWidget_2.setRowCount(len(apartment_data))
        for row, apartment in enumerate(apartment_data):
            for column, value in enumerate(apartment):
                item = QTableWidgetItem(str(value))
                item.setTextAlignment(Qt.AlignCenter)
                self.ui.Apartment_tableWidget_2.setItem(row, column, item)
                    
        self.ui.Apartment_tableWidget_2.verticalHeader().setVisible(False)
        self.ui.Apartment_tableWidget_2.setEditTriggers(QAbstractItemView.NoEditTriggers)
        
        # Set the header labels
        header_labels = ["Apartment_ID", "Apartment_No", "Floor_level", "Rental_bill"]
        self.ui.Apartment_tableWidget_2.setHorizontalHeaderLabels(header_labels)
    
    
    def set_button_connections(self,button_type):
        if button_type == "list":
            self.ui.Search_lineEdit_2.textChanged.disconnect()  # Disconnect the previous connection
            self.ui.Search_lineEdit_2.textChanged.connect(lambda: appFunctions.search_apartment(self))
            self.ui.AptOcctBtn.clicked.disconnect()  # Disconnect the previous connection
            self.ui.AptOcctBtn.clicked.connect(lambda: appFunctions.ocupy(self))
        elif button_type == "occupy":
            self.ui.Search_lineEdit_2.textChanged.disconnect()  # Disconnect the previous connection
            self.ui.Search_lineEdit_2.textChanged.connect(lambda: appFunctions.search_occupy(self))
            self.ui.AptOcctBtn.clicked.disconnect()  # Disconnect the previous connection
            self.ui.AptOcctBtn.clicked.connect(lambda: appFunctions.ocupy(self))
        elif button_type == "lease":
            self.ui.Search_lineEdit_2.textChanged.disconnect()  # Disconnect the previous connection
            self.ui.Search_lineEdit_2.textChanged.connect(lambda: appFunctions.search_lease(self))
            self.ui.AptOcctBtn.clicked.disconnect()  # Disconnect the previous connection
            self.ui.AptOcctBtn.clicked.connect(lambda: appFunctions.lease(self))

    def set_search_connection(self):
        if self.ui.AptOcctBtn.isChecked():
            self.ui.Search_lineEdit_2.textChanged.disconnect()  # Disconnect the previous connection
            self.ui.Search_lineEdit_2.textChanged.connect(lambda: appFunctions.search_occupy(self))
        else:
            self.ui.Search_lineEdit_2.textChanged.disconnect()  # Disconnect the previous connection
            self.ui.Search_lineEdit_2.textChanged.connect(lambda: appFunctions.search_apartment(self))
    
    
    
    def search_apartment(self):
        # Find the data in the Apartment table
        search_text = self.ui.Search_lineEdit_2.text()

        mycursor.execute("SELECT * FROM Apartment WHERE Apartment_ID LIKE %s OR Apartment_No LIKE %s OR Floor_level LIKE %s OR Rental_bill LIKE %s",
            (f"{search_text}%", f"{search_text}%", f"{search_text}%", f"{search_text}%"))

        result = mycursor.fetchall()

        # Set up the table
        table_widget = self.ui.Apartment_tableWidget_2
        table_widget.clearContents()
        table_widget.setRowCount(len(result))

        for row, apartment in enumerate(result):
            for col, data in enumerate(apartment):
                item = QTableWidgetItem(str(data))
                item.setTextAlignment(Qt.AlignCenter)
                table_widget.setItem(row, col, item)

        table_widget.setSizeAdjustPolicy(QAbstractItemView.AdjustToContents)
        table_widget.resizeColumnsToContents()
    
    def search_occupy(self):
        # Find the data in the Occupy table
        search_text = self.ui.Search_lineEdit_2.text()

        mycursor.execute("SELECT * FROM Occupy WHERE Tenant_ID LIKE %s OR Apartment_ID LIKE %s",
                        (f"{search_text}%", f"{search_text}%"))

        result = mycursor.fetchall()

        # Set up the table
        table_widget = self.ui.Apartment_tableWidget_2
        table_widget.clearContents()
        table_widget.setRowCount(len(result))

        for row, occupy in enumerate(result):
            for col, data in enumerate(occupy):
                item = QTableWidgetItem(str(data))
                item.setTextAlignment(Qt.AlignCenter)
                table_widget.setItem(row, col, item)

        table_widget.setSizeAdjustPolicy(QAbstractItemView.AdjustToContents)
        table_widget.resizeColumnsToContents()
    
    def apartlist(self):
         
        # Update the table widget with data from Apartment table
        update_table_widget_sql = "SELECT * FROM Apartment"
        mycursor.execute(update_table_widget_sql)
        apartment_data = mycursor.fetchall()
        
        self.ui.Apartment_tableWidget_2.clear()
        column_count = 4  
        self.ui.Apartment_tableWidget_2.setRowCount(len(apartment_data))
        self.ui.Apartment_tableWidget_2.setColumnCount(column_count)  
            
        self.ui.Apartment_tableWidget_2.setRowCount(len(apartment_data))
        for row, apartment in enumerate(apartment_data):
            for column, value in enumerate(apartment):
                item = QTableWidgetItem(str(value))
                item.setTextAlignment(Qt.AlignCenter)
                self.ui.Apartment_tableWidget_2.setItem(row, column, item)
                    
        self.ui.Apartment_tableWidget_2.verticalHeader().setVisible(False)
        self.ui.Apartment_tableWidget_2.setEditTriggers(QAbstractItemView.NoEditTriggers)
        
        # Set the header labels
        header_labels = ["Apartment_ID", "Apartment_No", "Floor_level", "Rental_bill"]
        self.ui.Apartment_tableWidget_2.setHorizontalHeaderLabels(header_labels)
    
    def ocupy(self): 
        
        # Update the table widget with data from Occupy table
        update_table_widget_sql = "SELECT * FROM Occupy"
        mycursor.execute(update_table_widget_sql)
        occupy_data = mycursor.fetchall()
        
        self.ui.Apartment_tableWidget_2.clear()
        column_count = 2  
        self.ui.Apartment_tableWidget_2.setRowCount(len(occupy_data))
        self.ui.Apartment_tableWidget_2.setColumnCount(column_count)  
    
        self.ui.Apartment_tableWidget_2.setRowCount(len(occupy_data))
        for row, occupy in enumerate(occupy_data):
            for column, value in enumerate(occupy):
                item = QTableWidgetItem(str(value))
                item.setTextAlignment(Qt.AlignCenter)
                self.ui.Apartment_tableWidget_2.setItem(row, column, item)
                    
        self.ui.Apartment_tableWidget_2.verticalHeader().setVisible(False)
        self.ui.Apartment_tableWidget_2.setEditTriggers(QAbstractItemView.NoEditTriggers)
        
        # Set the header labels
        header_labels = ["Tenant_ID", "Apartment_ID"]
        self.ui.Apartment_tableWidget_2.setHorizontalHeaderLabels(header_labels)
    
        
    def lease(self):
        
       # Update the table widget with data from Lease table
        update_table_widget_sql = "SELECT * FROM Lease"
        mycursor.execute(update_table_widget_sql)
        lease_data = mycursor.fetchall()
        
        self.ui.Apartment_tableWidget_2.clear()
        column_count = 4  
        self.ui.Apartment_tableWidget_2.setRowCount(len(lease_data))
        self.ui.Apartment_tableWidget_2.setColumnCount(column_count) 
            
        self.ui.Apartment_tableWidget_2.setRowCount(len(lease_data))
        for row, lease in enumerate(lease_data):
            for column, value in enumerate(lease):
                item = QTableWidgetItem(str(value))
                item.setTextAlignment(Qt.AlignCenter)
                self.ui.Apartment_tableWidget_2.setItem(row, column, item)
        
        self.ui.Apartment_tableWidget_2.verticalHeader().setVisible(False)
        self.ui.Apartment_tableWidget_2.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # Set the header labels
        header_labels = ["Lease_ID", "Date_Lease", "Tenant_ID", "Apartment_ID"]
        self.ui.Apartment_tableWidget_2.setHorizontalHeaderLabels(header_labels)
        
    
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
        
  ############################################################################################################################################################      
    
    def click_CRUD_apart_page(self):
        # Update the table widget with data from Apartment table
        update_table_widget_sql = "SELECT * FROM Apartment"
        mycursor.execute(update_table_widget_sql)
        apartment_data = mycursor.fetchall()
            
        self.ui.Apartment_tableWidget_3.setRowCount(len(apartment_data))
        for row, apartment in enumerate(apartment_data):
            for column, value in enumerate(apartment):
                item = QTableWidgetItem(str(value))
                item.setTextAlignment(Qt.AlignCenter)
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
        
        set_auto_increment_sql = "ALTER TABLE Apartment AUTO_INCREMENT = 8800"
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
                    item.setTextAlignment(Qt.AlignCenter)
                    self.ui.Apartment_tableWidget_3.setItem(row, column, item)
                    
            self.ui.Apartment_tableWidget_3.verticalHeader().setVisible(False)
            
            # Reset to blank all line edit and combo box    
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
                        item.setTextAlignment(Qt.AlignCenter)
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

        # Check if the apartment number already exists, except for the selected apartment
        check_existing_sql = "SELECT COUNT(*) FROM Apartment WHERE Apartment_No = %s AND Apartment_ID <> %s"  
        mycursor.execute(check_existing_sql, (ApartmentNumber, apartment_id))
        count = mycursor.fetchone()[0]
        if count > 0:
            QMessageBox.warning(self, "Duplicate Apartment Number", "Apartment number already exists.")
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
                    item.setTextAlignment(Qt.AlignCenter)
                    self.ui.Apartment_tableWidget_3.setItem(row, column, item)

            self.ui.Apartment_tableWidget_3.verticalHeader().setVisible(False)
            
            # Reset to blank all line edit and combo box
            self.ui.ApartNum_line_edit.setText("")
            self.ui.FloorLvl_comboBox.setCurrentIndex(0)
            self.ui.RentalBill_line_edit.setText("")

        except Error as e:
            print(e)
            
############################################################################################################################################################

    def click_pay_list_page(self): 
        # Update the table widget with data from Payment table
        update_table_widget_sql = "SELECT * FROM Payment"
        mycursor.execute(update_table_widget_sql)
        payment_data = mycursor.fetchall()
            
        self.ui.Payment_tableWidget.setRowCount(len(payment_data))
        for row, apartment in enumerate(payment_data):
            for column, value in enumerate(apartment):
                item = QTableWidgetItem(str(value))
                item.setTextAlignment(Qt.AlignCenter)
                self.ui.Payment_tableWidget.setItem(row, column, item)
                    
        self.ui.Payment_tableWidget.verticalHeader().setVisible(False)
        self.ui.Payment_tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers) 
    
    def search_payment(self):
        # Find the data in the Payment table
        search_text = self.ui.Search_lineEdit_3.text()

        sql_query = "SELECT * FROM Payment WHERE Payment_ID LIKE %s OR Payment_Status LIKE %s OR Payment_Date LIKE %s OR Amount_Paid LIKE %s OR Payment_Method LIKE %s OR Tenant_ID LIKE %s OR Apartment_ID LIKE %s"
        params = (f"{search_text}%", f"{search_text}%", f"{search_text}%", f"{search_text}%", f"{search_text}%", f"{search_text}%", f"{search_text}%")
        mycursor.execute(sql_query, params)
        result = mycursor.fetchall()

        # Set up the table
        table_widget = self.ui.Payment_tableWidget
        table_widget.clearContents()
        table_widget.setRowCount(len(result))

        for row, apartment in enumerate(result):
            for col, data in enumerate(apartment):
                item = QTableWidgetItem(str(data))
                item.setTextAlignment(Qt.AlignCenter)
                table_widget.setItem(row, col, item)

        table_widget.setSizeAdjustPolicy(QAbstractItemView.AdjustToContents)
        table_widget.resizeColumnsToContents()
                
############################################################################################################################################################

    def click_payment_page(self):
        # Update the table widget with data from Payment table
        update_table_widget_sql = "SELECT * FROM Payment"
        mycursor.execute(update_table_widget_sql)
        payment_data = mycursor.fetchall()

        self.ui.Payment_tableWidget_5.setRowCount(len(payment_data))
        for row, payment in enumerate(payment_data):
            for column, value in enumerate(payment):
                item = QTableWidgetItem(str(value))
                item.setTextAlignment(Qt.AlignCenter)
                self.ui.Payment_tableWidget_5.setItem(row, column, item)

        self.ui.Payment_tableWidget_5.verticalHeader().setVisible(False)
        self.ui.Payment_tableWidget_5.setEditTriggers(QAbstractItemView.NoEditTriggers)
        

    def add_payment(self):
        # Create table Payment if there is no existing table
        mycursor.execute("""
            CREATE TABLE IF NOT EXISTS Payment (
                Payment_ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                Payment_Status VARCHAR(15) NOT NULL,
                Payment_Date DATE,
                Amount_Paid DECIMAL(10, 2),
                Payment_Method VARCHAR(15),
                Tenant_ID INT NOT NULL,
                Apartment_ID INT NOT NULL,
                CONSTRAINT fk2 FOREIGN KEY (Apartment_ID) REFERENCES Apartment (Apartment_ID) ON DELETE CASCADE ON UPDATE CASCADE,
                CONSTRAINT fk3 FOREIGN KEY (Tenant_ID) REFERENCES Tenant (Tenant_ID) ON DELETE CASCADE ON UPDATE CASCADE
            )
        """)
        mydb.commit()

        set_auto_increment_sql = "ALTER TABLE Payment AUTO_INCREMENT = 7700"
        mycursor.execute(set_auto_increment_sql)
        mydb.commit()

        # Get input of the user in creating a payment
        apartment_id = self.ui.ApartID_line_edit_3.text()
        tenant_id = self.ui.TenantID_line_edit3.text()
        PayStatus = self.ui.PayStat_comboBox.currentText()
        
        # Check if any input is missing
        if not all((PayStatus, apartment_id, tenant_id)):
            QMessageBox.warning(self, "Missing Input", "Please enter all the necessary data.")
            return

        # Check if the apartment ID exists in the Apartment table
        check_apartment_sql = "SELECT COUNT(*) FROM Apartment WHERE Apartment_ID = %s"
        mycursor.execute(check_apartment_sql, (apartment_id,))
        count = mycursor.fetchone()[0]
        if count == 0:
            QMessageBox.warning(self, "Invalid Apartment ID", "Apartment ID does not exist.")
            return
        
        # Check if the Tenant ID exists in the Tenant table
        check_tenant_sql = "SELECT COUNT(*) FROM Tenant WHERE Tenant_ID = %s"
        mycursor.execute(check_tenant_sql, (tenant_id,))
        count = mycursor.fetchone()[0]
        if count == 0:
            QMessageBox.warning(self, "Invalid Tenant ID", "Tenant ID does not exist.")
            return

        # Check if the payment status is successful
        if PayStatus == "Successful":
            # Prompt for payment amount, payment date, and payment method
            payment_amount, ok = QInputDialog.getDouble(self, "Enter Payment Amount", "Payment Amount:")
            if not ok:
                return

            payment_date, ok = QInputDialog.getText(self, "Enter Payment Date", "Payment Date (YYYY-MM-DD):")
            if not ok:
                return

            payment_method, ok = QInputDialog.getItem(self, "Select Payment Method", "Payment Method:",
                                                    ["Cash", "G-cash", "Bank"], 0, False)
            if not ok:
                return

        else:
            # Set default values for payment amount, payment date, and payment method
            payment_amount = None
            payment_date = None
            payment_method = None


        insert_payment_sql = "INSERT INTO Payment (Payment_Status, Payment_Date, Amount_Paid, Payment_Method, Apartment_ID, Tenant_ID) VALUES (%s, %s, %s, %s, %s, %s)"

        try:
            # Insert the new payment data
            mycursor.execute(insert_payment_sql,
                         (PayStatus, payment_date, payment_amount, payment_method, apartment_id, tenant_id))
            mydb.commit()
            QMessageBox.information(self, "Success", "Payment inserted successfully.")


            # Update the table widget with data from Payment table
            update_table_widget_sql = "SELECT * FROM Payment"
            mycursor.execute(update_table_widget_sql)
            payment_data = mycursor.fetchall()

            self.ui.Payment_tableWidget_5.setRowCount(len(payment_data))
            for row, payment in enumerate(payment_data):
                for column, value in enumerate(payment):
                    item = QTableWidgetItem(str(value))
                    self.ui.Payment_tableWidget_5.setItem(row, column, item)

            self.ui.Payment_tableWidget_5.verticalHeader().setVisible(False)
            self.ui.Payment_tableWidget_5.setEditTriggers(QAbstractItemView.NoEditTriggers)
            
            # Reset to blank all line edit and combo box
            self.ui.TenantID_line_edit3.setText("")
            self.ui.ApartID_line_edit_3.setText("")
            self.ui.PayStat_comboBox.setCurrentIndex(0)
            
        except Error as e:
            print("Error inserting payment:", e)

    def get_payment(self):
        # Get the selected row index from Payment_tableWidget_5
        selected_row = self.ui.Payment_tableWidget_5.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "No Selection", "Please select a payment to update.")
            return

        # Get the Payment ID value from the selected row
        payment_id = self.ui.Payment_tableWidget_5.item(selected_row, 0).text()

        try:
            # Fetch the payment data from the database
            fetch_payment_sql = "SELECT * FROM Payment WHERE Payment_ID = %s"
            mycursor.execute(fetch_payment_sql, (payment_id,))
            payment_data = mycursor.fetchone()

            if payment_data is not None:
                # Update the input fields with the apartment data
                self.ui.TenantID_line_edit3.setText(str(payment_data[5]))
                self.ui.ApartID_line_edit_3.setText(str(payment_data[6]))
                self.ui.PayStat_comboBox.setCurrentText(str(payment_data[1]))
            
            else:
                QMessageBox.warning(self, "Payment Not Found", "Payment ID does not exist.")

        except Error as e:
            print(e)

    def update_payment(self):
        selected_row = self.ui.Payment_tableWidget_5.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "No Selection", "Please select an apartment to update.")
            return
        
        # Get the payment ID from the selected row
        payment_id = self.ui.Payment_tableWidget_5.item(selected_row, 0).text()
        
        # Get input of the user in creating a payment
        tenant_id = self.ui.TenantID_line_edit3.text()
        apartment_id = self.ui.ApartID_line_edit_3.text()
        PayStatus = self.ui.PayStat_comboBox.currentText()

        # Check if any input is missing
        if not all((apartment_id, tenant_id, PayStatus)):
            QMessageBox.warning(self, "Missing Input", "Please enter all the necessary data.")
            return

        # Check if the apartment ID exists in the Apartment table
        check_apartment_sql = "SELECT COUNT(*) FROM Apartment WHERE Apartment_ID = %s"
        mycursor.execute(check_apartment_sql, (apartment_id,))
        count = mycursor.fetchone()[0]
        if count == 0:
            QMessageBox.warning(self, "Invalid Apartment ID", "Apartment ID does not exist.")
            return
        
        # Check if the Tenant ID exists in the Tenant table
        check_tenant_sql = "SELECT COUNT(*) FROM Tenant WHERE Tenant_ID = %s"
        mycursor.execute(check_tenant_sql, (tenant_id,))
        count = mycursor.fetchone()[0]
        if count == 0:
            QMessageBox.warning(self, "Invalid Tenant ID", "Tenant ID does not exist.")
            return
        
        # Check if the payment status is successful
        if PayStatus == "Successful":
            # Prompt for payment amount, payment date, and payment method
            payment_amount, ok = QInputDialog.getDouble(self, "Enter Payment Amount", "Payment Amount:")
            if not ok:
                return

            payment_date, ok = QInputDialog.getText(self, "Enter Payment Date", "Payment Date (YYYY-MM-DD):")
            if not ok:
                return

            payment_method, ok = QInputDialog.getItem(self, "Select Payment Method", "Payment Method:",
                                                    ["Cash", "G-cash", "Bank"], 0, False)
            if not ok:
                return

        else:
            # Set default values for payment amount, payment date, and payment method
            payment_amount = None
            payment_date = None
            payment_method = None

        # Update the apartment data in the database
        try:
            update_payment_sql = "UPDATE Payment SET Payment_Status = %s, Payment_Date = %s, Amount_Paid = %s, Payment_Method = %s, Tenant_ID = %s, Apartment_ID = %s WHERE Payment_ID = %s"
            # Update the payment data
            mycursor.execute(update_payment_sql,
                            (PayStatus, payment_date, payment_amount, payment_method, tenant_id, apartment_id, payment_id))
            mydb.commit()
            QMessageBox.information(self, "Success", "Payment updated successfully.")

            # Update the table widget with data from Payment table
            update_table_widget_sql = "SELECT * FROM Payment"
            mycursor.execute(update_table_widget_sql)
            payment_data = mycursor.fetchall()

            self.ui.Payment_tableWidget_5.setRowCount(len(payment_data))
            for row, payment in enumerate(payment_data):
                for column, value in enumerate(payment):
                    item = QTableWidgetItem(str(value))
                    self.ui.Payment_tableWidget_5.setItem(row, column, item)

            self.ui.Payment_tableWidget_5.verticalHeader().setVisible(False)
            
            # Reset to blank all line edit and combo box
            self.ui.TenantID_line_edit3.setText("")
            self.ui.ApartID_line_edit_3.setText("")
            self.ui.PayStat_comboBox.setCurrentIndex(0)
            
        except Error as e:
            print("Error inserting payment:", e)

    def delete_payment(self):
        current_row = self.ui.Payment_tableWidget_5.currentRow()
        if current_row != -1:
            # Get the payment ID from the selected row
            payment_id = self.ui.Payment_tableWidget_5.item(current_row, 0).text()

            # Confirm the deletion with the user
            confirm = QMessageBox.question(
                self, "Delete Payment", "Are you sure you want to delete this payment?", 
                QMessageBox.Yes | QMessageBox.No
            )
            if confirm == QMessageBox.Yes:
                # Delete the payment from the Payment table
                delete_payment_sql = "DELETE FROM Payment WHERE Payment_ID = %s"

                try:
                    mycursor.execute(delete_payment_sql, (payment_id,))
                    mydb.commit()
                    QMessageBox.information(self, "Success", "Payment deleted successfully.")

                    # Update the table widget with data from Payment table
                    update_table_widget_sql = "SELECT * FROM Payment"
                    mycursor.execute(update_table_widget_sql)
                    payment_data = mycursor.fetchall()

                    self.ui.Payment_tableWidget_5.setRowCount(len(payment_data))
                    for row, payment in enumerate(payment_data):
                        for column, value in enumerate(payment):
                            item = QTableWidgetItem(str(value))
                            self.ui.Payment_tableWidget_5.setItem(row, column, item)

                    self.ui.Payment_tableWidget_5.verticalHeader().setVisible(False)

                except Error as e:
                    print("Error deleting payment:", e)
        else:
            QMessageBox.warning(self, "No Selection", "Please select a payment to delete.")
    
############################################################################################################################################################

    def click_EB_list_page(self): 
        # Update the table widget with data from Electric Bill table
        update_table_widget_sql = "SELECT * FROM Electric_Bill"
        mycursor.execute(update_table_widget_sql)
        ElectricBill_data = mycursor.fetchall()
            
        self.ui.ElectricBill_tableWidget.setRowCount(len(ElectricBill_data))
        for row, apartment in enumerate(ElectricBill_data):
            for column, value in enumerate(apartment):
                item = QTableWidgetItem(str(value))
                item.setTextAlignment(Qt.AlignCenter)
                self.ui.ElectricBill_tableWidget.setItem(row, column, item)
                    
        self.ui.ElectricBill_tableWidget.verticalHeader().setVisible(False)
        self.ui.ElectricBill_tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers) 
    
    def search_electricbill(self):
        # Find the data in the Electric Bill table
        search_text = self.ui.Search_lineEdit_4.text()

        mycursor.execute("SELECT * FROM Electric_Bill WHERE Elec_Bill_ID LIKE %s OR Date_Start LIKE %s OR KWH LIKE %s OR Status LIKE %s OR Apartment_ID LIKE %s",
            (f"{search_text}%", f"{search_text}%", f"{search_text}%", f"{search_text}%", f"{search_text}%"))

        result = mycursor.fetchall()

        # Set up the table
        table_widget = self.ui.ElectricBill_tableWidget
        table_widget.clearContents()
        table_widget.setRowCount(len(result))

        for row, apartment in enumerate(result):
            for col, data in enumerate(apartment):
                item = QTableWidgetItem(str(data))
                item.setTextAlignment(Qt.AlignCenter)
                table_widget.setItem(row, col, item)

        table_widget.setSizeAdjustPolicy(QAbstractItemView.AdjustToContents)          
        
############################################################################################################################################################

    def click_electric_bill_page(self):
        # Update the table widget with data from Electric_Bill table
        update_table_widget_sql = "SELECT * FROM Electric_Bill"
        mycursor.execute(update_table_widget_sql)
        electric_bill_data = mycursor.fetchall()

        self.ui.ElectricBill_tableWidget_2.setRowCount(len(electric_bill_data))
        for row, bill in enumerate(electric_bill_data):
            for column, value in enumerate(bill):
                item = QTableWidgetItem(str(value))
                item.setTextAlignment(Qt.AlignCenter)
                self.ui.ElectricBill_tableWidget_2.setItem(row, column, item)

        self.ui.ElectricBill_tableWidget_2.verticalHeader().setVisible(False)
        self.ui.ElectricBill_tableWidget_2.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def add_electric_bill(self):
        # Create table Electric_Bill if there is no existing table
        mycursor.execute("""
            CREATE TABLE IF NOT EXISTS Electric_Bill (
                Elec_Bill_ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                Date_Start DATE NOT NULL,
                KWH DECIMAL(10, 2) NOT NULL,
                Status VARCHAR(15)NOT NULL,
                Apartment_ID INT NOT NULL,
                CONSTRAINT fk4 FOREIGN KEY (Apartment_ID) REFERENCES Apartment (Apartment_ID) ON DELETE CASCADE ON UPDATE CASCADE
            )
        """)
        mydb.commit()

        set_auto_increment_sql = "ALTER TABLE Electric_Bill AUTO_INCREMENT = 9900"
        mycursor.execute(set_auto_increment_sql)
        mydb.commit()
        
        # Get input of the user in creating an electric bill
        DateStarted = self.ui.DateStart_dateEdit.date().toString("yyyy-MM-dd")
        Kwh = self.ui.kwh_line_edit.text()
        Status = self.ui.Status_comboBox.currentText()
        ApartmentID = self.ui.ApartID_line_edit_7.text()

        # Check if any input is missing
        if not all((DateStarted, Kwh, Status, ApartmentID)):
            QMessageBox.warning(self, "Missing Input", "Please enter all the necessary data.")
            return

        # Check if the apartment ID exists in the Apartment table
        check_apartment_sql = "SELECT COUNT(*) FROM Apartment WHERE Apartment_ID = %s"
        mycursor.execute(check_apartment_sql, (ApartmentID,))
        count = mycursor.fetchone()[0]
        if count == 0:
            QMessageBox.warning(self, "Invalid Apartment ID", "Apartment ID does not exist.")
            return

        insert_electric_bill_sql = "INSERT INTO Electric_Bill (Date_Start, KWH, Status, Apartment_ID) VALUES (%s, %s, %s, %s)"

        try:
            # Insert the new electric bill data
            mycursor.execute(insert_electric_bill_sql, (DateStarted, Kwh, Status, ApartmentID))
            mydb.commit()
            QMessageBox.information(self, "Success", "Electric bill inserted successfully.")

            # Update the table widget with data from Electric_Bill table
            update_table_widget_sql = "SELECT * FROM Electric_Bill"
            mycursor.execute(update_table_widget_sql)
            electric_bill_data = mycursor.fetchall()

            self.ui.ElectricBill_tableWidget_2.setRowCount(len(electric_bill_data))
            for row, bill in enumerate(electric_bill_data):
                for column, value in enumerate(bill):
                    item = QTableWidgetItem(str(value))
                    item.setTextAlignment(Qt.AlignCenter)
                    self.ui.ElectricBill_tableWidget_2.setItem(row, column, item)

            self.ui.ElectricBill_tableWidget_2.verticalHeader().setVisible(False)
            self.ui.ElectricBill_tableWidget_2.setEditTriggers(QAbstractItemView.NoEditTriggers)

            # Reset to blank all line edit and combo box
            self.ui.DateStart_dateEdit.setDate(QDate())
            self.ui.kwh_line_edit.setText("")
            self.ui.Status_comboBox.setCurrentIndex(0)
            self.ui.ApartID_line_edit_7.setText("")
            
        except Error as e:
            print("Error inserting electric bill:", e)
            
            
    def get_electric_bill(self):
        # Get the selected row index from ElectricBill_tableWidget_2
        selected_row = self.ui.ElectricBill_tableWidget_2.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "No Selection", "Please select a electric bill to update.")
            return

        # Get the Payment ID value from the selected row
        EB_ID = self.ui.ElectricBill_tableWidget_2.item(selected_row, 0).text()

        try:
            # Fetch the payment data from the database
            fetch_EB_sql = "SELECT * FROM Electric_Bill WHERE Elec_Bill_ID = %s"
            mycursor.execute(fetch_EB_sql, (EB_ID,))
            EB_data = mycursor.fetchone()

            if EB_data is not None:
                 # Convert the date string to a QDate object
                date_str = str(EB_data[1])
                year, month, day = map(int, date_str.split('-'))
                date_start = QDate(year, month, day)

                # Update the input fields with the apartment data
                self.ui.DateStart_dateEdit.setDate(date_start)
                self.ui.kwh_line_edit.setText(str(EB_data[2]))
                self.ui.Status_comboBox.setCurrentText(str(EB_data[3]))
                self.ui.ApartID_line_edit_7.setText(str(EB_data[4]))
            
            else:
                QMessageBox.warning(self, "Electric Bill Not Found", "Electric Bill ID does not exist.")

        except Error as e:
            print(e)


    def update_electric_bill(self):
        selected_row = self.ui.ElectricBill_tableWidget_2.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "No Selection", "Please select an apartment to update.")
            return
        
        # Get the electric bill ID from the selected row
        elec_bill_id = self.ui.ElectricBill_tableWidget_2.item(selected_row, 0).text()

        # Get input of the user in creating an electric bill
        DateStarted = self.ui.DateStart_dateEdit.date().toString("yyyy-MM-dd")
        Kwh = self.ui.kwh_line_edit.text()
        Status = self.ui.Status_comboBox.currentText()
        ApartmentID = self.ui.ApartID_line_edit_7.text()
        
        # Check if any input is missing
        if not all((DateStarted, Kwh, Status, ApartmentID)):
            QMessageBox.warning(self, "Missing Input", "Please enter all the necessary data.")
            return
        
        # Check if the apartment ID exists in the Apartment table
        check_apartment_sql = "SELECT COUNT(*) FROM Apartment WHERE Apartment_ID = %s"
        mycursor.execute(check_apartment_sql, (ApartmentID,))
        count = mycursor.fetchone()[0]
        if count == 0:
            QMessageBox.warning(self, "Invalid Apartment ID", "Apartment ID does not exist.")
            return

        # Update the apartment data in the database
        try:
            update_EB_sql = "UPDATE Electric_Bill SET Date_Start = %s, KWH = %s, Status = %s, Apartment_ID = %s WHERE Elec_Bill_ID = %s"
            # Update the payment data
            mycursor.execute(update_EB_sql,
                            (DateStarted, Kwh, Status, ApartmentID, elec_bill_id))
            mydb.commit()
            QMessageBox.information(self, "Success", "Electric Bill updated successfully.")

           # Update the table widget with data from Electric_Bill table
            update_table_widget_sql = "SELECT * FROM Electric_Bill"
            mycursor.execute(update_table_widget_sql)
            electric_bill_data = mycursor.fetchall()

            self.ui.ElectricBill_tableWidget_2.setRowCount(len(electric_bill_data))
            for row, bill in enumerate(electric_bill_data):
                for column, value in enumerate(bill):
                    item = QTableWidgetItem(str(value))
                    self.ui.ElectricBill_tableWidget_2.setItem(row, column, item)

            self.ui.ElectricBill_tableWidget_2.verticalHeader().setVisible(False)
            self.ui.ElectricBill_tableWidget_2.setEditTriggers(QAbstractItemView.NoEditTriggers)

            # Reset to blank all line edit and combo box
            self.ui.DateStart_dateEdit.setDate(QDate())
            self.ui.kwh_line_edit.setText("")
            self.ui.Status_comboBox.setCurrentIndex(0)
            self.ui.ApartID_line_edit_7.setText("")
            
        except Error as e:
            print("Error inserting electric bill:", e)

    def delete_electric_bill(self):
        selected_row = self.ui.ElectricBill_tableWidget_2.currentRow()
        if selected_row != -1:
            # Get the electric bill ID from the selected row
            elec_bill_id = self.ui.ElectricBill_tableWidget_2.item(selected_row, 0).text()

            # Confirm deletion with the user
            confirm = QMessageBox.question(self, "Delete Electric Bill", "Are you sure you want to delete this electric bill?",
                                           QMessageBox.Yes | QMessageBox.No)
            if confirm == QMessageBox.Yes:
                
                # Delete the electric bill from the Electric_Bill table
                delete_sql = "DELETE FROM Electric_Bill WHERE Elec_Bill_ID = %s"
                mycursor.execute(delete_sql, (elec_bill_id,))
                mydb.commit()

                QMessageBox.information(self, "Success", "Electric bill deleted successfully.")

                # Update the table widget with data from Electric_Bill table
                update_table_widget_sql = "SELECT * FROM Electric_Bill"
                mycursor.execute(update_table_widget_sql)
                electric_bill_data = mycursor.fetchall()

                self.ui.ElectricBill_tableWidget_2.setRowCount(len(electric_bill_data))
                for row, bill in enumerate(electric_bill_data):
                    for column, value in enumerate(bill):
                        item = QTableWidgetItem(str(value))
                        self.ui.ElectricBill_tableWidget_2.setItem(row, column, item)

        else:
            QMessageBox.warning(self, "No Selection", "Please select an electric bill to delete.")