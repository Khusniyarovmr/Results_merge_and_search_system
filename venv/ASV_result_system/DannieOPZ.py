# -*- coding: utf-8 -*-

import sys

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(792, 704)
        Dialog.setWindowTitle("Данные ОПЗ по заемщику")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ASV_image.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(1, 1, 791, 461))
        self.tableWidget.setTextElideMode(QtCore.Qt.ElideNone)
        self.tableWidget.setRowCount(47)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(["Категория", "Характеристики", "Данные анализа"])
        self.tableWidget.resizeRowsToContents()
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 337)
        self.tableWidget.setColumnWidth(2, 337)

        for i in range(47):
            item = QtWidgets.QTableWidgetItem()
            item.setFlags(QtCore.Qt.ItemIsEnabled)
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tableWidget.setItem(i, 0, item)

        self.tableWidget.item(0, 0).setText("Финансовое положение")
        self.tableWidget.item(5, 0).setText("Качество обслуживания долга")
        self.tableWidget.item(10, 0).setText("Иные существенные факторы (экономические)")
        self.tableWidget.item(20, 0).setText("Связанность")
        self.tableWidget.item(24, 0).setText("Иные существенные факторы (юридические)")
        self.tableWidget.item(37, 0).setText("Негативная информация в отношении заемщика")
        self.tableWidget.item(44, 0).setText("ИП в конкурсное производство")
        span_list1 = [0, 5, 10, 20, 24, 37, 44]
        span_list2 = [5, 5, 10, 4, 13, 7, 3]
        for i in range(len(span_list1)):
            self.tableWidget.setSpan(span_list1[i], 0, span_list2[i], 1)

        for i in range(47):
            item = QtWidgets.QTableWidgetItem()
            item.setFlags(QtCore.Qt.ItemIsEnabled)
            self.tableWidget.setItem(i, 1, item)
        n_rows = [0, 2, 3, 4, 19, 26, 28, 29, 32, 33, 34, 36, 37, 38, 40, 41]
        for i in n_rows:
            self.tableWidget.setRowHeight(i, 35)
        self.tableWidget.item(0, 1).setText(
            "Оценка финансового положения на момент образования первоначальной задолженности и в период кредитования в банке")
        self.tableWidget.item(1, 1).setText("Признаки недостоверности бухгалтерской отчетности")
        self.tableWidget.item(2, 1).setText("Наличие иных негативных факторов финансового положения")
        self.tableWidget.item(3, 1).setText("Наличие в распоряжении рабочей группы отчетности из органов ФНС")
        self.tableWidget.item(4, 1).setText("Отчетность из органов статистики СПАРК у рабочей группы отсутствовала")
        self.tableWidget.item(5, 1).setText("Признаки рефинансирования основого долга")
        self.tableWidget.item(6, 1).setText("Признаки рефинансирования процентов")
        self.tableWidget.item(7, 1).setText("Долг не обслуживается после д.о.л.")
        self.tableWidget.item(8, 1).setText("Плохое качество обслуживания долга по 254-П (590-П)")
        self.tableWidget.item(9, 1).setText("Иные негативные факторы при обслуживания долга")
        self.tableWidget.item(10, 1).setText("Уплата налогов")
        self.tableWidget.item(11, 1).setText("Уплата арендных платежей")
        self.tableWidget.item(12, 1).setText("Платежи, связанные с содержанием персонала")
        self.tableWidget.item(13, 1).setText("Прочие обязательные платежи")
        self.tableWidget.item(14, 1).setText("Наличие счетов в других КО")
        self.tableWidget.item(15, 1).setText("Наличие непроанализированных счетов в других банках")
        self.tableWidget.item(16, 1).setText("Участие в схемных операциях")
        self.tableWidget.item(17, 1).setText("Характер платежей в период кредитования")
        self.tableWidget.item(18, 1).setText("Нецелевое использование кредитных средств")
        self.tableWidget.item(19, 1).setText("Высокая зависимость от кредитных средств банка (более 40% от оборотов)")
        self.tableWidget.item(20, 1).setText("Наличие экономических связей с банком")
        self.tableWidget.item(21, 1).setText("Наличие юридических связей с банком")
        self.tableWidget.item(22, 1).setText("Наличие экономических связей с другими заемщиками")
        self.tableWidget.item(23, 1).setText("Наличие юридических связей с другими заемщиками")
        self.tableWidget.item(24, 1).setText("Адрес массовой регистрации")
        self.tableWidget.item(25, 1).setText("Адрес является массовым согласно ответу из ФНС")
        self.tableWidget.item(26, 1).setText(
            "Ненадлежащая форма договора аренды помещений для предоставления юр. адреса")
        self.tableWidget.item(27, 1).setText("Регистрация в квартире")
        self.tableWidget.item(28, 1).setText(
            "Отсутствие заемщика по месту нахождения, указанному в учредительных документах")
        self.tableWidget.item(29, 1).setText("Теелфон указан в документах нескольких юридических лиц")
        self.tableWidget.item(30, 1).setText("Отсутствие сайта или неработающий сайт")
        self.tableWidget.item(31, 1).setText("Уставный капитал (в тыс. руб.)")
        self.tableWidget.item(32, 1).setText("Массовый директор (>10 организаций) на дату выдачи 1 кредита")
        self.tableWidget.item(33, 1).setText("Массовый участник (>10 организаций) на дату выдачи 1 кредита")
        self.tableWidget.item(34, 1).setText("Совпадение директора и единственного участника в одном лице на дату")
        self.tableWidget.item(35, 1).setText("Отсутствие в штате должности главного бухгалтера")
        self.tableWidget.item(36, 1).setText(
            "Среднесписочная численность на 01 января предшествующего года по данным ФНС")
        self.tableWidget.item(37, 1).setText("Признана ранее техническиой в ходе проверок обстоятельств банкротства")
        self.tableWidget.item(38, 1).setText("Наличие негативной информации в Актах/Предписаниях банка")
        self.tableWidget.item(39, 1).setText("Наличие негативной информации в СМИ")
        self.tableWidget.item(40, 1).setText(
            "Заемщик является недействующей организацией или находится в процессе ликвидации")
        self.tableWidget.item(41, 1).setText("В отношении заемщика инициирована процедура банкротства")
        self.tableWidget.item(42, 1).setText("Заемщик фигурирует в уголовном деле")
        self.tableWidget.item(43, 1).setText("Налоговые правонарушения в проверяемый период")
        self.tableWidget.item(44, 1).setText("Невозможно установить местонахождение должника или имущества по результатам ИП")
        self.tableWidget.item(45, 1).setText("У должника отсутствует имущество по результатам ИП")
        self.tableWidget.item(46, 1).setText("У должника не выявлено имущество в ходе КП")
        for i in range(47):
            item = QtWidgets.QTableWidgetItem()
            item.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEditable)
            self.tableWidget.setItem(i, 2, item)
        self.tableWidget.verticalHeader().setVisible(False)

        self.groupBox = QtWidgets.QGroupBox("Важная информация", Dialog)
        self.groupBox.setGeometry(QtCore.QRect(1, 467, 789, 233))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        lwfont = QtGui.QFont()
        lwfont.setPointSize(8)
        lwfont.setBold(False)
        lwfont.setWeight(75)
        self.listView = QtWidgets.QListView(self.groupBox)
        self.listView.setGeometry(QtCore.QRect(0, 20, 789, 213))
        self.listView.setFont(lwfont)
        self.listView.setWordWrap(True)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


class DannieOPZ(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    win = DannieOPZ()
    win.show()
    sys.exit(app.exec_())
