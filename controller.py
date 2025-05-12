from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel
from madina.pyqt.task import Ui_MainWindow
from madina.pyqt.event import Ui_EventWindow
from PyQt6.QtCore import QDate

class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.main_window = None
        self.event_window = None
        self.ui_main = Ui_MainWindow()
        self.ui_event = Ui_EventWindow()

        self.setupUi(self)

    def show_main_window(self):
        self.main_window = QMainWindow()
        self.ui_main.setupUi(self.main_window)
        self.main_window.show()
        self.init_main_window_buttons()

        # Отключаем навигацию и ограничиваем только текущим месяцем
        self.ui_main.calendarWidget_2.setNavigationBarVisible(False)
        today = QDate.currentDate()
        first_day = QDate(today.year(), today.month(), 1)
        last_day = first_day.addMonths(1).addDays(-1)
        self.ui_main.calendarWidget_2.setMinimumDate(first_day)
        self.ui_main.calendarWidget_2.setMaximumDate(last_day)

    def show_event_window(self):
        self.event_window = QMainWindow()
        self.ui_event.setupUi(self.event_window)
        self.event_window.show()

    def init_main_window_buttons(self):
        self.ui_main.calendarWidget_2.selectionChanged.connect(self.on_date_clicked)
        self.ui_main.pushButton_2.clicked.connect(self.delete_task)
        self.ui_main.pushButton_3.clicked.connect(self.edit_task)
        self.ui_main.pushButton_4.clicked.connect(self.add_task)

    def delete_task(self):

    def edit_task(self):

    def add_task(self):

    def on_date_clicked(self):
        selected_date = self.ui_main.calendarWidget_2.selectedDate()
        date_str = selected_date.toString("yyyy-MM-dd")


