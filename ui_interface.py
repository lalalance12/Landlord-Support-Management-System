# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfacewFWAyp.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1114, 574)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
"   border: none;\n"
"   background-color: transparent;\n"
"   color: #fff;\n"
"}\n"
"\n"
"#centralwidget{\n"
"   background-color: #040f13;\n"
"}\n"
"\n"
"#side_menu{\n"
"   background-color: #071e26;\n"
"   border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton{\n"
"   padding: 10px;\n"
"   background-color: #02739C;\n"
"   border-radius: 5px;\n"
"}\n"
"#main_body{\n"
"    background-color: #071e26;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.header = QFrame(self.centralwidget)
        self.header.setObjectName(u"header")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.header.sizePolicy().hasHeightForWidth())
        self.header.setSizePolicy(sizePolicy)
        self.header.setMinimumSize(QSize(200, 50))
        self.header.setMaximumSize(QSize(1000, 50))
        self.header.setFrameShape(QFrame.StyledPanel)
        self.header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.header)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(220, 0))
        self.frame.setMaximumSize(QSize(220, 16777215))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setBold(True)
        self.label.setFont(font)

        self.horizontalLayout_4.addWidget(self.label, 0, Qt.AlignHCenter)


        self.horizontalLayout_2.addWidget(self.frame)

        self.frame_5 = QFrame(self.header)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(250, 0))
        self.frame_5.setMaximumSize(QSize(200, 16777215))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.frame_5)

        self.frame_3 = QFrame(self.header)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 20))
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(14)
        font1.setBold(True)
        self.label_2.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_2)


        self.horizontalLayout_2.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.header, 0, Qt.AlignLeft)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.side_menu = QFrame(self.frame_2)
        self.side_menu.setObjectName(u"side_menu")
        self.side_menu.setFrameShape(QFrame.StyledPanel)
        self.side_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.side_menu)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, -1, 0)
        self.frame_4 = QFrame(self.side_menu)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(200, 0))
        self.frame_4.setMaximumSize(QSize(200, 16777215))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.TenantStatListBtn = QPushButton(self.frame_4)
        self.TenantStatListBtn.setObjectName(u"TenantStatListBtn")
        self.TenantStatListBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/Icons/icons/file-text.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.TenantStatListBtn.setIcon(icon)

        self.verticalLayout_3.addWidget(self.TenantStatListBtn)

        self.CRUDTenantBtn = QPushButton(self.frame_4)
        self.CRUDTenantBtn.setObjectName(u"CRUDTenantBtn")
        self.CRUDTenantBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/Icons/icons/user-plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.CRUDTenantBtn.setIcon(icon1)

        self.verticalLayout_3.addWidget(self.CRUDTenantBtn)

        self.TenantInfoBtn = QPushButton(self.frame_4)
        self.TenantInfoBtn.setObjectName(u"TenantInfoBtn")
        self.TenantInfoBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/Icons/icons/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.TenantInfoBtn.setIcon(icon2)

        self.verticalLayout_3.addWidget(self.TenantInfoBtn)

        self.verticalSpacer = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.ApartmentInfoBtn = QPushButton(self.frame_4)
        self.ApartmentInfoBtn.setObjectName(u"ApartmentInfoBtn")
        self.ApartmentInfoBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/Icons/icons/trello.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.ApartmentInfoBtn.setIcon(icon3)

        self.verticalLayout_3.addWidget(self.ApartmentInfoBtn)

        self.CRUDApartmentBtn = QPushButton(self.frame_4)
        self.CRUDApartmentBtn.setObjectName(u"CRUDApartmentBtn")
        self.CRUDApartmentBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/Icons/icons/plus-square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.CRUDApartmentBtn.setIcon(icon4)

        self.verticalLayout_3.addWidget(self.CRUDApartmentBtn)

        self.verticalSpacer_2 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.PaymentListBtn = QPushButton(self.frame_4)
        self.PaymentListBtn.setObjectName(u"PaymentListBtn")
        self.PaymentListBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/Icons/icons/clipboard.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.PaymentListBtn.setIcon(icon5)

        self.verticalLayout_3.addWidget(self.PaymentListBtn)

        self.CRUDPaymentBtn = QPushButton(self.frame_4)
        self.CRUDPaymentBtn.setObjectName(u"CRUDPaymentBtn")
        self.CRUDPaymentBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u":/Icons/icons/credit-card.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.CRUDPaymentBtn.setIcon(icon6)

        self.verticalLayout_3.addWidget(self.CRUDPaymentBtn)

        self.verticalSpacer_3 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.ElecBillBtn = QPushButton(self.frame_4)
        self.ElecBillBtn.setObjectName(u"ElecBillBtn")
        self.ElecBillBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon7 = QIcon()
        icon7.addFile(u":/Icons/icons/server.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.ElecBillBtn.setIcon(icon7)

        self.verticalLayout_3.addWidget(self.ElecBillBtn)

        self.CRUDElectricBillBtn = QPushButton(self.frame_4)
        self.CRUDElectricBillBtn.setObjectName(u"CRUDElectricBillBtn")
        self.CRUDElectricBillBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon8 = QIcon()
        icon8.addFile(u":/Icons/icons/zap.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.CRUDElectricBillBtn.setIcon(icon8)

        self.verticalLayout_3.addWidget(self.CRUDElectricBillBtn)


        self.verticalLayout_2.addWidget(self.frame_4, 0, Qt.AlignTop)


        self.horizontalLayout.addWidget(self.side_menu, 0, Qt.AlignLeft)

        self.main_body = QFrame(self.frame_2)
        self.main_body.setObjectName(u"main_body")
        sizePolicy.setHeightForWidth(self.main_body.sizePolicy().hasHeightForWidth())
        self.main_body.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setPointSize(6)
        self.main_body.setFont(font2)
        self.main_body.setFrameShape(QFrame.StyledPanel)
        self.main_body.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.main_body)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.stackedWidget = QStackedWidget(self.main_body)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.TSListPage = QWidget()
        self.TSListPage.setObjectName(u"TSListPage")
        self.Search_lineEdit = QLineEdit(self.TSListPage)
        self.Search_lineEdit.setObjectName(u"Search_lineEdit")
        self.Search_lineEdit.setGeometry(QRect(610, 20, 240, 20))
        self.Search_lineEdit.setMinimumSize(QSize(240, 20))
        self.Search_lineEdit.setMaximumSize(QSize(240, 30))
        self.Search_lineEdit.setStyleSheet(u"QLineEdit {\n"
"    border: none;\n"
"    color: #FFF;\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"    background-color: rgb(33, 37, 41); \n"
"    border-image: url(rounded-border.png) 15 15 15 15 stretch stretch;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(48, 50, 62);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(85, 170, 255);\n"
"    background-color: rgb(33, 37, 41); \n"
"}")
        self.TenantStatList_label = QLabel(self.TSListPage)
        self.TenantStatList_label.setObjectName(u"TenantStatList_label")
        self.TenantStatList_label.setGeometry(QRect(30, 20, 201, 16))
        font3 = QFont()
        font3.setFamilies([u"Times New Roman"])
        font3.setPointSize(11)
        self.TenantStatList_label.setFont(font3)
        self.Tenant_tableWidget_3 = QTableWidget(self.TSListPage)
        if (self.Tenant_tableWidget_3.columnCount() < 6):
            self.Tenant_tableWidget_3.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.Tenant_tableWidget_3.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.Tenant_tableWidget_3.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.Tenant_tableWidget_3.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.Tenant_tableWidget_3.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.Tenant_tableWidget_3.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.Tenant_tableWidget_3.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.Tenant_tableWidget_3.setObjectName(u"Tenant_tableWidget_3")
        self.Tenant_tableWidget_3.setGeometry(QRect(20, 50, 831, 421))
        self.Tenant_tableWidget_3.setStyleSheet(u"QTableWidget {\n"
"    background-color: #333333;\n"
"    color: white;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #555555;\n"
"    color: white;\n"
"}\n"
"")
        self.stackedWidget.addWidget(self.TSListPage)
        self.TenantInfoPage = QWidget()
        self.TenantInfoPage.setObjectName(u"TenantInfoPage")
        self.frame_9 = QFrame(self.TenantInfoPage)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(10, 0, 851, 464))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.frame_10 = QFrame(self.frame_9)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"background-color: #333333;\n"
"color: white;")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.page_label_2 = QLabel(self.frame_10)
        self.page_label_2.setObjectName(u"page_label_2")
        self.page_label_2.setGeometry(QRect(10, 10, 201, 16))
        self.page_label_2.setFont(font3)
        self.Name_line_edit_2 = QLineEdit(self.frame_10)
        self.Name_line_edit_2.setObjectName(u"Name_line_edit_2")
        self.Name_line_edit_2.setGeometry(QRect(140, 140, 251, 21))
        self.Name_line_edit_2.setStyleSheet(u"QLineEdit {\n"
"    background-color: #666666;\n"
"    color: black;\n"
"}\n"
"\n"
"QLineEdit:!hasFocus {\n"
"    color: white;\n"
"}\n"
"")
        self.Name_2 = QLabel(self.frame_10)
        self.Name_2.setObjectName(u"Name_2")
        self.Name_2.setGeometry(QRect(40, 140, 41, 16))
        self.Age_2 = QLabel(self.frame_10)
        self.Age_2.setObjectName(u"Age_2")
        self.Age_2.setGeometry(QRect(40, 170, 41, 16))
        self.Age_line_edit_2 = QLineEdit(self.frame_10)
        self.Age_line_edit_2.setObjectName(u"Age_line_edit_2")
        self.Age_line_edit_2.setGeometry(QRect(140, 170, 31, 21))
        self.Age_line_edit_2.setStyleSheet(u"background-color: #666666; color: black;")
        self.Sex_2 = QLabel(self.frame_10)
        self.Sex_2.setObjectName(u"Sex_2")
        self.Sex_2.setGeometry(QRect(40, 200, 41, 16))
        self.PhoneNum_line_edit_2 = QLineEdit(self.frame_10)
        self.PhoneNum_line_edit_2.setObjectName(u"PhoneNum_line_edit_2")
        self.PhoneNum_line_edit_2.setGeometry(QRect(140, 230, 81, 21))
        self.PhoneNum_line_edit_2.setStyleSheet(u"background-color: #666666; color: black;")
        self.Email_line_edit_2 = QLineEdit(self.frame_10)
        self.Email_line_edit_2.setObjectName(u"Email_line_edit_2")
        self.Email_line_edit_2.setGeometry(QRect(140, 260, 251, 21))
        self.Email_line_edit_2.setStyleSheet(u"background-color: #666666; color: black;")
        self.Phone_number_2 = QLabel(self.frame_10)
        self.Phone_number_2.setObjectName(u"Phone_number_2")
        self.Phone_number_2.setGeometry(QRect(40, 230, 91, 16))
        self.Email_2 = QLabel(self.frame_10)
        self.Email_2.setObjectName(u"Email_2")
        self.Email_2.setGeometry(QRect(40, 260, 41, 16))
        self.Apart_num_2 = QLabel(self.frame_10)
        self.Apart_num_2.setObjectName(u"Apart_num_2")
        self.Apart_num_2.setGeometry(QRect(40, 290, 81, 16))
        self.SearchTenantBtn = QPushButton(self.frame_10)
        self.SearchTenantBtn.setObjectName(u"SearchTenantBtn")
        self.SearchTenantBtn.setGeometry(QRect(260, 60, 111, 41))
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(True)
        self.SearchTenantBtn.setFont(font4)
        self.SearchTenantBtn.setStyleSheet(u"background-color: #666666; color: white\n"
";\n"
"")
        self.PayHisBtn = QPushButton(self.frame_10)
        self.PayHisBtn.setObjectName(u"PayHisBtn")
        self.PayHisBtn.setGeometry(QRect(110, 380, 191, 41))
        self.PayHisBtn.setFont(font4)
        self.PayHisBtn.setStyleSheet(u"background-color: #666666; color: white\n"
";\n"
"")
        self.Search_line_edit = QLineEdit(self.frame_10)
        self.Search_line_edit.setObjectName(u"Search_line_edit")
        self.Search_line_edit.setGeometry(QRect(40, 70, 201, 21))
        self.Search_line_edit.setStyleSheet(u"background-color: #666666; color: black;")
        self.Payment_Stat_line_edit = QLineEdit(self.frame_10)
        self.Payment_Stat_line_edit.setObjectName(u"Payment_Stat_line_edit")
        self.Payment_Stat_line_edit.setGeometry(QRect(140, 340, 191, 21))
        self.Payment_Stat_line_edit.setStyleSheet(u"background-color: #666666; color: black;")
        self.PayStat = QLabel(self.frame_10)
        self.PayStat.setObjectName(u"PayStat")
        self.PayStat.setGeometry(QRect(40, 340, 91, 16))
        self.Sex_line_edit_2 = QLineEdit(self.frame_10)
        self.Sex_line_edit_2.setObjectName(u"Sex_line_edit_2")
        self.Sex_line_edit_2.setGeometry(QRect(140, 200, 81, 21))
        self.Sex_line_edit_2.setStyleSheet(u"background-color: #666666; color: black;")
        self.ApartNum_line_edit_2 = QLineEdit(self.frame_10)
        self.ApartNum_line_edit_2.setObjectName(u"ApartNum_line_edit_2")
        self.ApartNum_line_edit_2.setGeometry(QRect(140, 290, 61, 21))
        self.ApartNum_line_edit_2.setStyleSheet(u"background-color: #666666; color: black;")

        self.horizontalLayout_6.addWidget(self.frame_10)

        self.horizontalSpacer_2 = QSpacerItem(1, 1, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)

        self.frame_11 = QFrame(self.frame_9)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.PayHis_tableWidget_2 = QTableWidget(self.frame_11)
        if (self.PayHis_tableWidget_2.columnCount() < 7):
            self.PayHis_tableWidget_2.setColumnCount(7)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.PayHis_tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.PayHis_tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.PayHis_tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.PayHis_tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.PayHis_tableWidget_2.setHorizontalHeaderItem(4, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.PayHis_tableWidget_2.setHorizontalHeaderItem(5, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.PayHis_tableWidget_2.setHorizontalHeaderItem(6, __qtablewidgetitem12)
        self.PayHis_tableWidget_2.setObjectName(u"PayHis_tableWidget_2")
        self.PayHis_tableWidget_2.setGeometry(QRect(0, 0, 411, 451))
        self.PayHis_tableWidget_2.setStyleSheet(u"\n"
"    QTableWidget {\n"
"        background-color: #333333;\n"
"        color: white;\n"
"    }\n"
"\n"
"    QHeaderView::section {\n"
"        background-color: #555555;\n"
"        color: white;\n"
"    }\n"
"\n"
"    QScrollBar:vertical {\n"
"        background-color: #555555;\n"
"        width: 15px;\n"
"    }\n"
"\n"
"    QScrollBar::handle:vertical {\n"
"        background-color: #888888;\n"
"    }\n"
"\n"
"    QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"        background: none;\n"
"    }\n"
"")

        self.horizontalLayout_6.addWidget(self.frame_11)

        self.stackedWidget.addWidget(self.TenantInfoPage)
        self.ApartmentInfoPage = QWidget()
        self.ApartmentInfoPage.setObjectName(u"ApartmentInfoPage")
        self.ApartmentInfo_label = QLabel(self.ApartmentInfoPage)
        self.ApartmentInfo_label.setObjectName(u"ApartmentInfo_label")
        self.ApartmentInfo_label.setGeometry(QRect(20, 20, 201, 16))
        self.ApartmentInfo_label.setFont(font3)
        self.Search_lineEdit_2 = QLineEdit(self.ApartmentInfoPage)
        self.Search_lineEdit_2.setObjectName(u"Search_lineEdit_2")
        self.Search_lineEdit_2.setGeometry(QRect(600, 20, 240, 20))
        self.Search_lineEdit_2.setMinimumSize(QSize(240, 20))
        self.Search_lineEdit_2.setMaximumSize(QSize(240, 30))
        self.Search_lineEdit_2.setStyleSheet(u"QLineEdit {\n"
"    border: none;\n"
"    color: #FFF;\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"    background-color: rgb(33, 37, 41); \n"
"    border-image: url(rounded-border.png) 15 15 15 15 stretch stretch;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(48, 50, 62);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(85, 170, 255);\n"
"    background-color: rgb(33, 37, 41); \n"
"}")
        self.Apartment_tableWidget_2 = QTableWidget(self.ApartmentInfoPage)
        if (self.Apartment_tableWidget_2.columnCount() < 4):
            self.Apartment_tableWidget_2.setColumnCount(4)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.Apartment_tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.Apartment_tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.Apartment_tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.Apartment_tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem16)
        self.Apartment_tableWidget_2.setObjectName(u"Apartment_tableWidget_2")
        self.Apartment_tableWidget_2.setGeometry(QRect(230, 50, 611, 421))
        self.Apartment_tableWidget_2.setStyleSheet(u"QTableWidget {\n"
"    background-color: #333333;\n"
"    color: white;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #555555;\n"
"    color: white;\n"
"}\n"
"")
        self.Apartment_tableWidget_2.setSortingEnabled(False)
        self.Apartment_tableWidget_2.setWordWrap(True)
        self.Apartment_tableWidget_2.horizontalHeader().setVisible(True)
        self.Apartment_tableWidget_2.horizontalHeader().setCascadingSectionResizes(False)
        self.Apartment_tableWidget_2.horizontalHeader().setHighlightSections(True)
        self.Apartment_tableWidget_2.horizontalHeader().setProperty("showSortIndicator", False)
        self.Apartment_tableWidget_2.horizontalHeader().setStretchLastSection(False)
        self.Apartment_tableWidget_2.verticalHeader().setVisible(True)
        self.Apartment_tableWidget_2.verticalHeader().setStretchLastSection(False)
        self.frame_13 = QFrame(self.ApartmentInfoPage)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setGeometry(QRect(20, 50, 191, 421))
        self.frame_13.setStyleSheet(u"background-color: #333333;\n"
"color: white;")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.AptLeaseBtn = QPushButton(self.frame_13)
        self.AptLeaseBtn.setObjectName(u"AptLeaseBtn")
        self.AptLeaseBtn.setGeometry(QRect(40, 200, 111, 41))
        self.AptLeaseBtn.setFont(font4)
        self.AptLeaseBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.AptLeaseBtn.setStyleSheet(u"background-color: #666666; color: white\n"
";\n"
"")
        self.AptOcctBtn = QPushButton(self.frame_13)
        self.AptOcctBtn.setObjectName(u"AptOcctBtn")
        self.AptOcctBtn.setGeometry(QRect(40, 130, 111, 41))
        self.AptOcctBtn.setFont(font4)
        self.AptOcctBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.AptOcctBtn.setStyleSheet(u"background-color: #666666; color: white\n"
";\n"
"")
        self.AptListBtn = QPushButton(self.frame_13)
        self.AptListBtn.setObjectName(u"AptListBtn")
        self.AptListBtn.setGeometry(QRect(40, 60, 111, 41))
        self.AptListBtn.setFont(font4)
        self.AptListBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.AptListBtn.setStyleSheet(u"background-color: #666666; color: white\n"
";\n"
"")
        self.stackedWidget.addWidget(self.ApartmentInfoPage)
        self.CRUDApartPage = QWidget()
        self.CRUDApartPage.setObjectName(u"CRUDApartPage")
        self.frame_12 = QFrame(self.CRUDApartPage)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setGeometry(QRect(0, 0, 851, 464))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.frame_15 = QFrame(self.frame_12)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setStyleSheet(u"background-color: #333333;\n"
"color: white;")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.page_label_4 = QLabel(self.frame_15)
        self.page_label_4.setObjectName(u"page_label_4")
        self.page_label_4.setGeometry(QRect(10, 10, 201, 16))
        self.page_label_4.setFont(font3)
        self.ApartNum_line_edit = QLineEdit(self.frame_15)
        self.ApartNum_line_edit.setObjectName(u"ApartNum_line_edit")
        self.ApartNum_line_edit.setGeometry(QRect(160, 60, 231, 21))
        self.ApartNum_line_edit.setStyleSheet(u"QLineEdit {\n"
"    background-color: #666666;\n"
"    color: black;\n"
"}\n"
"\n"
"QLineEdit:!hasFocus {\n"
"    color: white;\n"
"}\n"
"")
        self.ApartNum = QLabel(self.frame_15)
        self.ApartNum.setObjectName(u"ApartNum")
        self.ApartNum.setGeometry(QRect(40, 60, 111, 16))
        self.FloorLevel = QLabel(self.frame_15)
        self.FloorLevel.setObjectName(u"FloorLevel")
        self.FloorLevel.setGeometry(QRect(40, 100, 91, 16))
        self.RentalBill = QLabel(self.frame_15)
        self.RentalBill.setObjectName(u"RentalBill")
        self.RentalBill.setGeometry(QRect(40, 140, 91, 16))
        self.RentalBill_line_edit = QLineEdit(self.frame_15)
        self.RentalBill_line_edit.setObjectName(u"RentalBill_line_edit")
        self.RentalBill_line_edit.setGeometry(QRect(160, 140, 121, 21))
        self.RentalBill_line_edit.setStyleSheet(u"background-color: #666666; color: black;")
        self.FloorLvl_comboBox = QComboBox(self.frame_15)
        self.FloorLvl_comboBox.addItem("")
        self.FloorLvl_comboBox.addItem("")
        self.FloorLvl_comboBox.setObjectName(u"FloorLvl_comboBox")
        self.FloorLvl_comboBox.setGeometry(QRect(160, 100, 61, 22))
        self.FloorLvl_comboBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.FloorLvl_comboBox.setStyleSheet(u"background-color: #666666; color: black;")
        self.AddApartBtn = QPushButton(self.frame_15)
        self.AddApartBtn.setObjectName(u"AddApartBtn")
        self.AddApartBtn.setGeometry(QRect(150, 200, 111, 41))
        self.AddApartBtn.setFont(font4)
        self.AddApartBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.AddApartBtn.setStyleSheet(u"background-color: #666666; color: white\n"
";\n"
"")
        self.DelApartBtn = QPushButton(self.frame_15)
        self.DelApartBtn.setObjectName(u"DelApartBtn")
        self.DelApartBtn.setGeometry(QRect(150, 340, 111, 41))
        self.DelApartBtn.setFont(font4)
        self.DelApartBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.DelApartBtn.setStyleSheet(u"background-color: #666666; color: white\n"
";\n"
"")
        self.UpdApartBtn = QPushButton(self.frame_15)
        self.UpdApartBtn.setObjectName(u"UpdApartBtn")
        self.UpdApartBtn.setGeometry(QRect(150, 270, 111, 41))
        self.UpdApartBtn.setFont(font4)
        self.UpdApartBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.UpdApartBtn.setStyleSheet(u"background-color: #666666; color: white\n"
";\n"
"")
        self.GetApartBtn = QPushButton(self.frame_15)
        self.GetApartBtn.setObjectName(u"GetApartBtn")
        self.GetApartBtn.setGeometry(QRect(320, 10, 71, 31))
        font5 = QFont()
        font5.setPointSize(9)
        font5.setBold(True)
        self.GetApartBtn.setFont(font5)
        self.GetApartBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.GetApartBtn.setStyleSheet(u"background-color: #666666; color: white\n"
";\n"
"")

        self.horizontalLayout_8.addWidget(self.frame_15)

        self.horizontalSpacer_4 = QSpacerItem(1, 1, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_4)

        self.frame_16 = QFrame(self.frame_12)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.Apartment_tableWidget_3 = QTableWidget(self.frame_16)
        if (self.Apartment_tableWidget_3.columnCount() < 4):
            self.Apartment_tableWidget_3.setColumnCount(4)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.Apartment_tableWidget_3.setHorizontalHeaderItem(0, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.Apartment_tableWidget_3.setHorizontalHeaderItem(1, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.Apartment_tableWidget_3.setHorizontalHeaderItem(2, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.Apartment_tableWidget_3.setHorizontalHeaderItem(3, __qtablewidgetitem20)
        self.Apartment_tableWidget_3.setObjectName(u"Apartment_tableWidget_3")
        self.Apartment_tableWidget_3.setGeometry(QRect(0, 0, 411, 451))
        self.Apartment_tableWidget_3.setStyleSheet(u"\n"
"    QTableWidget {\n"
"        background-color: #333333;\n"
"        color: white;\n"
"    }\n"
"\n"
"    QHeaderView::section {\n"
"        background-color: #555555;\n"
"        color: white;\n"
"    }\n"
"\n"
"    QScrollBar:vertical {\n"
"        background-color: #555555;\n"
"        width: 15px;\n"
"    }\n"
"\n"
"    QScrollBar::handle:vertical {\n"
"        background-color: #888888;\n"
"    }\n"
"\n"
"    QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"        background: none;\n"
"    }\n"
"")

        self.horizontalLayout_8.addWidget(self.frame_16)

        self.stackedWidget.addWidget(self.CRUDApartPage)
        self.PaymentListPage = QWidget()
        self.PaymentListPage.setObjectName(u"PaymentListPage")
        self.PaymentList_label = QLabel(self.PaymentListPage)
        self.PaymentList_label.setObjectName(u"PaymentList_label")
        self.PaymentList_label.setGeometry(QRect(10, 10, 201, 16))
        self.PaymentList_label.setFont(font3)
        self.Search_lineEdit_3 = QLineEdit(self.PaymentListPage)
        self.Search_lineEdit_3.setObjectName(u"Search_lineEdit_3")
        self.Search_lineEdit_3.setGeometry(QRect(590, 10, 240, 20))
        self.Search_lineEdit_3.setMinimumSize(QSize(240, 20))
        self.Search_lineEdit_3.setMaximumSize(QSize(240, 30))
        self.Search_lineEdit_3.setStyleSheet(u"QLineEdit {\n"
"    border: none;\n"
"    color: #FFF;\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"    background-color: rgb(33, 37, 41); \n"
"    border-image: url(rounded-border.png) 15 15 15 15 stretch stretch;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(48, 50, 62);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(85, 170, 255);\n"
"    background-color: rgb(33, 37, 41); \n"
"}")
        self.Payment_tableWidget = QTableWidget(self.PaymentListPage)
        if (self.Payment_tableWidget.columnCount() < 7):
            self.Payment_tableWidget.setColumnCount(7)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.Payment_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.Payment_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.Payment_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.Payment_tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.Payment_tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.Payment_tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.Payment_tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem27)
        self.Payment_tableWidget.setObjectName(u"Payment_tableWidget")
        self.Payment_tableWidget.setGeometry(QRect(0, 40, 831, 421))
        self.Payment_tableWidget.setStyleSheet(u"QTableWidget {\n"
"    background-color: #333333;\n"
"    color: white;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #555555;\n"
"    color: white;\n"
"}\n"
"")
        self.stackedWidget.addWidget(self.PaymentListPage)
        self.CRUDPaymentPage = QWidget()
        self.CRUDPaymentPage.setObjectName(u"CRUDPaymentPage")
        self.frame_20 = QFrame(self.CRUDPaymentPage)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setGeometry(QRect(0, 0, 851, 464))
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.frame_21 = QFrame(self.frame_20)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setStyleSheet(u"background-color: #333333;\n"
"color: white;")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.CRUDPayment_label = QLabel(self.frame_21)
        self.CRUDPayment_label.setObjectName(u"CRUDPayment_label")
        self.CRUDPayment_label.setGeometry(QRect(10, 10, 201, 16))
        self.CRUDPayment_label.setFont(font3)
        self.AddPayBtn = QPushButton(self.frame_21)
        self.AddPayBtn.setObjectName(u"AddPayBtn")
        self.AddPayBtn.setGeometry(QRect(150, 220, 111, 41))
        self.AddPayBtn.setFont(font4)
        self.AddPayBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.AddPayBtn.setStyleSheet(u"background-color: #666666; color: white\n"
";\n"
"")
        self.DelPayBtn = QPushButton(self.frame_21)
        self.DelPayBtn.setObjectName(u"DelPayBtn")
        self.DelPayBtn.setGeometry(QRect(150, 340, 111, 41))
        self.DelPayBtn.setFont(font4)
        self.DelPayBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.DelPayBtn.setStyleSheet(u"background-color: #666666; color: white\n"
";\n"
"")
        self.UpdPayBtn = QPushButton(self.frame_21)
        self.UpdPayBtn.setObjectName(u"UpdPayBtn")
        self.UpdPayBtn.setGeometry(QRect(150, 280, 111, 41))
        self.UpdPayBtn.setFont(font4)
        self.UpdPayBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.UpdPayBtn.setStyleSheet(u"background-color: #666666; color: white\n"
";\n"
"")
        self.PaymentStatus = QLabel(self.frame_21)
        self.PaymentStatus.setObjectName(u"PaymentStatus")
        self.PaymentStatus.setGeometry(QRect(40, 130, 101, 16))
        self.PayStat_comboBox = QComboBox(self.frame_21)
        self.PayStat_comboBox.addItem("")
        self.PayStat_comboBox.addItem("")
        self.PayStat_comboBox.addItem("")
        self.PayStat_comboBox.setObjectName(u"PayStat_comboBox")
        self.PayStat_comboBox.setGeometry(QRect(160, 130, 101, 22))
        self.PayStat_comboBox.setStyleSheet(u"background-color: #666666; color: black;")
        self.TenantID = QLabel(self.frame_21)
        self.TenantID.setObjectName(u"TenantID")
        self.TenantID.setGeometry(QRect(40, 50, 91, 16))
        self.ApartID = QLabel(self.frame_21)
        self.ApartID.setObjectName(u"ApartID")
        self.ApartID.setGeometry(QRect(40, 90, 91, 16))
        self.ApartID_line_edit_3 = QLineEdit(self.frame_21)
        self.ApartID_line_edit_3.setObjectName(u"ApartID_line_edit_3")
        self.ApartID_line_edit_3.setGeometry(QRect(160, 90, 101, 21))
        self.ApartID_line_edit_3.setStyleSheet(u"QLineEdit {\n"
"    background-color: #666666;\n"
"    color: black;\n"
"}\n"
"\n"
"QLineEdit:!hasFocus {\n"
"    color: white;\n"
"}\n"
"")
        self.TenantID_line_edit3 = QLineEdit(self.frame_21)
        self.TenantID_line_edit3.setObjectName(u"TenantID_line_edit3")
        self.TenantID_line_edit3.setGeometry(QRect(160, 50, 101, 21))
        self.TenantID_line_edit3.setStyleSheet(u"QLineEdit {\n"
"    background-color: #666666;\n"
"    color: black;\n"
"}\n"
"\n"
"QLineEdit:!hasFocus {\n"
"    color: white;\n"
"}\n"
"")
        self.GetPayBtn = QPushButton(self.frame_21)
        self.GetPayBtn.setObjectName(u"GetPayBtn")
        self.GetPayBtn.setGeometry(QRect(320, 10, 71, 31))
        self.GetPayBtn.setFont(font5)
        self.GetPayBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.GetPayBtn.setStyleSheet(u"background-color: #666666; color: white\n"
";\n"
"")

        self.horizontalLayout_10.addWidget(self.frame_21)

        self.horizontalSpacer_6 = QSpacerItem(1, 1, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_6)

        self.frame_22 = QFrame(self.frame_20)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.Payment_tableWidget_5 = QTableWidget(self.frame_22)
        if (self.Payment_tableWidget_5.columnCount() < 7):
            self.Payment_tableWidget_5.setColumnCount(7)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.Payment_tableWidget_5.setHorizontalHeaderItem(0, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.Payment_tableWidget_5.setHorizontalHeaderItem(1, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.Payment_tableWidget_5.setHorizontalHeaderItem(2, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.Payment_tableWidget_5.setHorizontalHeaderItem(3, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.Payment_tableWidget_5.setHorizontalHeaderItem(4, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.Payment_tableWidget_5.setHorizontalHeaderItem(5, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.Payment_tableWidget_5.setHorizontalHeaderItem(6, __qtablewidgetitem34)
        self.Payment_tableWidget_5.setObjectName(u"Payment_tableWidget_5")
        self.Payment_tableWidget_5.setGeometry(QRect(0, 0, 411, 451))
        self.Payment_tableWidget_5.setStyleSheet(u"\n"
"    QTableWidget {\n"
"        background-color: #333333;\n"
"        color: white;\n"
"    }\n"
"\n"
"    QHeaderView::section {\n"
"        background-color: #555555;\n"
"        color: white;\n"
"    }\n"
"\n"
"    QScrollBar:vertical {\n"
"        background-color: #555555;\n"
"        width: 15px;\n"
"    }\n"
"\n"
"    QScrollBar::handle:vertical {\n"
"        background-color: #888888;\n"
"    }\n"
"\n"
"    QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"        background: none;\n"
"    }\n"
"")

        self.horizontalLayout_10.addWidget(self.frame_22)

        self.stackedWidget.addWidget(self.CRUDPaymentPage)
        self.EBListPage = QWidget()
        self.EBListPage.setObjectName(u"EBListPage")
        self.ElectricBillList_label = QLabel(self.EBListPage)
        self.ElectricBillList_label.setObjectName(u"ElectricBillList_label")
        self.ElectricBillList_label.setGeometry(QRect(20, 10, 201, 16))
        self.ElectricBillList_label.setFont(font3)
        self.Search_lineEdit_4 = QLineEdit(self.EBListPage)
        self.Search_lineEdit_4.setObjectName(u"Search_lineEdit_4")
        self.Search_lineEdit_4.setGeometry(QRect(600, 10, 240, 20))
        self.Search_lineEdit_4.setMinimumSize(QSize(240, 20))
        self.Search_lineEdit_4.setMaximumSize(QSize(240, 30))
        self.Search_lineEdit_4.setStyleSheet(u"QLineEdit {\n"
"    border: none;\n"
"    color: #FFF;\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"    background-color: rgb(33, 37, 41); \n"
"    border-image: url(rounded-border.png) 15 15 15 15 stretch stretch;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(48, 50, 62);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(85, 170, 255);\n"
"    background-color: rgb(33, 37, 41); \n"
"}")
        self.ElectricBill_tableWidget = QTableWidget(self.EBListPage)
        if (self.ElectricBill_tableWidget.columnCount() < 5):
            self.ElectricBill_tableWidget.setColumnCount(5)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.ElectricBill_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.ElectricBill_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.ElectricBill_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.ElectricBill_tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.ElectricBill_tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem39)
        self.ElectricBill_tableWidget.setObjectName(u"ElectricBill_tableWidget")
        self.ElectricBill_tableWidget.setGeometry(QRect(10, 40, 831, 421))
        self.ElectricBill_tableWidget.setStyleSheet(u"QTableWidget {\n"
"    background-color: #333333;\n"
"    color: white;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #555555;\n"
"    color: white;\n"
"}\n"
"")
        self.stackedWidget.addWidget(self.EBListPage)
        self.CRUDElecBillPage = QWidget()
        self.CRUDElecBillPage.setObjectName(u"CRUDElecBillPage")
        self.frame_17 = QFrame(self.CRUDElecBillPage)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setGeometry(QRect(0, 0, 851, 464))
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.frame_18 = QFrame(self.frame_17)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setStyleSheet(u"background-color: #333333;\n"
"color: white;")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.CRUDElecBill_label = QLabel(self.frame_18)
        self.CRUDElecBill_label.setObjectName(u"CRUDElecBill_label")
        self.CRUDElecBill_label.setGeometry(QRect(10, 10, 201, 16))
        self.CRUDElecBill_label.setFont(font3)
        self.DateStarted = QLabel(self.frame_18)
        self.DateStarted.setObjectName(u"DateStarted")
        self.DateStarted.setGeometry(QRect(40, 60, 81, 16))
        self.Kwh = QLabel(self.frame_18)
        self.Kwh.setObjectName(u"Kwh")
        self.Kwh.setGeometry(QRect(40, 100, 91, 16))
        self.Status = QLabel(self.frame_18)
        self.Status.setObjectName(u"Status")
        self.Status.setGeometry(QRect(40, 140, 61, 16))
        self.kwh_line_edit = QLineEdit(self.frame_18)
        self.kwh_line_edit.setObjectName(u"kwh_line_edit")
        self.kwh_line_edit.setGeometry(QRect(130, 100, 91, 21))
        self.kwh_line_edit.setStyleSheet(u"background-color: #666666; color: black;")
        self.AddEBBtn = QPushButton(self.frame_18)
        self.AddEBBtn.setObjectName(u"AddEBBtn")
        self.AddEBBtn.setGeometry(QRect(20, 300, 111, 41))
        self.AddEBBtn.setFont(font4)
        self.AddEBBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.AddEBBtn.setStyleSheet(u"background-color: #666666; color: white\n"
";\n"
"")
        self.DelEBBtn = QPushButton(self.frame_18)
        self.DelEBBtn.setObjectName(u"DelEBBtn")
        self.DelEBBtn.setGeometry(QRect(260, 300, 111, 41))
        self.DelEBBtn.setFont(font4)
        self.DelEBBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.DelEBBtn.setStyleSheet(u"background-color: #666666; color: white\n"
";\n"
"")
        self.UpdEBBtn = QPushButton(self.frame_18)
        self.UpdEBBtn.setObjectName(u"UpdEBBtn")
        self.UpdEBBtn.setGeometry(QRect(140, 300, 111, 41))
        self.UpdEBBtn.setFont(font4)
        self.UpdEBBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.UpdEBBtn.setStyleSheet(u"background-color: #666666; color: white\n"
";\n"
"")
        self.DateStart_dateEdit = QDateEdit(self.frame_18)
        self.DateStart_dateEdit.setObjectName(u"DateStart_dateEdit")
        self.DateStart_dateEdit.setGeometry(QRect(130, 60, 91, 22))
        self.DateStart_dateEdit.setStyleSheet(u"background-color: #666666; color: black;")
        self.ApartmentID = QLabel(self.frame_18)
        self.ApartmentID.setObjectName(u"ApartmentID")
        self.ApartmentID.setGeometry(QRect(40, 180, 81, 16))
        self.ApartID_line_edit_7 = QLineEdit(self.frame_18)
        self.ApartID_line_edit_7.setObjectName(u"ApartID_line_edit_7")
        self.ApartID_line_edit_7.setGeometry(QRect(130, 180, 91, 21))
        self.ApartID_line_edit_7.setStyleSheet(u"background-color: #666666; color: black;")
        self.Status_comboBox = QComboBox(self.frame_18)
        self.Status_comboBox.addItem("")
        self.Status_comboBox.addItem("")
        self.Status_comboBox.addItem("")
        self.Status_comboBox.setObjectName(u"Status_comboBox")
        self.Status_comboBox.setGeometry(QRect(130, 140, 91, 22))
        self.Status_comboBox.setStyleSheet(u"background-color: #666666; color: black;")
        self.GetEBBtn = QPushButton(self.frame_18)
        self.GetEBBtn.setObjectName(u"GetEBBtn")
        self.GetEBBtn.setGeometry(QRect(320, 10, 71, 31))
        self.GetEBBtn.setFont(font5)
        self.GetEBBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.GetEBBtn.setStyleSheet(u"background-color: #666666; color: white\n"
";\n"
"")

        self.horizontalLayout_9.addWidget(self.frame_18)

        self.horizontalSpacer_5 = QSpacerItem(1, 1, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_5)

        self.frame_19 = QFrame(self.frame_17)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.ElectricBill_tableWidget_2 = QTableWidget(self.frame_19)
        if (self.ElectricBill_tableWidget_2.columnCount() < 5):
            self.ElectricBill_tableWidget_2.setColumnCount(5)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.ElectricBill_tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.ElectricBill_tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.ElectricBill_tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.ElectricBill_tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.ElectricBill_tableWidget_2.setHorizontalHeaderItem(4, __qtablewidgetitem44)
        self.ElectricBill_tableWidget_2.setObjectName(u"ElectricBill_tableWidget_2")
        self.ElectricBill_tableWidget_2.setGeometry(QRect(0, 0, 411, 451))
        self.ElectricBill_tableWidget_2.setStyleSheet(u"\n"
"    QTableWidget {\n"
"        background-color: #333333;\n"
"        color: white;\n"
"    }\n"
"\n"
"    QHeaderView::section {\n"
"        background-color: #555555;\n"
"        color: white;\n"
"    }\n"
"\n"
"    QScrollBar:vertical {\n"
"        background-color: #555555;\n"
"        width: 15px;\n"
"    }\n"
"\n"
"    QScrollBar::handle:vertical {\n"
"        background-color: #888888;\n"
"    }\n"
"\n"
"    QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"        background: none;\n"
"    }\n"
"")

        self.horizontalLayout_9.addWidget(self.frame_19)

        self.stackedWidget.addWidget(self.CRUDElecBillPage)
        self.CRUDTenantPage = QWidget()
        self.CRUDTenantPage.setObjectName(u"CRUDTenantPage")
        self.verticalLayout_5 = QVBoxLayout(self.CRUDTenantPage)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_6 = QFrame(self.CRUDTenantPage)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"background-color: #333333;\n"
"color: white;")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.page_label = QLabel(self.frame_7)
        self.page_label.setObjectName(u"page_label")
        self.page_label.setGeometry(QRect(10, 10, 201, 16))
        self.page_label.setFont(font3)
        self.Name_line_edit = QLineEdit(self.frame_7)
        self.Name_line_edit.setObjectName(u"Name_line_edit")
        self.Name_line_edit.setGeometry(QRect(140, 60, 231, 21))
        self.Name_line_edit.setStyleSheet(u"QLineEdit {\n"
"    background-color: #666666;\n"
"    color: black;\n"
"}\n"
"\n"
"QLineEdit:!hasFocus {\n"
"    color: white;\n"
"}\n"
"")
        self.Name = QLabel(self.frame_7)
        self.Name.setObjectName(u"Name")
        self.Name.setGeometry(QRect(40, 60, 41, 16))
        self.Age = QLabel(self.frame_7)
        self.Age.setObjectName(u"Age")
        self.Age.setGeometry(QRect(40, 100, 41, 16))
        self.Age_line_edit = QLineEdit(self.frame_7)
        self.Age_line_edit.setObjectName(u"Age_line_edit")
        self.Age_line_edit.setGeometry(QRect(140, 100, 31, 21))
        self.Age_line_edit.setStyleSheet(u"background-color: #666666; color: black;")
        self.Sex = QLabel(self.frame_7)
        self.Sex.setObjectName(u"Sex")
        self.Sex.setGeometry(QRect(40, 140, 41, 16))
        self.PhoneNum_line_edit = QLineEdit(self.frame_7)
        self.PhoneNum_line_edit.setObjectName(u"PhoneNum_line_edit")
        self.PhoneNum_line_edit.setGeometry(QRect(140, 180, 101, 21))
        self.PhoneNum_line_edit.setStyleSheet(u"background-color: #666666; color: black;")
        self.Email_line_edit = QLineEdit(self.frame_7)
        self.Email_line_edit.setObjectName(u"Email_line_edit")
        self.Email_line_edit.setGeometry(QRect(140, 220, 221, 21))
        self.Email_line_edit.setStyleSheet(u"background-color: #666666; color: black;")
        self.Phone_number = QLabel(self.frame_7)
        self.Phone_number.setObjectName(u"Phone_number")
        self.Phone_number.setGeometry(QRect(40, 180, 91, 16))
        self.Email = QLabel(self.frame_7)
        self.Email.setObjectName(u"Email")
        self.Email.setGeometry(QRect(40, 220, 41, 16))
        self.Apart_num = QLabel(self.frame_7)
        self.Apart_num.setObjectName(u"Apart_num")
        self.Apart_num.setGeometry(QRect(40, 260, 81, 16))
        self.Sex_comboBox = QComboBox(self.frame_7)
        self.Sex_comboBox.addItem("")
        self.Sex_comboBox.addItem("")
        self.Sex_comboBox.setObjectName(u"Sex_comboBox")
        self.Sex_comboBox.setGeometry(QRect(140, 140, 81, 22))
        self.Sex_comboBox.setStyleSheet(u"background-color: #666666; color: black;")
        self.AddTenantBtn = QPushButton(self.frame_7)
        self.AddTenantBtn.setObjectName(u"AddTenantBtn")
        self.AddTenantBtn.setGeometry(QRect(40, 330, 111, 41))
        self.AddTenantBtn.setFont(font4)
        self.AddTenantBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.AddTenantBtn.setStyleSheet(u"background-color: #666666; color: white\n"
";\n"
"")
        self.DelTenantBtn = QPushButton(self.frame_7)
        self.DelTenantBtn.setObjectName(u"DelTenantBtn")
        self.DelTenantBtn.setGeometry(QRect(160, 330, 111, 41))
        self.DelTenantBtn.setFont(font4)
        self.DelTenantBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.DelTenantBtn.setStyleSheet(u"background-color: #666666; color: white\n"
";\n"
"")
        self.UpdTenantBtn = QPushButton(self.frame_7)
        self.UpdTenantBtn.setObjectName(u"UpdTenantBtn")
        self.UpdTenantBtn.setGeometry(QRect(280, 330, 111, 41))
        self.UpdTenantBtn.setFont(font4)
        self.UpdTenantBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.UpdTenantBtn.setStyleSheet(u"background-color: #666666; color: white\n"
";\n"
"")
        self.GetTenantBtn = QPushButton(self.frame_7)
        self.GetTenantBtn.setObjectName(u"GetTenantBtn")
        self.GetTenantBtn.setGeometry(QRect(320, 10, 71, 31))
        self.GetTenantBtn.setFont(font5)
        self.GetTenantBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.GetTenantBtn.setStyleSheet(u"background-color: #666666; color: white\n"
";\n"
"")
        self.ApartNum_line_edit_3 = QLineEdit(self.frame_7)
        self.ApartNum_line_edit_3.setObjectName(u"ApartNum_line_edit_3")
        self.ApartNum_line_edit_3.setGeometry(QRect(140, 260, 41, 21))
        self.ApartNum_line_edit_3.setStyleSheet(u"background-color: #666666; color: black;")

        self.horizontalLayout_5.addWidget(self.frame_7)

        self.horizontalSpacer = QSpacerItem(1, 1, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.Tenant_tableWidget = QTableWidget(self.frame_8)
        if (self.Tenant_tableWidget.columnCount() < 7):
            self.Tenant_tableWidget.setColumnCount(7)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.Tenant_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.Tenant_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.Tenant_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.Tenant_tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.Tenant_tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.Tenant_tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.Tenant_tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem51)
        self.Tenant_tableWidget.setObjectName(u"Tenant_tableWidget")
        self.Tenant_tableWidget.setGeometry(QRect(0, 0, 411, 451))
        self.Tenant_tableWidget.setStyleSheet(u"\n"
"    QTableWidget {\n"
"        background-color: #333333;\n"
"        color: white;\n"
"    }\n"
"\n"
"    QHeaderView::section {\n"
"        background-color: #555555;\n"
"        color: white;\n"
"    }\n"
"\n"
"    QScrollBar:vertical {\n"
"        background-color: #555555;\n"
"        width: 15px;\n"
"    }\n"
"\n"
"    QScrollBar::handle:vertical {\n"
"        background-color: #888888;\n"
"    }\n"
"\n"
"    QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"        background: none;\n"
"    }\n"
"")

        self.horizontalLayout_5.addWidget(self.frame_8)


        self.verticalLayout_5.addWidget(self.frame_6)

        self.stackedWidget.addWidget(self.CRUDTenantPage)

        self.verticalLayout_4.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.main_body)


        self.verticalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"MENU", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Landlord Support Management System for VJ's Building", None))
        self.TenantStatListBtn.setText(QCoreApplication.translate("MainWindow", u"Tenant Status List", None))
        self.CRUDTenantBtn.setText(QCoreApplication.translate("MainWindow", u"CRUD Tenant", None))
        self.TenantInfoBtn.setText(QCoreApplication.translate("MainWindow", u"Tenant Information", None))
        self.ApartmentInfoBtn.setText(QCoreApplication.translate("MainWindow", u"Apartment Information", None))
        self.CRUDApartmentBtn.setText(QCoreApplication.translate("MainWindow", u"CRUD Apartment", None))
        self.PaymentListBtn.setText(QCoreApplication.translate("MainWindow", u"Payment List", None))
        self.CRUDPaymentBtn.setText(QCoreApplication.translate("MainWindow", u"CRUD Payment", None))
        self.ElecBillBtn.setText(QCoreApplication.translate("MainWindow", u"Electric Bill List", None))
        self.CRUDElectricBillBtn.setText(QCoreApplication.translate("MainWindow", u"CRUD Electric Bill", None))
        self.Search_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search....", None))
        self.TenantStatList_label.setText(QCoreApplication.translate("MainWindow", u"Tenant Status List", None))
        ___qtablewidgetitem = self.Tenant_tableWidget_3.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Tenant ID", None));
        ___qtablewidgetitem1 = self.Tenant_tableWidget_3.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem2 = self.Tenant_tableWidget_3.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Number", None));
        ___qtablewidgetitem3 = self.Tenant_tableWidget_3.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Payment Status", None));
        ___qtablewidgetitem4 = self.Tenant_tableWidget_3.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Payment Date", None));
        ___qtablewidgetitem5 = self.Tenant_tableWidget_3.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Payment ID", None));
        self.page_label_2.setText(QCoreApplication.translate("MainWindow", u"Tenant Information", None))
        self.Name_line_edit_2.setPlaceholderText("")
        self.Name_2.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.Age_2.setText(QCoreApplication.translate("MainWindow", u"Age:", None))
        self.Sex_2.setText(QCoreApplication.translate("MainWindow", u"Sex:", None))
        self.PhoneNum_line_edit_2.setPlaceholderText("")
        self.Email_line_edit_2.setText("")
        self.Phone_number_2.setText(QCoreApplication.translate("MainWindow", u"Phone Number:", None))
        self.Email_2.setText(QCoreApplication.translate("MainWindow", u"Email:", None))
        self.Apart_num_2.setText(QCoreApplication.translate("MainWindow", u"Apart. ID:", None))
        self.SearchTenantBtn.setText(QCoreApplication.translate("MainWindow", u"SEARCH", None))
        self.PayHisBtn.setText(QCoreApplication.translate("MainWindow", u"Payment History", None))
        self.Search_line_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Tenant ID", None))
        self.Payment_Stat_line_edit.setText("")
        self.PayStat.setText(QCoreApplication.translate("MainWindow", u"Payment Status:", None))
        ___qtablewidgetitem6 = self.PayHis_tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Payment ID", None));
        ___qtablewidgetitem7 = self.PayHis_tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Payment Status", None));
        ___qtablewidgetitem8 = self.PayHis_tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Payment Date", None));
        ___qtablewidgetitem9 = self.PayHis_tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Amount Paid", None));
        ___qtablewidgetitem10 = self.PayHis_tableWidget_2.horizontalHeaderItem(4)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Payment Method", None));
        ___qtablewidgetitem11 = self.PayHis_tableWidget_2.horizontalHeaderItem(5)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Tenant ID", None));
        ___qtablewidgetitem12 = self.PayHis_tableWidget_2.horizontalHeaderItem(6)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Apartment ID", None));
        self.ApartmentInfo_label.setText(QCoreApplication.translate("MainWindow", u"Apartment Information", None))
        self.Search_lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search....", None))
        ___qtablewidgetitem13 = self.Apartment_tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Apartment ID", None));
        ___qtablewidgetitem14 = self.Apartment_tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Apart. Number", None));
        ___qtablewidgetitem15 = self.Apartment_tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Floor Level ", None));
        ___qtablewidgetitem16 = self.Apartment_tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Rental Bill", None));
        self.AptLeaseBtn.setText(QCoreApplication.translate("MainWindow", u"LEASE", None))
        self.AptOcctBtn.setText(QCoreApplication.translate("MainWindow", u"OCCUPY", None))
        self.AptListBtn.setText(QCoreApplication.translate("MainWindow", u"APART. LIST", None))
        self.page_label_4.setText(QCoreApplication.translate("MainWindow", u"CRUD Apartment", None))
        self.ApartNum_line_edit.setPlaceholderText("")
        self.ApartNum.setText(QCoreApplication.translate("MainWindow", u"Apartment Number:", None))
        self.FloorLevel.setText(QCoreApplication.translate("MainWindow", u"Floor Level:", None))
        self.RentalBill.setText(QCoreApplication.translate("MainWindow", u"Rental Bill:", None))
        self.RentalBill_line_edit.setText("")
        self.FloorLvl_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.FloorLvl_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))

        self.AddApartBtn.setText(QCoreApplication.translate("MainWindow", u"ADD", None))
        self.DelApartBtn.setText(QCoreApplication.translate("MainWindow", u"DELETE", None))
        self.UpdApartBtn.setText(QCoreApplication.translate("MainWindow", u"UPDATE", None))
        self.GetApartBtn.setText(QCoreApplication.translate("MainWindow", u"GET", None))
        ___qtablewidgetitem17 = self.Apartment_tableWidget_3.horizontalHeaderItem(0)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Apartment ID", None));
        ___qtablewidgetitem18 = self.Apartment_tableWidget_3.horizontalHeaderItem(1)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Apart. Number", None));
        ___qtablewidgetitem19 = self.Apartment_tableWidget_3.horizontalHeaderItem(2)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Floor Level", None));
        ___qtablewidgetitem20 = self.Apartment_tableWidget_3.horizontalHeaderItem(3)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Rental Bill", None));
        self.PaymentList_label.setText(QCoreApplication.translate("MainWindow", u"Payment List", None))
        self.Search_lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search....", None))
        ___qtablewidgetitem21 = self.Payment_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Payment ID", None));
        ___qtablewidgetitem22 = self.Payment_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Payment Status", None));
        ___qtablewidgetitem23 = self.Payment_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Payment Date", None));
        ___qtablewidgetitem24 = self.Payment_tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Amount Paid", None));
        ___qtablewidgetitem25 = self.Payment_tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Payment Method", None));
        ___qtablewidgetitem26 = self.Payment_tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Tenant ID", None));
        ___qtablewidgetitem27 = self.Payment_tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Apartment ID", None));
        self.CRUDPayment_label.setText(QCoreApplication.translate("MainWindow", u"CRUD Payment", None))
        self.AddPayBtn.setText(QCoreApplication.translate("MainWindow", u"ADD", None))
        self.DelPayBtn.setText(QCoreApplication.translate("MainWindow", u"DELETE", None))
        self.UpdPayBtn.setText(QCoreApplication.translate("MainWindow", u"UPDATE", None))
        self.PaymentStatus.setText(QCoreApplication.translate("MainWindow", u"Payment Status:", None))
        self.PayStat_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Pending", None))
        self.PayStat_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Successful", None))
        self.PayStat_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Overdue", None))

        self.TenantID.setText(QCoreApplication.translate("MainWindow", u"Tenant ID:", None))
        self.ApartID.setText(QCoreApplication.translate("MainWindow", u"Apartment ID:", None))
        self.ApartID_line_edit_3.setPlaceholderText("")
        self.TenantID_line_edit3.setPlaceholderText("")
        self.GetPayBtn.setText(QCoreApplication.translate("MainWindow", u"GET", None))
        ___qtablewidgetitem28 = self.Payment_tableWidget_5.horizontalHeaderItem(0)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Payment ID", None));
        ___qtablewidgetitem29 = self.Payment_tableWidget_5.horizontalHeaderItem(1)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"Payment Status", None));
        ___qtablewidgetitem30 = self.Payment_tableWidget_5.horizontalHeaderItem(2)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"Payment Date", None));
        ___qtablewidgetitem31 = self.Payment_tableWidget_5.horizontalHeaderItem(3)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"Amount Paid", None));
        ___qtablewidgetitem32 = self.Payment_tableWidget_5.horizontalHeaderItem(4)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"Payment Method", None));
        ___qtablewidgetitem33 = self.Payment_tableWidget_5.horizontalHeaderItem(5)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"Tenant ID", None));
        ___qtablewidgetitem34 = self.Payment_tableWidget_5.horizontalHeaderItem(6)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"Apartment ID", None));
        self.ElectricBillList_label.setText(QCoreApplication.translate("MainWindow", u"Electric Bill List", None))
        self.Search_lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search....", None))
        ___qtablewidgetitem35 = self.ElectricBill_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"Electric Bill ID", None));
        ___qtablewidgetitem36 = self.ElectricBill_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"Date Started", None));
        ___qtablewidgetitem37 = self.ElectricBill_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"Kwh", None));
        ___qtablewidgetitem38 = self.ElectricBill_tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        ___qtablewidgetitem39 = self.ElectricBill_tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"Apartment ID", None));
        self.CRUDElecBill_label.setText(QCoreApplication.translate("MainWindow", u"CRUD Electric Bill", None))
        self.DateStarted.setText(QCoreApplication.translate("MainWindow", u"Date Started:", None))
        self.Kwh.setText(QCoreApplication.translate("MainWindow", u"Kwh:", None))
        self.Status.setText(QCoreApplication.translate("MainWindow", u"Status:", None))
        self.kwh_line_edit.setText("")
        self.AddEBBtn.setText(QCoreApplication.translate("MainWindow", u"ADD", None))
        self.DelEBBtn.setText(QCoreApplication.translate("MainWindow", u"DELETE", None))
        self.UpdEBBtn.setText(QCoreApplication.translate("MainWindow", u"UPDATE", None))
        self.ApartmentID.setText(QCoreApplication.translate("MainWindow", u"Apartment ID:", None))
        self.ApartID_line_edit_7.setText("")
        self.Status_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Pending", None))
        self.Status_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Succesful", None))
        self.Status_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Overdue", None))

        self.GetEBBtn.setText(QCoreApplication.translate("MainWindow", u"GET", None))
        ___qtablewidgetitem40 = self.ElectricBill_tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"Electric Bill ID", None));
        ___qtablewidgetitem41 = self.ElectricBill_tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"Date Started", None));
        ___qtablewidgetitem42 = self.ElectricBill_tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"Kwh", None));
        ___qtablewidgetitem43 = self.ElectricBill_tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        ___qtablewidgetitem44 = self.ElectricBill_tableWidget_2.horizontalHeaderItem(4)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"Apartment ID", None));
        self.page_label.setText(QCoreApplication.translate("MainWindow", u"CRUD Tenant", None))
        self.Name_line_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"First Name, Middle Name, Last Name", None))
        self.Name.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.Age.setText(QCoreApplication.translate("MainWindow", u"Age:", None))
        self.Sex.setText(QCoreApplication.translate("MainWindow", u"Sex:", None))
        self.PhoneNum_line_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"09xxxxxxxxx", None))
        self.Email_line_edit.setText("")
        self.Phone_number.setText(QCoreApplication.translate("MainWindow", u"Phone Number:", None))
        self.Email.setText(QCoreApplication.translate("MainWindow", u"Email:", None))
        self.Apart_num.setText(QCoreApplication.translate("MainWindow", u"Apartment ID:", None))
        self.Sex_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Male", None))
        self.Sex_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Female", None))

        self.AddTenantBtn.setText(QCoreApplication.translate("MainWindow", u"ADD", None))
        self.DelTenantBtn.setText(QCoreApplication.translate("MainWindow", u"DELETE", None))
        self.UpdTenantBtn.setText(QCoreApplication.translate("MainWindow", u"UPDATE", None))
        self.GetTenantBtn.setText(QCoreApplication.translate("MainWindow", u"GET", None))
        self.ApartNum_line_edit_3.setText("")
        ___qtablewidgetitem45 = self.Tenant_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"Tenant ID", None));
        ___qtablewidgetitem46 = self.Tenant_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem47 = self.Tenant_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"Age", None));
        ___qtablewidgetitem48 = self.Tenant_tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"Sex", None));
        ___qtablewidgetitem49 = self.Tenant_tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem50 = self.Tenant_tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("MainWindow", u"Phone Number", None));
        ___qtablewidgetitem51 = self.Tenant_tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("MainWindow", u"Apart. Number", None));
    # retranslateUi

