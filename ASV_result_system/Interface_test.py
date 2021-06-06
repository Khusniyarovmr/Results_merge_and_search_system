# -*- coding: utf-8 -*-

import os
import sys
import sqlite3

import keyboard
import psycopg2
from Client_card import ClientCardWindow
from ComboBox_ver_1 import ExtendedComboBox as excombo
from Dialog_bank_input import Ui_Dialog as BankInputDialog
from First_search_menu import Ui_FirstSearchMenu as SearchMenu
from Proect_window import Ui_ProectInfoWindow as ProectInfoWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from SearchFunction import Searching
from mainwindow import Ui_MainWindow as ProggrammMainMenu
from paragraph_show import Paragraph
from win32api import GetCursorPos

#con_to_DB = psycopg2.connect(database="New_system_ASV", user="postgres", password="qwerty", host="127.0.0.1",
#                             port="5432")
con_to_DB = sqlite3.connect('asv_db.db')

# con_to_DB = psycopg2.connect(database="ASV_Stress_Test_db", user="postgres", password="qwerty", host="127.0.0.1",
#                            port="5432")


class MyMainWindow(QtWidgets.QMainWindow, ProggrammMainMenu):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.B_1_clicked)
        self.pushButton_2.clicked.connect(self.B_2_clicked)
        self.pushButton_3.clicked.connect(self.B_3_clicked)

    def B_1_clicked(self):
        self.hide()
        self.first_dialog = FirstDialogWindow()
        self.first_dialog.show()

    def B_2_clicked(self):
        self.hide()
        self.Search_menu = FirstSearchMenu()
        self.Search_menu.show()

    def B_3_clicked(self):
        pass

    def closeEvent(self, event):
        con_to_DB.close()
        sys.exit(0)


class FirstDialogWindow(QtWidgets.QDialogButtonBox, BankInputDialog):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.b_info = ProectInfo()
        self.parent_win = MyMainWindow()
        self.buttonBox.accepted.connect(self.OK_button)
        self.buttonBox.rejected.connect(self.Cancel_button)
        self.combo = excombo(self)
        self.combo.setGeometry(QtCore.QRect(20, 60, 301, 22))
        self.combo.addItems(sorted(self.get_bank_names()))
        self.combo.activated[str].connect(self.buttonBox.setFocus)

    def OK_button(self):
        self.hide()
        self.b_info.bank_name = self.combo.currentText()
        self.b_info.show()

    def Cancel_button(self):
        self.hide()
        self.parent_win.show()

    def closeEvent(self, event):
        self.parent_win.show()

    def get_bank_names(self):
        cur = con_to_DB.cursor()
        cur.execute("SELECT small_name FROM banks")
        spisok_bankov = []
        rows = cur.fetchall()
        cur.close()
        for row in rows:
            spisok_bankov.append(row[0])
        return spisok_bankov


class ProectInfo(QtWidgets.QMainWindow, ProectInfoWindow):
    bank_name = ''

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.parent_win = MyMainWindow()
        self.stroka_bank_info = []

    def showEvent(self, a0: QtGui.QShowEvent):
        if self.stroka_bank_info == []:
            self.stroka_bank_info = self.choice_but_icon_and_link(self.bank_name)
            self.listWidget.addItem(self.stroka_bank_info[0][1])  # Полное наименование.
            self.listWidget_2.addItem(self.stroka_bank_info[0][2])  # Краткое наименование.
            self.listWidget_3.addItem(self.stroka_bank_info[0][3])  # ИНН.
            self.listWidget_4.addItem(self.stroka_bank_info[0][4])  # Регистрационный номер.
            self.listWidget_5.addItem(self.stroka_bank_info[0][5])  # Дата отзыва.
            self.listWidget_6.addItem(self.stroka_bank_info[0][6])  # Текущий статус.
            self.listWidget_7.addItem(self.stroka_bank_info[0][7])  # Филиалы.
            self.listWidget_8.addItem(self.stroka_bank_info[0][8])  # Адрес регистрации.
            self.listWidget_9.addItem(self.stroka_bank_info[0][10])  # Ответственный за проект.
            self.listWidget_10.addItem(self.stroka_bank_info[0][11])  # Исследуемый период.
            self.listWidget_11.addItem(self.stroka_bank_info[0][12])  # Дата КП.
            self.listWidget_12.addItem(self.stroka_bank_info[0][13])  # Дата утверждения.
            self.listWidget_13.addItem(self.stroka_bank_info[0][14])  # Вид проверки.

            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap("OK.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            icon2 = QtGui.QIcon()
            icon2.addPixmap(QtGui.QPixmap("Cancel.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

            if self.stroka_bank_info[0][20] != '':  #
                self.pushButton.setIcon(icon1)
                self.pushButton.clicked.connect(self.PB_1_clicked)
            else:
                self.pushButton.setIcon(icon2)
                self.pushButton.setEnabled(False)
            if self.stroka_bank_info[0][18] != '':  #
                self.pushButton_2.setIcon(icon1)
                self.pushButton_2.clicked.connect(self.PB_2_clicked)
            else:
                self.pushButton_2.setIcon(icon2)
                self.pushButton_2.setEnabled(False)
            if self.stroka_bank_info[0][16] != '':  #
                self.pushButton_3.setIcon(icon1)
                self.pushButton_3.clicked.connect(self.PB_3_clicked)
            else:
                self.pushButton_3.setIcon(icon2)
                self.pushButton_3.setEnabled(False)
            if self.stroka_bank_info[0][17] != '':  #
                self.pushButton_4.setIcon(icon1)
                self.pushButton_4.clicked.connect(self.PB_4_clicked)
            else:
                self.pushButton_4.setIcon(icon2)
                self.pushButton_4.setEnabled(False)
            if self.stroka_bank_info[0][15] != '':  #
                self.pushButton_5.setIcon(icon1)
                self.pushButton_5.clicked.connect(self.PB_5_clicked)
            else:
                self.pushButton_5.setIcon(icon2)
                self.pushButton_5.setEnabled(False)
            if self.stroka_bank_info[0][19] != '':  #
                self.pushButton_6.setIcon(icon1)
                self.pushButton_6.clicked.connect(self.PB_6_clicked)
            else:
                self.pushButton_6.setIcon(icon2)
                self.pushButton_6.setEnabled(False)
            if self.stroka_bank_info[0][21] != '':  #
                self.pushButton_7.setIcon(icon1)
                self.pushButton_7.clicked.connect(self.PB_7_clicked)
            else:
                self.pushButton_7.setIcon(icon2)
                self.pushButton_7.setEnabled(False)
            if self.stroka_bank_info[0][22] != '':  #
                self.pushButton_8.setIcon(icon1)
                self.pushButton_8.clicked.connect(self.PB_8_clicked)
            else:
                self.pushButton_8.setIcon(icon2)
                self.pushButton_8.setEnabled(False)
            if self.stroka_bank_info[0][23] != '':  #
                self.pushButton_9.setIcon(icon1)
                self.pushButton_9.clicked.connect(self.PB_9_clicked)
            else:
                self.pushButton_9.setIcon(icon2)
                self.pushButton_9.setEnabled(False)

    # Динамика и структура балансовых показателей
    def PB_1_clicked(self):
        os.startfile(self.stroka_bank_info[0][20], 'open')

    # динамика и структура основных активов банка (выборка)
    def PB_2_clicked(self):
        os.startfile(self.stroka_bank_info[0][18], 'open')

    # Анализ целевого использования кредитных средств
    def PB_3_clicked(self):
        os.startfile(self.stroka_bank_info[0][16], 'open')

    # Информация о платежах в Федеральный Бюджеу РФ (налоги)
    def PB_4_clicked(self):
        os.startfile(self.stroka_bank_info[0][17], 'open')

    # Заключение ВОБ
    def PB_5_clicked(self):
        os.startfile(self.stroka_bank_info[0][15], 'open')

    # Отчет о состоянии переданных Агентству данных
    def PB_6_clicked(self):
        os.startfile(self.stroka_bank_info[0][19], 'open')

    # Отчет аналитического блока
    def PB_7_clicked(self):
        os.startfile(self.stroka_bank_info[0][21], 'open')

    # Мастер-файл
    def PB_8_clicked(self):
        os.startfile(self.stroka_bank_info[0][22], 'open')

    # Прочие документы
    def PB_9_clicked(self):
        os.startfile(self.stroka_bank_info[0][23], 'open')

    def closeEvent(self, event):
        self.parent_win.show()

    def choice_but_icon_and_link(self, b_name):
        cur = con_to_DB.cursor()
        cur.execute(
            "SELECT * FROM banks, bank_information WHERE bank_information.bank_id = banks.id and banks.small_name=" + str(
                "'" + b_name + "'"))
        file_info = cur.fetchall()
        cur.close()
        return file_info


class FirstSearchMenu(QtWidgets.QMainWindow, SearchMenu):
    dannie_for_cc = []
    data_for_paragraph = []

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.width = self.size().width()
        self.height = self.size().height()
        self.len_of_cell_string_0 = int(self.centralwidget.geometry().width() / 13)
        self.len_of_cell_string_1 = int(self.centralwidget.geometry().width() / 13)
        self.pushButton.clicked.connect(self.PB_click_for_search)
        self.pushButton.setAutoDefault(True)
        self.lineEdit.returnPressed.connect(self.pushButton.click)
        self.tableWidget.itemDoubleClicked.connect(self.on_cell_item_Dclicked)
        self.tableWidget.itemClicked.connect(self.on_cell_item_clicked)
        self.par = Paragraph()
        self.Searching = Searching()
        self.Searching.status_mes[str].connect(self.status_bar_update)
        self.Searching.spisokList[list].connect(self.spisok_znacheniy)
        self.parent_win = MyMainWindow()

    def PB_click_for_search(self):
        if self.pushButton.text() == 'Найти':
            self.pushButton.setText('Стоп')
            self.tableWidget.setRowCount(0)
            self.Searching.working = True
            self.Searching.interested_text = self.lineEdit.text()
            self.Searching.start()
            self.Searching.data_for_table[list].connect(self.table_data_update)
            self.Searching.finished.connect(self.okonchanie_potoka)
        else:
            self.pushButton.setText('Найти')
            self.Searching.working = False

    def okonchanie_potoka(self):
        try:
            self.Searching.data_for_table[list].disconnect()
        except TypeError:
            pass
        self.pushButton.setText('Найти')

    def status_bar_update(self, message):
        self.statusBar().showMessage(message)

    def spisok_znacheniy(self, spisok):
        self.data_for_paragraph = spisok

    def on_cell_item_clicked(self, item):
        if keyboard.is_pressed('ctrl'):
            if (item.column() == 7 or item.column() == 8) and item.text() != '':
                self.par.paragraph_text(item.text(), self.data_for_paragraph)
                pos = GetCursorPos()
                self.par.move(pos[0], pos[1])
                self.par.show()

    def on_cell_item_Dclicked(self, item):
        if (
                item.column() == 1 or item.column() == 2) and item.text() != '':  # Наименование\ФИО - тут будет кнопка при множественном совпадении
            self.CCWindow = ClientCardWindow()
            self.CCWindow.data_for_client_card = self.dannie_for_cc
            self.CCWindow.row_number_click = item.row()
            self.CCWindow.show()

        elif item.column() == 3 and item.text() != '':  # Паспорт Серия\номер - заполняется при единственном совпадении
            pass
        elif item.column() == 4 and item.text() != '':  # Клиент\заемщик - заполняется при единственном совпадении
            pass
        elif item.column() == 5 and item.text() != '':  # Оценка
            pass
        elif item.column() == 6 and item.text() != '':  # Бенефициар
            pass
        elif item.column() == 7 and item.text() != '':  # Заключение - заполняется при единственном совпадении
            os.startfile(item.text(), 'open')
        elif item.column() == 8 and item.text() != '':  # Отчет АБ
            os.startfile(item.text(), 'open')
        elif item.column() == 9 and item.text() != '':  # Выборка - заполняется при единственном совпадении
            os.startfile(item.text(), 'open')
        elif item.column() == 10 and item.text() != '':  # Целевое - заполняется при единственном совпадении
            os.startfile(item.text(), 'open')
        elif item.column() == 11 and item.text() != '':  # Мастер_файл
            os.startfile(item.text(), 'open')

    def table_data_update(self, string_for_table):
        self.dannie_for_cc = string_for_table
        self.tableWidget.setRowCount(len(string_for_table))
        for k in range(len(string_for_table)):
            for i in range(0, 12):
                self.tableWidget.setItem(k, i, QtWidgets.QTableWidgetItem(string_for_table[k][i]))
                if i == 1:
                    self.tableWidget.setRowHeight(k, int(self.tableWidget.sizeHintForRow(k)))

        # Меняем цвет в столбце оценки в зависимости от оценки
        for i in range(self.tableWidget.rowCount()):
            self.tableWidget.item(i, 5).setFont(QtGui.QFont("TimesNewRoman", 10, QtGui.QFont.Bold))
            if self.tableWidget.item(i, 5).text() == 'Р':
                self.tableWidget.item(i, 5).setForeground(QtGui.QColor("#00ff00"))
            elif self.tableWidget.item(i, 5).text() == 'С':
                self.tableWidget.item(i, 5).setForeground(QtGui.QColor("#ffaa00"))
            elif self.tableWidget.item(i, 5).text() == 'Т':
                self.tableWidget.item(i, 5).setForeground(QtGui.QColor("#ff0000"))

        # проставляем виджеты с зеленым фоном для некоторых столбцов
        last_row = self.tableWidget.rowCount()
        for i in range(last_row):
            for j in range(7, 12):
                label_for_widget = QtWidgets.QLabel('', self)
                label_for_widget.setStyleSheet("background-color: green;")
                if not self.tableWidget.item(i, j).text() == '':
                    self.tableWidget.setCellWidget(i, j, label_for_widget)

    def closeEvent(self, event):
        self.parent_win.show()

    def resizeEvent(self, event):
        koefH = 60 * ((self.centralwidget.geometry().height() / self.height))
        if koefH < 60: koefH = 60
        self.gridLayout.setContentsMargins(10, int(koefH), 10, 10)
        for i in range(0, 12):
            self.tableWidget.setColumnWidth(i, int((self.centralwidget.geometry().width() - 30) / 12))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    win = MyMainWindow()
    win.show()
    sys.exit(app.exec_())
