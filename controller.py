from PyQt6.QtWidgets import QMainWindow, QMessageBox
from pyqt.task import Ui_MainWindow
from pyqt.event import Ui_EventWindow
from pyqt.task_input import Ui_AddTaskWindow
from pyqt.logintask import Ui_LoginWindow
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


from datetime import datetime
from PyQt6 import QtCore
from PyQt6 import QtWidgets, QtGui, QtCore
from pyqt.history import Ui_HistoryWindow


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

        self.ui_history = Ui_HistoryWindow()

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

        try:
            self.ui_add.addButton.clicked.disconnect()
        except:
            pass

        self.ui_add.addButton.clicked.connect(self.add_task_to_db)
        self.ui_add.addButton.setText("Add")

        self.add_task_window.show()

    def show_login_window(self):
        self.login_window = QMainWindow()
        self.ui_login.setupUi(self.login_window)
        self.login_window.show()
        self.init_login_window_buttons()

    def init_main_window_buttons(self):
        self.ui_main.calendarWidget_2.selectionChanged.connect(self.on_date_clicked)
        self.ui_main.pushButton_5.clicked.connect(self.show_login_window)
        self.ui_main.pushButton_6.clicked.connect(self.show_task_history)

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
        if self.current_username is not None:
            self.current_username = None
            self.ui_main.pushButton_5.setText("Login")
            self.clear_login_window()
            self.login_window.close()


    def load_today_and_tomorrow_tasks(self):
        if not self.main_window or not hasattr(self, 'ui_main'):
            print("DEBUG: Main window not available")
            return

        today = QDate.currentDate()
        date_today_str = today.toString("yyyy-MM-dd")
        print(f"DEBUG: Loading tasks for today: {date_today_str}")

        tasks_today = self.task_dao.get_tasks_by_date(date_today_str)

        filtered_tasks = [task for task in tasks_today if task.get_status().lower() != "complete"]

        self.ui_main.tableWidget.setRowCount(len(filtered_tasks))
        self.ui_main.tableWidget.setColumnCount(5)
        self.ui_main.tableWidget.setHorizontalHeaderLabels(["Tag", "Date", "Time", "Description", "Status"])

        header = self.ui_main.tableWidget.horizontalHeader()

        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)

        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeMode.Stretch)

        header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)

        self.ui_main.tableWidget.horizontalHeader().setVisible(True)

        for i, task in enumerate(filtered_tasks):
            self.ui_main.tableWidget.setItem(i, 0, QTableWidgetItem(task.get_tag()))
            self.ui_main.tableWidget.setItem(i, 1, QTableWidgetItem(task.get_date()))
            self.ui_main.tableWidget.setItem(i, 2, QTableWidgetItem(task.get_time()))
            self.ui_main.tableWidget.setItem(i, 3, QTableWidgetItem(task.get_task()))
            self.ui_main.tableWidget.setItem(i, 4, QTableWidgetItem(task.get_status()))

            for j in range(5):
                item = self.ui_main.tableWidget.item(i, j)
                if item:
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

        self.ui_main.tableWidget.horizontalHeader().setStretchLastSection(False)

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
        tag = self.ui_add.comboBox_tags.currentText().strip()
        date = self.ui_main.calendarWidget_2.selectedDate().toString("yyyy-MM-dd")
        time = self.ui_add.timeEdit.time().toString("HH:mm")
        description = self.ui_add.lineEdit_description.text().strip()
        status = self.ui_add.comboBox_status.currentText().strip()

        if not description:
            QMessageBox.warning(None, "Missing Field", "Please enter a description.")
            return
        self.task_dao.insert(Task(tag, date, time, description, status))

        self.log_task_history(description, tag, "addition")

        self.ui_add.lineEdit_description.clear()
        self.ui_add.timeEdit.setTime(QtCore.QTime(0, 0))

        self.add_task_window.close()

        QMessageBox.information(None, "Task Added", "The task has been successfully added.")

        QtCore.QTimer.singleShot(100, self.refresh_all_tables)
        row_position = self.ui_event.tableWidget.rowCount()
        self.ui_event.tableWidget.insertRow(row_position)

        self.ui_add.lineEdit_description.clear()
        self.ui_add.timeEdit.setTime(QtCore.QTime(0, 0))
        self.add_task_window.close()
        self.load_today_and_tomorrow_tasks()

    def delete_task(self):
        selected_row = self.ui_event.tableWidget.currentRow()
        if selected_row == -1:
            QMessageBox.warning(None, "Error", "Please select a task to delete.")
            return

        task_description = self.ui_event.tableWidget.item(selected_row, 3).text()
        task_date = self.ui_event.labelTitle.text().replace("Tasks for ", "")

        date_object = datetime.strptime(task_date, "%B %d, %Y")

        formatted_date = date_object.strftime("%Y-%m-%d")
        print(f"Deleting task: {task_description}, Date: {formatted_date}")  # Debug print

        reply = QMessageBox.question(
            None,
            "Confirm Deletion",
            f"Are you sure you want to delete the task: '{task_description}'?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            task_tag = self.ui_event.tableWidget.item(selected_row, 1).text()
            self.task_dao.delete_task_by_description_and_date(task_description, formatted_date)

            self.log_task_history(task_description, task_tag, "deletion")

            self.ui_event.tableWidget.removeRow(selected_row)

            QMessageBox.information(None, "Success", "Task deleted successfully.")
            self.load_today_and_tomorrow_tasks()

    def edit_task(self):
        selected_row = self.ui_event.tableWidget.currentRow()
        if selected_row == -1:
            QMessageBox.warning(None, "Error", "Please select a task to edit.")
            return

        task_tag = self.ui_event.tableWidget.item(selected_row, 1).text()
        task_time = self.ui_event.tableWidget.item(selected_row, 2).text()
        task_description = self.ui_event.tableWidget.item(selected_row, 3).text()
        task_status = self.ui_event.tableWidget.item(selected_row, 4).text()

        task_date_str = self.ui_event.labelTitle.text().replace("Tasks for ", "")
        try:
            date_object = datetime.strptime(task_date_str, "%B %d, %Y")
            task_date = date_object.strftime("%Y-%m-%d")
        except Exception:
            QMessageBox.warning(None, "Error", "Could not parse date format.")
            return

        self.show_add_task_window()
        self.ui_add.addButton.setText("Update")
        self.ui_add.comboBox_tags.setCurrentText(task_tag)
        self.ui_add.timeEdit.setTime(QtCore.QTime.fromString(task_time, "HH:mm"))
        self.ui_add.lineEdit_description.setText(task_description)
        self.ui_add.comboBox_status.setCurrentText(task_status)

        try:
            self.ui_add.addButton.clicked.disconnect()
        except Exception:
            pass

        self.ui_add.addButton.clicked.connect(lambda: self.update_task(selected_row, task_date, task_description))

    def update_task(self, row, original_date, original_description):
        """Обновляет задачу в БД и перезагружает все таблицы"""
        tag = self.ui_add.comboBox_tags.currentText().strip()
        time = self.ui_add.timeEdit.time().toString("HH:mm")
        description = self.ui_add.lineEdit_description.text().strip()
        status = self.ui_add.comboBox_status.currentText().strip()
        date = original_date

        if not description:
            QMessageBox.warning(None, "Missing Field", "Please enter a description.")
            return

        print(f"DEBUG: Updating task from {original_date}, '{original_description}'")
        print(f"DEBUG: New values: {tag}, {date}, {time}, '{description}', {status}")

        result = self.task_dao.update_task_by_description_and_date(
            original_description, original_date, tag, date, time, description, status
        )

        if result:
            self.log_task_history(description, tag, "edited")

        if not result:
            QMessageBox.warning(None, "Error", "Failed to update task.")
            return

        task_date_str = self.ui_event.labelTitle.text().replace("Tasks for ", "")
        selected_date = None
        try:
            date_object = datetime.strptime(task_date_str, "%B %d, %Y")
            selected_date = QDate(date_object.year, date_object.month, date_object.day)
        except Exception:
            selected_date = QDate.currentDate()

        self.add_task_window.close()

        self.refresh_all_tables()

        QMessageBox.information(None, "Success", "Task updated successfully!")

    def add_task(self):
        self.show_add_task_window()

    def on_date_clicked(self):
        selected_date = self.ui_main.calendarWidget_2.selectedDate()
        date_str = selected_date.toString("MMMM d, yyyy")  # → May 15, 2025

        self.show_event_window()
        self.ui_event.labelTitle.setText(f"Tasks for {date_str}")
        self.print_task_for_a_day(selected_date)

    def print_task_for_a_day(self, selected_date):
        if not self.event_window or not hasattr(self, 'ui_event'):
            print("DEBUG: Event window not available")
            return

        date_str = selected_date.toString("yyyy-MM-dd")

        tasks = self.task_dao.get_tasks_by_date(date_str)

        current_width = self.ui_event.tableWidget.width()
        current_height = self.ui_event.tableWidget.height()

        self.ui_event.tableWidget.setRowCount(len(tasks))
        self.ui_event.tableWidget.setColumnCount(5)
        self.ui_event.tableWidget.setHorizontalHeaderLabels(["№", "Tag", "Time", "Description", "Status"])
        self.ui_event.tableWidget.horizontalHeader().setVisible(True)

        self.ui_event.tableWidget.setMinimumSize(600, 300)

        self.ui_event.tableWidget.setSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Expanding
        )

        # Применяем стили к таблице
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

        header = self.ui_event.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)  # №
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)  # Tag
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)  # Time
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeMode.Stretch)  # Description
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)  # Status

        for i, task in enumerate(tasks):
            self.ui_event.tableWidget.setItem(i, 0, QTableWidgetItem(str(i + 1)))
            self.ui_event.tableWidget.setItem(i, 1, QTableWidgetItem(task.get_tag()))
            self.ui_event.tableWidget.setItem(i, 2, QTableWidgetItem(task.get_time()))
            self.ui_event.tableWidget.setItem(i, 3, QTableWidgetItem(task.get_task()))
            self.ui_event.tableWidget.setItem(i, 4, QTableWidgetItem(task.get_status()))

            for j in range(5):
                item = self.ui_event.tableWidget.item(i, j)
                if item:
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

        self.ui_event.tableWidget.horizontalHeader().setStretchLastSection(True)

        if current_width > 0 and current_height > 0:
            self.ui_event.tableWidget.resize(current_width, current_height)

    def refresh_all_tables(self):
        print("DEBUG: Manual refresh of all tables")

        if self.main_window and hasattr(self, 'ui_main'):
            QtCore.QTimer.singleShot(100, self.load_today_and_tomorrow_tasks)

        if self.event_window and hasattr(self, 'ui_event'):
            task_date_str = self.ui_event.labelTitle.text().replace("Tasks for ", "")
            try:
                date_object = datetime.strptime(task_date_str, "%B %d, %Y")
                selected_date = QDate(date_object.year, date_object.month, date_object.day)
                QtCore.QTimer.singleShot(200, lambda: self.print_task_for_a_day(selected_date))
            except Exception as e:
                print(f"DEBUG: Error updating event table: {e}")

    def log_task_history(self, task_description, tag, operation):
        try:
            current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            user_id = self.current_user_id if hasattr(self, 'current_user_id') else None

            print(f"DEBUG logging: desc='{task_description}', tag='{tag}', op='{operation}'")

            history_entry = Task_History(
                task_description=task_description,
                date_added=current_date,
                tag=tag,
                operation=operation,
                user_id=user_id
            )

            self.task_history_dao.insert(history_entry)
        except Exception as e:
            print(f"ERROR: Failed to log task history: {e}")

    def show_task_history(self):
        self.history_window = QMainWindow()
        self.ui_history.setupUi(self.history_window)

        history_items = self.task_history_dao.get_all_history()

        self.ui_history.tableWidget.setRowCount(len(history_items))
        self.ui_history.tableWidget.setColumnCount(4)  # Обратно 4 колонки
        self.ui_history.tableWidget.setHorizontalHeaderLabels(["Task", "Date Added", "Tag", "Operation"])

        self.ui_history.tableWidget.setStyleSheet("""
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

        for i, history in enumerate(history_items):
            self.ui_history.tableWidget.setItem(i, 0, QTableWidgetItem(history.get_task_description()))
            self.ui_history.tableWidget.setItem(i, 1, QTableWidgetItem(history.get_date_added()))
            self.ui_history.tableWidget.setItem(i, 2, QTableWidgetItem(history.get_tag()))

            operation_item = QTableWidgetItem(history.get_operation())
            if history.get_operation() == "addition":
                operation_item.setForeground(QBrush(Qt.GlobalColor.green))
            elif history.get_operation() == "deletion":
                operation_item.setForeground(QBrush(Qt.GlobalColor.red))
            else:
                operation_item.setForeground(QBrush(Qt.GlobalColor.yellow))

            self.ui_history.tableWidget.setItem(i, 3, operation_item)

        header = self.ui_history.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeMode.Stretch)  # Task
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)  # Date
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)  # Tag
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)  # Operation

        self.history_window.show()

        self.ui_history.closeButton.clicked.connect(self.history_window.close)