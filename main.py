import sys

import os
os.environ['ICONIFY_QTLIB'] = 'PySide6'


from ui_interface import *

from functions import appFunctions

class MainWindow(QMainWindow):
    def __init__(self, parent = None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
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
        
        
        
        
        ##  CRUDApartPage BUTTONS
        ####################################################################################################
        
        self.ui.AddApartBtn.clicked.connect(lambda: appFunctions.addapartment(self))
        
        
        
        
        
        
        
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
    sys.exit(app.exec_())
    
    