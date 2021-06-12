import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
import design
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication, QProgressBar

import connection
import Controller
import DataBase


class Windowed_application(QtWidgets.QMainWindow, Controller.ConnectWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна




def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Windowed_application()
    window.setWindowIcon(QIcon('orig.ico'))
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()цию main()

