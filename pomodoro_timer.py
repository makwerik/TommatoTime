from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 600)  # Устанавливаем размер окна

        # Применяем стили к MainWindow
        self.apply_styles(MainWindow)

        # Центральный виджет
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Главный вертикальный лейаут
        self.main_layout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.main_layout.setContentsMargins(20, 20, 20, 20)
        self.main_layout.setSpacing(20)
        self.main_layout.setObjectName("main_layout")

        # Таймер (центральный текст)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")  # Устанавливаем современный шрифт
        font.setPointSize(64)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)  # Центрируем текст
        self.label.setObjectName("label")
        self.main_layout.addWidget(self.label)

        # Горизонтальный лейаут для кнопок
        self.button_layout = QtWidgets.QHBoxLayout()
        self.button_layout.setSpacing(20)
        self.button_layout.setObjectName("button_layout")

        # Кнопка "Пуск"
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.button_layout.addWidget(self.pushButton_3)

        # Кнопка "Пауза"
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.button_layout.addWidget(self.pushButton_2)

        # Кнопка "Сброс"
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.button_layout.addWidget(self.pushButton)

        self.main_layout.addLayout(self.button_layout)

        # Разделитель
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.main_layout.addWidget(self.line)

        # Заголовок напоминаний о здоровье
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.main_layout.addWidget(self.label_2)

        # GridLayout для чекбоксов
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName("gridLayout")

        # Чекбокс "Упражнение для глаз"
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 0, 0)

        # Чекбокс "Осанка"
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout.addWidget(self.checkBox_2, 1, 0)

        # Чекбокс "Напоминание о близости к экрану"
        self.checkBox_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout.addWidget(self.checkBox_4, 3, 0)

        self.main_layout.addLayout(self.gridLayout)

        # Устанавливаем центральный виджет
        MainWindow.setCentralWidget(self.centralwidget)

        # Меню и статус бар
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # Перевод текста элементов интерфейса
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        """Функция для установки текста элементов интерфейса"""
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pomodoro Timer"))
        self.label.setText(_translate("MainWindow", "60:00"))
        self.pushButton_3.setText(_translate("MainWindow", "Пуск"))
        self.pushButton_2.setText(_translate("MainWindow", "Пауза"))
        self.pushButton.setText(_translate("MainWindow", "Сброс"))
        self.label_2.setText(_translate("MainWindow", "Укажите, о чём вам напоминать во время работы?"))
        self.checkBox.setText(_translate("MainWindow", "Упражнение для глаз, каждые 20 минут"))
        self.checkBox_2.setText(_translate("MainWindow", "Контроль осанки, каждые 10 минут"))
        self.checkBox_4.setText(_translate("MainWindow", "Напоминание о близости к экрану (функция в разработке)"))

    def apply_styles(self, MainWindow):
        MainWindow.setStyleSheet("""
            QWidget {
                background-color: #f5f5f5;
                font-family: 'Segoe UI', sans-serif;
            }
            QLabel#label {
                color: #333333;
            }
            QLabel#label_2 {
                color: #555555;
            }
            QPushButton {
                background-color: #00BCD4;
                border: none;
                color: white;
                padding: 12px;
                text-align: center;
                font-size: 16px;
                border-radius: 12px;
            }
            QPushButton:hover {
                background-color: #0097A7;
            }
            QPushButton:pressed {
                background-color: #00796B;
            }
            QProgressBar {
                border: 1px solid #ced4da;
                border-radius: 10px;
                background-color: #e9ecef;
            }
            QProgressBar::chunk {
                background-color: #00BCD4;
                border-radius: 10px;
            }
            QCheckBox {
                font-size: 14px;
                color: #333333;
            }
            QFrame {
                background-color: #dee2e6;
            }
        """)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    # Устанавливаем стиль Fusion для более современного вида
    app.setStyle('Fusion')
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
