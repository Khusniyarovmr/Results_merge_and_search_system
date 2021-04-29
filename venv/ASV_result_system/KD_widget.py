# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(841, 141)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(0, 0, 840, 140))
        self.widget.setObjectName("widget")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_33 = QtWidgets.QLabel("№ Договора", self.widget)
        self.label_33.setGeometry(QtCore.QRect(10, 7, 110, 41))
        self.label_34 = QtWidgets.QLabel("Дата договора", self.widget)
        self.label_34.setGeometry(QtCore.QRect(120, 7, 131, 41))
        self.label_35 = QtWidgets.QLabel("Срок окончания\n договора", self.widget)
        self.label_35.setGeometry(QtCore.QRect(250, 7, 131, 41))
        self.label_35.setWordWrap(True)
        self.label_36 = QtWidgets.QLabel("Ставка", self.widget)
        self.label_36.setGeometry(QtCore.QRect(380, 7, 131, 41))
        self.label_37 = QtWidgets.QLabel("Просрочка по текущему\n платежу, дней", self.widget)
        self.label_37.setGeometry(QtCore.QRect(510, 7, 141, 41))
        self.label_37.setWordWrap(True)
        self.label_38 = QtWidgets.QLabel("Группа активов", self.widget)
        self.label_38.setGeometry(QtCore.QRect(650, 7, 101, 41))
        self.label_39 = QtWidgets.QLabel("Балансовая стоимость, руб.", self.widget)
        self.label_39.setGeometry(QtCore.QRect(10, 67, 110, 31))
        self.label_40 = QtWidgets.QLabel("Резерв, руб.", self.widget)
        self.label_40.setGeometry(QtCore.QRect(120, 67, 131, 31))
        self.label_41 = QtWidgets.QLabel("Сумма обеспечения,\n руб.", self.widget)
        self.label_41.setGeometry(QtCore.QRect(250, 67, 131, 31))
        self.label_41.setWordWrap(True)
        self.label_42 = QtWidgets.QLabel("Корректировка, руб.", self.widget)
        self.label_42.setGeometry(QtCore.QRect(380, 67, 131, 31))
        self.label_43 = QtWidgets.QLabel("Справедливая стоимость,\n руб.", self.widget)
        self.label_43.setWordWrap(True)
        self.label_43.setGeometry(QtCore.QRect(510, 67, 141, 31))
        self.label_44 = QtWidgets.QLabel("Действие", self.widget)
        self.label_44.setGeometry(QtCore.QRect(750, 7, 81, 41))

        list_of_labels = [self.label_33, self.label_34, self.label_35, self.label_36, self.label_37, self.label_38
            , self.label_39, self.label_40, self.label_41, self.label_42, self.label_43, self.label_44]
        for l in list_of_labels:
            l.setFont(font)
            l.setAlignment(QtCore.Qt.AlignCenter)
            l.setWordWrap(True)

        self.listView_31 = QtWidgets.QListView(self.widget)
        self.listView_31.setGeometry(QtCore.QRect(7, 46, 113, 22))
        self.listView_32 = QtWidgets.QListView(self.widget)
        self.listView_32.setGeometry(QtCore.QRect(119, 46, 131, 22))
        self.listView_33 = QtWidgets.QListView(self.widget)
        self.listView_33.setGeometry(QtCore.QRect(249, 46, 131, 22))
        self.listView_34 = QtWidgets.QListView(self.widget)
        self.listView_34.setGeometry(QtCore.QRect(379, 46, 131, 22))
        self.listView_35 = QtWidgets.QListView(self.widget)
        self.listView_35.setGeometry(QtCore.QRect(509, 46, 141, 22))
        self.listView_36 = QtWidgets.QListView(self.widget)
        self.listView_36.setGeometry(QtCore.QRect(7, 97, 113, 21))
        self.listView_37 = QtWidgets.QListView(self.widget)
        self.listView_37.setGeometry(QtCore.QRect(119, 97, 131, 21))
        self.listView_38 = QtWidgets.QListView(self.widget)
        self.listView_38.setGeometry(QtCore.QRect(249, 97, 131, 21))
        self.listView_39 = QtWidgets.QListView(self.widget)
        self.listView_39.setGeometry(QtCore.QRect(379, 97, 131, 21))
        self.listView_40 = QtWidgets.QListView(self.widget)
        self.listView_40.setGeometry(QtCore.QRect(509, 97, 141, 21))
        self.listView_41 = QtWidgets.QListView(self.widget)
        self.listView_41.setGeometry(QtCore.QRect(649, 46, 101, 72))
        list_of_listview = [self.listView_31, self.listView_32, self.listView_33, self.listView_34, self.listView_35
            , self.listView_36, self.listView_37, self.listView_38, self.listView_39, self.listView_40
            , self.listView_41]
        for l in list_of_listview:
            l.setFont(font)

        self.line = QtWidgets.QFrame(self.widget)
        self.line.setGeometry(QtCore.QRect(8, 39, 821, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2 = QtWidgets.QFrame(self.widget)
        self.line_2.setGeometry(QtCore.QRect(240, 7, 20, 110))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3 = QtWidgets.QFrame(self.widget)
        self.line_3.setGeometry(QtCore.QRect(370, 7, 20, 110))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4 = QtWidgets.QFrame(self.widget)
        self.line_4.setGeometry(QtCore.QRect(500, 7, 20, 110))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5 = QtWidgets.QFrame(self.widget)
        self.line_5.setGeometry(QtCore.QRect(640, 7, 20, 110))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6 = QtWidgets.QFrame(self.widget)
        self.line_6.setGeometry(QtCore.QRect(740, 7, 20, 110))
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7 = QtWidgets.QFrame(self.widget)
        self.line_7.setGeometry(QtCore.QRect(110, 7, 20, 110))
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8 = QtWidgets.QFrame(self.widget)
        self.line_8.setGeometry(QtCore.QRect(8, 60, 642, 16))
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9 = QtWidgets.QFrame(self.widget)
        self.line_9.setGeometry(QtCore.QRect(8, 90, 642, 16))
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10 = QtWidgets.QFrame(self.widget)
        self.line_10.setGeometry(QtCore.QRect(7, 113, 823, 11))
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_12 = QtWidgets.QFrame(self.widget)
        self.line_12.setGeometry(QtCore.QRect(820, 7, 20, 110))
        self.line_12.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_13 = QtWidgets.QFrame(self.widget)
        self.line_13.setGeometry(QtCore.QRect(9, 0, 820, 16))
        self.line_13.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_14 = QtWidgets.QFrame(self.widget)
        self.line_14.setGeometry(QtCore.QRect(0, 7, 16, 110))
        self.line_14.setFrameShape(QtWidgets.QFrame.VLine)
        list_of_lines = [self.line, self.line_2, self.line_3, self.line_4, self.line_5, self.line_6, self.line_7
            , self.line_8, self.line_9, self.line_10, self.line_12, self.line_13, self.line_14]
        for l in list_of_lines:
            l.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.pushButton_3 = QtWidgets.QPushButton("Подробнее", self.widget)
        self.pushButton_3.setGeometry(QtCore.QRect(755, 60, 68, 23))
        self.pushButton_3.setFont(font)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))


class KredDogovor(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)