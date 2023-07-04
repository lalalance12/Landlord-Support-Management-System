import sys

import os
os.environ['ICONIFY_QTLIB'] = 'PySide6'

from PySide6.QtWidgets import QAbstractItemView
from ui_interface import *

from functions import appFunctions

class MainWindow(QMainWindow):
    def __init__(self, parent = None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        tables = [
            self.ui.Apartment_tableWidget_2,
            self.ui.Apartment_tableWidget_3,
            self.ui.ElectricBill_tableWidget_2,
            self.ui.Payment_tableWidget_5,
            self.ui.Tenant_tableWidget,
            self.ui.ElectricBill_tableWidget,
            self.ui.Payment_tableWidget,
            self.ui.Tenant_tableWidget_3,
            self.ui.PayHis_tableWidget_2
        ]

        for table in tables:
            table.setEditTriggers(QAbstractItemView.NoEditTriggers)
            
            table.verticalHeader().setVisible(False)
                
        
        ##  MAIN PAGES
        ####################################################################################################
        self.ui.TenantStatListBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.TSListPage))
        self.ui.CRUDTenantBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.CRUDTenantPage))
        self.ui.TenantInfoBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.TenantInfoPage))
        
        self.ui.ApartmentInfoBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.ApartmentInfoPage))
        self.ui.CRUDApartmentBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.CRUDApartPage))
        
        self.ui.PaymentListBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.PaymentListPage))
        self.ui.CRUDPaymentBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.CRUDPaymentPage))
        
        self.ui.ElecBillBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.EBListPage))
        self.ui.CRUDElectricBillBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.CRUDElecBillPage))
        
        
        
        ##  TSListPage BUTTONS
        ####################################################################################################
        
        
        
        
        
        ##  CRUDTenantPage BUTTONS
        ####################################################################################################
        
        
        
        
         
        ##  TenantInfoPage BUTTONS
        ####################################################################################################
        
        
        
        
        
        
        
        
        
        ##  ApartmentInfoPage BUTTONS
        ####################################################################################################
        
        self.ui.ApartmentInfoBtn.clicked.connect(lambda: appFunctions.click_apart_info_page(self))           # table
        self.ui.Search_lineEdit_2.textChanged.connect(lambda: appFunctions.search_apartment(self))           # search bar
        
        ##  CRUDApartPage BUTTON
        ####################################################################################################
        
        self.ui.CRUDApartmentBtn.clicked.connect(lambda: appFunctions.click_CRUD_apart_page(self))           # table
        self.ui.AddApartBtn.clicked.connect(lambda: appFunctions.add_apartment(self))                        # add button
        self.ui.DelApartBtn.clicked.connect(lambda: appFunctions.delete_apartment(self))                     # delete button
        self.ui.GetApartBtn.clicked.connect(lambda: appFunctions.get_apartment(self))                        # get button
        self.ui.UpdApartBtn.clicked.connect(lambda: appFunctions.update_apartment(self))                     # update button
        
        ##  PaymentListPage BUTTONS
        ####################################################################################################
        
        
        
        
        ##  CRUDPaymentPage BUTTONS
        ####################################################################################################
        
        
        
        
        
        
        
        
        ##  EBListPage BUTTONS
        ####################################################################################################
        
        
        
        
        
        
        ##  CRUDElecBillPage BUTTONS
        ####################################################################################################
        
        
        
        
        
        self.show()
        
        
        
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
    
    