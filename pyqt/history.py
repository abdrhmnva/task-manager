from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_HistoryWindow(object):
    def setupUi(self, HistoryWindow):
        HistoryWindow.setObjectName("HistoryWindow")
        HistoryWindow.resize(800, 500)
        HistoryWindow.setStyleSheet("background-color: #282a36;")
        
        self.centralwidget = QtWidgets.QWidget(HistoryWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 20, 760, 420))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        
        self.closeButton = QtWidgets.QPushButton(self.centralwidget)
        self.closeButton.setGeometry(QtCore.QRect(350, 450, 100, 30))
        self.closeButton.setObjectName("closeButton")
        self.closeButton.setText("Close")
        self.closeButton.setStyleSheet("""
            QPushButton {
                background-color: #44475a;
                color: white;
                border-radius: 4px;
                font-weight: bold;
                padding: 5px 10px;
            }
            QPushButton:hover {
                background-color: #6272a4;
            }
            QPushButton:pressed {
                background-color: #282a36;
            }
        """)
        
        HistoryWindow.setCentralWidget(self.centralwidget)