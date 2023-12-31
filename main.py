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
        
        self.ui.TenantStatListBtn.clicked.connect(lambda: appFunctions.click_tenant_stat_list_page(self))    # table
        
        ##  CRUDTenantPage BUTTONS
        ####################################################################################################
        
        self.ui.CRUDTenantBtn.clicked.connect(lambda: appFunctions.click_CRUD_tenant_page(self))             # table
        self.ui.AddTenantBtn.clicked.connect(lambda: appFunctions.add_tenant(self))                          # add button
        self.ui.DelTenantBtn.clicked.connect(lambda: appFunctions.delete_tenant(self))                       # delete button
        self.ui.GetTenantBtn.clicked.connect(lambda: appFunctions.get_tenant(self))                          # get button
        self.ui.UpdTenantBtn.clicked.connect(lambda: appFunctions.update_tenant(self))                       # update button
        
        ##  TenantInfoPage BUTTONS
        ####################################################################################################
        
        self.ui.TenantInfoBtn.clicked.connect(lambda: appFunctions.click_tenant_info_page(self))             # clear line edits and tables
        self.ui.SearchTenantBtn.clicked.connect(lambda: appFunctions.search_tenant(self))                    # search button
        self.ui.PayHisBtn.clicked.connect(lambda: appFunctions.payment_history(self))                        # payment history button
        
        ##  ApartmentInfoPage BUTTONS
        ####################################################################################################
        
        ## Stack Widget Pages on Apartment Info
        self.ui.AptListBtn.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.Apartment_ListPage))
        self.ui.AptOcctBtn.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.OccupyPage))
        self.ui.AptLeaseBtn.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.LeasePage))
        
        self.ui.ApartmentInfoBtn.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.Apartment_ListPage))    # Landing Page
        self.ui.ApartmentInfoBtn.clicked.connect(lambda: appFunctions.click_apart_info_page(self))                                # table
        
        self.ui.AptListBtn.clicked.connect(lambda: appFunctions.apart_list(self))                                                 # apart. list
        self.ui.AptList_Search_lineEdit.textChanged.connect(lambda: appFunctions.search_apartment_list(self))                     # search bar (apartment list)
        
        self.ui.AptOcctBtn.clicked.connect(lambda: appFunctions.ocupy(self))                                                      # occupy
        self.ui.Occupy_Search_lineEdit.textChanged.connect(lambda: appFunctions.search_occupy(self))                              # search bar (occupy)
        
        self.ui.AptLeaseBtn.clicked.connect(lambda: appFunctions.lease(self))                                                     # lease
        self.ui.Lease_Search_lineEdit.textChanged.connect(lambda: appFunctions.search_lease(self))                                # search bar (lease)
        ##  CRUDApartPage BUTTON
        ####################################################################################################
        
        self.ui.CRUDApartmentBtn.clicked.connect(lambda: appFunctions.click_CRUD_apart_page(self))           # table
        self.ui.AddApartBtn.clicked.connect(lambda: appFunctions.add_apartment(self))                        # add button
        self.ui.DelApartBtn.clicked.connect(lambda: appFunctions.delete_apartment(self))                     # delete button
        self.ui.GetApartBtn.clicked.connect(lambda: appFunctions.get_apartment(self))                        # get button
        self.ui.UpdApartBtn.clicked.connect(lambda: appFunctions.update_apartment(self))                     # update button
        
        ##  PaymentListPage BUTTONS
        ####################################################################################################
        
        self.ui.PaymentListBtn.clicked.connect(lambda: appFunctions.click_pay_list_page(self))               # table
        self.ui.Search_lineEdit_3.textChanged.connect(lambda: appFunctions.search_payment(self))             # search bar
        
        ##  CRUDPaymentPage BUTTONS
        ####################################################################################################
        
        self.ui.CRUDPaymentBtn.clicked.connect(lambda: appFunctions.click_payment_page(self))                # table
        self.ui.AddPayBtn.clicked.connect(lambda: appFunctions.add_payment(self))                            # add button
        self.ui.UpdPayBtn.clicked.connect(lambda: appFunctions.update_payment(self))                         # update button
        self.ui.GetPayBtn.clicked.connect(lambda: appFunctions.get_payment(self))                            # get button
        self.ui.DelPayBtn.clicked.connect(lambda: appFunctions.delete_payment(self))                         # delete button  
              
        ##  EBListPage BUTTONS
        ####################################################################################################
     
        self.ui.ElecBillBtn.clicked.connect(lambda: appFunctions.click_EB_list_page(self))                   # table
        self.ui.Search_lineEdit_4.textChanged.connect(lambda: appFunctions.search_electricbill(self))        # search bar
        
        ##  CRUDElecBillPage BUTTONS
        ####################################################################################################
        
        self.ui.CRUDElectricBillBtn.clicked.connect(lambda: appFunctions.click_electric_bill_page(self))     # table
        self.ui.AddEBBtn.clicked.connect(lambda: appFunctions.add_electric_bill(self))                       # add button
        self.ui.UpdEBBtn.clicked.connect(lambda: appFunctions.update_electric_bill(self))                    # update button
        self.ui.GetEBBtn.clicked.connect(lambda: appFunctions.get_electric_bill(self))                       # get button
        self.ui.DelEBBtn.clicked.connect(lambda: appFunctions.delete_electric_bill(self))                    # delete button  
        
        
        
        self.show()
        
        
        
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
    
    