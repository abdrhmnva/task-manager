from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_EventWindow(object):
    def setupUi(self, EventWindow):
        EventWindow.setObjectName("EventWindow")
        EventWindow.resize(636, 352)

        # Стиль для кнопок
        button_style = """
            QPushButton {
                background-color: #5e4b8b;
                color: white;
                border-radius: 12px;
                padding: 8px 20px;
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

        self.centralwidget = QtWidgets.QWidget(parent=EventWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Главный вертикальный layout (всё содержимое окна)
        self.mainVerticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.mainVerticalLayout.setObjectName("mainVerticalLayout")

        # Заголовок Tasks
        self.labelTitle = QtWidgets.QLabel("Tasks", parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.labelTitle.setFont(font)
        self.labelTitle.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.mainVerticalLayout.addWidget(self.labelTitle)

        # Горизонтальный layout: таблица + кнопки
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        # Таблица слева
        self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget.setStyleSheet("color: rgb(0, 0, 0);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)  # 3 столбца
        self.tableWidget.setRowCount(0)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setVisible(True)  # Показываем заголовки

        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)

        # Устанавливаем ResizeMode для всех столбцов
        header = self.tableWidget.horizontalHeader()
        
        # Первые две колонки — по содержимому, но ограничиваем их ширину
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 100)

        # Третья колонка (description) — растягивается
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeMode.Stretch)

        self.horizontalLayout.addWidget(self.tableWidget)

        # Layout для кнопок справа
        self.buttonLayout = QtWidgets.QVBoxLayout()
        self.buttonLayout.setObjectName("buttonLayout")

        self.addButton = QtWidgets.QPushButton("Add", parent=self.centralwidget)
        self.addButton.setStyleSheet(button_style)
        self.buttonLayout.addWidget(self.addButton)

        self.deleteButton = QtWidgets.QPushButton("Delete", parent=self.centralwidget)
        self.deleteButton.setStyleSheet(button_style)
        self.buttonLayout.addWidget(self.deleteButton)

        self.editButton = QtWidgets.QPushButton("Edit", parent=self.centralwidget)
        self.editButton.setStyleSheet(button_style)
        self.buttonLayout.addWidget(self.editButton)

        self.exitButton = QtWidgets.QPushButton("Exit", parent=self.centralwidget)
        self.exitButton.setStyleSheet(button_style)
        self.buttonLayout.addWidget(self.exitButton)

        self.buttonLayout.addStretch()
        self.horizontalLayout.addLayout(self.buttonLayout)

        self.mainVerticalLayout.addLayout(self.horizontalLayout)

        EventWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(parent=EventWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 636, 21))
        self.menubar.setObjectName("menubar")
        EventWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(parent=EventWindow)
        self.statusbar.setObjectName("statusbar")
        EventWindow.setStatusBar(self.statusbar)

        self.retranslateUi(EventWindow)
        QtCore.QMetaObject.connectSlotsByName(EventWindow)

    def retranslateUi(self, EventWindow):
        _translate = QtCore.QCoreApplication.translate
        EventWindow.setWindowTitle(_translate("EventWindow", "Event Manager"))