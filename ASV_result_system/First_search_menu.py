# -*- coding: utf-8 -*-

import sys
import csv
import io
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FirstSearchMenu(object):
    def setupUi(self, MainWindow):
        MainWindow.resize(700, 400)
        MainWindow.setWindowTitle("Поиск информации по параметрам")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ASV_image.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setFixedSize(QtCore.QSize(300, 20))
        self.pushButton = QtWidgets.QPushButton("Найти", self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setFixedSize(QtCore.QSize(130, 30))
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setRowCount(8)
        self.tableWidget.setColumnCount(12)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(140)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Interactive)
        self.tableWidget.setTextElideMode(QtCore.Qt.ElideNone)
        self.tableWidget.setHorizontalHeaderLabels(
            ["Банк", "Наименование\ФИО", "ИНН", "Паспорт_Серия\номер", "Клиент\Заемщик", "Оценка",
             "Бенефициар", "Заключение", 'Отчет АБ', "Выборка", "Целевое", 'Мастер_файл'])
        self.tableWidget.setWordWrap(True)
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2 = QtWidgets.QHBoxLayout()
        self.gridLayout_3 = QtWidgets.QHBoxLayout()
        self.gridLayout_2.addWidget(self.lineEdit)
        self.gridLayout_3.addWidget(self.pushButton)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_3, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.tableWidget, 2, 0, 1, 1)
        self.gridLayout.setVerticalSpacing(30)
        self.status_bar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.status_bar)
        MainWindow.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.tableWidget.installEventFilter(self)

    # add event filter
    def eventFilter(self, source, event):
        if (event.type() == QtCore.QEvent.KeyPress and
                event.matches(QtGui.QKeySequence.Copy)):
            self.copySelection()
            return True
        return self.eventFilter(source, event)

    # add copy method
    def copySelection(self):
        selection = self.tableWidget.selectedIndexes()
        if selection:
            rows = sorted(index.row() for index in selection)
            columns = sorted(index.column() for index in selection)
            rowcount = rows[-1] - rows[0] + 1
            colcount = columns[-1] - columns[0] + 1
            table = [[''] * colcount for _ in range(rowcount)]
            for index in selection:
                row = index.row() - rows[0]
                column = index.column() - columns[0]
                table[row][column] = index.data()
            stream = io.StringIO()
            csv.writer(stream, delimiter='\t').writerows(table)
            QtWidgets.qApp.clipboard().setText(stream.getvalue())

class FSM(QtWidgets.QMainWindow, Ui_FirstSearchMenu):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    win = FSM()
    win.show()
    sys.exit(app.exec_())