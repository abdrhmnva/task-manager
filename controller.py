from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel
from madina.pyqt.task import Ui_MainWindow
from madina.pyqt.event import Ui_EventWindow
from madina.pyqt.task_input import Ui_AddTaskWindow
from madina.pyqt.logintask import Ui_LoginWindow
from model import Model
from PyQt6.QtCore import QDate, QTimer
from PyQt6.QtWidgets import QMessageBox
from classes.task import Task
from classes.user import User
from classes.task_history import Task_History
from dao.user_dao import UserDAO
from dao.task_dao import TaskDAO
from dao.task_history_dao import TaskHistoryDAO
from PyQt6.QtWidgets import QTableWidgetItem
from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QTableWidgetItem
from PyQt6.QtWidgets import QHeaderView
from PyQt6.QtGui import QBrush
from PyQt6.QtCore import Qt

from PyQt6.QtWidgets import QMessageBox
from datetime import datetime
from PyQt6.QtWidgets import QTableWidget, QVBoxLayout, QWidget, QLabel
from PyQt6.QtGui import QFont, QColor
from PyQt6 import QtCore
from PyQt6 import QtWidgets, QtGui, QtCore



class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.main_window = None
        self.event_window = None
        self.add_task_window = None
        self.login_window = None
        self.ui_main = Ui_MainWindow()
        self.ui_event = Ui_EventWindow()
        self.ui_add = Ui_AddTaskWindow()
        self.ui_login = Ui_LoginWindow()
        self.model = Model()
        self.dao = UserDAO("/Users/argenkulzhanov/Desktop/Designer/madina/task_manager.sqlite")
        self.task_dao = TaskDAO("/Users/argenkulzhanov/Desktop/Designer/madina/task_manager.sqlite")
        self.task_history_dao = TaskHistoryDAO("/Users/argenkulzhanov/Desktop/Designer/madina/task_manager.sqlite")
        self.current_username = None


    def show_main_window(self):
        self.main_window = QMainWindow()
        self.ui_main.setupUi(self.main_window)
        self.main_window.show()
        self.init_main_window_buttons()
        self.load_today_and_tomorrow_tasks()

    def show_event_window(self):
        self.event_window = QMainWindow()
        self.ui_event.setupUi(self.event_window)
        self.event_window.show()
        self.init_event_window_buttons()

    def show_add_task_window(self):
        self.add_task_window = QMainWindow()
        self.ui_add.setupUi(self.add_task_window)
        self.add_task_window.show()
        self.ui_add.addButton.clicked.connect(self.add_task_to_db)

    def show_login_window(self):
        self.login_window = QMainWindow()
        self.ui_login.setupUi(self.login_window)
        self.login_window.show()
        self.init_login_window_buttons()

    def init_main_window_buttons(self):
        self.ui_main.calendarWidget_2.selectionChanged.connect(self.on_date_clicked)
        self.ui_main.pushButton_5.clicked.connect(self.show_login_window)

    def init_event_window_buttons(self):
        self.ui_event.addButton.clicked.connect(self.add_task)
        self.ui_event.editButton.clicked.connect(self.edit_task)
        self.ui_event.deleteButton.clicked.connect(self.delete_task)
        self.ui_event.exitButton.clicked.connect(self.event_window.close)

    def init_login_window_buttons(self):
        self.ui_login.button_login_submit.clicked.connect(self.login)
        self.ui_login.button_signup.clicked.connect(self.create_account)

        self.ui_login.button_login.clicked.connect(lambda: self.ui_login.tabWidget.setCurrentIndex(1))
        self.ui_login.button_create.clicked.connect(lambda: self.ui_login.tabWidget.setCurrentIndex(2))
        self.ui_login.button_logout.clicked.connect(self.logout)
        self.ui_login.button_login_cancel.clicked.connect(lambda: self.ui_login.tabWidget.setCurrentIndex(0))
        self.ui_login.button_signup_cancel.clicked.connect(lambda: self.ui_login.tabWidget.setCurrentIndex(0))
        self.ui_login.tabWidget.tabBar().hide()

    def logout(self):
        self.current_username = None
        self.ui_main.pushButton_5.setText("Login")
        self.clear_login_window()
        self.main_window.close()
        self.show_login_window()

    def load_today_and_tomorrow_tasks(self):
        today = QDate.currentDate()
        date_today_str = today.toString("yyyy-MM-dd")

        tasks_today = self.task_dao.get_tasks_by_date(date_today_str)

        # Фильтруем: только не complete
        filtered_tasks = [task for task in tasks_today if task.get_status().lower() != "complete"]

        self.ui_main.tableWidget.setRowCount(len(filtered_tasks))
        self.ui_main.tableWidget.setColumnCount(5)
        self.ui_main.tableWidget.setHorizontalHeaderLabels(["Tag", "Date", "Time", "Description", "Status"])
        self.ui_main.tableWidget.horizontalHeader().setVisible(True)

        for i, task in enumerate(filtered_tasks):
            self.ui_main.tableWidget.setItem(i, 0, QTableWidgetItem(task.get_tag()))
            self.ui_main.tableWidget.setItem(i, 1, QTableWidgetItem(task.get_date()))
            self.ui_main.tableWidget.setItem(i, 2, QTableWidgetItem(task.get_time()))
            self.ui_main.tableWidget.setItem(i, 3, QTableWidgetItem(task.get_task()))
            self.ui_main.tableWidget.setItem(i, 4, QTableWidgetItem(task.get_status()))

            # Центрируем текст
            for j in range(5):
                item = self.ui_main.tableWidget.item(i, j)
                if item:
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

        # Автоширина колонок
        self.ui_main.tableWidget.resizeColumnsToContents()

        # Растянуть последнюю колонку
        self.ui_main.tableWidget.horizontalHeader().setStretchLastSection(True)

        # Чтобы таблица занимала всё пространство (если нужно программно)
        self.ui_main.tableWidget.setSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Expanding
        )

    def clear_login_window(self):
        self.ui_login.input_username.clear()
        self.ui_login.input_password.clear()
        self.ui_login.input_email.clear()
        self.ui_login.input_reg_username.clear()
        self.ui_login.input_reg_password.clear()

    def create_account(self):
        username = self.ui_login.input_reg_username.text().strip()
        email = self.ui_login.input_email.text().strip()
        password = self.ui_login.input_reg_password.text().strip()

        success, message = self.model.create_account(username, password, email)

        if not success:
            QMessageBox.warning(None, "Error", message)
        else:
            QMessageBox.information(None, "Success", message)
            self.ui_login.tabWidget.setCurrentIndex(1)

    def login(self):
        self.current_username = self.ui_login.input_username.text().strip()
        password = self.ui_login.input_password.text().strip()

        success, message = self.model.validate_login(self.current_username, password)

        if not success:
            QMessageBox.warning(None, "Login Failed", message)
        else:
            QMessageBox.information(None, "Welcome", message)
            self.login_window.close()
            self.show_main_window()
            self.ui_main.pushButton_5.setText(self.current_username)


    def add_task_to_db(self):
        self.ui_add.timeEdit.setTime(QtCore.QTime(0, 0))
        tag = self.ui_add.comboBox_tags.currentText().strip()
        date = self.ui_main.calendarWidget_2.selectedDate().toString("yyyy-MM-dd")
        time = self.ui_add.timeEdit.time().toString("HH:mm")
        description = self.ui_add.lineEdit_description.text().strip()
        status = self.ui_add.comboBox_status.currentText().strip()

        if not description:
            QMessageBox.warning(None, "Missing Field", "Please enter a description.")
            return

        self.task_dao.insert(Task(tag, date, time, description, status))
        QMessageBox.information(None, "Task Added", "The task has been successfully added.")
        # Add the task to the table
        row_position = self.ui_event.tableWidget.rowCount()
        self.ui_event.tableWidget.insertRow(row_position)

        self.ui_add.lineEdit_description.clear()
        self.add_task_window.close()
        self.load_today_and_tomorrow_tasks()

    def delete_task(self):
        # Получаем выбранную строку из таблицы
        selected_row = self.ui_event.tableWidget.currentRow()
        if selected_row == -1:
            QMessageBox.warning(None, "Error", "Please select a task to delete.")
            return

        # Получаем данные задачи из таблицы
        task_description = self.ui_event.tableWidget.item(selected_row, 3).text()
        task_date = self.ui_event.labelTitle.text().replace("Tasks for ", "")

        # Convert to datetime object
        date_object = datetime.strptime(task_date, "%B %d, %Y")

        # Format to "yyyy-MM-dd"
        formatted_date = date_object.strftime("%Y-%m-%d")
        print(f"Deleting task: {task_description}, Date: {formatted_date}")  # Debug print

        # Подтверждение удаления
        reply = QMessageBox.question(
            None,
            "Confirm Deletion",
            f"Are you sure you want to delete the task: '{task_description}'?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            # Удаляем задачу из базы данных
            self.task_dao.delete_task_by_description_and_date(task_description, formatted_date)

            # Удаляем строку из таблицы
            self.ui_event.tableWidget.removeRow(selected_row)

            QMessageBox.information(None, "Success", "Task deleted successfully.")
            self.load_today_and_tomorrow_tasks()

    def edit_task(self):
        # Get the selected row
        selected_row = self.ui_event.tableWidget.currentRow()
        if selected_row == -1:
            QMessageBox.warning(None, "Error", "Please select a task to edit.")
            return

        # Retrieve task details from the selected row
        task_tag = self.ui_event.tableWidget.item(selected_row, 1).text()
        task_time = self.ui_event.tableWidget.item(selected_row, 2).text()
        task_description = self.ui_event.tableWidget.item(selected_row, 3).text()
        task_status = self.ui_event.tableWidget.item(selected_row, 4).text()
        task_date = self.ui_event.labelTitle.text().replace("Tasks for ", "")

        # Open the task_input window and populate fields
        self.show_add_task_window()
        self.ui_add.comboBox_tags.setCurrentText(task_tag)
        self.ui_add.timeEdit.setTime(QtCore.QTime.fromString(task_time, "HH:mm"))
        self.ui_add.lineEdit_description.setText(task_description)
        self.ui_add.comboBox_status.setCurrentText(task_status)

        # Connect the save button to update the task
        self.ui_add.addButton.clicked.disconnect()  # Disconnect previous signal
        self.ui_add.addButton.clicked.connect(lambda: self.update_task(selected_row, task_date, task_description))

    def update_task(self, row, original_date, original_description):
        # Get updated task details
        tag = self.ui_add.comboBox_tags.currentText().strip()
        date = self.ui_main.calendarWidget_2.selectedDate().toString("yyyy-MM-dd")
        time = self.ui_add.timeEdit.time().toString("HH:mm")
        description = self.ui_add.lineEdit_description.text().strip()
        status = self.ui_add.comboBox_status.currentText().strip()

        if not description:
            QMessageBox.warning(None, "Missing Field", "Please enter a description.")
            return

        # Update the task in the database
        self.task_dao.update_task_by_description_and_date(
            original_description, original_date, tag, date, time, description, status
        )

        # Update the table
        self.ui_event.tableWidget.setItem(row, 1, QTableWidgetItem(tag))
        self.ui_event.tableWidget.setItem(row, 2, QTableWidgetItem(time))
        self.ui_event.tableWidget.setItem(row, 3, QTableWidgetItem(description))
        self.ui_event.tableWidget.setItem(row, 4, QTableWidgetItem(status))

        QMessageBox.information(None, "Task Updated", "The task has been successfully updated.")
        self.add_task_window.close()
        self.load_today_and_tomorrow_tasks()


    def add_task(self):
        self.show_add_task_window()

    def on_date_clicked(self):
        selected_date = self.ui_main.calendarWidget_2.selectedDate()
        date_str = selected_date.toString("MMMM d, yyyy")  # → May 15, 2025


        self.show_event_window()
        self.ui_event.labelTitle.setText(f"Tasks for {date_str}")
        self.print_task_for_a_day(selected_date)

    def print_task_for_a_day(self, selected_date):
        date_str = selected_date.toString("yyyy-MM-dd")
        tasks = self.task_dao.get_tasks_by_date(date_str)

        self.ui_event.tableWidget.setRowCount(len(tasks))
        self.ui_event.tableWidget.setColumnCount(5)
        self.ui_event.tableWidget.setHorizontalHeaderLabels(["№", "Tag", "Time", "Description", "Status"])
        self.ui_event.tableWidget.horizontalHeader().setVisible(True)

        self.ui_event.tableWidget.setStyleSheet("""
            QTableWidget {
                background-color: #2b2b2b;
                color: white;
                gridline-color: #444;
                font-size: 13px;
            }

            QHeaderView::section {
                background-color: #44475a;
                color: white;
                font-weight: bold;
                padding: 6px;
                border: 1px solid #3c3f41;
            }
        """)

        for i, task in enumerate(tasks):
            # Номер
            self.ui_event.tableWidget.setItem(i, 0, QTableWidgetItem(str(i + 1)))
            self.ui_event.tableWidget.setItem(i, 1, QTableWidgetItem(task.get_tag()))
            self.ui_event.tableWidget.setItem(i, 2, QTableWidgetItem(task.get_time()))
            self.ui_event.tableWidget.setItem(i, 3, QTableWidgetItem(task.get_task()))
            self.ui_event.tableWidget.setItem(i, 4, QTableWidgetItem(task.get_status()))

            # Центрируем всё
            for j in range(5):
                item = self.ui_event.tableWidget.item(i, j)
                if item:
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

        # Подгонка ширины
        self.ui_event.tableWidget.resizeColumnsToContents()
        self.ui_event.tableWidget.horizontalHeader().setStretchLastSection(True)







