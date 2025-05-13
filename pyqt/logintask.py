from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(500, 300)
        LoginWindow.setStyleSheet("""
            QWidget {
                background-color: #2b2b2b;
                color: white;
                font-size: 14px;
            }
            QLineEdit {
                background-color: #3c3f41;
                border: 1px solid #5e5e5e;
                border-radius: 8px;
                padding: 8px;
                color: white;
            }
            QPushButton {
                background-color: #5e4b8b;
                color: white;
                border-radius: 10px;
                padding: 10px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #7a62b3;
            }
        """)

        self.centralwidget = QtWidgets.QWidget(parent=LoginWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")

        # --- Tab: Start ---
        self.tab_start = QtWidgets.QWidget()
        layout_start = QtWidgets.QVBoxLayout(self.tab_start)

        self.label_start = QtWidgets.QLabel("Start")
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.label_start.setFont(font)
        self.label_start.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        layout_start.addWidget(self.label_start)

        self.button_login = QtWidgets.QPushButton("Log in")
        self.button_create = QtWidgets.QPushButton("Create account")
        self.button_logout = QtWidgets.QPushButton("Log out")


        for btn in [self.button_login, self.button_create, self.button_logout]:
            layout_start.addWidget(btn)

        layout_start.addStretch()
        self.tabWidget.addTab(self.tab_start, "Home")

        # --- Tab: Login ---
        self.tab_login = QtWidgets.QWidget()
        layout_login = QtWidgets.QVBoxLayout(self.tab_login)

        self.label_login = QtWidgets.QLabel("Login")
        self.label_login.setFont(font)
        self.label_login.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        layout_login.addWidget(self.label_login)

        self.input_username = QtWidgets.QLineEdit()
        self.input_username.setPlaceholderText("Username")
        self.input_password = QtWidgets.QLineEdit()
        self.input_password.setPlaceholderText("Password")
        self.input_password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

        layout_login.addWidget(self.input_username)
        layout_login.addWidget(self.input_password)

        self.button_login_submit = QtWidgets.QPushButton("Log in")
        self.button_login_cancel = QtWidgets.QPushButton("Cancel")

        layout_login.addWidget(self.button_login_submit)
        layout_login.addWidget(self.button_login_cancel)
        layout_login.addStretch()

        self.tabWidget.addTab(self.tab_login, "Login")

        # --- Tab: Register ---
        self.tab_register = QtWidgets.QWidget()
        layout_register = QtWidgets.QVBoxLayout(self.tab_register)

        self.label_register = QtWidgets.QLabel("Create Account")
        self.label_register.setFont(font)
        self.label_register.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        layout_register.addWidget(self.label_register)

        self.input_email = QtWidgets.QLineEdit()
        self.input_email.setPlaceholderText("Email")
        self.input_reg_username = QtWidgets.QLineEdit()
        self.input_reg_username.setPlaceholderText("Username")
        self.input_reg_password = QtWidgets.QLineEdit()
        self.input_reg_password.setPlaceholderText("Password")
        self.input_reg_password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

        layout_register.addWidget(self.input_email)
        layout_register.addWidget(self.input_reg_username)
        layout_register.addWidget(self.input_reg_password)

        self.button_signup = QtWidgets.QPushButton("Create account")
        self.button_signup_cancel = QtWidgets.QPushButton("Cancel")

        layout_register.addWidget(self.button_signup)
        layout_register.addWidget(self.button_signup_cancel)
        layout_register.addStretch()

        self.tabWidget.addTab(self.tab_register, "Sign Up")

        # --- Final layout ---
        main_layout = QtWidgets.QVBoxLayout(self.centralwidget)
        main_layout.addWidget(self.tabWidget)
        LoginWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "Login"))


