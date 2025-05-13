from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_AddTaskWindow(object):
    def setupUi(self, AddTaskWindow):
        AddTaskWindow.setObjectName("AddTaskWindow")
        AddTaskWindow.resize(400, 350)

        # Тёмный стиль
        dark_style = """
            QWidget {
                background-color: #2b2b2b;
                color: #f0f0f0;
                font-size: 14px;
                font-family: "Segoe UI", sans-serif;
            }

            QLineEdit, QComboBox, QDateEdit, QTimeEdit {
                background-color: #3c3f41;
                border: 1px solid #5e5e5e;
                border-radius: 6px;
                padding: 6px;
                color: #ffffff;
            }

            QLineEdit:focus, QComboBox:focus, QDateEdit:focus, QTimeEdit:focus {
                border: 1px solid #7a62b3;
                background-color: #44475a;
            }

            QPushButton {
                background-color: #5e4b8b;
                color: white;
                border-radius: 10px;
                padding: 10px;
                font-size: 16px;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #7a62b3;
            }

            QPushButton:pressed {
                background-color: #483370;
            }
        """

        AddTaskWindow.setStyleSheet(dark_style)

        self.centralwidget = QtWidgets.QWidget(parent=AddTaskWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(30, 30, 30, 30)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName("verticalLayout")

        # Заголовок
        self.labelTitle = QtWidgets.QLabel("Add Task", parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.labelTitle.setFont(font)
        self.labelTitle.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout.addWidget(self.labelTitle)

        # Политика размеров
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Fixed)

        # Tags (заменено на ComboBox)
        self.comboBox_tags = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox_tags.addItems(["Work", "Personal", "Study", "Important", "Other"])
        self.comboBox_tags.setSizePolicy(size_policy)
        self.verticalLayout.addWidget(self.comboBox_tags)

        # Time
        self.timeEdit = QtWidgets.QTimeEdit(parent=self.centralwidget)
        self.timeEdit.setDisplayFormat("HH:mm")
        self.timeEdit.setTime(QtCore.QTime.currentTime())
        self.timeEdit.setSizePolicy(size_policy)
        self.verticalLayout.addWidget(self.timeEdit)

        # Description
        self.lineEdit_description = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_description.setPlaceholderText("Description")
        self.lineEdit_description.setSizePolicy(size_policy)
        self.verticalLayout.addWidget(self.lineEdit_description)

        # Status
        self.comboBox_status = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox_status.addItems(["Pending", "Complete"])
        self.comboBox_status.setSizePolicy(size_policy)
        self.verticalLayout.addWidget(self.comboBox_status)

        # Add Button
        self.addButton = QtWidgets.QPushButton("Add", parent=self.centralwidget)
        self.addButton.setMinimumHeight(40)
        self.addButton.setSizePolicy(size_policy)
        self.verticalLayout.addWidget(self.addButton)

        AddTaskWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(parent=AddTaskWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 21))
        self.menubar.setObjectName("menubar")
        AddTaskWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(parent=AddTaskWindow)
        self.statusbar.setObjectName("statusbar")
        AddTaskWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AddTaskWindow)
        QtCore.QMetaObject.connectSlotsByName(AddTaskWindow)

    def retranslateUi(self, AddTaskWindow):
        _translate = QtCore.QCoreApplication.translate
        AddTaskWindow.setWindowTitle(_translate("AddTaskWindow", "Add New Task"))


# Запуск отдельно
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddTaskWindow = QtWidgets.QMainWindow()
    ui = Ui_AddTaskWindow()
    ui.setupUi(AddTaskWindow)
    AddTaskWindow.show()
    sys.exit(app.exec())
