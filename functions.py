import mysql.connector
from mysql.connector import Error
from PySide6.QtWidgets import QTableWidgetItem, QComboBox, QHeaderView, QDialog, QVBoxLayout, QMessageBox, QInputDialog, QAbstractItemView, QCalendarWidget, QDialogButtonBox, QLabel, QDialogButtonBox
from PySide6.QtCore import Qt, QDate
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
        
############################################################################################################################################################

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
        
        set_auto_increment_sql = "ALTER TABLE Lease AUTO_INCREMENT = 4000"
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
        
        set_auto_increment_sql = "ALTER TABLE Tenant AUTO_INCREMENT = 2020"
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

        mycursor.execute("SELECT * FROM Apartment WHERE Payment_ID LIKE %s OR Payment_Status LIKE %s OR Payment_Date LIKE %s OR Amount_Paid LIKE %s OR Payment_Method LIKE %s OR Tenant_ID %s OR Apartment_ID LIKE %s",
            (f"{search_text}%", f"{search_text}%", f"{search_text}%", f"{search_text}%" f"{search_text}%", f"{search_text}%", f"{search_text}%"))

        result = mycursor.fetchall()

        # Set up the table
        table_widget = self.ui.Payment_tableWidget
        table_widget.clearContents()
        table_widget.setRowCount(len(result))

        for row, apartment in enumerate(result):
            for col, data in enumerate(apartment):
                item = QTableWidgetItem(str(data))
                table_widget.setItem(row, col, item)

        table_widget.setSizeAdjustPolicy(QAbstractItemView.AdjustToContents)
        table_widget.resizeColumnsToContents()
        
        
############################################################################################################################################################


    def click_CRUD_payment_page(self):
        # Update the table widget with data from Payment table
        update_table_widget_sql = "SELECT * FROM Payment"
        mycursor.execute(update_table_widget_sql)
        payment_data = mycursor.fetchall()
            
        self.ui.Payment_tableWidget_5.setRowCount(len( payment_data))
        for row, apartment in enumerate(payment_data):
            for column, value in enumerate(apartment):
                item = QTableWidgetItem(str(value))
                item.setTextAlignment(Qt.AlignCenter)
                self.ui.Payment_tableWidget_5.setItem(row, column, item)
                    
        self.ui.Payment_tableWidget_5.verticalHeader().setVisible(False)
        self.ui.Payment_tableWidget_5.setEditTriggers(QAbstractItemView.NoEditTriggers)
        
        
    def add_payment(self):
        # Create table Payment if there is no existing table
        mycursor.execute("""
            CREATE TABLE IF NOT EXISTS Payment (
                Payment_ID INT PRIMARY KEY,
                Payment_Status VARCHAR(15),
                Payment_Date DATE,
                Amount_Paid DECIMAL(6, 2),
                Payment_Method VARCHAR(15),
                Tenant_ID INT,
                Apartment_ID INT,
                CONSTRAINT fk2 FOREIGN KEY (Apartment_ID) REFERENCES Apartment (Apartment_ID) ON DELETE CASCADE ON UPDATE CASCADE,
                CONSTRAINT fk3 FOREIGN KEY (Tenant_ID) REFERENCES Tenant (Tenant_ID) ON DELETE CASCADE ON UPDATE CASCADE
                )
        """)
        mydb.commit()
        
        set_auto_increment_sql = "ALTER TABLE Payment AUTO_INCREMENT = 4000"
        mycursor.execute(set_auto_increment_sql)
        mydb.commit()
        
        #######################################     RESUME HERE
        
        """"
        # Get input of the user in creating an payment
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
    
        """
    
    
    
    
    
    
 
    
    
    
    
    



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

        mycursor.execute("SELECT * FROM Apartment WHERE Elec_Bill_ID LIKE %s OR Date_Start LIKE %s OR KWH LIKE %s OR Status LIKE %s OR Apartment_ID LIKE %s",
            (f"{search_text}%", f"{search_text}%", f"{search_text}%", f"{search_text}%" f"{search_text}%"))

        result = mycursor.fetchall()

        # Set up the table
        table_widget = self.ui.ElectricBill_tableWidget
        table_widget.clearContents()
        table_widget.setRowCount(len(result))

        for row, apartment in enumerate(result):
            for col, data in enumerate(apartment):
                item = QTableWidgetItem(str(data))
                table_widget.setItem(row, col, item)

        table_widget.setSizeAdjustPolicy(QAbstractItemView.AdjustToContents)
        table_widget.resizeColumnsToContents()            
        
############################################################################################################################################################