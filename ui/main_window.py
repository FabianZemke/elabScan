# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QCheckBox, QComboBox,
    QDateEdit, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QRadioButton,
    QScrollArea, QSizePolicy, QSpacerItem, QSpinBox,
    QStatusBar, QTabWidget, QTableWidget, QTableWidgetItem,
    QTextBrowser, QToolBox, QToolButton, QVBoxLayout,
    QWidget)
import Resourcefile_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(914, 794)
        font = QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/Images/myQR.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.Main_tab = QTabWidget(self.centralwidget)
        self.Main_tab.setObjectName(u"Main_tab")
        self.Main_tab.setTabPosition(QTabWidget.West)
        self.Main_tab.setIconSize(QSize(50, 50))
        self.Home_Main_tab = QWidget()
        self.Home_Main_tab.setObjectName(u"Home_Main_tab")
        self.gridLayout_2 = QGridLayout(self.Home_Main_tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.Home_tab = QTabWidget(self.Home_Main_tab)
        self.Home_tab.setObjectName(u"Home_tab")
        self.Home_tab.setEnabled(True)
        self.Home_tab.setFont(font)
        self.Home_tab.setTabPosition(QTabWidget.West)
        self.Home_tab.setTabShape(QTabWidget.Rounded)
        self.Home_tab.setDocumentMode(False)
        self.Home_Home_tab = QWidget()
        self.Home_Home_tab.setObjectName(u"Home_Home_tab")
        self.gridLayout_4 = QGridLayout(self.Home_Home_tab)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(25)
        self.label_3 = QLabel(self.Home_Home_tab)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.gridLayout_3.addWidget(self.label_3, 2, 2, 1, 1)

        self.label = QLabel(self.Home_Home_tab)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.gridLayout_3.addWidget(self.label, 2, 0, 1, 1)

        self.HomeScan_button = QPushButton(self.Home_Home_tab)
        self.HomeScan_button.setObjectName(u"HomeScan_button")
        icon1 = QIcon()
        icon1.addFile(u":/Images/qr-code-scan-icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.HomeScan_button.setIcon(icon1)
        self.HomeScan_button.setIconSize(QSize(75, 75))
        self.HomeScan_button.setFlat(True)

        self.gridLayout_3.addWidget(self.HomeScan_button, 1, 2, 1, 1)

        self.HomeCreate_button = QPushButton(self.Home_Home_tab)
        self.HomeCreate_button.setObjectName(u"HomeCreate_button")
        icon2 = QIcon()
        icon2.addFile(u":/Images/pencil-square-outline-icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.HomeCreate_button.setIcon(icon2)
        self.HomeCreate_button.setIconSize(QSize(75, 75))
        self.HomeCreate_button.setAutoDefault(False)
        self.HomeCreate_button.setFlat(True)

        self.gridLayout_3.addWidget(self.HomeCreate_button, 1, 0, 1, 1)

        self.HomeSearch_button = QPushButton(self.Home_Home_tab)
        self.HomeSearch_button.setObjectName(u"HomeSearch_button")
        icon3 = QIcon()
        icon3.addFile(u":/Images/book-research-icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.HomeSearch_button.setIcon(icon3)
        self.HomeSearch_button.setIconSize(QSize(75, 75))
        self.HomeSearch_button.setFlat(True)

        self.gridLayout_3.addWidget(self.HomeSearch_button, 1, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 0, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_3, 0, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 0, 1, 1, 1)

        self.label_2 = QLabel(self.Home_Home_tab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setLayoutDirection(Qt.LeftToRight)
        self.label_2.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.gridLayout_3.addWidget(self.label_2, 2, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_4, 3, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_5, 3, 1, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_6, 3, 2, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)

        self.Home_tab.addTab(self.Home_Home_tab, "")
        self.Advanced_Home_tab = QWidget()
        self.Advanced_Home_tab.setObjectName(u"Advanced_Home_tab")
        self.gridLayout_5 = QGridLayout(self.Advanced_Home_tab)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.HomeAddEquipment_button = QPushButton(self.Advanced_Home_tab)
        self.HomeAddEquipment_button.setObjectName(u"HomeAddEquipment_button")
        self.HomeAddEquipment_button.setEnabled(False)
        icon4 = QIcon()
        icon4.addFile(u":/Images/repair-service-icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.HomeAddEquipment_button.setIcon(icon4)
        self.HomeAddEquipment_button.setIconSize(QSize(75, 75))
        self.HomeAddEquipment_button.setFlat(True)

        self.gridLayout_5.addWidget(self.HomeAddEquipment_button, 4, 1, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_7, 6, 0, 1, 1)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_11, 0, 1, 1, 1)

        self.HomeAddChemical_button = QPushButton(self.Advanced_Home_tab)
        self.HomeAddChemical_button.setObjectName(u"HomeAddChemical_button")
        self.HomeAddChemical_button.setEnabled(True)
        icon5 = QIcon()
        icon5.addFile(u":/Images/chemical-engineering-icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.HomeAddChemical_button.setIcon(icon5)
        self.HomeAddChemical_button.setIconSize(QSize(75, 75))
        self.HomeAddChemical_button.setFlat(True)

        self.gridLayout_5.addWidget(self.HomeAddChemical_button, 4, 0, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_9, 6, 1, 1, 1)

        self.label_12 = QLabel(self.Advanced_Home_tab)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.gridLayout_5.addWidget(self.label_12, 2, 1, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 114, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_8, 3, 0, 1, 1)

        self.label_4 = QLabel(self.Advanced_Home_tab)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.gridLayout_5.addWidget(self.label_4, 2, 0, 1, 1)

        self.label_5 = QLabel(self.Advanced_Home_tab)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.gridLayout_5.addWidget(self.label_5, 5, 0, 1, 1)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_10, 0, 0, 1, 1)

        self.label_6 = QLabel(self.Advanced_Home_tab)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.gridLayout_5.addWidget(self.label_6, 5, 1, 1, 1)

        self.HomeAbout_button = QPushButton(self.Advanced_Home_tab)
        self.HomeAbout_button.setObjectName(u"HomeAbout_button")
        icon6 = QIcon()
        icon6.addFile(u":/Images/info-information-icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.HomeAbout_button.setIcon(icon6)
        self.HomeAbout_button.setIconSize(QSize(75, 75))
        self.HomeAbout_button.setFlat(True)

        self.gridLayout_5.addWidget(self.HomeAbout_button, 1, 1, 1, 1)

        self.verticalSpacer_34 = QSpacerItem(20, 114, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_34, 3, 1, 1, 1)

        self.HomeLog_button = QPushButton(self.Advanced_Home_tab)
        self.HomeLog_button.setObjectName(u"HomeLog_button")
        icon7 = QIcon()
        icon7.addFile(u":/Images/wood-icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.HomeLog_button.setIcon(icon7)
        self.HomeLog_button.setIconSize(QSize(75, 75))
        self.HomeLog_button.setFlat(True)

        self.gridLayout_5.addWidget(self.HomeLog_button, 1, 0, 1, 1)

        self.Home_tab.addTab(self.Advanced_Home_tab, "")

        self.gridLayout_2.addWidget(self.Home_tab, 0, 0, 1, 1)

        icon8 = QIcon()
        icon8.addFile(u":/Images/homepage-icon_90.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Main_tab.addTab(self.Home_Main_tab, icon8, "")
        self.Create_Main_tab = QWidget()
        self.Create_Main_tab.setObjectName(u"Create_Main_tab")
        self.gridLayout_8 = QGridLayout(self.Create_Main_tab)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.SampleID_tab = QTabWidget(self.Create_Main_tab)
        self.SampleID_tab.setObjectName(u"SampleID_tab")
        self.SampleID_tab.setFont(font)
        self.SampleID_tab.setTabPosition(QTabWidget.West)
        self.IDdecryption_SampleID_tab = QWidget()
        self.IDdecryption_SampleID_tab.setObjectName(u"IDdecryption_SampleID_tab")
        self.gridLayout_9 = QGridLayout(self.IDdecryption_SampleID_tab)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.DecryptgroupBox = QGroupBox(self.IDdecryption_SampleID_tab)
        self.DecryptgroupBox.setObjectName(u"DecryptgroupBox")
        self.DecryptgroupBox.setFont(font)
        self.gridLayout_12 = QGridLayout(self.DecryptgroupBox)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_11.addItem(self.verticalSpacer_13, 0, 1, 1, 1)

        self.DecryptLabel = QLabel(self.DecryptgroupBox)
        self.DecryptLabel.setObjectName(u"DecryptLabel")

        self.gridLayout_11.addWidget(self.DecryptLabel, 1, 0, 1, 2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Decrypt_lineEdit = QLineEdit(self.DecryptgroupBox)
        self.Decrypt_lineEdit.setObjectName(u"Decrypt_lineEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Decrypt_lineEdit.sizePolicy().hasHeightForWidth())
        self.Decrypt_lineEdit.setSizePolicy(sizePolicy)
        self.Decrypt_lineEdit.setFocusPolicy(Qt.StrongFocus)
        self.Decrypt_lineEdit.setInputMethodHints(Qt.ImhNone)
        self.Decrypt_lineEdit.setClearButtonEnabled(True)

        self.horizontalLayout.addWidget(self.Decrypt_lineEdit)

        self.Decrypt_button = QPushButton(self.DecryptgroupBox)
        self.Decrypt_button.setObjectName(u"Decrypt_button")
        icon9 = QIcon()
        icon9.addFile(u":/Images/task-sync-icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Decrypt_button.setIcon(icon9)
        self.Decrypt_button.setIconSize(QSize(50, 50))

        self.horizontalLayout.addWidget(self.Decrypt_button)


        self.gridLayout_11.addLayout(self.horizontalLayout, 2, 0, 1, 2)

        self.DecryptResponse_label = QLabel(self.DecryptgroupBox)
        self.DecryptResponse_label.setObjectName(u"DecryptResponse_label")

        self.gridLayout_11.addWidget(self.DecryptResponse_label, 3, 0, 1, 1)

        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_11.addItem(self.verticalSpacer_14, 4, 1, 1, 1)

        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.SampleidBack1_button = QPushButton(self.DecryptgroupBox)
        self.SampleidBack1_button.setObjectName(u"SampleidBack1_button")
        icon10 = QIcon()
        icon10.addFile(u":/Images/curved-arrow-back-outline-icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.SampleidBack1_button.setIcon(icon10)
        self.SampleidBack1_button.setIconSize(QSize(40, 40))
        self.SampleidBack1_button.setFlat(False)

        self.gridLayout_10.addWidget(self.SampleidBack1_button, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)

        self.SampleidForward1_button = QPushButton(self.DecryptgroupBox)
        self.SampleidForward1_button.setObjectName(u"SampleidForward1_button")
        icon11 = QIcon()
        icon11.addFile(u":/Images/forward-arrow-outline-icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.SampleidForward1_button.setIcon(icon11)
        self.SampleidForward1_button.setIconSize(QSize(40, 40))
        self.SampleidForward1_button.setFlat(False)

        self.gridLayout_10.addWidget(self.SampleidForward1_button, 0, 3, 1, 1)


        self.gridLayout_11.addLayout(self.gridLayout_10, 5, 0, 1, 2)

        self.verticalSpacer_15 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_11.addItem(self.verticalSpacer_15, 4, 0, 1, 1)

        self.verticalSpacer_16 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_11.addItem(self.verticalSpacer_16, 0, 0, 1, 1)


        self.gridLayout_12.addLayout(self.gridLayout_11, 0, 0, 1, 1)


        self.gridLayout_9.addWidget(self.DecryptgroupBox, 0, 0, 1, 1)

        self.SampleID_tab.addTab(self.IDdecryption_SampleID_tab, "")
        self.MandInfo_SampleID_tab = QWidget()
        self.MandInfo_SampleID_tab.setObjectName(u"MandInfo_SampleID_tab")
        self.gridLayout_13 = QGridLayout(self.MandInfo_SampleID_tab)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.groupBox = QGroupBox(self.MandInfo_SampleID_tab)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_15 = QGridLayout(self.groupBox)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.verticalSpacer_24 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_15.addItem(self.verticalSpacer_24, 3, 1, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.FirstNameLabel = QLabel(self.groupBox)
        self.FirstNameLabel.setObjectName(u"FirstNameLabel")
        self.FirstNameLabel.setFont(font)
        self.FirstNameLabel.setLayoutDirection(Qt.RightToLeft)

        self.verticalLayout_4.addWidget(self.FirstNameLabel)

        self.LastNameLabel = QLabel(self.groupBox)
        self.LastNameLabel.setObjectName(u"LastNameLabel")
        self.LastNameLabel.setFont(font)

        self.verticalLayout_4.addWidget(self.LastNameLabel)

        self.SupervisorLabel = QLabel(self.groupBox)
        self.SupervisorLabel.setObjectName(u"SupervisorLabel")
        self.SupervisorLabel.setFont(font)

        self.verticalLayout_4.addWidget(self.SupervisorLabel)

        self.DateLabel = QLabel(self.groupBox)
        self.DateLabel.setObjectName(u"DateLabel")
        self.DateLabel.setFont(font)

        self.verticalLayout_4.addWidget(self.DateLabel)

        self.ExpirationLabel = QLabel(self.groupBox)
        self.ExpirationLabel.setObjectName(u"ExpirationLabel")
        self.ExpirationLabel.setFont(font)

        self.verticalLayout_4.addWidget(self.ExpirationLabel)


        self.horizontalLayout_3.addLayout(self.verticalLayout_4)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.FirstName_lineEdit = QLineEdit(self.groupBox)
        self.FirstName_lineEdit.setObjectName(u"FirstName_lineEdit")
        self.FirstName_lineEdit.setFont(font)
        self.FirstName_lineEdit.setMaxLength(32)

        self.verticalLayout_2.addWidget(self.FirstName_lineEdit)

        self.LastName_lineEdit = QLineEdit(self.groupBox)
        self.LastName_lineEdit.setObjectName(u"LastName_lineEdit")
        self.LastName_lineEdit.setFont(font)
        self.LastName_lineEdit.setMaxLength(32)

        self.verticalLayout_2.addWidget(self.LastName_lineEdit)

        self.Supervisor_lineEdit = QLineEdit(self.groupBox)
        self.Supervisor_lineEdit.setObjectName(u"Supervisor_lineEdit")
        self.Supervisor_lineEdit.setFont(font)
        self.Supervisor_lineEdit.setMaxLength(32)

        self.verticalLayout_2.addWidget(self.Supervisor_lineEdit)

        self.Current_dateEdit = QDateEdit(self.groupBox)
        self.Current_dateEdit.setObjectName(u"Current_dateEdit")
        sizePolicy.setHeightForWidth(self.Current_dateEdit.sizePolicy().hasHeightForWidth())
        self.Current_dateEdit.setSizePolicy(sizePolicy)
        self.Current_dateEdit.setFont(font)
        self.Current_dateEdit.setDateTime(QDateTime(QDate(2020, 1, 1), QTime(0, 0, 0)))
        self.Current_dateEdit.setMaximumDateTime(QDateTime(QDate(2037, 12, 31), QTime(23, 59, 59)))
        self.Current_dateEdit.setMinimumDateTime(QDateTime(QDate(2011, 1, 1), QTime(0, 0, 0)))
        self.Current_dateEdit.setCalendarPopup(True)

        self.verticalLayout_2.addWidget(self.Current_dateEdit)

        self.Expiration_dateEdit = QDateEdit(self.groupBox)
        self.Expiration_dateEdit.setObjectName(u"Expiration_dateEdit")
        sizePolicy.setHeightForWidth(self.Expiration_dateEdit.sizePolicy().hasHeightForWidth())
        self.Expiration_dateEdit.setSizePolicy(sizePolicy)
        self.Expiration_dateEdit.setFont(font)
        self.Expiration_dateEdit.setDateTime(QDateTime(QDate(2011, 12, 31), QTime(23, 59, 59)))
        self.Expiration_dateEdit.setMaximumDateTime(QDateTime(QDate(2100, 12, 31), QTime(23, 59, 59)))
        self.Expiration_dateEdit.setMinimumDateTime(QDateTime(QDate(2011, 1, 1), QTime(0, 0, 0)))
        self.Expiration_dateEdit.setCalendarPopup(True)

        self.verticalLayout_2.addWidget(self.Expiration_dateEdit)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)


        self.gridLayout_15.addLayout(self.horizontalLayout_3, 1, 0, 1, 2)

        self.verticalSpacer_18 = QSpacerItem(20, 169, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_15.addItem(self.verticalSpacer_18, 3, 0, 1, 1)

        self.gridLayout_14 = QGridLayout()
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.SampleidBack2_button = QPushButton(self.groupBox)
        self.SampleidBack2_button.setObjectName(u"SampleidBack2_button")
        self.SampleidBack2_button.setIcon(icon10)
        self.SampleidBack2_button.setIconSize(QSize(40, 40))
        self.SampleidBack2_button.setFlat(False)

        self.gridLayout_14.addWidget(self.SampleidBack2_button, 0, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_14.addItem(self.horizontalSpacer_3, 0, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_14.addItem(self.horizontalSpacer_4, 0, 2, 1, 1)

        self.SampleidForward2_button = QPushButton(self.groupBox)
        self.SampleidForward2_button.setObjectName(u"SampleidForward2_button")
        self.SampleidForward2_button.setIcon(icon11)
        self.SampleidForward2_button.setIconSize(QSize(40, 40))
        self.SampleidForward2_button.setFlat(False)

        self.gridLayout_14.addWidget(self.SampleidForward2_button, 0, 3, 1, 1)


        self.gridLayout_15.addLayout(self.gridLayout_14, 4, 0, 1, 2)

        self.verticalSpacer_17 = QSpacerItem(20, 170, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_15.addItem(self.verticalSpacer_17, 0, 1, 1, 1)

        self.verticalSpacer_23 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_15.addItem(self.verticalSpacer_23, 0, 0, 1, 1)

        self.NameDateOutput_label = QLabel(self.groupBox)
        self.NameDateOutput_label.setObjectName(u"NameDateOutput_label")

        self.gridLayout_15.addWidget(self.NameDateOutput_label, 2, 0, 1, 2)


        self.gridLayout_13.addWidget(self.groupBox, 0, 0, 1, 1)

        self.SampleID_tab.addTab(self.MandInfo_SampleID_tab, "")
        self.SampleNumber_SampleID_tab = QWidget()
        self.SampleNumber_SampleID_tab.setObjectName(u"SampleNumber_SampleID_tab")
        self.gridLayout_34 = QGridLayout(self.SampleNumber_SampleID_tab)
        self.gridLayout_34.setObjectName(u"gridLayout_34")
        self.groupBox_10 = QGroupBox(self.SampleNumber_SampleID_tab)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.gridLayout_41 = QGridLayout(self.groupBox_10)
        self.gridLayout_41.setObjectName(u"gridLayout_41")
        self.line_4 = QFrame(self.groupBox_10)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.gridLayout_41.addWidget(self.line_4, 9, 0, 1, 1)

        self.gridLayout_40 = QGridLayout()
        self.gridLayout_40.setObjectName(u"gridLayout_40")
        self.SampleNumberLabel_2 = QLabel(self.groupBox_10)
        self.SampleNumberLabel_2.setObjectName(u"SampleNumberLabel_2")
        self.SampleNumberLabel_2.setFont(font)

        self.gridLayout_40.addWidget(self.SampleNumberLabel_2, 0, 2, 1, 1)

        self.Subsample3_spinBox = QSpinBox(self.groupBox_10)
        self.Subsample3_spinBox.setObjectName(u"Subsample3_spinBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Subsample3_spinBox.sizePolicy().hasHeightForWidth())
        self.Subsample3_spinBox.setSizePolicy(sizePolicy1)
        self.Subsample3_spinBox.setMinimum(1)

        self.gridLayout_40.addWidget(self.Subsample3_spinBox, 1, 5, 1, 1)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.gridLayout_40.addItem(self.horizontalSpacer_19, 1, 1, 1, 1)

        self.label_11 = QLabel(self.groupBox_10)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_40.addWidget(self.label_11, 1, 4, 1, 1)

        self.label_10 = QLabel(self.groupBox_10)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_40.addWidget(self.label_10, 0, 4, 1, 1)

        self.Samplenumber2_spinBox = QSpinBox(self.groupBox_10)
        self.Samplenumber2_spinBox.setObjectName(u"Samplenumber2_spinBox")
        sizePolicy1.setHeightForWidth(self.Samplenumber2_spinBox.sizePolicy().hasHeightForWidth())
        self.Samplenumber2_spinBox.setSizePolicy(sizePolicy1)
        self.Samplenumber2_spinBox.setFont(font)
        self.Samplenumber2_spinBox.setMinimum(1)
        self.Samplenumber2_spinBox.setMaximum(999)

        self.gridLayout_40.addWidget(self.Samplenumber2_spinBox, 0, 3, 1, 1)

        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_40.addItem(self.horizontalSpacer_23, 0, 6, 1, 1)

        self.label_8 = QLabel(self.groupBox_10)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_40.addWidget(self.label_8, 1, 0, 1, 1)

        self.SubSample2_checkBox = QCheckBox(self.groupBox_10)
        self.SubSample2_checkBox.setObjectName(u"SubSample2_checkBox")
        sizePolicy1.setHeightForWidth(self.SubSample2_checkBox.sizePolicy().hasHeightForWidth())
        self.SubSample2_checkBox.setSizePolicy(sizePolicy1)

        self.gridLayout_40.addWidget(self.SubSample2_checkBox, 1, 2, 1, 1)

        self.Subsample2_spinBox = QSpinBox(self.groupBox_10)
        self.Subsample2_spinBox.setObjectName(u"Subsample2_spinBox")
        sizePolicy1.setHeightForWidth(self.Subsample2_spinBox.sizePolicy().hasHeightForWidth())
        self.Subsample2_spinBox.setSizePolicy(sizePolicy1)
        self.Subsample2_spinBox.setMinimum(1)

        self.gridLayout_40.addWidget(self.Subsample2_spinBox, 1, 3, 1, 1)

        self.Batch_radioButton = QRadioButton(self.groupBox_10)
        self.Batch_radioButton.setObjectName(u"Batch_radioButton")

        self.gridLayout_40.addWidget(self.Batch_radioButton, 0, 0, 1, 1)

        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_40.addItem(self.horizontalSpacer_24, 1, 6, 1, 1)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.gridLayout_40.addItem(self.horizontalSpacer_18, 0, 1, 1, 1)

        self.Samplenumber3_spinBox = QSpinBox(self.groupBox_10)
        self.Samplenumber3_spinBox.setObjectName(u"Samplenumber3_spinBox")
        sizePolicy1.setHeightForWidth(self.Samplenumber3_spinBox.sizePolicy().hasHeightForWidth())
        self.Samplenumber3_spinBox.setSizePolicy(sizePolicy1)
        self.Samplenumber3_spinBox.setFont(font)
        self.Samplenumber3_spinBox.setMinimum(1)
        self.Samplenumber3_spinBox.setMaximum(999)

        self.gridLayout_40.addWidget(self.Samplenumber3_spinBox, 0, 5, 1, 1)


        self.gridLayout_41.addLayout(self.gridLayout_40, 7, 0, 1, 1)

        self.gridLayout_35 = QGridLayout()
        self.gridLayout_35.setObjectName(u"gridLayout_35")
        self.SampleidBack3_button = QPushButton(self.groupBox_10)
        self.SampleidBack3_button.setObjectName(u"SampleidBack3_button")
        self.SampleidBack3_button.setIcon(icon10)
        self.SampleidBack3_button.setIconSize(QSize(40, 40))
        self.SampleidBack3_button.setFlat(False)

        self.gridLayout_35.addWidget(self.SampleidBack3_button, 0, 0, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_35.addItem(self.horizontalSpacer_11, 0, 1, 1, 1)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_35.addItem(self.horizontalSpacer_14, 0, 2, 1, 1)

        self.SampleidForward3_button = QPushButton(self.groupBox_10)
        self.SampleidForward3_button.setObjectName(u"SampleidForward3_button")
        self.SampleidForward3_button.setIcon(icon11)
        self.SampleidForward3_button.setIconSize(QSize(40, 40))
        self.SampleidForward3_button.setFlat(False)

        self.gridLayout_35.addWidget(self.SampleidForward3_button, 0, 3, 1, 1)


        self.gridLayout_41.addLayout(self.gridLayout_35, 11, 0, 1, 1)

        self.verticalSpacer_33 = QSpacerItem(20, 120, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_41.addItem(self.verticalSpacer_33, 4, 0, 1, 1)

        self.gridLayout_39 = QGridLayout()
        self.gridLayout_39.setObjectName(u"gridLayout_39")
        self.SubSample1_checkBox = QCheckBox(self.groupBox_10)
        self.SubSample1_checkBox.setObjectName(u"SubSample1_checkBox")
        sizePolicy1.setHeightForWidth(self.SubSample1_checkBox.sizePolicy().hasHeightForWidth())
        self.SubSample1_checkBox.setSizePolicy(sizePolicy1)

        self.gridLayout_39.addWidget(self.SubSample1_checkBox, 1, 2, 1, 1)

        self.label_9 = QLabel(self.groupBox_10)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_39.addWidget(self.label_9, 1, 0, 1, 1)

        self.Subsample1_spinBox = QSpinBox(self.groupBox_10)
        self.Subsample1_spinBox.setObjectName(u"Subsample1_spinBox")
        sizePolicy1.setHeightForWidth(self.Subsample1_spinBox.sizePolicy().hasHeightForWidth())
        self.Subsample1_spinBox.setSizePolicy(sizePolicy1)
        self.Subsample1_spinBox.setMinimum(1)

        self.gridLayout_39.addWidget(self.Subsample1_spinBox, 1, 3, 1, 1)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_39.addItem(self.horizontalSpacer_22, 1, 4, 1, 1)

        self.SampleNumberLabel = QLabel(self.groupBox_10)
        self.SampleNumberLabel.setObjectName(u"SampleNumberLabel")
        self.SampleNumberLabel.setFont(font)

        self.gridLayout_39.addWidget(self.SampleNumberLabel, 0, 2, 1, 1)

        self.Single_radioButton = QRadioButton(self.groupBox_10)
        self.Single_radioButton.setObjectName(u"Single_radioButton")
        self.Single_radioButton.setChecked(True)

        self.gridLayout_39.addWidget(self.Single_radioButton, 0, 0, 1, 1)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_39.addItem(self.horizontalSpacer_21, 0, 4, 1, 1)

        self.Samplenumber1_spinBox = QSpinBox(self.groupBox_10)
        self.Samplenumber1_spinBox.setObjectName(u"Samplenumber1_spinBox")
        sizePolicy1.setHeightForWidth(self.Samplenumber1_spinBox.sizePolicy().hasHeightForWidth())
        self.Samplenumber1_spinBox.setSizePolicy(sizePolicy1)
        self.Samplenumber1_spinBox.setFont(font)
        self.Samplenumber1_spinBox.setMinimum(1)
        self.Samplenumber1_spinBox.setMaximum(999)

        self.gridLayout_39.addWidget(self.Samplenumber1_spinBox, 0, 3, 1, 1)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.gridLayout_39.addItem(self.horizontalSpacer_20, 1, 1, 1, 1)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.gridLayout_39.addItem(self.horizontalSpacer_17, 0, 1, 1, 1)


        self.gridLayout_41.addLayout(self.gridLayout_39, 2, 0, 1, 1)

        self.line_3 = QFrame(self.groupBox_10)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout_41.addWidget(self.line_3, 5, 0, 1, 1)

        self.line_2 = QFrame(self.groupBox_10)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_41.addWidget(self.line_2, 3, 0, 1, 1)

        self.verticalSpacer_32 = QSpacerItem(20, 119, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_41.addItem(self.verticalSpacer_32, 0, 0, 1, 1)

        self.line = QFrame(self.groupBox_10)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_41.addWidget(self.line, 1, 0, 1, 1)

        self.verticalSpacer_31 = QSpacerItem(20, 119, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_41.addItem(self.verticalSpacer_31, 10, 0, 1, 1)

        self.label_17 = QLabel(self.groupBox_10)
        self.label_17.setObjectName(u"label_17")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setItalic(True)
        self.label_17.setFont(font1)

        self.gridLayout_41.addWidget(self.label_17, 8, 0, 1, 1)


        self.gridLayout_34.addWidget(self.groupBox_10, 0, 0, 1, 1)

        self.SampleID_tab.addTab(self.SampleNumber_SampleID_tab, "")
        self.GHS_SampleID_tab = QWidget()
        self.GHS_SampleID_tab.setObjectName(u"GHS_SampleID_tab")
        self.gridLayout_16 = QGridLayout(self.GHS_SampleID_tab)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.groupBox_2 = QGroupBox(self.GHS_SampleID_tab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_19 = QGridLayout(self.groupBox_2)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.gridLayout_18 = QGridLayout()
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.SampleidBack4_button = QPushButton(self.groupBox_2)
        self.SampleidBack4_button.setObjectName(u"SampleidBack4_button")
        self.SampleidBack4_button.setIcon(icon10)
        self.SampleidBack4_button.setIconSize(QSize(40, 40))
        self.SampleidBack4_button.setFlat(False)

        self.gridLayout_18.addWidget(self.SampleidBack4_button, 0, 0, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_18.addItem(self.horizontalSpacer_5, 0, 1, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_18.addItem(self.horizontalSpacer_6, 0, 2, 1, 1)

        self.SampleidForward4_button = QPushButton(self.groupBox_2)
        self.SampleidForward4_button.setObjectName(u"SampleidForward4_button")
        self.SampleidForward4_button.setIcon(icon11)
        self.SampleidForward4_button.setIconSize(QSize(40, 40))
        self.SampleidForward4_button.setFlat(False)

        self.gridLayout_18.addWidget(self.SampleidForward4_button, 0, 3, 1, 1)


        self.gridLayout_19.addLayout(self.gridLayout_18, 4, 0, 1, 1)

        self.gridLayout_17 = QGridLayout()
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.Explos_checkBox = QCheckBox(self.groupBox_2)
        self.Explos_checkBox.setObjectName(u"Explos_checkBox")
        sizePolicy1.setHeightForWidth(self.Explos_checkBox.sizePolicy().hasHeightForWidth())
        self.Explos_checkBox.setSizePolicy(sizePolicy1)
        icon12 = QIcon()
        icon12.addFile(u":/Images/hazard-explosive-icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Explos_checkBox.setIcon(icon12)
        self.Explos_checkBox.setIconSize(QSize(50, 50))

        self.gridLayout_17.addWidget(self.Explos_checkBox, 0, 0, 1, 1)

        self.Flamme_checkBox = QCheckBox(self.groupBox_2)
        self.Flamme_checkBox.setObjectName(u"Flamme_checkBox")
        sizePolicy1.setHeightForWidth(self.Flamme_checkBox.sizePolicy().hasHeightForWidth())
        self.Flamme_checkBox.setSizePolicy(sizePolicy1)
        icon13 = QIcon()
        icon13.addFile(u":/Images/hazard-flammable-icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Flamme_checkBox.setIcon(icon13)
        self.Flamme_checkBox.setIconSize(QSize(50, 50))

        self.gridLayout_17.addWidget(self.Flamme_checkBox, 0, 1, 1, 1)

        self.Rondflam_checkBox = QCheckBox(self.groupBox_2)
        self.Rondflam_checkBox.setObjectName(u"Rondflam_checkBox")
        sizePolicy1.setHeightForWidth(self.Rondflam_checkBox.sizePolicy().hasHeightForWidth())
        self.Rondflam_checkBox.setSizePolicy(sizePolicy1)
        icon14 = QIcon()
        icon14.addFile(u":/Images/hazard-oxidising-icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Rondflam_checkBox.setIcon(icon14)
        self.Rondflam_checkBox.setIconSize(QSize(50, 50))

        self.gridLayout_17.addWidget(self.Rondflam_checkBox, 0, 2, 1, 1)

        self.Acid_checkBox = QCheckBox(self.groupBox_2)
        self.Acid_checkBox.setObjectName(u"Acid_checkBox")
        sizePolicy1.setHeightForWidth(self.Acid_checkBox.sizePolicy().hasHeightForWidth())
        self.Acid_checkBox.setSizePolicy(sizePolicy1)
        icon15 = QIcon()
        icon15.addFile(u":/Images/hazard-corrosive-icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Acid_checkBox.setIcon(icon15)
        self.Acid_checkBox.setIconSize(QSize(50, 50))

        self.gridLayout_17.addWidget(self.Acid_checkBox, 1, 0, 1, 1)

        self.Skull_checkBox = QCheckBox(self.groupBox_2)
        self.Skull_checkBox.setObjectName(u"Skull_checkBox")
        sizePolicy1.setHeightForWidth(self.Skull_checkBox.sizePolicy().hasHeightForWidth())
        self.Skull_checkBox.setSizePolicy(sizePolicy1)
        icon16 = QIcon()
        icon16.addFile(u":/Images/hazard-acute-toxicity-icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Skull_checkBox.setIcon(icon16)
        self.Skull_checkBox.setIconSize(QSize(50, 50))

        self.gridLayout_17.addWidget(self.Skull_checkBox, 1, 1, 1, 1)

        self.Exclam_checkBox = QCheckBox(self.groupBox_2)
        self.Exclam_checkBox.setObjectName(u"Exclam_checkBox")
        sizePolicy1.setHeightForWidth(self.Exclam_checkBox.sizePolicy().hasHeightForWidth())
        self.Exclam_checkBox.setSizePolicy(sizePolicy1)
        icon17 = QIcon()
        icon17.addFile(u":/Images/hazard-harmful-icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Exclam_checkBox.setIcon(icon17)
        self.Exclam_checkBox.setIconSize(QSize(50, 50))

        self.gridLayout_17.addWidget(self.Exclam_checkBox, 1, 2, 1, 1)

        self.Silhouette_checkBox = QCheckBox(self.groupBox_2)
        self.Silhouette_checkBox.setObjectName(u"Silhouette_checkBox")
        sizePolicy1.setHeightForWidth(self.Silhouette_checkBox.sizePolicy().hasHeightForWidth())
        self.Silhouette_checkBox.setSizePolicy(sizePolicy1)
        icon18 = QIcon()
        icon18.addFile(u":/Images/hazard-serious-health-icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Silhouette_checkBox.setIcon(icon18)
        self.Silhouette_checkBox.setIconSize(QSize(50, 50))

        self.gridLayout_17.addWidget(self.Silhouette_checkBox, 2, 0, 1, 1)

        self.Pollu_checkBox = QCheckBox(self.groupBox_2)
        self.Pollu_checkBox.setObjectName(u"Pollu_checkBox")
        sizePolicy1.setHeightForWidth(self.Pollu_checkBox.sizePolicy().hasHeightForWidth())
        self.Pollu_checkBox.setSizePolicy(sizePolicy1)
        icon19 = QIcon()
        icon19.addFile(u":/Images/hazard-environmental-icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Pollu_checkBox.setIcon(icon19)
        self.Pollu_checkBox.setIconSize(QSize(50, 50))

        self.gridLayout_17.addWidget(self.Pollu_checkBox, 2, 1, 1, 1)


        self.gridLayout_19.addLayout(self.gridLayout_17, 2, 0, 1, 1)

        self.verticalSpacer_19 = QSpacerItem(20, 150, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_19.addItem(self.verticalSpacer_19, 3, 0, 1, 1)

        self.verticalSpacer_22 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_19.addItem(self.verticalSpacer_22, 0, 0, 1, 1)

        self.label_14 = QLabel(self.groupBox_2)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_19.addWidget(self.label_14, 1, 0, 1, 1)


        self.gridLayout_16.addWidget(self.groupBox_2, 0, 0, 1, 1)

        self.SampleID_tab.addTab(self.GHS_SampleID_tab, "")
        self.Disposal_SampleID_tab = QWidget()
        self.Disposal_SampleID_tab.setObjectName(u"Disposal_SampleID_tab")
        self.gridLayout_21 = QGridLayout(self.Disposal_SampleID_tab)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.groupBox_3 = QGroupBox(self.Disposal_SampleID_tab)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_23 = QGridLayout(self.groupBox_3)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.gridLayout_20 = QGridLayout()
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.SampleidBack5_button = QPushButton(self.groupBox_3)
        self.SampleidBack5_button.setObjectName(u"SampleidBack5_button")
        self.SampleidBack5_button.setIcon(icon10)
        self.SampleidBack5_button.setIconSize(QSize(40, 40))
        self.SampleidBack5_button.setFlat(False)

        self.gridLayout_20.addWidget(self.SampleidBack5_button, 0, 0, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_20.addItem(self.horizontalSpacer_7, 0, 1, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_20.addItem(self.horizontalSpacer_8, 0, 2, 1, 1)

        self.SampleidForward5_button = QPushButton(self.groupBox_3)
        self.SampleidForward5_button.setObjectName(u"SampleidForward5_button")
        self.SampleidForward5_button.setIcon(icon11)
        self.SampleidForward5_button.setIconSize(QSize(40, 40))
        self.SampleidForward5_button.setFlat(False)

        self.gridLayout_20.addWidget(self.SampleidForward5_button, 0, 3, 1, 1)


        self.gridLayout_23.addLayout(self.gridLayout_20, 4, 0, 1, 1)

        self.verticalSpacer_21 = QSpacerItem(20, 213, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_23.addItem(self.verticalSpacer_21, 3, 0, 1, 1)

        self.gridLayout_22 = QGridLayout()
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.NoIdea_radioButton = QRadioButton(self.groupBox_3)
        self.NoIdea_radioButton.setObjectName(u"NoIdea_radioButton")
        self.NoIdea_radioButton.setToolTipDuration(0)
        self.NoIdea_radioButton.setChecked(True)
        self.NoIdea_radioButton.setAutoExclusive(True)

        self.gridLayout_22.addWidget(self.NoIdea_radioButton, 0, 0, 1, 1)

        self.NonHarzardous_radioButton = QRadioButton(self.groupBox_3)
        self.NonHarzardous_radioButton.setObjectName(u"NonHarzardous_radioButton")
        self.NonHarzardous_radioButton.setToolTipDuration(0)
        self.NonHarzardous_radioButton.setAutoExclusive(True)

        self.gridLayout_22.addWidget(self.NonHarzardous_radioButton, 0, 1, 1, 1)

        self.ContaminatedSolids_radioButton = QRadioButton(self.groupBox_3)
        self.ContaminatedSolids_radioButton.setObjectName(u"ContaminatedSolids_radioButton")
        self.ContaminatedSolids_radioButton.setToolTipDuration(0)
        self.ContaminatedSolids_radioButton.setAutoExclusive(True)

        self.gridLayout_22.addWidget(self.ContaminatedSolids_radioButton, 0, 2, 1, 1)

        self.HalogenatedSolvents_radioButton = QRadioButton(self.groupBox_3)
        self.HalogenatedSolvents_radioButton.setObjectName(u"HalogenatedSolvents_radioButton")
        self.HalogenatedSolvents_radioButton.setToolTipDuration(0)
        self.HalogenatedSolvents_radioButton.setAutoExclusive(True)

        self.gridLayout_22.addWidget(self.HalogenatedSolvents_radioButton, 1, 0, 1, 1)

        self.HalogenFreeSolvents_radioButton = QRadioButton(self.groupBox_3)
        self.HalogenFreeSolvents_radioButton.setObjectName(u"HalogenFreeSolvents_radioButton")
        self.HalogenFreeSolvents_radioButton.setToolTipDuration(0)

        self.gridLayout_22.addWidget(self.HalogenFreeSolvents_radioButton, 1, 1, 1, 1)

        self.SpecialPrecautions_radioButton = QRadioButton(self.groupBox_3)
        self.SpecialPrecautions_radioButton.setObjectName(u"SpecialPrecautions_radioButton")
        self.SpecialPrecautions_radioButton.setToolTipDuration(0)

        self.gridLayout_22.addWidget(self.SpecialPrecautions_radioButton, 1, 2, 1, 1)


        self.gridLayout_23.addLayout(self.gridLayout_22, 2, 0, 1, 1)

        self.verticalSpacer_20 = QSpacerItem(20, 214, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_23.addItem(self.verticalSpacer_20, 0, 0, 1, 1)

        self.label_15 = QLabel(self.groupBox_3)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_23.addWidget(self.label_15, 1, 0, 1, 1)


        self.gridLayout_21.addWidget(self.groupBox_3, 0, 0, 1, 1)

        self.SampleID_tab.addTab(self.Disposal_SampleID_tab, "")
        self.AddInformation_SampleID_tab = QWidget()
        self.AddInformation_SampleID_tab.setObjectName(u"AddInformation_SampleID_tab")
        self.gridLayout_36 = QGridLayout(self.AddInformation_SampleID_tab)
        self.gridLayout_36.setObjectName(u"gridLayout_36")
        self.groupBox_11 = QGroupBox(self.AddInformation_SampleID_tab)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.gridLayout_38 = QGridLayout(self.groupBox_11)
        self.gridLayout_38.setObjectName(u"gridLayout_38")
        self.gridLayout_37 = QGridLayout()
        self.gridLayout_37.setObjectName(u"gridLayout_37")
        self.SampleidBack6_button = QPushButton(self.groupBox_11)
        self.SampleidBack6_button.setObjectName(u"SampleidBack6_button")
        self.SampleidBack6_button.setIcon(icon10)
        self.SampleidBack6_button.setIconSize(QSize(40, 40))
        self.SampleidBack6_button.setFlat(False)

        self.gridLayout_37.addWidget(self.SampleidBack6_button, 0, 0, 1, 1)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_37.addItem(self.horizontalSpacer_15, 0, 1, 1, 1)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_37.addItem(self.horizontalSpacer_16, 0, 2, 1, 1)

        self.SampleidForward6_button = QPushButton(self.groupBox_11)
        self.SampleidForward6_button.setObjectName(u"SampleidForward6_button")
        self.SampleidForward6_button.setEnabled(True)
        self.SampleidForward6_button.setIcon(icon11)
        self.SampleidForward6_button.setIconSize(QSize(40, 40))
        self.SampleidForward6_button.setFlat(False)

        self.gridLayout_37.addWidget(self.SampleidForward6_button, 0, 3, 1, 1)


        self.gridLayout_38.addLayout(self.gridLayout_37, 1, 0, 1, 1)

        self.AddInformation_tableWidget = QTableWidget(self.groupBox_11)
        if (self.AddInformation_tableWidget.columnCount() < 6):
            self.AddInformation_tableWidget.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setIcon(icon3);
        self.AddInformation_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.AddInformation_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.AddInformation_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        icon20 = QIcon()
        icon20.addFile(u":/Images/create-task-icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qtablewidgetitem3.setIcon(icon20);
        self.AddInformation_tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        icon21 = QIcon()
        icon21.addFile(u":/Images/save-all-files-icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qtablewidgetitem4.setIcon(icon21);
        self.AddInformation_tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        icon22 = QIcon()
        icon22.addFile(u":/Images/printer-icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qtablewidgetitem5.setIcon(icon22);
        self.AddInformation_tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        if (self.AddInformation_tableWidget.rowCount() < 20):
            self.AddInformation_tableWidget.setRowCount(20)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.AddInformation_tableWidget.setItem(0, 0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setCheckState(Qt.Checked);
        __qtablewidgetitem7.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.AddInformation_tableWidget.setItem(0, 3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setCheckState(Qt.Checked);
        __qtablewidgetitem8.setFlags(Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.AddInformation_tableWidget.setItem(0, 4, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setCheckState(Qt.Checked);
        __qtablewidgetitem9.setFlags(Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.AddInformation_tableWidget.setItem(0, 5, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.AddInformation_tableWidget.setItem(1, 0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setCheckState(Qt.Checked);
        __qtablewidgetitem11.setFlags(Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.AddInformation_tableWidget.setItem(1, 3, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setCheckState(Qt.Checked);
        __qtablewidgetitem12.setFlags(Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.AddInformation_tableWidget.setItem(1, 4, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setCheckState(Qt.Checked);
        __qtablewidgetitem13.setFlags(Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.AddInformation_tableWidget.setItem(1, 5, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.AddInformation_tableWidget.setItem(2, 0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setCheckState(Qt.Checked);
        __qtablewidgetitem15.setFlags(Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.AddInformation_tableWidget.setItem(2, 3, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setCheckState(Qt.Checked);
        __qtablewidgetitem16.setFlags(Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.AddInformation_tableWidget.setItem(2, 4, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setCheckState(Qt.Checked);
        __qtablewidgetitem17.setFlags(Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.AddInformation_tableWidget.setItem(2, 5, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.AddInformation_tableWidget.setItem(3, 0, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setCheckState(Qt.Checked);
        __qtablewidgetitem19.setFlags(Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.AddInformation_tableWidget.setItem(3, 3, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setCheckState(Qt.Checked);
        __qtablewidgetitem20.setFlags(Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.AddInformation_tableWidget.setItem(3, 4, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setCheckState(Qt.Checked);
        __qtablewidgetitem21.setFlags(Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.AddInformation_tableWidget.setItem(3, 5, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.AddInformation_tableWidget.setItem(4, 0, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        __qtablewidgetitem23.setCheckState(Qt.Checked);
        __qtablewidgetitem23.setFlags(Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.AddInformation_tableWidget.setItem(4, 3, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        __qtablewidgetitem24.setCheckState(Qt.Checked);
        __qtablewidgetitem24.setFlags(Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.AddInformation_tableWidget.setItem(4, 4, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        __qtablewidgetitem25.setCheckState(Qt.Checked);
        __qtablewidgetitem25.setFlags(Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.AddInformation_tableWidget.setItem(4, 5, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        __qtablewidgetitem26.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.AddInformation_tableWidget.setItem(5, 0, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        __qtablewidgetitem27.setCheckState(Qt.Checked);
        __qtablewidgetitem27.setFlags(Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.AddInformation_tableWidget.setItem(5, 3, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        __qtablewidgetitem28.setCheckState(Qt.Checked);
        __qtablewidgetitem28.setFlags(Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.AddInformation_tableWidget.setItem(5, 4, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        __qtablewidgetitem29.setCheckState(Qt.Checked);
        __qtablewidgetitem29.setFlags(Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.AddInformation_tableWidget.setItem(5, 5, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        __qtablewidgetitem30.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.AddInformation_tableWidget.setItem(6, 0, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        __qtablewidgetitem31.setCheckState(Qt.Checked);
        __qtablewidgetitem31.setFlags(Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.AddInformation_tableWidget.setItem(6, 3, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        __qtablewidgetitem32.setCheckState(Qt.Checked);
        __qtablewidgetitem32.setFlags(Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.AddInformation_tableWidget.setItem(6, 4, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        __qtablewidgetitem33.setCheckState(Qt.Checked);
        __qtablewidgetitem33.setFlags(Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.AddInformation_tableWidget.setItem(6, 5, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        __qtablewidgetitem34.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.AddInformation_tableWidget.setItem(7, 0, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        __qtablewidgetitem35.setCheckState(Qt.Checked);
        __qtablewidgetitem35.setFlags(Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.AddInformation_tableWidget.setItem(7, 3, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        __qtablewidgetitem36.setCheckState(Qt.Checked);
        __qtablewidgetitem36.setFlags(Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.AddInformation_tableWidget.setItem(7, 4, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        __qtablewidgetitem37.setCheckState(Qt.Checked);
        __qtablewidgetitem37.setFlags(Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.AddInformation_tableWidget.setItem(7, 5, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        __qtablewidgetitem38.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.AddInformation_tableWidget.setItem(8, 0, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        __qtablewidgetitem39.setCheckState(Qt.Checked);
        __qtablewidgetitem39.setFlags(Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.AddInformation_tableWidget.setItem(8, 3, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        __qtablewidgetitem40.setCheckState(Qt.Checked);
        __qtablewidgetitem40.setFlags(Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.AddInformation_tableWidget.setItem(8, 4, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        __qtablewidgetitem41.setCheckState(Qt.Checked);
        __qtablewidgetitem41.setFlags(Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.AddInformation_tableWidget.setItem(8, 5, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        __qtablewidgetitem42.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.AddInformation_tableWidget.setItem(9, 0, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        __qtablewidgetitem43.setCheckState(Qt.Checked);
        __qtablewidgetitem43.setFlags(Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.AddInformation_tableWidget.setItem(9, 3, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        __qtablewidgetitem44.setCheckState(Qt.Checked);
        __qtablewidgetitem44.setFlags(Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.AddInformation_tableWidget.setItem(9, 4, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        __qtablewidgetitem45.setCheckState(Qt.Checked);
        __qtablewidgetitem45.setFlags(Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.AddInformation_tableWidget.setItem(9, 5, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        __qtablewidgetitem46.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.AddInformation_tableWidget.setItem(10, 0, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        __qtablewidgetitem47.setCheckState(Qt.Checked);
        __qtablewidgetitem47.setFlags(Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.AddInformation_tableWidget.setItem(10, 3, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        __qtablewidgetitem48.setCheckState(Qt.Checked);
        __qtablewidgetitem48.setFlags(Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.AddInformation_tableWidget.setItem(10, 4, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        __qtablewidgetitem49.setCheckState(Qt.Checked);
        __qtablewidgetitem49.setFlags(Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.AddInformation_tableWidget.setItem(10, 5, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        __qtablewidgetitem50.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.AddInformation_tableWidget.setItem(11, 0, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        __qtablewidgetitem51.setCheckState(Qt.Checked);
        __qtablewidgetitem51.setFlags(Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.AddInformation_tableWidget.setItem(11, 3, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        __qtablewidgetitem52.setCheckState(Qt.Checked);
        __qtablewidgetitem52.setFlags(Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.AddInformation_tableWidget.setItem(11, 4, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        __qtablewidgetitem53.setCheckState(Qt.Checked);
        __qtablewidgetitem53.setFlags(Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.AddInformation_tableWidget.setItem(11, 5, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        __qtablewidgetitem54.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.AddInformation_tableWidget.setItem(12, 0, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        __qtablewidgetitem55.setCheckState(Qt.Checked);
        __qtablewidgetitem55.setFlags(Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.AddInformation_tableWidget.setItem(12, 3, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        __qtablewidgetitem56.setCheckState(Qt.Checked);
        __qtablewidgetitem56.setFlags(Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.AddInformation_tableWidget.setItem(12, 4, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        __qtablewidgetitem57.setCheckState(Qt.Checked);
        __qtablewidgetitem57.setFlags(Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.AddInformation_tableWidget.setItem(12, 5, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        __qtablewidgetitem58.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.AddInformation_tableWidget.setItem(13, 0, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        __qtablewidgetitem59.setCheckState(Qt.Checked);
        __qtablewidgetitem59.setFlags(Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.AddInformation_tableWidget.setItem(13, 3, __qtablewidgetitem59)
        __qtablewidgetitem60 = QTableWidgetItem()
        __qtablewidgetitem60.setCheckState(Qt.Checked);
        __qtablewidgetitem60.setFlags(Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.AddInformation_tableWidget.setItem(13, 4, __qtablewidgetitem60)
        __qtablewidgetitem61 = QTableWidgetItem()
        __qtablewidgetitem61.setCheckState(Qt.Checked);
        __qtablewidgetitem61.setFlags(Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.AddInformation_tableWidget.setItem(13, 5, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        __qtablewidgetitem62.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.AddInformation_tableWidget.setItem(14, 0, __qtablewidgetitem62)
        __qtablewidgetitem63 = QTableWidgetItem()
        __qtablewidgetitem63.setCheckState(Qt.Checked);
        __qtablewidgetitem63.setFlags(Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.AddInformation_tableWidget.setItem(14, 3, __qtablewidgetitem63)
        __qtablewidgetitem64 = QTableWidgetItem()
        __qtablewidgetitem64.setCheckState(Qt.Checked);
        __qtablewidgetitem64.setFlags(Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.AddInformation_tableWidget.setItem(14, 4, __qtablewidgetitem64)
        __qtablewidgetitem65 = QTableWidgetItem()
        __qtablewidgetitem65.setCheckState(Qt.Checked);
        __qtablewidgetitem65.setFlags(Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.AddInformation_tableWidget.setItem(14, 5, __qtablewidgetitem65)
        __qtablewidgetitem66 = QTableWidgetItem()
        __qtablewidgetitem66.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.AddInformation_tableWidget.setItem(15, 0, __qtablewidgetitem66)
        __qtablewidgetitem67 = QTableWidgetItem()
        __qtablewidgetitem67.setCheckState(Qt.Checked);
        __qtablewidgetitem67.setFlags(Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.AddInformation_tableWidget.setItem(15, 3, __qtablewidgetitem67)
        __qtablewidgetitem68 = QTableWidgetItem()
        __qtablewidgetitem68.setCheckState(Qt.Checked);
        __qtablewidgetitem68.setFlags(Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.AddInformation_tableWidget.setItem(15, 4, __qtablewidgetitem68)
        __qtablewidgetitem69 = QTableWidgetItem()
        __qtablewidgetitem69.setCheckState(Qt.Checked);
        __qtablewidgetitem69.setFlags(Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.AddInformation_tableWidget.setItem(15, 5, __qtablewidgetitem69)
        __qtablewidgetitem70 = QTableWidgetItem()
        __qtablewidgetitem70.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.AddInformation_tableWidget.setItem(16, 0, __qtablewidgetitem70)
        __qtablewidgetitem71 = QTableWidgetItem()
        __qtablewidgetitem71.setCheckState(Qt.Checked);
        __qtablewidgetitem71.setFlags(Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.AddInformation_tableWidget.setItem(16, 3, __qtablewidgetitem71)
        __qtablewidgetitem72 = QTableWidgetItem()
        __qtablewidgetitem72.setCheckState(Qt.Checked);
        __qtablewidgetitem72.setFlags(Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.AddInformation_tableWidget.setItem(16, 4, __qtablewidgetitem72)
        __qtablewidgetitem73 = QTableWidgetItem()
        __qtablewidgetitem73.setCheckState(Qt.Checked);
        __qtablewidgetitem73.setFlags(Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.AddInformation_tableWidget.setItem(16, 5, __qtablewidgetitem73)
        __qtablewidgetitem74 = QTableWidgetItem()
        __qtablewidgetitem74.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.AddInformation_tableWidget.setItem(17, 0, __qtablewidgetitem74)
        __qtablewidgetitem75 = QTableWidgetItem()
        __qtablewidgetitem75.setCheckState(Qt.Checked);
        __qtablewidgetitem75.setFlags(Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.AddInformation_tableWidget.setItem(17, 3, __qtablewidgetitem75)
        __qtablewidgetitem76 = QTableWidgetItem()
        __qtablewidgetitem76.setCheckState(Qt.Checked);
        __qtablewidgetitem76.setFlags(Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.AddInformation_tableWidget.setItem(17, 4, __qtablewidgetitem76)
        __qtablewidgetitem77 = QTableWidgetItem()
        __qtablewidgetitem77.setCheckState(Qt.Checked);
        __qtablewidgetitem77.setFlags(Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.AddInformation_tableWidget.setItem(17, 5, __qtablewidgetitem77)
        __qtablewidgetitem78 = QTableWidgetItem()
        __qtablewidgetitem78.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.AddInformation_tableWidget.setItem(18, 0, __qtablewidgetitem78)
        __qtablewidgetitem79 = QTableWidgetItem()
        __qtablewidgetitem79.setCheckState(Qt.Checked);
        __qtablewidgetitem79.setFlags(Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.AddInformation_tableWidget.setItem(18, 3, __qtablewidgetitem79)
        __qtablewidgetitem80 = QTableWidgetItem()
        __qtablewidgetitem80.setCheckState(Qt.Checked);
        __qtablewidgetitem80.setFlags(Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.AddInformation_tableWidget.setItem(18, 4, __qtablewidgetitem80)
        __qtablewidgetitem81 = QTableWidgetItem()
        __qtablewidgetitem81.setCheckState(Qt.Checked);
        __qtablewidgetitem81.setFlags(Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.AddInformation_tableWidget.setItem(18, 5, __qtablewidgetitem81)
        __qtablewidgetitem82 = QTableWidgetItem()
        __qtablewidgetitem82.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.AddInformation_tableWidget.setItem(19, 0, __qtablewidgetitem82)
        __qtablewidgetitem83 = QTableWidgetItem()
        __qtablewidgetitem83.setCheckState(Qt.Checked);
        __qtablewidgetitem83.setFlags(Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.AddInformation_tableWidget.setItem(19, 3, __qtablewidgetitem83)
        __qtablewidgetitem84 = QTableWidgetItem()
        __qtablewidgetitem84.setCheckState(Qt.Checked);
        __qtablewidgetitem84.setFlags(Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.AddInformation_tableWidget.setItem(19, 4, __qtablewidgetitem84)
        __qtablewidgetitem85 = QTableWidgetItem()
        __qtablewidgetitem85.setCheckState(Qt.Checked);
        __qtablewidgetitem85.setFlags(Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.AddInformation_tableWidget.setItem(19, 5, __qtablewidgetitem85)
        self.AddInformation_tableWidget.setObjectName(u"AddInformation_tableWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.AddInformation_tableWidget.sizePolicy().hasHeightForWidth())
        self.AddInformation_tableWidget.setSizePolicy(sizePolicy2)
        self.AddInformation_tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.AddInformation_tableWidget.setShowGrid(True)
        self.AddInformation_tableWidget.setRowCount(20)
        self.AddInformation_tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.AddInformation_tableWidget.horizontalHeader().setDefaultSectionSize(135)

        self.gridLayout_38.addWidget(self.AddInformation_tableWidget, 0, 0, 1, 1)


        self.gridLayout_36.addWidget(self.groupBox_11, 0, 0, 1, 1)

        self.SampleID_tab.addTab(self.AddInformation_SampleID_tab, "")
        self.ElabFTW_SampleID_tab = QWidget()
        self.ElabFTW_SampleID_tab.setObjectName(u"ElabFTW_SampleID_tab")
        self.gridLayout_30 = QGridLayout(self.ElabFTW_SampleID_tab)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.groupBox_8 = QGroupBox(self.ElabFTW_SampleID_tab)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.gridLayout_32 = QGridLayout(self.groupBox_8)
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.groupBox_4 = QGroupBox(self.groupBox_8)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_25 = QGridLayout(self.groupBox_4)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.ElabFTW_button = QPushButton(self.groupBox_4)
        self.ElabFTW_button.setObjectName(u"ElabFTW_button")
        sizePolicy1.setHeightForWidth(self.ElabFTW_button.sizePolicy().hasHeightForWidth())
        self.ElabFTW_button.setSizePolicy(sizePolicy1)
        self.ElabFTW_button.setMinimumSize(QSize(0, 0))
        self.ElabFTW_button.setMaximumSize(QSize(2700000, 300000))
        self.ElabFTW_button.setFont(font)
        self.ElabFTW_button.setLayoutDirection(Qt.LeftToRight)
        self.ElabFTW_button.setAutoFillBackground(False)
        self.ElabFTW_button.setIcon(icon20)
        self.ElabFTW_button.setIconSize(QSize(75, 75))

        self.gridLayout_25.addWidget(self.ElabFTW_button, 0, 0, 1, 1)


        self.gridLayout_32.addWidget(self.groupBox_4, 0, 0, 1, 1)

        self.groupBox_5 = QGroupBox(self.groupBox_8)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.gridLayout_26 = QGridLayout(self.groupBox_5)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.Foldersave_button = QToolButton(self.groupBox_5)
        self.Foldersave_button.setObjectName(u"Foldersave_button")
        sizePolicy1.setHeightForWidth(self.Foldersave_button.sizePolicy().hasHeightForWidth())
        self.Foldersave_button.setSizePolicy(sizePolicy1)
        self.Foldersave_button.setMinimumSize(QSize(0, 0))
        self.Foldersave_button.setMaximumSize(QSize(2900, 2900))
        icon23 = QIcon()
        icon23.addFile(u":/Images/open-folder-outline-icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Foldersave_button.setIcon(icon23)
        self.Foldersave_button.setIconSize(QSize(75, 75))

        self.gridLayout_26.addWidget(self.Foldersave_button, 0, 0, 1, 1)

        self.Save_button = QPushButton(self.groupBox_5)
        self.Save_button.setObjectName(u"Save_button")
        sizePolicy1.setHeightForWidth(self.Save_button.sizePolicy().hasHeightForWidth())
        self.Save_button.setSizePolicy(sizePolicy1)
        self.Save_button.setMinimumSize(QSize(0, 0))
        self.Save_button.setMaximumSize(QSize(2400000, 5000000))
        self.Save_button.setFont(font)
        self.Save_button.setIcon(icon21)
        self.Save_button.setIconSize(QSize(75, 75))

        self.gridLayout_26.addWidget(self.Save_button, 0, 1, 1, 1)


        self.gridLayout_32.addWidget(self.groupBox_5, 0, 1, 1, 1)

        self.verticalSpacer_29 = QSpacerItem(20, 125, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_32.addItem(self.verticalSpacer_29, 1, 0, 1, 1)

        self.verticalSpacer_30 = QSpacerItem(20, 125, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_32.addItem(self.verticalSpacer_30, 1, 1, 1, 1)

        self.groupBox_6 = QGroupBox(self.groupBox_8)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.gridLayout_27 = QGridLayout(self.groupBox_6)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.PrintLayout_comboBox = QComboBox(self.groupBox_6)
        icon24 = QIcon()
        icon24.addFile(u":/Images/qr-code-icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.PrintLayout_comboBox.addItem(icon24, "")
        self.PrintLayout_comboBox.addItem(icon24, "")
        self.PrintLayout_comboBox.addItem(icon24, "")
        self.PrintLayout_comboBox.addItem(icon24, "")
        self.PrintLayout_comboBox.setObjectName(u"PrintLayout_comboBox")
        sizePolicy1.setHeightForWidth(self.PrintLayout_comboBox.sizePolicy().hasHeightForWidth())
        self.PrintLayout_comboBox.setSizePolicy(sizePolicy1)
        self.PrintLayout_comboBox.setMinimumSize(QSize(0, 0))
        self.PrintLayout_comboBox.setMaximumSize(QSize(250000, 31000))
        self.PrintLayout_comboBox.setFont(font)
        self.PrintLayout_comboBox.setLayoutDirection(Qt.LeftToRight)
        self.PrintLayout_comboBox.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.PrintLayout_comboBox.setIconSize(QSize(50, 50))

        self.gridLayout_27.addWidget(self.PrintLayout_comboBox, 0, 0, 1, 1)

        self.Print_button = QPushButton(self.groupBox_6)
        self.Print_button.setObjectName(u"Print_button")
        sizePolicy1.setHeightForWidth(self.Print_button.sizePolicy().hasHeightForWidth())
        self.Print_button.setSizePolicy(sizePolicy1)
        self.Print_button.setIcon(icon22)
        self.Print_button.setIconSize(QSize(75, 75))

        self.gridLayout_27.addWidget(self.Print_button, 0, 1, 1, 1)


        self.gridLayout_32.addWidget(self.groupBox_6, 2, 0, 1, 1)

        self.groupBox_7 = QGroupBox(self.groupBox_8)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.gridLayout_29 = QGridLayout(self.groupBox_7)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.ElabFTWOutput1_label = QLabel(self.groupBox_7)
        self.ElabFTWOutput1_label.setObjectName(u"ElabFTWOutput1_label")

        self.gridLayout_29.addWidget(self.ElabFTWOutput1_label, 0, 0, 1, 1)

        self.ElabFTWOutput2_label = QLabel(self.groupBox_7)
        self.ElabFTWOutput2_label.setObjectName(u"ElabFTWOutput2_label")

        self.gridLayout_29.addWidget(self.ElabFTWOutput2_label, 0, 1, 1, 1)


        self.gridLayout_32.addWidget(self.groupBox_7, 2, 1, 1, 1)

        self.verticalSpacer_28 = QSpacerItem(20, 124, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_32.addItem(self.verticalSpacer_28, 3, 0, 1, 1)

        self.verticalSpacer_27 = QSpacerItem(20, 124, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_32.addItem(self.verticalSpacer_27, 3, 1, 1, 1)

        self.gridLayout_24 = QGridLayout()
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.SampleidBack7_button = QPushButton(self.groupBox_8)
        self.SampleidBack7_button.setObjectName(u"SampleidBack7_button")
        self.SampleidBack7_button.setIcon(icon10)
        self.SampleidBack7_button.setIconSize(QSize(40, 40))
        self.SampleidBack7_button.setFlat(False)

        self.gridLayout_24.addWidget(self.SampleidBack7_button, 0, 0, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_24.addItem(self.horizontalSpacer_9, 0, 1, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_24.addItem(self.horizontalSpacer_10, 0, 2, 1, 1)

        self.SampleidForward7_button = QPushButton(self.groupBox_8)
        self.SampleidForward7_button.setObjectName(u"SampleidForward7_button")
        self.SampleidForward7_button.setEnabled(True)
        self.SampleidForward7_button.setIcon(icon11)
        self.SampleidForward7_button.setIconSize(QSize(40, 40))
        self.SampleidForward7_button.setFlat(False)

        self.gridLayout_24.addWidget(self.SampleidForward7_button, 0, 3, 1, 1)


        self.gridLayout_32.addLayout(self.gridLayout_24, 4, 0, 1, 2)


        self.gridLayout_30.addWidget(self.groupBox_8, 0, 0, 1, 1)

        self.SampleID_tab.addTab(self.ElabFTW_SampleID_tab, "")
        self.Finish_SampleID_tab = QWidget()
        self.Finish_SampleID_tab.setObjectName(u"Finish_SampleID_tab")
        self.gridLayout_31 = QGridLayout(self.Finish_SampleID_tab)
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.groupBox_9 = QGroupBox(self.Finish_SampleID_tab)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.gridLayout_33 = QGridLayout(self.groupBox_9)
        self.gridLayout_33.setObjectName(u"gridLayout_33")
        self.verticalSpacer_25 = QSpacerItem(20, 197, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_33.addItem(self.verticalSpacer_25, 0, 0, 1, 1)

        self.Reset_button = QPushButton(self.groupBox_9)
        self.Reset_button.setObjectName(u"Reset_button")
        icon25 = QIcon()
        icon25.addFile(u":/Images/restart-computer-icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Reset_button.setIcon(icon25)
        self.Reset_button.setIconSize(QSize(75, 75))

        self.gridLayout_33.addWidget(self.Reset_button, 1, 0, 1, 1)

        self.verticalSpacer_26 = QSpacerItem(20, 197, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_33.addItem(self.verticalSpacer_26, 2, 0, 1, 1)

        self.gridLayout_28 = QGridLayout()
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.SampleidBack8_button = QPushButton(self.groupBox_9)
        self.SampleidBack8_button.setObjectName(u"SampleidBack8_button")
        self.SampleidBack8_button.setIcon(icon10)
        self.SampleidBack8_button.setIconSize(QSize(40, 40))
        self.SampleidBack8_button.setFlat(False)

        self.gridLayout_28.addWidget(self.SampleidBack8_button, 0, 0, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_28.addItem(self.horizontalSpacer_12, 0, 1, 1, 1)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_28.addItem(self.horizontalSpacer_13, 0, 2, 1, 1)

        self.SampleidForward8_button = QPushButton(self.groupBox_9)
        self.SampleidForward8_button.setObjectName(u"SampleidForward8_button")
        self.SampleidForward8_button.setEnabled(False)
        self.SampleidForward8_button.setIcon(icon11)
        self.SampleidForward8_button.setIconSize(QSize(40, 40))
        self.SampleidForward8_button.setFlat(False)

        self.gridLayout_28.addWidget(self.SampleidForward8_button, 0, 3, 1, 1)


        self.gridLayout_33.addLayout(self.gridLayout_28, 3, 0, 1, 1)


        self.gridLayout_31.addWidget(self.groupBox_9, 0, 0, 1, 1)

        self.SampleID_tab.addTab(self.Finish_SampleID_tab, "")

        self.gridLayout_8.addWidget(self.SampleID_tab, 0, 0, 1, 1)

        icon26 = QIcon()
        icon26.addFile(u":/Images/pencil-square-outline-icon_90.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Main_tab.addTab(self.Create_Main_tab, icon26, "")
        self.Search_Main_tab = QWidget()
        self.Search_Main_tab.setObjectName(u"Search_Main_tab")
        self.gridLayout_43 = QGridLayout(self.Search_Main_tab)
        self.gridLayout_43.setObjectName(u"gridLayout_43")
        self.groupBox_12 = QGroupBox(self.Search_Main_tab)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.groupBox_12.setFont(font)
        self.gridLayout_44 = QGridLayout(self.groupBox_12)
        self.gridLayout_44.setObjectName(u"gridLayout_44")
        self.SearchID_textBrowser = QTextBrowser(self.groupBox_12)
        self.SearchID_textBrowser.setObjectName(u"SearchID_textBrowser")

        self.gridLayout_44.addWidget(self.SearchID_textBrowser, 1, 0, 1, 2)

        self.SearchID_lineEdit = QLineEdit(self.groupBox_12)
        self.SearchID_lineEdit.setObjectName(u"SearchID_lineEdit")
        self.SearchID_lineEdit.setClearButtonEnabled(True)

        self.gridLayout_44.addWidget(self.SearchID_lineEdit, 0, 0, 1, 1)

        self.SearchID_pushButton = QPushButton(self.groupBox_12)
        self.SearchID_pushButton.setObjectName(u"SearchID_pushButton")
        self.SearchID_pushButton.setIcon(icon3)
        self.SearchID_pushButton.setIconSize(QSize(75, 75))

        self.gridLayout_44.addWidget(self.SearchID_pushButton, 0, 1, 1, 1)


        self.gridLayout_43.addWidget(self.groupBox_12, 0, 0, 1, 1)

        icon27 = QIcon()
        icon27.addFile(u":/Images/book-research-icon_90.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Main_tab.addTab(self.Search_Main_tab, icon27, "")
        self.Scan_Main_tab = QWidget()
        self.Scan_Main_tab.setObjectName(u"Scan_Main_tab")
        self.gridLayout_45 = QGridLayout(self.Scan_Main_tab)
        self.gridLayout_45.setObjectName(u"gridLayout_45")
        self.groupBox_13 = QGroupBox(self.Scan_Main_tab)
        self.groupBox_13.setObjectName(u"groupBox_13")
        self.gridLayout_46 = QGridLayout(self.groupBox_13)
        self.gridLayout_46.setObjectName(u"gridLayout_46")
        self.ScanQR_button = QPushButton(self.groupBox_13)
        self.ScanQR_button.setObjectName(u"ScanQR_button")
        self.ScanQR_button.setIcon(icon1)
        self.ScanQR_button.setIconSize(QSize(75, 75))

        self.gridLayout_46.addWidget(self.ScanQR_button, 0, 0, 1, 1)

        self.ShowQR_button = QPushButton(self.groupBox_13)
        self.ShowQR_button.setObjectName(u"ShowQR_button")
        icon28 = QIcon()
        icon28.addFile(u":/Images/view-show-all-icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.ShowQR_button.setIcon(icon28)
        self.ShowQR_button.setIconSize(QSize(75, 75))

        self.gridLayout_46.addWidget(self.ShowQR_button, 0, 1, 1, 1)

        self.ScanToCreate_button = QPushButton(self.groupBox_13)
        self.ScanToCreate_button.setObjectName(u"ScanToCreate_button")
        self.ScanToCreate_button.setIcon(icon20)
        self.ScanToCreate_button.setIconSize(QSize(75, 75))

        self.gridLayout_46.addWidget(self.ScanToCreate_button, 0, 2, 1, 1)

        self.label_7 = QLabel(self.groupBox_13)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout_46.addWidget(self.label_7, 1, 0, 1, 1)

        self.label_13 = QLabel(self.groupBox_13)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.gridLayout_46.addWidget(self.label_13, 1, 1, 1, 1)

        self.label_16 = QLabel(self.groupBox_13)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignCenter)

        self.gridLayout_46.addWidget(self.label_16, 1, 2, 1, 1)

        self.ScanResult_textBrowser = QTextBrowser(self.groupBox_13)
        self.ScanResult_textBrowser.setObjectName(u"ScanResult_textBrowser")

        self.gridLayout_46.addWidget(self.ScanResult_textBrowser, 2, 0, 1, 3)


        self.gridLayout_45.addWidget(self.groupBox_13, 0, 0, 1, 1)

        icon29 = QIcon()
        icon29.addFile(u":/Images/qr-code-scan-icon_90.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Main_tab.addTab(self.Scan_Main_tab, icon29, "")
        self.Log_Main_tab = QWidget()
        self.Log_Main_tab.setObjectName(u"Log_Main_tab")
        self.gridLayout_7 = QGridLayout(self.Log_Main_tab)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.LogGroupBox = QGroupBox(self.Log_Main_tab)
        self.LogGroupBox.setObjectName(u"LogGroupBox")
        self.gridLayout_6 = QGridLayout(self.LogGroupBox)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.Log_textBrowser = QTextBrowser(self.LogGroupBox)
        self.Log_textBrowser.setObjectName(u"Log_textBrowser")
        self.Log_textBrowser.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        self.gridLayout_6.addWidget(self.Log_textBrowser, 0, 0, 1, 1)


        self.gridLayout_7.addWidget(self.LogGroupBox, 0, 0, 1, 1)

        icon30 = QIcon()
        icon30.addFile(u":/Images/wood-icon_90.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Main_tab.addTab(self.Log_Main_tab, icon30, "")
        self.About_Main_tab = QWidget()
        self.About_Main_tab.setObjectName(u"About_Main_tab")
        self.gridLayout_42 = QGridLayout(self.About_Main_tab)
        self.gridLayout_42.setObjectName(u"gridLayout_42")
        self.About_label = QLabel(self.About_Main_tab)
        self.About_label.setObjectName(u"About_label")
        font2 = QFont()
        font2.setPointSize(13)
        self.About_label.setFont(font2)
        self.About_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_42.addWidget(self.About_label, 0, 0, 1, 1)

        icon31 = QIcon()
        icon31.addFile(u":/Images/info-information-icon_90.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Main_tab.addTab(self.About_Main_tab, icon31, "")
        self.Chemical_Main_tab = QWidget()
        self.Chemical_Main_tab.setObjectName(u"Chemical_Main_tab")
        self.gridLayout_47 = QGridLayout(self.Chemical_Main_tab)
        self.gridLayout_47.setObjectName(u"gridLayout_47")
        self.AddChemical_tab = QTabWidget(self.Chemical_Main_tab)
        self.AddChemical_tab.setObjectName(u"AddChemical_tab")
        self.AddChemical_tab.setTabPosition(QTabWidget.West)
        self.AddChemical_widget = QWidget()
        self.AddChemical_widget.setObjectName(u"AddChemical_widget")
        self.gridLayout_48 = QGridLayout(self.AddChemical_widget)
        self.gridLayout_48.setObjectName(u"gridLayout_48")
        self.groupBox_14 = QGroupBox(self.AddChemical_widget)
        self.groupBox_14.setObjectName(u"groupBox_14")
        self.gridLayout_52 = QGridLayout(self.groupBox_14)
        self.gridLayout_52.setObjectName(u"gridLayout_52")
        self.gridLayout_51 = QGridLayout()
        self.gridLayout_51.setObjectName(u"gridLayout_51")
        self.groupBox_16 = QGroupBox(self.groupBox_14)
        self.groupBox_16.setObjectName(u"groupBox_16")
        self.gridLayout_56 = QGridLayout(self.groupBox_16)
        self.gridLayout_56.setObjectName(u"gridLayout_56")
        self.AddChemical_fromID_button = QPushButton(self.groupBox_16)
        self.AddChemical_fromID_button.setObjectName(u"AddChemical_fromID_button")

        self.gridLayout_56.addWidget(self.AddChemical_fromID_button, 1, 0, 1, 1)

        self.gridLayout_55 = QGridLayout()
        self.gridLayout_55.setObjectName(u"gridLayout_55")
        self.PubChem_lineedit = QLineEdit(self.groupBox_16)
        self.PubChem_lineedit.setObjectName(u"PubChem_lineedit")

        self.gridLayout_55.addWidget(self.PubChem_lineedit, 0, 1, 1, 1)

        self.CAS_lineedit = QLineEdit(self.groupBox_16)
        self.CAS_lineedit.setObjectName(u"CAS_lineedit")
        self.CAS_lineedit.setEnabled(False)

        self.gridLayout_55.addWidget(self.CAS_lineedit, 1, 1, 1, 1)

        self.label_18 = QLabel(self.groupBox_16)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_55.addWidget(self.label_18, 0, 0, 1, 1)

        self.InChIKey_lineedit = QLineEdit(self.groupBox_16)
        self.InChIKey_lineedit.setObjectName(u"InChIKey_lineedit")
        self.InChIKey_lineedit.setEnabled(False)

        self.gridLayout_55.addWidget(self.InChIKey_lineedit, 2, 1, 1, 1)

        self.label_19 = QLabel(self.groupBox_16)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_55.addWidget(self.label_19, 1, 0, 1, 1)

        self.label_21 = QLabel(self.groupBox_16)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_55.addWidget(self.label_21, 2, 0, 1, 1)


        self.gridLayout_56.addLayout(self.gridLayout_55, 0, 0, 1, 1)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_56.addItem(self.verticalSpacer_12, 2, 0, 1, 1)


        self.gridLayout_51.addWidget(self.groupBox_16, 0, 0, 3, 1)

        self.line_6 = QFrame(self.groupBox_14)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.VLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.gridLayout_51.addWidget(self.line_6, 0, 1, 3, 1)

        self.groupBox_17 = QGroupBox(self.groupBox_14)
        self.groupBox_17.setObjectName(u"groupBox_17")
        self.gridLayout_53 = QGridLayout(self.groupBox_17)
        self.gridLayout_53.setObjectName(u"gridLayout_53")
        self.ChemicalAdd_CreateNew_button = QPushButton(self.groupBox_17)
        self.ChemicalAdd_CreateNew_button.setObjectName(u"ChemicalAdd_CreateNew_button")

        self.gridLayout_53.addWidget(self.ChemicalAdd_CreateNew_button, 0, 0, 1, 1)


        self.gridLayout_51.addWidget(self.groupBox_17, 0, 2, 1, 1)

        self.line_5 = QFrame(self.groupBox_14)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.gridLayout_51.addWidget(self.line_5, 1, 2, 1, 1)

        self.groupBox_18 = QGroupBox(self.groupBox_14)
        self.groupBox_18.setObjectName(u"groupBox_18")
        self.gridLayout_54 = QGridLayout(self.groupBox_18)
        self.gridLayout_54.setObjectName(u"gridLayout_54")
        self.ChemicalAdd_CreatefromOld_button = QPushButton(self.groupBox_18)
        self.ChemicalAdd_CreatefromOld_button.setObjectName(u"ChemicalAdd_CreatefromOld_button")

        self.gridLayout_54.addWidget(self.ChemicalAdd_CreatefromOld_button, 0, 0, 1, 1)


        self.gridLayout_51.addWidget(self.groupBox_18, 2, 2, 1, 1)


        self.gridLayout_52.addLayout(self.gridLayout_51, 0, 0, 1, 1)


        self.gridLayout_48.addWidget(self.groupBox_14, 0, 0, 1, 1)

        self.AddChemical_tab.addTab(self.AddChemical_widget, "")
        self.SelectChemical_tab = QWidget()
        self.SelectChemical_tab.setObjectName(u"SelectChemical_tab")
        self.gridLayout_49 = QGridLayout(self.SelectChemical_tab)
        self.gridLayout_49.setObjectName(u"gridLayout_49")
        self.groupBox_15 = QGroupBox(self.SelectChemical_tab)
        self.groupBox_15.setObjectName(u"groupBox_15")
        self.gridLayout_50 = QGridLayout(self.groupBox_15)
        self.gridLayout_50.setObjectName(u"gridLayout_50")
        self.SearchChemicals_tableWidget = QTableWidget(self.groupBox_15)
        self.SearchChemicals_tableWidget.setObjectName(u"SearchChemicals_tableWidget")

        self.gridLayout_50.addWidget(self.SearchChemicals_tableWidget, 0, 0, 1, 1)


        self.gridLayout_49.addWidget(self.groupBox_15, 0, 0, 1, 1)

        self.AddChemical_tab.addTab(self.SelectChemical_tab, "")
        self.ChemicalToElab_tab = QWidget()
        self.ChemicalToElab_tab.setObjectName(u"ChemicalToElab_tab")
        self.gridLayout_62 = QGridLayout(self.ChemicalToElab_tab)
        self.gridLayout_62.setObjectName(u"gridLayout_62")
        self.toolBox = QToolBox(self.ChemicalToElab_tab)
        self.toolBox.setObjectName(u"toolBox")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 711, 401))
        self.gridLayout_58 = QGridLayout(self.page)
        self.gridLayout_58.setObjectName(u"gridLayout_58")
        self.Addchemical_current_scrollarea = QScrollArea(self.page)
        self.Addchemical_current_scrollarea.setObjectName(u"Addchemical_current_scrollarea")
        self.Addchemical_current_scrollarea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 691, 381))
        self.Addchemical_current_scrollarea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_58.addWidget(self.Addchemical_current_scrollarea, 0, 0, 1, 1)

        self.toolBox.addItem(self.page, u"Current Status")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 711, 401))
        self.gridLayout_59 = QGridLayout(self.page_2)
        self.gridLayout_59.setObjectName(u"gridLayout_59")
        self.Addchemical_supplier_scrollarea = QScrollArea(self.page_2)
        self.Addchemical_supplier_scrollarea.setObjectName(u"Addchemical_supplier_scrollarea")
        self.Addchemical_supplier_scrollarea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 691, 381))
        self.Addchemical_supplier_scrollarea.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout_59.addWidget(self.Addchemical_supplier_scrollarea, 0, 0, 1, 1)

        self.toolBox.addItem(self.page_2, u"Supplier and Ordering Details")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_61 = QGridLayout(self.page_3)
        self.gridLayout_61.setObjectName(u"gridLayout_61")
        self.Addchemical_datasheet_scrollarea = QScrollArea(self.page_3)
        self.Addchemical_datasheet_scrollarea.setObjectName(u"Addchemical_datasheet_scrollarea")
        self.Addchemical_datasheet_scrollarea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 691, 381))
        self.Addchemical_datasheet_scrollarea.setWidget(self.scrollAreaWidgetContents_3)

        self.gridLayout_61.addWidget(self.Addchemical_datasheet_scrollarea, 0, 0, 1, 1)

        self.toolBox.addItem(self.page_3, u"Chemical Datasheet")
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.gridLayout_57 = QGridLayout(self.page_4)
        self.gridLayout_57.setObjectName(u"gridLayout_57")
        self.Addchemical_hpstatements_scrollarea = QScrollArea(self.page_4)
        self.Addchemical_hpstatements_scrollarea.setObjectName(u"Addchemical_hpstatements_scrollarea")
        self.Addchemical_hpstatements_scrollarea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 736, 398))
        self.Addchemical_hpstatements_scrollarea.setWidget(self.scrollAreaWidgetContents_4)

        self.gridLayout_57.addWidget(self.Addchemical_hpstatements_scrollarea, 0, 0, 1, 1)

        self.toolBox.addItem(self.page_4, u"Hazard and Precautionary Statements")

        self.gridLayout_62.addWidget(self.toolBox, 0, 0, 1, 1)

        self.groupBox_22 = QGroupBox(self.ChemicalToElab_tab)
        self.groupBox_22.setObjectName(u"groupBox_22")
        self.gridLayout_60 = QGridLayout(self.groupBox_22)
        self.gridLayout_60.setObjectName(u"gridLayout_60")
        self.AddChemicalToElab_button = QPushButton(self.groupBox_22)
        self.AddChemicalToElab_button.setObjectName(u"AddChemicalToElab_button")
        self.AddChemicalToElab_button.setIcon(icon20)
        self.AddChemicalToElab_button.setIconSize(QSize(75, 75))

        self.gridLayout_60.addWidget(self.AddChemicalToElab_button, 0, 0, 1, 1)

        self.AddChemicalResponse_label = QLabel(self.groupBox_22)
        self.AddChemicalResponse_label.setObjectName(u"AddChemicalResponse_label")

        self.gridLayout_60.addWidget(self.AddChemicalResponse_label, 1, 0, 1, 1)


        self.gridLayout_62.addWidget(self.groupBox_22, 1, 0, 1, 1)

        self.AddChemical_tab.addTab(self.ChemicalToElab_tab, "")

        self.gridLayout_47.addWidget(self.AddChemical_tab, 0, 0, 1, 1)

        self.Main_tab.addTab(self.Chemical_Main_tab, icon5, "")

        self.gridLayout.addWidget(self.Main_tab, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 914, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.Main_tab.setCurrentIndex(6)
        self.Home_tab.setCurrentIndex(1)
        self.HomeCreate_button.setDefault(False)
        self.SampleID_tab.setCurrentIndex(6)
        self.AddChemical_tab.setCurrentIndex(2)
        self.toolBox.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"CeramScan", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Scan a QR-code", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Create a SampleID", None))
        self.HomeScan_button.setText("")
        self.HomeCreate_button.setText("")
        self.HomeSearch_button.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Search a SampleID/UserID", None))
        self.Home_tab.setTabText(self.Home_tab.indexOf(self.Home_Home_tab), QCoreApplication.translate("MainWindow", u"Home", None))
        self.HomeAddEquipment_button.setText("")
        self.HomeAddChemical_button.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Show the log", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Add Chemical", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Add Equipment (admin only)", None))
        self.HomeAbout_button.setText("")
        self.HomeLog_button.setText("")
        self.Home_tab.setTabText(self.Home_tab.indexOf(self.Advanced_Home_tab), QCoreApplication.translate("MainWindow", u"Advanced", None))
        self.Main_tab.setTabText(self.Main_tab.indexOf(self.Home_Main_tab), "")
        self.DecryptgroupBox.setTitle(QCoreApplication.translate("MainWindow", u"SampleID / UserID decryption (optional)", None))
        self.DecryptLabel.setText(QCoreApplication.translate("MainWindow", u"(Optional) Enter a UserID or a SampleID to autofil some of the next sections.", None))
        self.Decrypt_lineEdit.setText("")
        self.Decrypt_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"UserID or SampleID", None))
        self.Decrypt_button.setText("")
        self.DecryptResponse_label.setText("")
        self.SampleidBack1_button.setText("")
        self.SampleidForward1_button.setText("")
        self.SampleID_tab.setTabText(self.SampleID_tab.indexOf(self.IDdecryption_SampleID_tab), QCoreApplication.translate("MainWindow", u"ID decryption", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Mandatory information", None))
        self.FirstNameLabel.setText(QCoreApplication.translate("MainWindow", u"First name:", None))
        self.LastNameLabel.setText(QCoreApplication.translate("MainWindow", u"Last name:", None))
        self.SupervisorLabel.setText(QCoreApplication.translate("MainWindow", u"Supervisor:", None))
        self.DateLabel.setText(QCoreApplication.translate("MainWindow", u"Date: ", None))
        self.ExpirationLabel.setText(QCoreApplication.translate("MainWindow", u"Expiration date:", None))
        self.FirstName_lineEdit.setPlaceholderText("")
        self.SampleidBack2_button.setText("")
        self.SampleidForward2_button.setText("")
        self.NameDateOutput_label.setText("")
        self.SampleID_tab.setTabText(self.SampleID_tab.indexOf(self.MandInfo_SampleID_tab), QCoreApplication.translate("MainWindow", u"Mand. info.", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("MainWindow", u"Sample number(s)", None))
        self.SampleNumberLabel_2.setText(QCoreApplication.translate("MainWindow", u"Sample number from:", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"to:", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"to:", None))
        self.label_8.setText("")
        self.SubSample2_checkBox.setText(QCoreApplication.translate("MainWindow", u"Sub-Sample from:", None))
        self.Batch_radioButton.setText(QCoreApplication.translate("MainWindow", u"Batch samples", None))
        self.SampleidBack3_button.setText("")
        self.SampleidForward3_button.setText("")
        self.SubSample1_checkBox.setText(QCoreApplication.translate("MainWindow", u"Sub-Sample", None))
        self.label_9.setText("")
        self.SampleNumberLabel.setText(QCoreApplication.translate("MainWindow", u"Sample number (1-999):", None))
        self.Single_radioButton.setText(QCoreApplication.translate("MainWindow", u"Single sample", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Maximum amount of samples is set to 20.", None))
        self.SampleID_tab.setTabText(self.SampleID_tab.indexOf(self.SampleNumber_SampleID_tab), QCoreApplication.translate("MainWindow", u"Sample number(s)", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Globally Harmonised System", None))
        self.SampleidBack4_button.setText("")
        self.SampleidForward4_button.setText("")
        self.Explos_checkBox.setText("")
        self.Flamme_checkBox.setText("")
        self.Rondflam_checkBox.setText("")
        self.Acid_checkBox.setText("")
        self.Skull_checkBox.setText("")
        self.Exclam_checkBox.setText("")
        self.Silhouette_checkBox.setText("")
        self.Pollu_checkBox.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Please check all the checkboxes which may apply for your sample(s):", None))
        self.SampleID_tab.setTabText(self.SampleID_tab.indexOf(self.GHS_SampleID_tab), QCoreApplication.translate("MainWindow", u"GHS info", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Disposal of the samples", None))
        self.SampleidBack5_button.setText("")
        self.SampleidForward5_button.setText("")
#if QT_CONFIG(tooltip)
        self.NoIdea_radioButton.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">I have absolutely no idea.</span></p><p><span style=\" font-size:12pt;\">--&gt; Please take a look into the Chairmanual or ask Delf.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.NoIdea_radioButton.setText(QCoreApplication.translate("MainWindow", u"No idea", None))
#if QT_CONFIG(tooltip)
        self.NonHarzardous_radioButton.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Non-hazardous materials, e.g.:</span></p><p><br/></p><p><span style=\" font-size:12pt;\">- Wipes, gloves, tissues without hazardous residues;</span></p><p><span style=\" font-size:12pt;\">--&gt; Household waste</span></p><p><span style=\" font-size:12pt;\">- Solvent residues e.g. on gloves evaporated under fume hood;</span></p><p><span style=\" font-size:12pt;\">--&gt; Household waste</span></p><p><span style=\" font-size:12pt;\">- Culture media autoclaved (except for toxic components e.g. heavy metals);</span></p><p><span style=\" font-size:12pt;\">--&gt; Household waste</span></p><p><span style=\" font-size:12pt;\">- Empty, clean chemical plastic or glass bottles with removed hazard warnings/packages; </span></p><p><span style=\" font-size:12pt;\">--&gt; Glass/packaging</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.NonHarzardous_radioButton.setText(QCoreApplication.translate("MainWindow", u"Non-hazardous", None))
#if QT_CONFIG(tooltip)
        self.ContaminatedSolids_radioButton.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Solid materials with hazardous residues e.g.:</span></p><p><br/></p><p><span style=\" font-size:12pt;\">- Contaminated rags, wipes, gloves, foils;</span></p><p><span style=\" font-size:12pt;\">- Silica gel, activated charcoal, filter materials;</span></p><p><span style=\" font-size:12pt;\">- Pipettes (+tips) TLC-plates;</span></p><p><span style=\" font-size:12pt;\">- Small contaminated containers (metal, plastic);</span></p><p><span style=\" font-size:12pt;\">- Toxic culture media;</span></p><p><span style=\" font-size:12pt;\">- Respiratory filters (used or superimposed)</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.ContaminatedSolids_radioButton.setText(QCoreApplication.translate("MainWindow", u"Contaminated solids", None))
#if QT_CONFIG(tooltip)
        self.HalogenatedSolvents_radioButton.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Waste solvent in the laboratory seperated into hologenated &amp; holgenfree.</span></p><p><br/></p><p><span style=\" font-size:12pt;\">Holgenated solvents, e.g.:</span></p><p><span style=\" font-size:12pt;\">ACK, BH-N, C-LN, TC</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.HalogenatedSolvents_radioButton.setText(QCoreApplication.translate("MainWindow", u"Halogenated solvents", None))
#if QT_CONFIG(tooltip)
        self.HalogenFreeSolvents_radioButton.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Waste solvent in the laboratory seperated into hologenated &amp; holgenfree.</span></p><p><br/></p><p><span style=\" font-size:12pt;\">Holgen-free solvents, e.g.:</span></p><p><span style=\" font-size:12pt;\">KL, TIB, RDH</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.HalogenFreeSolvents_radioButton.setText(QCoreApplication.translate("MainWindow", u"Halogen-free solvents", None))
#if QT_CONFIG(tooltip)
        self.SpecialPrecautions_radioButton.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Special precautions need to be taken for my samples. E.g.:</span></p><p><br/></p><p><span style=\" font-size:12pt;\">The samples form a gel when in contact with other chemicals.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.SpecialPrecautions_radioButton.setText(QCoreApplication.translate("MainWindow", u"Special precautions", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Please check how your sample(s) should be disposed:", None))
        self.SampleID_tab.setTabText(self.SampleID_tab.indexOf(self.Disposal_SampleID_tab), QCoreApplication.translate("MainWindow", u"Disposal", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("MainWindow", u"Overview of the created sample(s) // Sample texts can be adjusted", None))
        self.SampleidBack6_button.setText("")
        self.SampleidForward6_button.setText("")
        ___qtablewidgetitem = self.AddInformation_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"SampleID", None));
        ___qtablewidgetitem1 = self.AddInformation_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Custom Sample name", None));
        ___qtablewidgetitem2 = self.AddInformation_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Additional Comments", None));
        ___qtablewidgetitem3 = self.AddInformation_tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"ElabFTW", None));
        ___qtablewidgetitem4 = self.AddInformation_tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Save PNG", None));
        ___qtablewidgetitem5 = self.AddInformation_tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Print", None));

        __sortingEnabled = self.AddInformation_tableWidget.isSortingEnabled()
        self.AddInformation_tableWidget.setSortingEnabled(False)
        self.AddInformation_tableWidget.setSortingEnabled(__sortingEnabled)

        self.SampleID_tab.setTabText(self.SampleID_tab.indexOf(self.AddInformation_SampleID_tab), QCoreApplication.translate("MainWindow", u"Add. information", None))
        self.groupBox_8.setTitle("")
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"SampleID(s) to ElabFTW:", None))
        self.ElabFTW_button.setText(QCoreApplication.translate("MainWindow", u" Sample ID to ElabFTW", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Save QR-code(s)", None))
        self.Foldersave_button.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.Save_button.setText(QCoreApplication.translate("MainWindow", u" Save QR-code", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Print QR-code(s)", None))
        self.PrintLayout_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u" 60 mm", None))
        self.PrintLayout_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u" 30 mm", None))
        self.PrintLayout_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u" 20 mm", None))
        self.PrintLayout_comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u" 15 mm", None))

        self.Print_button.setText(QCoreApplication.translate("MainWindow", u" Print QR-code", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"Output/Feedback", None))
        self.ElabFTWOutput1_label.setText("")
        self.ElabFTWOutput2_label.setText("")
        self.SampleidBack7_button.setText("")
        self.SampleidForward7_button.setText("")
        self.SampleID_tab.setTabText(self.SampleID_tab.indexOf(self.ElabFTW_SampleID_tab), QCoreApplication.translate("MainWindow", u"ElabFTW/PNG", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("MainWindow", u"Finish and start over", None))
        self.Reset_button.setText(QCoreApplication.translate("MainWindow", u" Reset", None))
        self.SampleidBack8_button.setText("")
        self.SampleidForward8_button.setText("")
        self.SampleID_tab.setTabText(self.SampleID_tab.indexOf(self.Finish_SampleID_tab), QCoreApplication.translate("MainWindow", u"Finish", None))
        self.Main_tab.setTabText(self.Main_tab.indexOf(self.Create_Main_tab), "")
        self.groupBox_12.setTitle(QCoreApplication.translate("MainWindow", u"Search a SampleID/UserID", None))
        self.SearchID_lineEdit.setText("")
        self.SearchID_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"UserID or SampleID", None))
        self.SearchID_pushButton.setText("")
        self.Main_tab.setTabText(self.Main_tab.indexOf(self.Search_Main_tab), "")
        self.groupBox_13.setTitle(QCoreApplication.translate("MainWindow", u"Scan a QR-code", None))
        self.ScanQR_button.setText("")
        self.ShowQR_button.setText("")
        self.ScanToCreate_button.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Scan QR-code", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Show QR-code", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Use result to create a SampleID", None))
        self.Main_tab.setTabText(self.Main_tab.indexOf(self.Scan_Main_tab), "")
        self.LogGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Log", None))
        self.Log_textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Ubuntu'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:8.25pt;\"><br /></p></body></html>", None))
        self.Main_tab.setTabText(self.Main_tab.indexOf(self.Log_Main_tab), "")
        self.About_label.setText(QCoreApplication.translate("MainWindow", u"This is CeramScan v1.618.\n"
"\n"
"Authors: Fabian Zemke.\n"
"\n"
"For bug reports write to: fabian.zemke@ceramics.tu-berlin.de\n"
"\n"
"\n"
"\n"
"\n"
"Icons were taken from UXWing: https://uxwing.com/\n"
" (free to download, and use for personal, commercial projects.\n"
"Credit and contribution was not required, but appreciated.)", None))
        self.Main_tab.setTabText(self.Main_tab.indexOf(self.About_Main_tab), "")
        self.groupBox_14.setTitle(QCoreApplication.translate("MainWindow", u"Add Chemical", None))
        self.groupBox_16.setTitle(QCoreApplication.translate("MainWindow", u"Create from Pubchem", None))
        self.AddChemical_fromID_button.setText(QCoreApplication.translate("MainWindow", u"Create from ID or Name", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"PubChem CID:", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"CAS:", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"InChIKey:", None))
        self.groupBox_17.setTitle(QCoreApplication.translate("MainWindow", u"Create new", None))
        self.ChemicalAdd_CreateNew_button.setText(QCoreApplication.translate("MainWindow", u"Create new", None))
        self.groupBox_18.setTitle(QCoreApplication.translate("MainWindow", u"Create from old CeramChemID", None))
        self.ChemicalAdd_CreatefromOld_button.setText(QCoreApplication.translate("MainWindow", u"Create from old CeramChemID", None))
        self.AddChemical_tab.setTabText(self.AddChemical_tab.indexOf(self.AddChemical_widget), QCoreApplication.translate("MainWindow", u"Add Chemical", None))
        self.groupBox_15.setTitle(QCoreApplication.translate("MainWindow", u"Search results from Pubchem", None))
        self.AddChemical_tab.setTabText(self.AddChemical_tab.indexOf(self.SelectChemical_tab), QCoreApplication.translate("MainWindow", u"Select Chemical", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("MainWindow", u"Current Status", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"Supplier and Ordering Details", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), QCoreApplication.translate("MainWindow", u"Chemical Datasheet", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_4), QCoreApplication.translate("MainWindow", u"Hazard and Precautionary Statements", None))
        self.groupBox_22.setTitle(QCoreApplication.translate("MainWindow", u"Add chemical to ElabFTW", None))
        self.AddChemicalToElab_button.setText(QCoreApplication.translate("MainWindow", u"Add chemical to ElabFTW", None))
        self.AddChemicalResponse_label.setText("")
        self.AddChemical_tab.setTabText(self.AddChemical_tab.indexOf(self.ChemicalToElab_tab), QCoreApplication.translate("MainWindow", u"Chemical to ElabFTW", None))
        self.Main_tab.setTabText(self.Main_tab.indexOf(self.Chemical_Main_tab), "")
    # retranslateUi

