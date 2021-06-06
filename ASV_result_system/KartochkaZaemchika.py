# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from win32api import GetSystemMetrics

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        self.width = GetSystemMetrics(0)
        self.height = GetSystemMetrics(1)
        if self.height > 769:
            self.K = 1
        else:
            self.K = 0.71
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(777, 834*self.K)
        Dialog.setWindowTitle("Карточка заемщика ")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ASV_image.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox = QtWidgets.QGroupBox("Описание деятельности заемщика", Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 0, 760, 161*self.K))
        self.groupBox.setFont(font)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.listWidget = QtWidgets.QListWidget(self.groupBox)
        self.listWidget.setGeometry(QtCore.QRect(0, 20, 760, 141*self.K))
        self.listWidget.setWordWrap(True)
        self.listWidget.setTextElideMode(QtCore.Qt.ElideNone)
        self.listWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.listWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)

        self.groupBox_2 = QtWidgets.QGroupBox("Вывод по ссуде", Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 670*self.K, 760, 161*self.K))
        self.groupBox_2.setFont(font)
        self.groupBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.listWidget_2 = QtWidgets.QListWidget(self.groupBox_2)
        self.listWidget_2.setGeometry(QtCore.QRect(0, 20, 760, 141*self.K))
        self.listWidget_2.setWordWrap(True)
        self.listWidget_2.setTextElideMode(QtCore.Qt.ElideNone)
        self.listWidget_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.listWidget_2.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.groupBox_3 = QtWidgets.QGroupBox("Целевое использование средств", Dialog)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 520*self.K, 761, 150*self.K))
        self.groupBox_3.setFont(font)
        self.groupBox_3.setAlignment(QtCore.Qt.AlignCenter)
        self.listWidget_3 = QtWidgets.QListWidget(self.groupBox_3)
        self.listWidget_3.setGeometry(QtCore.QRect(0, 20, 760, 130*self.K))
        self.listWidget_3.setWordWrap(True)
        self.listWidget_3.setTextElideMode(QtCore.Qt.ElideNone)
        self.listWidget_3.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.listWidget_3.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)

        self.groupBox_5 = QtWidgets.QGroupBox("Анализ финансового положения", Dialog)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 160*self.K, 411, 361*self.K))
        self.groupBox_5.setFont(font)
        self.groupBox_5.setAlignment(QtCore.Qt.AlignCenter)
        self.listWidget_4 = QtWidgets.QListWidget(self.groupBox_5)
        self.listWidget_4.setGeometry(QtCore.QRect(0, 20, 410, 341*self.K))
        self.listWidget_4.setWordWrap(True)
        self.listWidget_4.setTextElideMode(QtCore.Qt.ElideNone)
        self.listWidget_4.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.listWidget_4.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)

        label_3_font = QtGui.QFont()
        label_3_font.setPointSize(8)
        label_3_font.setBold(True)
        label_3_font.setItalic(True)
        self.groupBox_7 = QtWidgets.QGroupBox("Бухгалтерская отчетность", Dialog)
        self.groupBox_7.setGeometry(QtCore.QRect(430, 160*self.K, 341, 361*self.K))
        self.groupBox_7.setFont(font)
        self.groupBox_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label = QtWidgets.QLabel("Источник данных: ", self.groupBox_7)
        self.label.setGeometry(QtCore.QRect(10, 20, 341, 20))
        self.label_2 = QtWidgets.QLabel("Дата отчетности: ", self.groupBox_7)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 271, 20))
        self.label_3 = QtWidgets.QLabel("тыс. руб.", self.groupBox_7)
        self.label_3.setGeometry(QtCore.QRect(260, 40, 70, 20))
        self.label_3.setAlignment(QtCore.Qt.AlignLeft)
        self.label_3.setFont(label_3_font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_30 = QtWidgets.QLabel("Результаты деятельности", self.groupBox_7)
        self.label_30.setGeometry(QtCore.QRect(10, 280*self.K, 321, 20))

        TW_font = QtGui.QFont()
        TW_font.setPointSize(8)
        TW_font.setBold(False)
        TW_font.setItalic(False)
        TW_font_special = QtGui.QFont()
        TW_font_special.setPointSize(10)
        TW_font_special.setBold(True)
        TW_font_special.setItalic(False)
        self.tableView = QtWidgets.QTableView(self.groupBox_7)
        self.tableView.setFont(TW_font)
        self.tableView.setGeometry(QtCore.QRect(10, 60, 321, 208*self.K))
        self.tableView.verticalHeader().setVisible(False)
        self.tableView.horizontalHeader().setVisible(False)
        self.tableView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        model = QtGui.QStandardItemModel(Dialog)
        str_1 = ['АКТИВЫ', 'Основные средства', 'Запасы', 'Дебиторская задолженность', 'Финансовые вложения',
                 'Денежные средства', 'Прочие активы', 'ПАССИВЫ', 'Капитал и резервы', 'Кредиты и займы',
                 'Кредиторская задолженность', 'Прочие обязательства']
        str_2 = ['', '', '', '', '', '', '', '', '', '', '', '']
        for i in range(len(str_1)):
            col_0_item = QtGui.QStandardItem(str_1[i])
            col_1_item = QtGui.QStandardItem(str_2[i])
            if i == 0 or i == 7:
                col_0_item.setFont(TW_font_special)
            model.appendRow([col_0_item, col_1_item])
        self.tableView.setModel(model)
        self.tableView.setColumnWidth(0, 201)
        self.tableView.setColumnWidth(1, 119)
        self.tableView.resizeRowsToContents()

        self.tableView_2 = QtWidgets.QTableView(self.groupBox_7)
        self.tableView_2.setGeometry(QtCore.QRect(10, 300*self.K, 321, 36*self.K))
        self.tableView_2.verticalHeader().setVisible(False)
        self.tableView_2.horizontalHeader().setVisible(False)
        self.tableView_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableView_2.setFont(TW_font)
        model_2 = QtGui.QStandardItemModel(Dialog)
        str_1 = ['Выручка', 'EBITDA, приведенная к годовой']
        str_2 = ['', '']
        for i in range(len(str_1)):
            col_0_item = QtGui.QStandardItem(str_1[i])
            col_1_item = QtGui.QStandardItem(str_2[i])
            model_2.appendRow([col_0_item, col_1_item])
        self.tableView_2.setModel(model_2)
        self.tableView_2.setColumnWidth(0, 201)
        self.tableView_2.setColumnWidth(1, 119)
        self.tableView_2.resizeRowsToContents()
        QtCore.QMetaObject.connectSlotsByName(Dialog)


class ZaemchikCard(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    win = ZaemchikCard()
    win.show()
    sys.exit(app.exec_())