# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)
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
        self.lineEdit = QLineEdit(self.TSListPage)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(610, 20, 240, 20))
        self.lineEdit.setMinimumSize(QSize(240, 20))
        self.lineEdit.setMaximumSize(QSize(240, 30))
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
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
        self.label_3 = QLabel(self.TSListPage)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 20, 201, 16))
        font3 = QFont()
        font3.setFamilies([u"Times New Roman"])
        font3.setPointSize(11)
        self.label_3.setFont(font3)
        self.tableWidget = QTableWidget(self.TSListPage)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(20, 50, 831, 421))
        self.tableWidget.setStyleSheet(u"QTableWidget {\n"
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
        self.Email_line_edit_3 = QLineEdit(self.frame_10)
        self.Email_line_edit_3.setObjectName(u"Email_line_edit_3")
        self.Email_line_edit_3.setGeometry(QRect(140, 340, 191, 21))
        self.Email_line_edit_3.setStyleSheet(u"background-color: #666666; color: black;")
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
        if (self.PayHis_tableWidget_2.columnCount() < 4):
            self.PayHis_tableWidget_2.setColumnCount(4)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.PayHis_tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.PayHis_tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.PayHis_tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.PayHis_tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem6)
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
        self.label_4 = QLabel(self.ApartmentInfoPage)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(100, 100, 281, 16))
        self.stackedWidget.addWidget(self.ApartmentInfoPage)
        self.CRUDApartPage = QWidget()
        self.CRUDApartPage.setObjectName(u"CRUDApartPage")
        self.label_5 = QLabel(self.CRUDApartPage)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(300, 210, 281, 16))
        self.stackedWidget.addWidget(self.CRUDApartPage)
        self.PaymentListPage = QWidget()
        self.PaymentListPage.setObjectName(u"PaymentListPage")
        self.label_9 = QLabel(self.PaymentListPage)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(300, 220, 281, 16))
        self.stackedWidget.addWidget(self.PaymentListPage)
        self.CRUDPaymentPage = QWidget()
        self.CRUDPaymentPage.setObjectName(u"CRUDPaymentPage")
        self.label_7 = QLabel(self.CRUDPaymentPage)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(250, 240, 281, 16))
        self.stackedWidget.addWidget(self.CRUDPaymentPage)
        self.EBListPage = QWidget()
        self.EBListPage.setObjectName(u"EBListPage")
        self.label_8 = QLabel(self.EBListPage)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(290, 210, 281, 16))
        self.stackedWidget.addWidget(self.EBListPage)
        self.CRUDElecBillPage = QWidget()
        self.CRUDElecBillPage.setObjectName(u"CRUDElecBillPage")
        self.label_6 = QLabel(self.CRUDElecBillPage)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(300, 210, 281, 16))
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
        self.Name_line_edit.setGeometry(QRect(140, 60, 251, 21))
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
        self.PhoneNum_line_edit.setGeometry(QRect(140, 180, 81, 21))
        self.PhoneNum_line_edit.setStyleSheet(u"background-color: #666666; color: black;")
        self.Email_line_edit = QLineEdit(self.frame_7)
        self.Email_line_edit.setObjectName(u"Email_line_edit")
        self.Email_line_edit.setGeometry(QRect(140, 220, 251, 21))
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
        self.Sex_comboBox.setObjectName(u"Sex_comboBox")
        self.Sex_comboBox.setGeometry(QRect(140, 140, 81, 22))
        self.Sex_comboBox.setStyleSheet(u"background-color: #666666; color: black;")
        self.ApartNum_comboBox = QComboBox(self.frame_7)
        self.ApartNum_comboBox.setObjectName(u"ApartNum_comboBox")
        self.ApartNum_comboBox.setGeometry(QRect(140, 260, 61, 22))
        self.ApartNum_comboBox.setStyleSheet(u"background-color: #666666; color: black;")
        self.AddTenantBtn = QPushButton(self.frame_7)
        self.AddTenantBtn.setObjectName(u"AddTenantBtn")
        self.AddTenantBtn.setGeometry(QRect(40, 330, 111, 41))
        self.AddTenantBtn.setFont(font4)
        self.AddTenantBtn.setStyleSheet(u"background-color: #666666; color: white\n"
";\n"
"")
        self.DelTenantBtn = QPushButton(self.frame_7)
        self.DelTenantBtn.setObjectName(u"DelTenantBtn")
        self.DelTenantBtn.setGeometry(QRect(160, 330, 111, 41))
        self.DelTenantBtn.setFont(font4)
        self.DelTenantBtn.setStyleSheet(u"background-color: #666666; color: white\n"
";\n"
"")
        self.UpdTenantBtn = QPushButton(self.frame_7)
        self.UpdTenantBtn.setObjectName(u"UpdTenantBtn")
        self.UpdTenantBtn.setGeometry(QRect(280, 330, 111, 41))
        self.UpdTenantBtn.setFont(font4)
        self.UpdTenantBtn.setStyleSheet(u"background-color: #666666; color: white\n"
";\n"
"")

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
        __qtablewidgetitem7 = QTableWidgetItem()
        self.Tenant_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.Tenant_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.Tenant_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.Tenant_tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.Tenant_tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.Tenant_tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.Tenant_tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem13)
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

        self.stackedWidget.setCurrentIndex(8)


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
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search....", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Tenant Status List", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Tenant ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Number", None));
        self.page_label_2.setText(QCoreApplication.translate("MainWindow", u"Tenant Information", None))
        self.Name_line_edit_2.setPlaceholderText("")
        self.Name_2.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.Age_2.setText(QCoreApplication.translate("MainWindow", u"Age:", None))
        self.Sex_2.setText(QCoreApplication.translate("MainWindow", u"Sex:", None))
        self.PhoneNum_line_edit_2.setPlaceholderText("")
        self.Email_line_edit_2.setText("")
        self.Phone_number_2.setText(QCoreApplication.translate("MainWindow", u"Phone Number:", None))
        self.Email_2.setText(QCoreApplication.translate("MainWindow", u"Email:", None))
        self.Apart_num_2.setText(QCoreApplication.translate("MainWindow", u"Apart. Number:", None))
        self.SearchTenantBtn.setText(QCoreApplication.translate("MainWindow", u"SEARCH", None))
        self.PayHisBtn.setText(QCoreApplication.translate("MainWindow", u"Payment History", None))
        self.Search_line_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Tenant ID", None))
        self.Email_line_edit_3.setText("")
        self.PayStat.setText(QCoreApplication.translate("MainWindow", u"Payment Status:", None))
        ___qtablewidgetitem3 = self.PayHis_tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Payment ID", None));
        ___qtablewidgetitem4 = self.PayHis_tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Amount Paid", None));
        ___qtablewidgetitem5 = self.PayHis_tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Payment Date", None));
        ___qtablewidgetitem6 = self.PayHis_tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Payment Method", None));
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Apartment Info Page", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"CRUD Apartment Page", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Payment List Page", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"CRUD Payment Page", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Electric Bill List Page", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"CRUD Electric Bill Page", None))
        self.page_label.setText(QCoreApplication.translate("MainWindow", u"CRUD Tenant", None))
        self.Name_line_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"First Name, Middle Initial, Last Name", None))
        self.Name.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.Age.setText(QCoreApplication.translate("MainWindow", u"Age:", None))
        self.Sex.setText(QCoreApplication.translate("MainWindow", u"Sex:", None))
        self.PhoneNum_line_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"09xxxxxxxxx", None))
        self.Email_line_edit.setText("")
        self.Phone_number.setText(QCoreApplication.translate("MainWindow", u"Phone Number:", None))
        self.Email.setText(QCoreApplication.translate("MainWindow", u"Email:", None))
        self.Apart_num.setText(QCoreApplication.translate("MainWindow", u"Apart. Number:", None))
        self.AddTenantBtn.setText(QCoreApplication.translate("MainWindow", u"ADD", None))
        self.DelTenantBtn.setText(QCoreApplication.translate("MainWindow", u"DELETE", None))
        self.UpdTenantBtn.setText(QCoreApplication.translate("MainWindow", u"UPDATE", None))
        ___qtablewidgetitem7 = self.Tenant_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Tenant ID", None));
        ___qtablewidgetitem8 = self.Tenant_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem9 = self.Tenant_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Age", None));
        ___qtablewidgetitem10 = self.Tenant_tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Sex", None));
        ___qtablewidgetitem11 = self.Tenant_tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Phone Number", None));
        ___qtablewidgetitem12 = self.Tenant_tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem13 = self.Tenant_tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Apart. Number", None));
    # retranslateUi

