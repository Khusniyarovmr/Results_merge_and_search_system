import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.Qt import QTransform
from PyQt5 import Qt, QtCore


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 image - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.angle = 0
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create widget
        self.label = QLabel(self)
        self.pixmap = QPixmap("ASV_image.png")
        self.label.setPixmap(self.pixmap)


    def keyPressEvent(self, event):
        # on any key
        self.angle += 45 if event.key() == QtCore.Qt.Key_Down else -45
        t = QTransform().rotate(self.angle)
        self.label.setPixmap(self.pixmap.transformed(t))
        #return super().keyPressEvent(event)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    ex.move(app.desktop().screen().rect().center() - ex.rect().center())
    sys.exit(app.exec_())