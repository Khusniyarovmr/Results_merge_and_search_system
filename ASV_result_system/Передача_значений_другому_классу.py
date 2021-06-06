import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal


class MainWindow(QMainWindow):
    login_data = pyqtSignal(str, str)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        uic.loadUi("main_window.ui", self)
        self.sec = SecondWindow(self)
        self.pushButton.clicked.connect(self.on_click)
        self.pushButton_2.clicked.connect(self.send_data)

    def on_click(self):
        self.sec.show()
        self.hide()

    def send_data(self):
        self.login_data.emit(self.lineEdit.text(), self.lineEdit_2.text())



class SecondWindow(QMainWindow):
    def __init__(self, root, **kwargs):
        super().__init__(root, **kwargs)
        uic.loadUi("second_window.ui", self)
        self.fist = root
        self.fist.login_data[str, str].connect(self.handle_input)

    def handle_input(self, name, login):
        self.label.setText(name)
        self.label_2.setText(login)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())
