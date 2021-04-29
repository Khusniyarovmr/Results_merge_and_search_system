# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(700, 500)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setStyleSheet('''
                QMainWindow {
                    border-image: url(main_image.png) 0 0 0 0 stretch stretch;
                }''')
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ASV_image.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)

        self.centralwidget = QtWidgets.QWidget(MainWindow)

        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton = QtWidgets.QPushButton("Найти Банк", self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(210, 100, 280, 91))
        self.pushButton.setFont(font)
        self.pushButton_2 = QtWidgets.QPushButton("Поиск по параметрам", self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 208, 280, 91))
        self.pushButton_2.setFont(font)
        self.pushButton_3 = QtWidgets.QPushButton("Поиск по контрагентам", self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(210, 315, 280, 91))
        self.pushButton_3.setFont(font)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Система результатов проверки банков"))
