import sys
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton, QApplication
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

StyleSheet = '''
QPushButton { border: none; }

#BlueButton {
    background-color: #2196f3;
    min-width:  96px;
    max-width:  96px;
    min-height: 96px;
    max-height: 96px;
    border-radius: 48px;        /* круглый */
}
'''

class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)

        layout = QHBoxLayout(self)
        pushButton_2 = QPushButton(self, objectName="BlueButton", minimumHeight=48)
        layout.addWidget(pushButton_2)
        iicon = QIcon('иконка_ОПЗ.png')
        size = QSize(96, 96)
        pushButton_2.setIcon(iicon)
        pushButton_2.setIconSize(size)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(StyleSheet)
    w = Window()
    w.show()
    sys.exit(app.exec_())