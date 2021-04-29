# -*- coding: utf-8 -*-

from ctypes import *

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ProectInfoWindow(object):
    def setupUi(self, MainWindow):
        self.w = self.size().width()  # "определение ширины"
        self.h = self.size().height()  # "определение высоты"
        MainWindow.resize(640, 480)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ASV_image.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.label = QtWidgets.QLabel("Информация о проекте", self.centralwidget)  # Информация о проекте
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)  # Информация о проекте
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        # ----------------Виджет с вкладками-----------------------------------------
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setMinimumSize(QtCore.QSize(640, 480))
        self.tabWidget.setMaximumSize(
            QtCore.QSize(windll.user32.GetSystemMetrics(0), windll.user32.GetSystemMetrics(1)))
        self.tabWidget.setSizePolicy(
            QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding))
        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 1)
        # ----------------Общая информация-----------------------------------------
        self.tab = QtWidgets.QWidget()
        self.tabWidget.addTab(self.tab, "Общая информация")

        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2 = QtWidgets.QLabel("Проверяемый банк", self.tab)  # Проверяемый банк
        self.label_2.setFont(font)  # Проверяемый банк
        self.label_3 = QtWidgets.QLabel("Полное наименование", self.tab)  # Полное наименование банка
        self.label_4 = QtWidgets.QLabel("Краткое наименование", self.tab)  # Краткое наименование банка
        self.label_5 = QtWidgets.QLabel("ИНН", self.tab)  # ИНН банка
        self.label_6 = QtWidgets.QLabel("Регистрационный номер", self.tab)  # Рег номер банка
        self.label_7 = QtWidgets.QLabel("Дата отзыва лицензии", self.tab)  # Дата отзыва
        self.label_8 = QtWidgets.QLabel("Текущий статус", self.tab)  # Статус
        self.label_9 = QtWidgets.QLabel("Филиалы", self.tab)  # Филиалы
        self.label_10 = QtWidgets.QLabel("Адрес регистрации", self.tab)  # Адрес регистрации
        self.label_11 = QtWidgets.QLabel("Параметры проекта", self.tab)  # Инфо о проекте
        self.label_11.setFont(font)  # Инфо о проекте
        self.label_12 = QtWidgets.QLabel("Ответственный за проект", self.tab)  # Исполнитель
        self.label_13 = QtWidgets.QLabel("Исследуемый период", self.tab)  # Период
        self.label_14 = QtWidgets.QLabel("Дата утверждения", self.tab)  # Дата КП
        self.label_15 = QtWidgets.QLabel("Дата КП", self.tab)  # Дата утверждения
        self.label_16 = QtWidgets.QLabel("Вид проверки", self.tab)  # Вид проверки

        self.listWidget = QtWidgets.QListWidget(self.tab)  # Полное наименование
        self.listWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget.setFlow(QtWidgets.QListView.LeftToRight)
        self.listWidget_2 = QtWidgets.QListWidget(self.tab)  # Краткое наименование
        self.listWidget_2.setFlow(QtWidgets.QListView.LeftToRight)
        self.listWidget_3 = QtWidgets.QListWidget(self.tab)  # Краткое наименование
        self.listWidget_3.setFlow(QtWidgets.QListView.LeftToRight)
        self.listWidget_4 = QtWidgets.QListWidget(self.tab)  # Регистрационный номер
        self.listWidget_4.setFlow(QtWidgets.QListView.LeftToRight)
        self.listWidget_5 = QtWidgets.QListWidget(self.tab)  # Дата отзыва
        self.listWidget_5.setFlow(QtWidgets.QListView.LeftToRight)
        self.listWidget_6 = QtWidgets.QListWidget(self.tab)  # Статус
        self.listWidget_6.setFlow(QtWidgets.QListView.LeftToRight)
        self.listWidget_7 = QtWidgets.QListWidget(self.tab)  # Филиалы
        self.listWidget_7.setFlow(QtWidgets.QListView.LeftToRight)
        self.listWidget_8 = QtWidgets.QListWidget(self.tab)  # Адрес регистрации
        self.listWidget_8.setFlow(QtWidgets.QListView.LeftToRight)
        self.listWidget_8.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget_9 = QtWidgets.QListWidget(self.tab)  # Ответственный за проект
        self.listWidget_9.setFlow(QtWidgets.QListView.LeftToRight)
        self.listWidget_10 = QtWidgets.QListWidget(self.tab)  # Исследуемый период
        self.listWidget_10.setFlow(QtWidgets.QListView.LeftToRight)
        self.listWidget_11 = QtWidgets.QListWidget(self.tab)  # Дата утверждения
        self.listWidget_11.setFlow(QtWidgets.QListView.LeftToRight)
        self.listWidget_12 = QtWidgets.QListWidget(self.tab)  # Дата КП
        self.listWidget_12.setFlow(QtWidgets.QListView.LeftToRight)
        self.listWidget_13 = QtWidgets.QListWidget(self.tab)  # Вид проверки
        self.listWidget_13.setFlow(QtWidgets.QListView.LeftToRight)

        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setContentsMargins(20, 20, 20, 40)
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)
        self.gridLayout_2.addWidget(self.label_5, 3, 0, 1, 1)
        self.gridLayout_2.addWidget(self.label_6, 4, 0, 1, 1)
        self.gridLayout_2.addWidget(self.label_7, 5, 0, 1, 1)
        self.gridLayout_2.addWidget(self.label_8, 6, 0, 1, 1)
        self.gridLayout_2.addWidget(self.label_9, 7, 0, 1, 1)
        self.gridLayout_2.addWidget(self.label_10, 8, 0, 1, 1)
        self.gridLayout_2.addWidget(self.label_11, 9, 0, 1, 1)
        self.gridLayout_2.addWidget(self.label_12, 10, 0, 1, 1)
        self.gridLayout_2.addWidget(self.label_13, 11, 0, 1, 1)
        self.gridLayout_2.addWidget(self.label_14, 12, 0, 1, 1)
        self.gridLayout_2.addWidget(self.label_15, 13, 0, 1, 1)
        self.gridLayout_2.addWidget(self.label_16, 14, 0, 1, 1)
        self.gridLayout_2.addWidget(self.listWidget, 1, 1, 1, 1)
        self.gridLayout_2.addWidget(self.listWidget_2, 2, 1, 1, 1)
        self.gridLayout_2.addWidget(self.listWidget_3, 3, 1, 1, 1)
        self.gridLayout_2.addWidget(self.listWidget_4, 4, 1, 1, 1)
        self.gridLayout_2.addWidget(self.listWidget_5, 5, 1, 1, 1)
        self.gridLayout_2.addWidget(self.listWidget_6, 6, 1, 1, 1)
        self.gridLayout_2.addWidget(self.listWidget_7, 7, 1, 1, 1)
        self.gridLayout_2.addWidget(self.listWidget_8, 8, 1, 1, 1)
        self.gridLayout_2.addWidget(self.listWidget_9, 10, 1, 1, 1)
        self.gridLayout_2.addWidget(self.listWidget_10, 11, 1, 1, 1)
        self.gridLayout_2.addWidget(self.listWidget_11, 12, 1, 1, 1)
        self.gridLayout_2.addWidget(self.listWidget_12, 13, 1, 1, 1)
        self.gridLayout_2.addWidget(self.listWidget_13, 14, 1, 1, 1)
        # ----------------Выборка-----------------------------------------
        self.tab_2 = QtWidgets.QWidget()
        self.tabWidget.addTab(self.tab_2, "Выборка")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_3.setContentsMargins(20, 20, 20, 20)
        # ----------------Бенефициары-----------------------------------------
        self.tab_3 = QtWidgets.QWidget()
        self.tabWidget.addTab(self.tab_3, "Бенефициары")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_4.setContentsMargins(20, 20, 20, 20)
        # ----------------Сделки-----------------------------------------
        self.tab_4 = QtWidgets.QWidget()
        self.tabWidget.addTab(self.tab_4, "Сделки")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_5.setContentsMargins(20, 20, 20, 20)
        self.tableWidget = QtWidgets.QTableWidget(self.tab_4)
        self.gridLayout_5.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.tableWidget.setColumnCount(10)
        self.tableWidget.setRowCount(5)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(True)
        # ----------------Документы и файлы-----------------------------------------
        self.tab_5 = QtWidgets.QWidget()
        self.tabWidget.addTab(self.tab_5, "Документы и файлы")
        self.pushButton = QtWidgets.QPushButton("Динамика и структура балансовых показателей банка", self.tab_5)
        self.pushButton.setMaximumSize(QtCore.QSize(700, 30))
        self.pushButton_2 = QtWidgets.QPushButton("Динамика и структура основных активов банка (выборка)", self.tab_5)
        self.pushButton_2.setMaximumSize(QtCore.QSize(700, 30))
        self.pushButton_3 = QtWidgets.QPushButton("Анализ целевого использования кредитных средств", self.tab_5)
        self.pushButton_3.setMaximumSize(QtCore.QSize(700, 30))
        self.pushButton_4 = QtWidgets.QPushButton(
            "Информация о платежах в Федеральный Бюджет РФ, в т.ч. налоговые платежи", self.tab_5)
        self.pushButton_4.setMaximumSize(QtCore.QSize(700, 30))
        self.pushButton_5 = QtWidgets.QPushButton("Заключение по результатам проверки обстоятельств банкротства банка",
                                                  self.tab_5)
        self.pushButton_5.setMaximumSize(QtCore.QSize(700, 30))
        self.pushButton_6 = QtWidgets.QPushButton("Отчет о состоянии переданных Агентству данных", self.tab_5)
        self.pushButton_6.setMaximumSize(QtCore.QSize(700, 30))
        self.pushButton_7 = QtWidgets.QPushButton("Отчет аналитического блока", self.tab_5)
        self.pushButton_7.setMaximumSize(QtCore.QSize(700, 30))
        self.pushButton_8 = QtWidgets.QPushButton("Мастер-файл", self.tab_5)
        self.pushButton_8.setMaximumSize(QtCore.QSize(700, 30))
        self.pushButton_9 = QtWidgets.QPushButton("Прочие документы", self.tab_5)
        self.pushButton_9.setMaximumSize(QtCore.QSize(700, 30))

        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_5)
        self.gridLayout_6.setContentsMargins(130, 0, 130, 0)
        self.gridLayout_6.addWidget(self.pushButton, 0, 0, 1, 1)
        self.gridLayout_6.addWidget(self.pushButton_2, 1, 0, 1, 1)
        self.gridLayout_6.addWidget(self.pushButton_3, 2, 0, 1, 1)
        self.gridLayout_6.addWidget(self.pushButton_4, 3, 0, 1, 1)
        self.gridLayout_6.addWidget(self.pushButton_5, 4, 0, 1, 1)
        self.gridLayout_6.addWidget(self.pushButton_6, 5, 0, 1, 1)
        self.gridLayout_6.addWidget(self.pushButton_7, 6, 0, 1, 1)
        self.gridLayout_6.addWidget(self.pushButton_8, 7, 0, 1, 1)
        self.gridLayout_6.addWidget(self.pushButton_9, 8, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def resizeEvent(self, event):
        width = self.size().width()
        height = self.size().height()
        koefW = (windll.user32.GetSystemMetrics(0) * 0.203) * ((width / windll.user32.GetSystemMetrics(0)) ** 2.5)
        koefH = (windll.user32.GetSystemMetrics(1) * 0.203) * ((height / windll.user32.GetSystemMetrics(1)) ** 2.5)
        koefW2 = 300 * ((width / windll.user32.GetSystemMetrics(0)) ** 2.5)
        koefH2 = 200 * ((height / windll.user32.GetSystemMetrics(1)) ** 2.5)
        self.gridLayout_2.setContentsMargins(20, 20, koefW, koefH)
        self.gridLayout_6.setContentsMargins(koefW2, koefH2, koefW2, koefH2)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Информация о проекте"))