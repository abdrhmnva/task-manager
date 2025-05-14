from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 700)
        MainWindow.setStyleSheet("background-color: #323232;")

        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.mainLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.mainLayout.setContentsMargins(20, 20, 20, 20)
        self.mainLayout.setSpacing(20)

        # --- Top Bar ---
        self.topBar = QtWidgets.QFrame()
        self.topBar.setStyleSheet("background-color: #5e4b8b;")
        self.topBar.setFixedHeight(60)
        self.topLayout = QtWidgets.QHBoxLayout(self.topBar)

        self.pushButton_6 = QtWidgets.QPushButton("History")
        self.pushButton_5 = QtWidgets.QPushButton("Sign up")

        for btn in (self.pushButton_6, self.pushButton_5):
            btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
            btn.setStyleSheet("""
                QPushButton {
                    background-color: transparent;
                    color: white;
                    border: 2px solid white;
                    border-radius: 12px;
                    padding: 8px 20px;
                    font-size: 16px;
                    font-weight: bold;
                }
                QPushButton:hover {
                    background-color: rgba(255, 255, 255, 0.1);
                }
            """)

        self.topLayout.addWidget(self.pushButton_6)
        self.topLayout.addStretch()
        self.topLayout.addWidget(self.pushButton_5)
        self.mainLayout.addWidget(self.topBar)

        # --- Calendar ---
        self.calendarWidget_2 = QtWidgets.QCalendarWidget()
        self.calendarWidget_2.setStyleSheet("""
            QCalendarWidget {
                background-color: #1e1e1e;
                color: #dcdcdc;
                border: 1px solid #444;
                selection-background-color: #00ff88;
            }
            QCalendarWidget QAbstractItemView {
                background-color: #121212;
                selection-background-color: #00ff88;
                selection-color: black;
                gridline-color: #333;
                color: #dcdcdc;
                font-size: 14px;
            }
            QCalendarWidget QWidget#qt_calendar_navigationbar {
                background-color: #2b2b2b;
                color: white;
            }
            QCalendarWidget QToolButton {
                color: white;
                background-color: #5e4b8b;
                font-weight: bold;
                font-size: 16px;
                border-radius: 10px;
                padding: 5px 12px;
                margin: 2px;
            }
            QCalendarWidget QToolButton::menu-indicator {
                image: none;
            }
            QCalendarWidget QHeaderView::section {
                background-color: #1e1e1e;
                color: #bbbbbb;
                font-weight: bold;
                padding: 4px;
                border: none;
            }
        """)
        self.calendarWidget_2.setObjectName("calendarWidget_2")
        self.calendarWidget_2.setSelectionMode(QtWidgets.QCalendarWidget.SelectionMode.SingleSelection)
        self.calendarWidget_2.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.HorizontalHeaderFormat.ShortDayNames)
        self.calendarWidget_2.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.VerticalHeaderFormat.NoVerticalHeader)
        self.calendarWidget_2.setNavigationBarVisible(True)
        self.calendarWidget_2.setDateEditEnabled(False)
        self.mainLayout.addWidget(self.calendarWidget_2)

        # --- Label ---
        self.label_2 = QtWidgets.QLabel("Today's tasks")
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: white;")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.mainLayout.addWidget(self.label_2)

        # --- Table ---
        self.tableWidget = QtWidgets.QTableWidget()
        self.tableWidget.setStyleSheet("""
            QTableWidget {
                background-color: #1e1e1e;
                color: #e0e0e0;
                gridline-color: #444;
                border: 1px solid #333;
                font-size: 14px;
                selection-background-color: #5e4b8b;
                selection-color: white;
            }
            QHeaderView::section {
                background-color: #2b2b2b;
                color: #ffffff;
                font-weight: bold;
                padding: 5px;
                border: 1px solid #444;
            }
            QTableWidget QTableCornerButton::section {
                background-color: #2b2b2b;
                border: 1px solid #444;
            }
        """)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.mainLayout.addWidget(self.tableWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
