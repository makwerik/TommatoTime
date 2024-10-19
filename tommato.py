import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import QTimer, QTime
from pomodoro_timer import Ui_MainWindow


class PomodoroApp(QMainWindow, Ui_MainWindow):
    """Класс который унаследовался от QMainWindow и нашего графического интерфейса Ui_MainWindow"""

    def __init__(self):
        super().__init__()
        # Установка созданного интерфейса
        self.setupUi(self)

        # Таймер для основной работы
        self.time_left = QTime(1, 0, 0)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)

        # Таймер для глаз
        self.eye_timer = QTimer(self)
        self.eye_timer.timeout.connect(self.remind_eye_rest)
        self.eye_rest_interval = 20 * 60  # Каждые 20 мин. нужно напоминание
        self.time_worked = 0  # Время, которое пользователь работал

        # Таймер для осанки
        self.back_timer = QTimer(self)
        self.back_timer.timeout.connect(self.check_back)
        self.back_interval = 10 * 60
        self.time_worked_back = 0


        # Привязывю кнопки к функциям
        self.pushButton_3.clicked.connect(self.start_timer)
        self.pushButton_2.clicked.connect(self.pause_timer)
        self.pushButton.clicked.connect(self.reset_timer)

        # Счётчик сессий
        self.completed_sessions = 0
        self.long_break_time = 15 * 60  # Длительный перерыв - 15 минут



    def start_timer(self):
        """Метод для запуска таймера и таймера для уведомления для глаз"""
        if not self.timer.isActive():
            self.timer.start(1000)

        # Проверка чекбокса что необходимо напоминание о глазах
        if self.checkBox.isChecked():
            self.eye_timer.start(1000)

        if self.checkBox_2.isChecked():
            self.back_timer.start(1000)

    def pause_timer(self):
        """Метод для приостановки таймера и напоминаний о глазах, осанке"""
        self.timer.stop()
        self.eye_timer.stop()
        self.back_timer.stop()

    def reset_timer(self):
        """Метод для сброса таймера"""

        self.timer.stop()
        self.eye_timer.stop()
        self.back_timer.stop()
        self.time_left = QTime(1, 0, 0)
        self.label.setText(self.time_left.toString("mm:ss"))
        self.time_worked = 0
        self.time_worked_back = 0

    def update_time(self):
        """Метод для обновления таймера и напоминаний о перерывах"""
        try:
            self.time_left = self.time_left.addSecs(-1)
            self.label.setText(self.time_left.toString("mm:ss"))

            # Останавливаем таймер, когда время истекает
            if self.time_left == QTime(0, 0, 0):
                self.timer.stop()
                self.eye_timer.stop()
                self.completed_sessions += 1
                self.check_long_break()

                # Сбрасываем таймер на 25 минут после завершения сессии
                self.time_left = QTime(1, 0, 0)
                self.label.setText(self.time_left.toString("mm:ss"))
        except Exception as e:
            print(f"Произошла ошибка: {e}")

    def check_long_break(self):
        if self.completed_sessions >= 1:
            self.completed_sessions = 0
            self.start_long_break()

    def start_long_break(self):
        """Перерыв на 15 минут (или любое другое время, установленное пользователем)"""
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Вы провели за компьютером 1 час")
        msg.setText("Время сделать 15 минутный перерыв!")
        msg.exec_()



    def remind_eye_rest(self):
        """Метод для отслеживапния времени работы перед монитором и напоминание для глаз, чтобы сделать перерыв"""

        self.time_worked += 1

        # Напоминание чере каждые 20 минут
        if self.time_worked >= self.eye_rest_interval:
            self.time_worked = 0
            self.show_eye_rest_message()

    def show_eye_rest_message(self):
        """Показ уведомлений для перерыва для глаз"""
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Перерыв для глаз")
        msg.setText("Вы работаете уже 20 минут. Сделайте перерыв и посмотрите вдаль на 20 секунд.")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def check_back(self):
        """Метод для отслеживания осанки"""
        self.time_worked_back += 1
        if self.time_worked_back >= self.back_interval:
            self.time_worked_back = 0
            self.show_back()

    def show_back(self):
        """Показ уведомлений для перерыва для глаз"""
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Выпрямите осанку")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PomodoroApp()
    window.show()
    sys.exit(app.exec_())
