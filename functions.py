import mysql.connector
from mysql.connector import Error
from PySide6.QtWidgets import QTableWidgetItem, QComboBox, QHeaderView, QDialog, QVBoxLayout, QMessageBox, QInputDialog
from PySide6.QtCore import Qt
from datetime import date


mydb = mysql.connector.connect (

    host="localhost",
    user ="root",
    password="root",
    database="LSMS_database"

)


mycursor = mydb.cursor ()


class appFunctions():
    def __init__(self, arg):
        super(appFunctions, self).__init__()
        self.arg = arg