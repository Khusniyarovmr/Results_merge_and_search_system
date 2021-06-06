# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import io
import locale
import csv
import sqlite3
from KD_widget import KredDogovor
from DannieOPZ import DannieOPZ
from KartochkaZaemchika import ZaemchikCard


class UI_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(896, 536)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ASV_image.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        # -------------------------------------------------
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.label_46 = QtWidgets.QLabel("Выберите банк", self.centralwidget)
        self.label_46.setFixedSize(150, 20)
        font_bank_choice = QtGui.QFont()
        font_bank_choice.setFamily("Arial")
        font_bank_choice.setPointSize(10)
        font_bank_choice.setBold(True)
        font_bank_choice.setUnderline(True)
        font_bank_choice.setWeight(75)
        self.label_46.setFont(font_bank_choice)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setFixedSize(200, 20)
        font_combo = QtGui.QFont()
        font_combo.setPointSize(10)
        self.comboBox.setFont(font_combo)
        self.comboBox.setFrame(True)
        self.comboBox.setDuplicatesEnabled(False)
        self.verticalLayout_2.addWidget(self.label_46)
        self.verticalLayout_2.addWidget(self.comboBox)
        # -------------------------------------------------
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tab = QtWidgets.QWidget()
        self.label = QtWidgets.QLabel("Наименование клиента", self.tab)
        self.label.setGeometry(QtCore.QRect(20, 10, 175, 21))
        font_header_1 = QtGui.QFont()
        font_header_1.setFamily("Arial")
        font_header_1.setPointSize(11)
        font_header_1.setBold(True)
        font_header_1.setWeight(75)
        self.label.setFont(font_header_1)
        self.listWidget = QtWidgets.QListWidget(self.tab)
        self.listWidget.setGeometry(QtCore.QRect(210, 10, 410, 21))
        self.label_11 = QtWidgets.QLabel("Группа актива", self.tab)
        self.label_11.setGeometry(QtCore.QRect(630, 10, 111, 21))
        self.label_11.setFont(font_header_1)
        self.listWidget_11 = QtWidgets.QListWidget(self.tab)
        self.listWidget_11.setGeometry(QtCore.QRect(750, 10, 111, 21))

        self.groupBox = QtWidgets.QGroupBox("Общая информация", self.tab)
        self.groupBox.setGeometry(QtCore.QRect(10, 50, 851, 221))
        font_all_group_box = QtGui.QFont()
        font_all_group_box.setFamily("Arial")
        font_all_group_box.setPointSize(11)
        font_all_group_box.setBold(True)
        font_all_group_box.setWeight(75)
        self.groupBox.setFont(font_all_group_box)
        font_all_labels_1 = QtGui.QFont()
        font_all_labels_1.setFamily("Arial")
        font_all_labels_1.setPointSize(10)
        font_all_labels_1.setBold(False)
        font_all_labels_1.setWeight(50)
        font_2_all_labels_1 = QtGui.QFont()
        font_2_all_labels_1.setFamily("Arial")
        font_2_all_labels_1.setPointSize(8)
        font_2_all_labels_1.setBold(False)
        font_2_all_labels_1.setWeight(50)
        font_all_LW_1 = QtGui.QFont()
        font_all_LW_1.setFamily("Arial")
        font_all_LW_1.setPointSize(9)
        font_all_LW_1.setBold(False)
        font_all_LW_1.setWeight(40)
        self.label_2 = QtWidgets.QLabel("Дата регистрации", self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 111, 16))
        self.label_2.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_3 = QtWidgets.QLabel("Адрес регистрации", self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 60, 121, 16))
        self.label_3.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_4 = QtWidgets.QLabel("Вид деятельности", self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(20, 90, 111, 20))
        self.label_4.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_5 = QtWidgets.QLabel("Дата и номер дела о банкротстве", self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 130, 200, 16))
        self.label_5.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_6 = QtWidgets.QLabel("Статус", self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(50, 160, 81, 20))
        self.label_6.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_7 = QtWidgets.QLabel("Руководитель", self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(20, 190, 111, 20))
        self.label_7.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_8 = QtWidgets.QLabel("ИНН", self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(215, 30, 31, 20))
        self.label_8.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_9 = QtWidgets.QLabel("Уставный капитал, руб.", self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(360, 30, 171, 20))
        self.label_9.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_10 = QtWidgets.QLabel("Количество работников", self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(640, 30, 141, 20))
        self.label_10.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_12 = QtWidgets.QLabel("Участники / акционеры", self.groupBox)
        self.label_12.setGeometry(QtCore.QRect(610, 110, 141, 20))
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)

        self.listWidget_2 = QtWidgets.QListWidget(self.groupBox)
        self.listWidget_2.setGeometry(QtCore.QRect(255, 30, 100, 21))
        self.listWidget_3 = QtWidgets.QListWidget(self.groupBox)
        self.listWidget_3.setGeometry(QtCore.QRect(540, 30, 91, 21))
        self.listWidget_4 = QtWidgets.QListWidget(self.groupBox)
        self.listWidget_4.setGeometry(QtCore.QRect(790, 30, 51, 21))
        self.listWidget_5 = QtWidgets.QListWidget(self.groupBox)
        self.listWidget_5.setGeometry(QtCore.QRect(130, 30, 71, 21))
        self.listWidget_6 = QtWidgets.QListWidget(self.groupBox)
        self.listWidget_6.setGeometry(QtCore.QRect(140, 60, 701, 21))
        self.listWidget_7 = QtWidgets.QListWidget(self.groupBox)
        self.listWidget_7.setGeometry(QtCore.QRect(140, 90, 701, 21))
        self.listWidget_8 = QtWidgets.QListWidget(self.groupBox)
        self.listWidget_8.setGeometry(QtCore.QRect(220, 130, 301, 21))
        self.listWidget_9 = QtWidgets.QListWidget(self.groupBox)
        self.listWidget_9.setGeometry(QtCore.QRect(140, 160, 381, 21))
        self.listWidget_10 = QtWidgets.QListWidget(self.groupBox)
        self.listWidget_10.setGeometry(QtCore.QRect(140, 190, 381, 21))
        self.listWidget_12 = QtWidgets.QListWidget(self.groupBox)
        self.listWidget_12.setGeometry(QtCore.QRect(540, 130, 301, 81))
        self.listWidget_12.setWordWrap(True)

        self.groupBox_2 = QtWidgets.QGroupBox("Информация по задолженности", self.tab)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 280, 521, 151))
        self.groupBox_2.setFont(font_all_group_box)
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_13 = QtWidgets.QLabel("Обслуживание после отзыва", self.groupBox_2)
        self.label_13.setGeometry(QtCore.QRect(10, 30, 220, 16))
        self.label_14 = QtWidgets.QLabel("Балансовая стоимость задолженности, руб.", self.groupBox_2)
        self.label_14.setGeometry(QtCore.QRect(10, 60, 240, 16))
        self.label_15 = QtWidgets.QLabel("Справедливая стоимость задолженности, руб.", self.groupBox_2)
        self.label_15.setGeometry(QtCore.QRect(260, 60, 250, 16))
        self.label_16 = QtWidgets.QLabel("Справедливая стоимость обеспечения, руб.", self.groupBox_2)
        self.label_16.setGeometry(QtCore.QRect(10, 110, 240, 16))

        self.listWidget_13 = QtWidgets.QListWidget(self.groupBox_2)
        self.listWidget_13.setGeometry(QtCore.QRect(190, 30, 321, 21))
        self.listWidget_14 = QtWidgets.QListWidget(self.groupBox_2)
        self.listWidget_14.setGeometry(QtCore.QRect(10, 80, 241, 21))
        self.listWidget_15 = QtWidgets.QListWidget(self.groupBox_2)
        self.listWidget_15.setGeometry(QtCore.QRect(260, 80, 251, 21))
        self.listWidget_16 = QtWidgets.QListWidget(self.groupBox_2)
        self.listWidget_16.setGeometry(QtCore.QRect(260, 110, 251, 21))

        self.groupBox_3 = QtWidgets.QGroupBox("Работа с активами", self.tab)
        self.groupBox_3.setGeometry(QtCore.QRect(549, 280, 311, 151))
        self.groupBox_3.setFont(font_all_group_box)
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_3)
        self.listWidget_17 = QtWidgets.QListWidget(self.groupBox_3)
        self.gridLayout_2.addWidget(self.listWidget_17, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        list_of_lab_1 = [self.label_2, self.label_3, self.label_4, self.label_5, self.label_6
            , self.label_7, self.label_8, self.label_9, self.label_10, self.label_12]
        for l in list_of_lab_1:
            l.setFont(font_all_labels_1)
        list_2_of_tab_1 = [self.label_13, self.label_14, self.label_15, self.label_16]
        for l in list_2_of_tab_1:
            l.setFont(font_2_all_labels_1)

        list_of_LW_1 = [self.listWidget_2, self.listWidget_3, self.listWidget_4, self.listWidget_5, self.listWidget_6
            , self.listWidget_7, self.listWidget_8, self.listWidget_9, self.listWidget_10, self.listWidget_11
            , self.listWidget_12, self.listWidget_13, self.listWidget_14, self.listWidget_15, self.listWidget_16
            , self.listWidget_17]
        for lw in list_of_LW_1:
            lw.setFont(font_all_LW_1)
            lw.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        # -----------------------------------------------------------------------------
        self.tab_2 = QtWidgets.QWidget()
        self.groupBox_4 = QtWidgets.QGroupBox("Результаты анализа", self.tab_2)
        self.groupBox_4.setGeometry(QtCore.QRect(0, 0, 871, 141))
        self.groupBox_4.setFont(font_all_group_box)
        self.groupBox_4.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_17 = QtWidgets.QLabel("Финансовое положение", self.groupBox_4)
        self.label_17.setGeometry(QtCore.QRect(20, 50, 171, 16))
        self.label_17.setFont(font_all_labels_1)
        self.label_17.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_18 = QtWidgets.QLabel("Обслуживание долга", self.groupBox_4)
        self.label_18.setGeometry(QtCore.QRect(20, 80, 171, 16))
        self.label_18.setFont(font_all_labels_1)
        self.label_18.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_19 = QtWidgets.QLabel("РВП / корректировка", self.groupBox_4)
        self.label_19.setGeometry(QtCore.QRect(20, 110, 171, 16))
        self.label_19.setFont(font_all_labels_1)
        self.label_19.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)

        self.listWidget_18 = QtWidgets.QListWidget(self.groupBox_4)
        self.listWidget_18.setGeometry(QtCore.QRect(210, 50, 146, 21))
        self.listWidget_18.setFont(font_all_LW_1)
        self.listWidget_19 = QtWidgets.QListWidget(self.groupBox_4)
        self.listWidget_19.setGeometry(QtCore.QRect(210, 80, 146, 21))
        self.listWidget_19.setFont(font_all_LW_1)
        self.listWidget_20 = QtWidgets.QListWidget(self.groupBox_4)
        self.listWidget_20.setGeometry(QtCore.QRect(210, 110, 146, 21))
        self.listWidget_20.setFont(font_all_LW_1)
        self.listWidget_21 = QtWidgets.QListWidget(self.groupBox_4)
        self.listWidget_21.setGeometry(QtCore.QRect(375, 50, 146, 21))
        self.listWidget_21.setFont(font_all_LW_1)
        self.listWidget_22 = QtWidgets.QListWidget(self.groupBox_4)
        self.listWidget_22.setGeometry(QtCore.QRect(375, 80, 146, 21))
        self.listWidget_22.setFont(font_all_LW_1)
        self.listWidget_23 = QtWidgets.QListWidget(self.groupBox_4)
        self.listWidget_23.setGeometry(QtCore.QRect(375, 110, 146, 21))
        self.listWidget_23.setFont(font_all_LW_1)

        self.pushButton = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setGeometry(QtCore.QRect(570, 50, 48, 48))
        Circle_style_but_1 = '''
        #pushButton {
            background-color: #2196f3;
            min-width:  48px;
            max-width:  48;
            min-height: 48;
            max-height: 48;
            border-radius: 24;        /* круглый */
        }
        '''
        self.pushButton.setStyleSheet(Circle_style_but_1)
        iicon = QtGui.QIcon('иконка_клиент.png')
        Icon_size = QtCore.QSize(48, 48)
        self.pushButton.setIcon(iicon)
        self.pushButton.setIconSize(Icon_size)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setGeometry(QtCore.QRect(730, 50, 48, 48))
        Circle_style_but_2 = '''
        #pushButton_2 {
            background-color: #2196f3;
            min-width:  48px;
            max-width:  48;
            min-height: 48;
            max-height: 48;
            border-radius: 24;        /* круглый */
        }
        '''
        self.pushButton_2.setStyleSheet(Circle_style_but_2)
        iicon2 = QtGui.QIcon('иконка_ОПЗ.png')
        self.pushButton_2.setIcon(iicon2)
        self.pushButton_2.setIconSize(Icon_size)

        self.label_20 = QtWidgets.QLabel("Подробнее о заемщике", self.groupBox_4)
        self.label_20.setGeometry(QtCore.QRect(530, 30, 141, 16))
        self.label_20.setFont(font_all_labels_1)
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21 = QtWidgets.QLabel("Данные из ОПЗ", self.groupBox_4)
        self.label_21.setGeometry(QtCore.QRect(700, 30, 111, 20))
        self.label_21.setFont(font_all_labels_1)
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        font_labels_21_22 = QtGui.QFont()
        font_labels_21_22.setFamily("Arial")
        font_labels_21_22.setPointSize(8)
        font_labels_21_22.setBold(False)
        font_labels_21_22.setWeight(50)
        self.label_22 = QtWidgets.QLabel("Оценка АСВ (экспертная)", self.groupBox_4)
        self.label_22.setGeometry(QtCore.QRect(210, 30, 146, 16))
        self.label_22.setFont(font_labels_21_22)
        self.label_22.setStyleSheet("")
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23 = QtWidgets.QLabel("Оценка АСВ (590-П)", self.groupBox_4)
        self.label_23.setGeometry(QtCore.QRect(375, 30, 146, 16))
        self.label_23.setFont(font_labels_21_22)
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)

        self.groupBox_5 = QtWidgets.QGroupBox("Информация по задолженности", self.tab_2)
        self.groupBox_5.setGeometry(QtCore.QRect(0, 140, 871, 81))
        self.groupBox_5.setFont(font_all_group_box)
        self.label_29 = QtWidgets.QLabel("(руб.)", self.groupBox_5)
        self.label_29.setGeometry(QtCore.QRect(820, 7, 41, 21))
        font_rub_label = QtGui.QFont()
        font_rub_label.setFamily("Arial")
        font_rub_label.setPointSize(9)
        font_rub_label.setBold(False)
        font_rub_label.setItalic(True)
        font_rub_label.setWeight(50)
        self.label_29.setFont(font_rub_label)
        self.label_29.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTop | QtCore.Qt.AlignTrailing)
        self.layoutWidget = QtWidgets.QWidget(self.groupBox_5)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 30, 851, 41))
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setHorizontalSpacing(26)
        self.label_24 = QtWidgets.QLabel("Балансовая стоимость", self.layoutWidget)
        self.label_24.setFont(font_all_labels_1)
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25 = QtWidgets.QLabel("Резервы", self.layoutWidget)
        self.label_25.setFont(font_all_labels_1)
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_26 = QtWidgets.QLabel("Обеспечение", self.layoutWidget)
        self.label_26.setFont(font_all_labels_1)
        self.label_26.setAlignment(QtCore.Qt.AlignCenter)
        self.label_27 = QtWidgets.QLabel("Корректировка АСВ", self.layoutWidget)
        self.label_27.setFont(font_all_labels_1)
        self.label_27.setAlignment(QtCore.Qt.AlignCenter)
        self.label_28 = QtWidgets.QLabel("Справедливая стоимость", self.layoutWidget)
        self.label_28.setFont(font_all_labels_1)
        self.label_28.setAlignment(QtCore.Qt.AlignCenter)

        self.listWidget_24 = QtWidgets.QListWidget(self.layoutWidget)
        self.listWidget_24.setFont(font_all_LW_1)
        self.listWidget_25 = QtWidgets.QListWidget(self.layoutWidget)
        self.listWidget_25.setFont(font_all_LW_1)
        self.listWidget_26 = QtWidgets.QListWidget(self.layoutWidget)
        self.listWidget_26.setFont(font_all_LW_1)
        self.listWidget_27 = QtWidgets.QListWidget(self.layoutWidget)
        self.listWidget_27.setFont(font_all_LW_1)
        self.listWidget_28 = QtWidgets.QListWidget(self.layoutWidget)
        self.listWidget_28.setFont(font_all_LW_1)

        self.gridLayout_3.addWidget(self.label_24, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.label_25, 0, 1, 1, 1)
        self.gridLayout_3.addWidget(self.label_26, 0, 2, 1, 1)
        self.gridLayout_3.addWidget(self.label_27, 0, 3, 1, 1)
        self.gridLayout_3.addWidget(self.label_28, 0, 4, 1, 1)
        self.gridLayout_3.addWidget(self.listWidget_24, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.listWidget_25, 1, 1, 1, 1)
        self.gridLayout_3.addWidget(self.listWidget_26, 1, 2, 1, 1)
        self.gridLayout_3.addWidget(self.listWidget_27, 1, 3, 1, 1)
        self.gridLayout_3.addWidget(self.listWidget_28, 1, 4, 1, 1)
        # ------------------------------------------ТУТ СКРОЛЛ БОКС---------------------------------------------
        self.groupBox_6 = QtWidgets.QGroupBox("Кредитные договора", self.tab_2)
        self.groupBox_6.setGeometry(QtCore.QRect(0, 220, 871, 221))
        self.groupBox_6.setFont(font_all_group_box)
        self.listWidget_31 = QtWidgets.QListWidget(self.groupBox_6)
        self.listWidget_31.setGeometry(QtCore.QRect(0, 0, 870, 220))
        self.listWidget_31.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tabWidget.addTab(self.tab_2, "")
        # ------------------------------------------ТУТ СКРОЛЛ БОКС ЗАКАНЧИВАЕТСЯ---------------------------
        # -----------------------------------------------------------------------------
        self.tab_3 = QtWidgets.QWidget()
        self.label_30 = QtWidgets.QLabel(self.tab_3)  # тут пишется наименование клиента
        self.label_30.setGeometry(QtCore.QRect(0, 14, 871, 21))
        Header_label_3 = QtGui.QFont()
        Header_label_3.setFamily("Arial")
        Header_label_3.setPointSize(11)
        Header_label_3.setBold(True)
        Header_label_3.setWeight(75)
        self.label_30.setFont(Header_label_3)
        self.label_30.setAlignment(QtCore.Qt.AlignCenter)
        self.label_31 = QtWidgets.QLabel("Виды обеспечения", self.tab_3)
        self.label_31.setGeometry(QtCore.QRect(20, 40, 81, 31))
        self.label_31.setFont(font_all_labels_1)
        self.label_31.setWordWrap(True)
        self.listWidget_29 = QtWidgets.QListWidget(self.tab_3)
        self.listWidget_29.setGeometry(QtCore.QRect(100, 40, 511, 30))
        self.listWidget_29.setFont(font_all_LW_1)

        self.groupBox_7 = QtWidgets.QGroupBox("Договоры обеспечения", self.tab_3)
        self.groupBox_7.setGeometry(QtCore.QRect(0, 90, 871, 341))
        self.groupBox_7.setFont(font_all_group_box)
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox_7)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setGeometry(QtCore.QRect(0, 20, 871, 321))
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.setHorizontalHeaderLabels(
            ["№ КД", "Договор залога/поручительства", "Вид обеспечения", "Наименование предмета обеспечения",
             "Местонахождение объекта залога", "Площадь/Год выпуска", "Справедливая стоимость"])
        font_TW = QtGui.QFont()
        font_TW.setFamily("Arial")
        font_TW.setPointSize(8)
        font_TW.setBold(False)
        font_TW.setWeight(50)
        font_TW.setKerning(False)
        self.tableWidget.setFont(font_TW)
        self.tableWidget.installEventFilter(self)
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidget.setTextElideMode(QtCore.Qt.ElideNone)
        self.label_32 = QtWidgets.QLabel("Справедливая стоимость", self.tab_3)
        self.label_32.setGeometry(QtCore.QRect(630, 40, 91, 31))
        self.label_32.setFont(font_all_labels_1)
        self.label_32.setWordWrap(True)
        self.listWidget_30 = QtWidgets.QListWidget(self.tab_3)
        self.listWidget_30.setGeometry(QtCore.QRect(730, 40, 111, 30))
        self.listWidget_30.setFont(font_all_LW_1)
        self.tabWidget.addTab(self.tab_3, "")
        # -----------------------------------------------------------------------------
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.splitter = QtWidgets.QSplitter(self.tab_4)
        self.splitter.setGeometry(QtCore.QRect(0, 10, 871, 441))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.label_45 = QtWidgets.QLabel(self.splitter)  # Тут пишется наименование клиента
        self.label_45.setGeometry(QtCore.QRect(0, 10, 871, 21))
        self.label_45.setFont(Header_label_3)
        self.label_45.setAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.splitter)
        self.tableWidget_2.setGeometry(QtCore.QRect(20, 60, 831, 281))
        self.tableWidget_2.setAlternatingRowColors(True)
        self.tableWidget_2.setColumnCount(2)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(166)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_2.setSortingEnabled(True)
        self.tableWidget_2.setHorizontalHeaderLabels(["Номер счета", "Наименование счета"])
        self.tableWidget_2.installEventFilter(self)
        self.tableWidget_2.setTextElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.addTab(self.tab_4, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.splitter.addWidget(self.label_45)
        self.splitter.addWidget(self.tableWidget_2)
        # -----------------------------------------------------------------------------
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # add event filter
    def eventFilter(self, source, event):
        if (event.type() == QtCore.QEvent.KeyPress and
                event.matches(QtGui.QKeySequence.Copy)):
            self.copySelection(source)
            return True
        return self.eventFilter(source, event)

    # add copy method
    def copySelection(self, tab):
        if tab.objectName() == 'tableWidget':
            selection = self.tableWidget.selectedIndexes()
        elif tab.objectName() == 'tableWidget_2':
            selection = self.tableWidget_2.selectedIndexes()
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

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Карточка клиента"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Описание клиента"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2),
                                  _translate("MainWindow", "Финансовый анализ / кредитные договора"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Обеспечение"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Счета"))


class ClientCardWindow(QtWidgets.QMainWindow, UI_MainWindow):
    data_for_client_card = []
    row_number_click = 0
    prepared_data = []

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.comboBox.activated[str].connect(self.onActivated)
        self.common_data_for_cc = []
        self.acc_data_for_cc = []
        self.ob_data_for_cc = []
        self.kd_data_for_cc = []
        self.OPZ_data_for_cc = []
        self.Zcard_data_for_cc = []
        self.OPZCard = ''
        self.Zcard = ''
        self.client_name = ''
        self.pushButton.clicked.connect(self.but_1_clicked)
        self.pushButton_2.clicked.connect(self.but_2_clicked)
        locale.setlocale(locale.LC_NUMERIC, 'rus')

    def data_preparation(self, data_for_prepare):
        # print('data_for_prepare: ', data_for_prepare)
        if len(data_for_prepare) == 1:  # Если нашли только одного клиента, то карточку заполняем по нему.
            data_for_cc = data_for_prepare
        elif len(data_for_prepare) > 1:
            iskomiy_client = [data_for_prepare[self.row_number_click]]
            name = iskomiy_client[0][1]
            inn = iskomiy_client[0][2]
            pasp = iskomiy_client[0][3]
            sovpadenie = []  # Идентичные клиенты
            for i in range(len(data_for_prepare)):
                if i == self.row_number_click:
                    pass
                else:
                    if data_for_prepare[i][1] == name and data_for_prepare[i][2] == inn and inn != '':
                        sovpadenie.append(data_for_prepare[i])
                    elif data_for_prepare[i][1] == name and data_for_prepare[i][3] == pasp and pasp != '':
                        sovpadenie.append(data_for_prepare[i])
                    elif data_for_prepare[i][2] == inn and inn != '' and data_for_prepare[i][3] == pasp and pasp != '':
                        sovpadenie.append(data_for_prepare[i])
                    elif data_for_prepare[i][2] == inn and inn != '':
                        sovpadenie.append(data_for_prepare[i])
            if sovpadenie:  # Если в таблице несколько идентичных клиентов
                sovpadenie.append(data_for_prepare[self.row_number_click])
                data_for_cc = sovpadenie
            else:  # Если в таблице нет идентичных клиентов и выбранный единственный
                data_for_cc = iskomiy_client
        return data_for_cc

    def common_data(self, data_from_db):
        data_for_return = []
        data_for_tab_1 = self.zapros_1(data_from_db)  # kp_ul_fl_raschet
        data_for_tab_2 = self.zapros_2(data_from_db)  # kp_ul_opis
        data_for_tab_3 = self.zapros_3(data_from_db)  # kp_ul_spark
        data_for_tab_4 = self.zapros_4(data_from_db)  # obespechenie - общая сумма и виды обеспечения
        data_for_tab_5 = self.zapros_5(data_from_db)  # opz - обслуживается или нет
        # print('data_for_tab_1: ', data_for_tab_1)
        # print('data_for_tab_2: ', data_for_tab_2)
        # print('data_for_tab_3: ', data_for_tab_3)
        # print('data_for_tab_4: ', data_for_tab_4)
        # print('data_for_tab_5: ', data_for_tab_5)

        for i in range(len(data_from_db)):
            data = []
            data2 = []
            d1 = ['', '', '', '', '', '', '', '', '']
            d2 = ['', '', '', '', '', '']
            d3 = ['', '', '', '', '', '', '']
            d4 = ['', '']
            d5 = ['']
            if data_for_tab_1:
                for k in data_for_tab_1:
                    if k[0] == data_from_db[i][0]:
                        d1[0] = data_from_db[i][0]
                        d1[1] = data_from_db[i][1]
                        d1[2] = data_from_db[i][2]
                        d1[3] = data_from_db[i][3]
                        d1[4] = k[5]
                        d1[5] = k[6]
                        d1[6] = k[7]
                        d1[7] = k[8]
                        d1[8] = k[9]
                        data.append(d1)
                    else:
                        d1[0] = data_from_db[i][0]
                        d1[1] = data_from_db[i][1]
                        d1[2] = data_from_db[i][2]
                        d1[3] = data_from_db[i][3]
                        data.append(d1)
            else:
                d1[0] = data_from_db[i][0]
                d1[1] = data_from_db[i][1]
                d1[2] = data_from_db[i][2]
                d1[3] = data_from_db[i][3]
                data.append(d1)
            if data_for_tab_2:
                for k in data_for_tab_2:
                    if k[0] == data_from_db[i][0]:
                        data.append(k[5:])
                    else:
                        data.append(d2)
            else:
                data.append(d2)
            if data_for_tab_3:
                for k in data_for_tab_3:
                    if k[0] == data_from_db[i][0]:
                        data.append(k[5:])
                    else:
                        data.append(d3)
            else:
                data.append(d3)
            if data_for_tab_4:
                for k in data_for_tab_4:
                    if k[0] == data_from_db[i][0]:
                        data.append(k[5:])
                    else:
                        data.append(d4)
            else:
                data.append(d4)
            if data_for_tab_5:
                for k in data_for_tab_5:
                    if k[0] == data_from_db[i][0]:
                        data.append(k[5:])
                    else:
                        data.append(d5)
            else:
                data.append(d5)

            for da in data:
                data2.extend(da)
            data_for_return.append(data2)

        # print('data_for_return: ', data_for_return)
        return data_for_return

    def acc_data(self, data_from_db):
        data_for_return = []
        data_for_tab_6 = self.zapros_6(data_from_db)  # accounts - все счета клиента
        # print('data_for_tab_6: ', data_for_tab_6)

        for i in range(len(data_from_db)):
            data = []
            d6 = ['', '', '']
            if data_for_tab_6:
                for k in data_for_tab_6:
                    if k[0] == data_from_db[i][0]:
                        d6[0] = data_from_db[i][0]
                        d6[1] = k[4]
                        d6[2] = k[5]
                        data.append(list(d6))
                        # print(data)
            else:
                d6[0] = data_from_db[i][0]
                data.append(list(d6))
            data_for_return.extend(data)
        # print('data_for_return: ', data_for_return)
        return data_for_return

    def ob_data(self, data_from_db):
        data_for_return = []
        data_for_tab_7 = self.zapros_7(data_from_db)  # obespechenie - информация об обеспечении
        # print('data_for_tab_7: ', data_for_tab_7)

        for i in range(len(data_from_db)):
            data = []
            d7 = ['', '', '', '', '', '', '', '', '']
            if data_for_tab_7:
                for k in data_for_tab_7:
                    if k[0] == data_from_db[i][0]:
                        d7[0] = k[0]
                        for j in range(1, 9):
                            d7[j] = k[j+3]
                        data.append(list(d7))
            else:
                d7[0] = data_from_db[i][0]
                data.append(list(d7))
            data_for_return.extend(data)
        # print('data_for_return: ', data_for_return)
        return data_for_return

    def kd_data(self, data_from_db):
        data_for_return = []
        data_for_tab_8 = self.zapros_8(data_from_db)  # obespechenie - информация об обеспечении
        # print('data_for_tab_8: ', data_for_tab_8)

        for i in range(len(data_from_db)):
            data = []
            d8 = ['', '', '', '', '', '', '', '', '', '', '', '']
            if data_for_tab_8:
                for k in data_for_tab_8:
                    if k[0] == data_from_db[i][0]:
                        d8[0] = k[0]
                        for j in range(1, 12):
                            d8[j] = k[j+3]
                        data.append(list(d8))
            else:
                d8[0] = data_from_db[i][0]
                data.append(list(d8))
            data_for_return.extend(data)
        # print('data_for_return: ', data_for_return)
        return data_for_return

    def OPZ_data(self, data_from_db):
        data_for_return = []
        data_for_tab_9 = self.zapros_9(data_from_db)  # obespechenie - информация об обеспечении
        #print('data_for_tab_9: ', data_for_tab_9)

        for i in range(len(data_from_db)):
            data = []
            d9 = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''
                  , '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''
                  , '', '', '', '', '', '', '', '', '']
            if data_for_tab_9:
                for k in data_for_tab_9:
                    if k[0] == data_from_db[i][0]:
                        d9[0] = k[0]
                        for j in range(1, 49):
                            d9[j] = k[j+3]
                        data.append(list(d9))
            else:
                d9[0] = data_from_db[i][0]
                data.append(list(d9))
            data_for_return.extend(data)
        #print('data_for_return: ', data_for_return)
        return data_for_return

    def Zcard_data(self, data_from_db):
        data_for_return = []
        data_for_tab_10 = self.zapros_10(data_from_db)  # obespechenie - информация об обеспечении
        #print('data_for_tab_10: ', data_for_tab_10)

        for i in range(len(data_from_db)):
            data = []
            d10 = ['', '', '', '', '', '', '', '', '', '', '', '',
                   '', '', '', '', '', '', '', '', '', '', '']
            if data_for_tab_10:
                for k in data_for_tab_10:
                    if k[0] == data_from_db[i][0]:
                        d10[0] = k[0]
                        for j in range(1, 23):
                            d10[j] = k[j+3]
                        data.append(list(d10))
            else:
                d10[0] = data_from_db[i][0]
                data.append(list(d10))
            data_for_return.extend(data)
        #print('data_for_return: ', data_for_return)
        return data_for_return

    def showEvent(self, a0: QtGui.QShowEvent):
        self.prepared_data = self.data_preparation(self.data_for_client_card)
        self.common_data_for_cc = self.common_data(self.prepared_data)
        self.acc_data_for_cc = self.acc_data(self.prepared_data)
        self.ob_data_for_cc = self.ob_data(self.prepared_data)
        self.kd_data_for_cc = self.kd_data(self.prepared_data)
        self.OPZ_data_for_cc = self.OPZ_data(self.prepared_data)
        self.Zcard_data_for_cc = self.Zcard_data(self.prepared_data)
        self.comboBox.clear()
        self.comboBox.addItem(self.data_for_client_card[self.row_number_click][0])
        for i in range(len(self.common_data_for_cc)):
            if not self.common_data_for_cc[i][0] == self.data_for_client_card[self.row_number_click][0]:
                self.comboBox.addItem(self.common_data_for_cc[i][0])

        self.add_common_data_for_cc(self.comboBox.currentText(), self.common_data_for_cc)
        self.add_acc_data_for_cc(self.comboBox.currentText(), self.acc_data_for_cc)
        self.add_ob_data_for_cc(self.comboBox.currentText(), self.ob_data_for_cc)
        self.add_KD_widgets(self.comboBox.currentText(), self.kd_data_for_cc)

    def add_common_data_for_cc(self, bank, data):
        # print('bank: ', bank, 'data: ', data)
        locale.setlocale(locale.LC_NUMERIC, 'rus')
        list_widgets = (
            self.listWidget, self.listWidget_2, self.listWidget_3, self.listWidget_4, self.listWidget_5,
            self.listWidget_6
            , self.listWidget_7, self.listWidget_8, self.listWidget_9, self.listWidget_10, self.listWidget_11,
            self.listWidget_12
            , self.listWidget_13, self.listWidget_14, self.listWidget_15, self.listWidget_16, self.listWidget_17,
            self.listWidget_18
            , self.listWidget_19, self.listWidget_20, self.listWidget_21, self.listWidget_22, self.listWidget_23,
            self.listWidget_24
            , self.listWidget_25, self.listWidget_26, self.listWidget_27, self.listWidget_28, self.listWidget_29,
            self.listWidget_30)
        for lw in list_widgets:
            lw.clear()
        if not str(data[0][3]).replace(' ', '') == '':
            self.client_name = str(data[0][1]) + ' (' + str(data[0][3]) + ')'
        else:
            self.client_name = str(data[0][1])
        self.setWindowTitle("Карточка клиента " + self.client_name)
        for i in range(len(data)):
            if data[i][0] == bank:
                if not str(data[i][1]).replace(' ', '') == '':
                    if not str(data[i][3]).replace(' ', '') == '':
                        self.label_30.setText(str(data[i][1]) + ' (' + str(data[0][3]) + ')')
                        self.label_45.setText(str(data[i][1]) + ' (' + str(data[0][3]) + ')')
                        self.listWidget.addItem(str(data[i][1]) + ' (' + str(data[0][3]) + ')')  # Наименование
                    else:
                        self.label_30.setText(str(data[i][1]))
                        self.label_45.setText(str(data[i][1]))
                        self.listWidget.addItem(str(data[i][1]))  # Наименование
                    self.listWidget.item(0).setSizeHint(QtCore.QSize(408, 20))
                    self.listWidget.item(0).setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEditable)
                if not str(data[i][2]).replace(' ', '') == '':
                    self.listWidget_2.addItem(str(data[i][2]))  # ИНН
                    self.listWidget_2.item(0).setSizeHint(QtCore.QSize(98, 20))
                    self.listWidget_2.item(0).setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEditable)
                if not str(data[i][16]).replace(' ', '') == '':
                    self.listWidget_3.addItem('{:.12n}'.format(float('{:-.2f}'.format(data[i][16]))))  # Уставный капитал
                    self.listWidget_3.item(0).setSizeHint(QtCore.QSize(89, 20))
                    self.listWidget_3.item(0).setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEditable)
                if not str(data[i][17]).replace(' ', '') == '':
                    self.listWidget_4.addItem(str(data[i][17]))  # Количество работников
                    self.listWidget_4.item(0).setSizeHint(QtCore.QSize(49, 20))
                    self.listWidget_4.item(0).setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEditable)
                if not str(data[i][15]).replace(' ', '') == '':
                    self.listWidget_5.addItem(str(data[i][15]))  # Дата регистрации
                    self.listWidget_5.item(0).setSizeHint(QtCore.QSize(69, 20))
                    self.listWidget_5.item(0).setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEditable)
                if not str(data[i][18]).replace(' ', '') == '':
                    self.listWidget_6.addItem(str(data[i][18]))  # Адрес регистрации
                    self.listWidget_6.item(0).setSizeHint(QtCore.QSize(699, 20))
                    self.listWidget_6.item(0).setTextAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
                    self.listWidget_6.item(0).setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEditable)
                if not data[i][19].replace(' ', '') == '':
                    self.listWidget_7.addItem(str(data[i][19]))  # Вид деятельности
                    self.listWidget_7.item(0).setSizeHint(QtCore.QSize(699, 20))
                    self.listWidget_7.item(0).setTextAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
                    self.listWidget_7.item(0).setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEditable)
                if data[i][9] == '- от -':
                    self.listWidget_8.addItem('НД')
                else:
                    self.listWidget_8.addItem(str(data[i][9]))  # Дата и номер дела о банкротстве
                    self.listWidget_8.item(0).setSizeHint(QtCore.QSize(299, 20))
                    self.listWidget_8.item(0).setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEditable)
                if not str(data[i][20]).replace(' ', '') == '':
                    self.listWidget_9.addItem(str(data[i][20]))  # Статус
                    self.listWidget_9.item(0).setSizeHint(QtCore.QSize(379, 20))
                    self.listWidget_9.item(0).setTextAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
                    self.listWidget_9.item(0).setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEditable)
                if not str(data[i][21]).replace(' ', '') == '':
                    self.listWidget_10.addItem(str(data[i][21]))  # Руководитель
                    self.listWidget_10.item(0).setSizeHint(QtCore.QSize(379, 20))
                    self.listWidget_10.item(0).setTextAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
                    self.listWidget_10.item(0).setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEditable)
                if not str(data[i][8]).replace(' ', '') == '':
                    self.listWidget_11.addItem(str(data[i][8]))  # Группа актива
                    self.listWidget_11.item(0).setSizeHint(QtCore.QSize(109, 20))
                    self.listWidget_11.item(0).setToolTip(str(data[i][8]))
                    self.listWidget_11.item(0).setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEditable)
                if not str(data[i][10]).replace(' ', '') == '':
                    self.listWidget_12.addItem(str(data[i][10]))  # Участники акционеры
                    self.listWidget_12.item(0).setSizeHint(QtCore.QSize(299, 80))
                    self.listWidget_12.item(0).setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEditable)
                if not str(data[i][24]).replace(' ', '') == '':
                    self.listWidget_13.addItem(str(data[i][24]))  # Обслуживание после отзыва
                    self.listWidget_13.item(0).setSizeHint(QtCore.QSize(319, 20))
                    self.listWidget_13.item(0).setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEditable)
                if not str(data[i][4]).replace(' ', '') == '':
                    self.listWidget_14.addItem('{:.12n}'.format(float('{:-.2f}'.format(data[i][4]))))  # Балансовая стоимость задолженности
                    self.listWidget_14.item(0).setSizeHint(QtCore.QSize(250, 20))
                    self.listWidget_14.item(0).setTextAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
                    self.listWidget_14.item(0).setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEditable)
                if not str(data[i][5]).replace(' ', '') == '':
                    self.listWidget_15.addItem('{:.12n}'.format(float('{:-.2f}'.format(data[i][5]))))  # справедливая стоимость задолженности
                    self.listWidget_15.item(0).setSizeHint(QtCore.QSize(250, 20))
                    self.listWidget_15.item(0).setTextAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
                    self.listWidget_15.item(0).setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEditable)
                if not str(data[i][22]).replace(' ', '') == '':
                    self.listWidget_16.addItem('{:.12n}'.format(float('{:-.2f}'.format(data[i][22]))))  # Справедливая стоимость обеспечения
                    self.listWidget_16.item(0).setSizeHint(QtCore.QSize(250, 20))
                    self.listWidget_16.item(0).setTextAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
                    self.listWidget_16.item(0).setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEditable)
                self.listWidget_17.addItem('НД')  # Работа с активами
                self.listWidget_17.item(0).setSizeHint(QtCore.QSize(289, 112))
                self.listWidget_17.item(0).setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEditable)
                if not str(data[i][11]).replace(' ', '') == '':
                    self.listWidget_18.addItem(str(data[i][11]))  # Финансовое положение №1
                    self.listWidget_18.item(0).setSizeHint(QtCore.QSize(119, 20))
                    self.listWidget_18.item(0).setTextAlignment(QtCore.Qt.AlignCenter)
                    self.listWidget_18.item(0).setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEditable)
                if not str(data[i][12]).replace(' ', '') == '':
                    self.listWidget_19.addItem(str(data[i][12]))  # Обслуживание долга №1
                    self.listWidget_19.item(0).setSizeHint(QtCore.QSize(119, 20))
                    self.listWidget_19.item(0).setTextAlignment(QtCore.Qt.AlignCenter)
                    self.listWidget_19.item(0).setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEditable)
                if not str(data[i][13]).replace(' ', '') == '':
                    try:
                        self.listWidget_20.addItem("{:.0%}".format(float(str(data[i][13]).replace(',','.'))))  # РВП корректировка №1
                    except ValueError:
                        self.listWidget_20.addItem(str(data[i][13]))  # РВП корректировка №1
                    except TypeError:
                        self.listWidget_20.addItem(str(data[i][13]))  # РВП корректировка №1
                    self.listWidget_20.item(0).setSizeHint(QtCore.QSize(119, 20))
                    self.listWidget_20.item(0).setTextAlignment(QtCore.Qt.AlignCenter)
                    self.listWidget_20.item(0).setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEditable)
                if not str(data[i][11]).replace(' ', '') == '':
                    self.listWidget_21.addItem(str(data[i][11]))  # Финансовое положение №2
                    self.listWidget_21.item(0).setSizeHint(QtCore.QSize(119, 20))
                    self.listWidget_21.item(0).setTextAlignment(QtCore.Qt.AlignCenter)
                    self.listWidget_21.item(0).setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEditable)
                if not str(data[i][12]).replace(' ', '') == '':
                    self.listWidget_22.addItem(str(data[i][12]))  # Обслуживание долга №2
                    self.listWidget_22.item(0).setSizeHint(QtCore.QSize(119, 20))
                    self.listWidget_22.item(0).setTextAlignment(QtCore.Qt.AlignCenter)
                    self.listWidget_22.item(0).setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEditable)
                if not str(data[i][14]).replace(' ', '') == '':
                    try:
                        self.listWidget_23.addItem("{:.0%}".format(float(str(data[i][14]).replace(',','.'))))  # РВП корректировка №1
                    except ValueError:
                        self.listWidget_23.addItem(str(data[i][14]))  # РВП корректировка №1
                    except TypeError:
                        self.listWidget_23.addItem(str(data[i][14]))  # РВП корректировка №1
                    self.listWidget_23.item(0).setSizeHint(QtCore.QSize(119, 20))
                    self.listWidget_23.item(0).setTextAlignment(QtCore.Qt.AlignCenter)
                    self.listWidget_23.item(0).setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEditable)
                if not str(data[i][4]).replace(' ', '') == '':
                    self.listWidget_24.addItem('{:.12n}'.format(float('{:-.2f}'.format(data[i][4]))))  # Балансовая стоимость
                    self.listWidget_24.item(0).setSizeHint(QtCore.QSize(146, 16))
                    self.listWidget_24.item(0).setTextAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
                    self.listWidget_24.item(0).setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEditable)
                if not str(data[i][6]).replace(' ', '') == '':
                    self.listWidget_25.addItem('{:.12n}'.format(float('{:-.2f}'.format(data[i][6]))))  # Резервы
                    self.listWidget_25.item(0).setSizeHint(QtCore.QSize(146, 16))
                    self.listWidget_25.item(0).setTextAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
                    self.listWidget_25.item(0).setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEditable)
                if not str(data[i][22]).replace(' ', '') == '':
                    self.listWidget_26.addItem('{:.12n}'.format(float('{:-.2f}'.format(data[i][22]))))  # Обеспечение
                    self.listWidget_26.item(0).setSizeHint(QtCore.QSize(146, 16))
                    self.listWidget_26.item(0).setTextAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
                    self.listWidget_26.item(0).setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEditable)
                if not str(data[i][7]).replace(' ', '') == '':
                    self.listWidget_27.addItem('{:.12n}'.format(float('{:-.2f}'.format(data[i][7])))) # Корректировка АСВ
                    self.listWidget_27.item(0).setSizeHint(QtCore.QSize(146, 16))
                    self.listWidget_27.item(0).setTextAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
                    self.listWidget_27.item(0).setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEditable)
                if not str(data[i][5]).replace(' ', '') == '':
                    self.listWidget_28.addItem('{:.12n}'.format(float('{:-.2f}'.format(data[i][5]))))  # Справедливая стоимость
                    self.listWidget_28.item(0).setSizeHint(QtCore.QSize(146, 16))
                    self.listWidget_28.item(0).setTextAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
                    self.listWidget_28.item(0).setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEditable)
                if not str(data[i][22]).replace(' ', '') == '':
                    self.listWidget_30.addItem('{:.12n}'.format(float('{:-.2f}'.format(data[i][22]))))  # Справедливая стоимость обеспечения
                    self.listWidget_30.item(0).setSizeHint(QtCore.QSize(109, 29))
                    self.listWidget_30.item(0).setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEditable)
                if not str(data[i][23]).replace(' ', '') == '':
                    self.listWidget_29.addItem(str(data[i][23]))  # виды обеспечения
                    self.listWidget_29.item(0).setSizeHint(QtCore.QSize(509, 29))
                    self.listWidget_29.item(0).setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEditable)

    def add_acc_data_for_cc(self, bank, data):
        # print('acc_bank: ', bank, 'acc_data: ', data)
        self.tableWidget_2.setRowCount(0)
        k = 1
        for i in range(len(data)):
            if data[i][0] == bank:
                self.tableWidget_2.setRowCount(k)
                self.tableWidget_2.setItem(k - 1, 0, QtWidgets.QTableWidgetItem(data[i][1]))
                self.tableWidget_2.setItem(k - 1, 1, QtWidgets.QTableWidgetItem(data[i][2]))
                k += 1

    def add_ob_data_for_cc(self, bank, data):
        # print('bank: ', bank, 'data: ', data)
        locale.setlocale(locale.LC_NUMERIC, 'rus')
        self.tableWidget.setRowCount(0)
        spisok_nedvizki = 'квартира, земельный участок, недвижимое имущество, нежилое здание, ' \
                          'нежилое помещение, Нежилое здание , Сооружение, право аренды на земельный участок, ' \
                          'здание, жилой дом, жилое помещение, ДДУ, недвижимость'
        k = 1
        for i in range(len(data)):
            if data[i][0] == bank:
                self.tableWidget.setRowCount(k)
                self.tableWidget.setItem(k - 1, 0, QtWidgets.QTableWidgetItem(data[i][1]))
                self.tableWidget.setItem(k - 1, 1, QtWidgets.QTableWidgetItem(data[i][2]))
                self.tableWidget.setItem(k - 1, 2, QtWidgets.QTableWidgetItem(data[i][3]))
                self.tableWidget.setItem(k - 1, 3, QtWidgets.QTableWidgetItem(data[i][4]))
                self.tableWidget.setItem(k - 1, 4, QtWidgets.QTableWidgetItem(data[i][5]))
                self.tableWidget.setRowHeight(k-1, int(self.tableWidget.sizeHintForRow(k-1)))
                if data[i][3] in spisok_nedvizki:
                    self.tableWidget.setItem(k - 1, 5, QtWidgets.QTableWidgetItem(data[i][6]))
                elif not data[i][3] in spisok_nedvizki and data[i][7] != '':
                    self.tableWidget.setItem(k - 1, 5, QtWidgets.QTableWidgetItem(data[i][7]))
                else:
                    self.tableWidget.setItem(k - 1, 5, QtWidgets.QTableWidgetItem(data[i][6]))
                try:
                    self.tableWidget.setItem(k - 1, 6, QtWidgets.QTableWidgetItem('{:.10n}'.format(data[i][8])))
                except ValueError:
                    self.tableWidget.setItem(k - 1, 6, QtWidgets.QTableWidgetItem(''))
                k += 1

    def add_KD_widgets(self, bank, data):
        locale.setlocale(locale.LC_NUMERIC, 'rus')
        self.listWidget_31.clear()
        for i in range(len(data)):
            if data[i][0] == bank:
                kdw = KredDogovor()
                list_of_listview = [kdw.listView_31, kdw.listView_32, kdw.listView_33, kdw.listView_34, kdw.listView_35
                    , kdw.listView_36, kdw.listView_37, kdw.listView_38, kdw.listView_39, kdw.listView_40
                    , kdw.listView_41]
                k = 1
                for l in list_of_listview:
                    if l == kdw.listView_40 or l == kdw.listView_39 or l == kdw.listView_38 or l == kdw.listView_37 or l == kdw.listView_36:
                        model = QtGui.QStandardItemModel()
                        try:
                            modelItem = QtGui.QStandardItem('{:.12n}'.format(float('{:-.2f}'.format(float(str(data[i][k]).replace(',', '.'))))))
                        except ValueError:
                            modelItem = QtGui.QStandardItem('')
                        modelItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        modelItem.setSizeHint(QtCore.QSize(l.size().width() - 5, l.size().height()))
                        model.appendRow(modelItem)
                        l.setModel(model)
                        k += 1
                    else:
                        model = QtGui.QStandardItemModel()
                        modelItem = QtGui.QStandardItem(data[i][k])
                        model.appendRow(modelItem)
                        modelItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        modelItem.setSizeHint(QtCore.QSize(l.size().width() - 5, l.size().height()))
                        l.setModel(model)
                        l.setTextElideMode(QtCore.Qt.ElideNone)
                        l.setWordWrap(True)
                        k += 1

                LWItem = QtWidgets.QListWidgetItem(self.listWidget_31)
                LWItem.setSizeHint(QtCore.QSize(830, 130))
                LWItem.setFlags(QtCore.Qt.ItemIsEnabled)
                self.listWidget_31.setItemWidget(LWItem, kdw)

    def add_OPZ_info(self, bank, data):
        self.OPZCard.setWindowTitle("Данные ОПЗ по заемщику " + self.client_name)
        for i in range(len(data)):
            if data[i][0] == bank:
                k = 1
                for j in range(0, 47):
                    self.OPZCard.tableWidget.item(j, 2).setText(str(data[i][k]))
                    k += 1
                lwmodel = QtGui.QStandardItemModel()
                lwmodelItem = QtGui.QStandardItem(str(data[i][48]))
                lwfont = QtGui.QFont()
                lwfont.setPointSize(10)
                lwfont.setBold(False)
                lwmodelItem.setFont(lwfont)
                lwmodelItem.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEditable)
                lwmodelItem.setSizeHint(QtCore.QSize(self.OPZCard.listView.size().width()-5, self.OPZCard.listView.size().height()))
                lwmodelItem.setTextAlignment(QtCore.Qt.AlignTop|QtCore.Qt.AlignLeft)
                lwmodel.appendRow(lwmodelItem)
                self.OPZCard.listView.setModel(lwmodel)

    def add_Zcard_info(self, bank, data):
        locale.setlocale(locale.LC_NUMERIC, 'rus')
        self.Zcard.setWindowTitle("Карточка заемщика " + self.client_name)
        for i in range(len(data)):
            if data[i][0] == bank:
                if data[i][20] == None:
                    #Описание деятельности заемщика
                    model_font = QtGui.QFont()
                    model_font.setPointSize(10)
                    model_font.setBold(False)
                    self.Zcard.listWidget.addItem(str(data[i][1]))
                    self.Zcard.listWidget.item(0).setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEditable)
                    self.Zcard.listWidget.sizeHintForRow(0)
                    self.Zcard.listWidget.setFont(model_font)
                    # Вывод по ссуде
                    self.Zcard.listWidget_2.addItem(str(data[i][4]))
                    self.Zcard.listWidget_2.item(0).setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEditable)
                    self.Zcard.listWidget_2.sizeHintForRow(0)
                    self.Zcard.listWidget_2.setFont(model_font)
                    # Целевое использование средств
                    self.Zcard.listWidget_3.addItem(str(data[i][3]))
                    self.Zcard.listWidget_3.item(0).setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEditable)
                    self.Zcard.listWidget_3.sizeHintForRow(0)
                    self.Zcard.listWidget_3.setFont(model_font)
                    # Анализ финансового положения
                    self.Zcard.listWidget_4.addItem(str(data[i][2]))
                    self.Zcard.listWidget_4.item(0).setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEditable)
                    self.Zcard.listWidget_4.sizeHintForRow(0)
                    self.Zcard.listWidget_4.setFont(model_font)
                    self.Zcard.label.setText("Источник данных: " + str(data[i][6]))
                    self.Zcard.label_2.setText("Дата отчетности: " + str(data[i][5]))
                    TW_font_special = QtGui.QFont()
                    TW_font_special.setPointSize(10)
                    TW_font_special.setBold(True)
                    TW_font_special.setItalic(False)
                    model_5 = QtGui.QStandardItemModel()  # финансовая отчетность
                    str_1 = ['АКТИВЫ', 'Основные средства', 'Запасы', 'Дебиторская задолженность',
                             'Финансовые вложения', 'Денежные средства', 'Прочие активы', 'ПАССИВЫ',
                             'Капитал и резервы', 'Кредиты и займы', 'Кредиторская задолженность',
                             'Прочие обязательства']
                    k = 8
                    for j in range(len(str_1)):
                        col_0_item = QtGui.QStandardItem(str_1[j])
                        if j == 0 or j == 7:
                            col_0_item.setFont(TW_font_special)
                            try:
                                col_1_item = QtGui.QStandardItem('{:.12n}'.format(float('{:-.2f}'.format(int(data[i][7])))))
                            except ValueError:
                                col_1_item = QtGui.QStandardItem('нд')
                            except TypeError:
                                col_1_item = QtGui.QStandardItem('нд')

                        else:
                            try:
                                col_1_item = QtGui.QStandardItem('{:.12n}'.format(float('{:-.2f}'.format(int(data[i][k])))))
                            except ValueError:
                                col_1_item = QtGui.QStandardItem('нд')
                            except TypeError:
                                col_1_item = QtGui.QStandardItem('нд')
                            k += 1
                        col_0_item.setTextAlignment(QtCore.Qt.AlignCenter)
                        col_1_item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignLeft)
                        model_5.appendRow([col_0_item, col_1_item])
                    self.Zcard.tableView.setModel(model_5)

                    model_6 = QtGui.QStandardItemModel()  # финансовая отчетность 2
                    str_1 = ['Выручка', 'EBITDA, приведенная к годовой']
                    for j in range(len(str_1)):
                        col_0_item = QtGui.QStandardItem(str_1[j])
                        try:
                            col_1_item = QtGui.QStandardItem('{:.12n}'.format(float('{:-.2f}'.format(int(data[i][j + 18])))))
                        except ValueError:
                            col_1_item = QtGui.QStandardItem('нд')
                        except TypeError:
                            col_1_item = QtGui.QStandardItem('нд')
                        col_0_item.setTextAlignment(QtCore.Qt.AlignCenter)
                        col_1_item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignLeft)
                        model_6.appendRow([col_0_item, col_1_item])
                    self.Zcard.tableView_2.setModel(model_6)
                else:
                    # Описание деятельности заемщика
                    model_font = QtGui.QFont()
                    model_font.setPointSize(10)
                    model_font.setBold(False)
                    self.Zcard.listWidget.addItem(str(data[i][1]))
                    self.Zcard.listWidget.item(0).setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEditable)
                    self.Zcard.listWidget.sizeHintForRow(0)
                    self.Zcard.listWidget.setFont(model_font)
                    # Вывод по ссуде
                    self.Zcard.listWidget_2.addItem(str(data[i][4]))
                    self.Zcard.listWidget_2.item(0).setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEditable)
                    self.Zcard.listWidget_2.sizeHintForRow(0)
                    self.Zcard.listWidget_2.setFont(model_font)
                    # Целевое использование средств
                    self.Zcard.listWidget_3.addItem(str(data[i][3]))
                    self.Zcard.listWidget_3.item(0).setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEditable)
                    self.Zcard.listWidget_3.sizeHintForRow(0)
                    self.Zcard.listWidget_3.setFont(model_font)

    def onActivated(self):
        if self.prepared_data:
            self.add_common_data_for_cc(self.comboBox.currentText(), self.common_data_for_cc)
            self.add_acc_data_for_cc(self.comboBox.currentText(), self.acc_data_for_cc)
            self.add_ob_data_for_cc(self.comboBox.currentText(), self.ob_data_for_cc)
            self.add_KD_widgets(self.comboBox.currentText(), self.kd_data_for_cc)

    def closeEvent(self, event):
        self.destroy()

    def but_1_clicked(self):
        #print('Нажали кнопку KartochkaZaemchika')
        self.Zcard = ZaemchikCard()
        self.add_Zcard_info(self.comboBox.currentText(), self.Zcard_data_for_cc)
        self.Zcard.show()

    def but_2_clicked(self):
        #print('Нажали кнопку OPZ')
        self.OPZCard = DannieOPZ()
        self.add_OPZ_info(self.comboBox.currentText(), self.OPZ_data_for_cc)
        self.OPZCard.show()

    def zapros_1(self, data_from_db):  # kp_ul_fl_raschet
        con_to_DB = sqlite3.connect('asv_db.db')
        cur = con_to_DB.cursor()
        data_for_tab = []
        for i in range(len(data_from_db)):
            cur.execute("""
                        SELECT
                        banks.small_name, banks.id, clients.inn, clients.name, 
                        REPLACE(clients.doc_seria,' ','') || ' ' || REPLACE(clients.doc_number,' ',''),                        
                        SUM(CAST(REPLACE(kp_ul_fl_raschet.balance_cost, ',', '.') AS real)) AS balance_cost,
                        SUM(CAST(REPLACE(kp_ul_fl_raschet.real_cost_exp, ',', '.') AS real)) AS real_cost_exp,
                        SUM(CAST(REPLACE(kp_ul_fl_raschet.reservi, ',', '.') AS real)) AS reservi,
                        SUM(CAST(REPLACE(kp_ul_fl_raschet.corr_expert, ',', '.') AS real)) AS corr_expert,
                        GROUP_CONCAT(grp.gruppa, ';') AS gruppa
                        FROM 
                        banks,                         
                        clients,
                        kp_ul_fl_raschet,                         
                        (SELECT DISTINCT kp_ul_fl_raschet.gruppa FROM kp_ul_fl_raschet) as grp
                        WHERE
                        banks.small_name = '""" + str(data_from_db[i][0]) + """'
                        AND clients.id_client = '""" + str(data_from_db[i][12]) + """'
                        AND clients.inn = kp_ul_fl_raschet.inn and banks.id = kp_ul_fl_raschet.bank_id
                        GROUP BY banks.small_name, banks.id, clients.inn, clients.name, clients.doc_seria, 
                        clients.doc_number, grp.gruppa""")
            data_prep_tab = cur.fetchall()
            if data_prep_tab:
                data_for_tab.append(data_prep_tab[0])
        cur.close()
        con_to_DB.close()
        return data_for_tab

    def zapros_2(self, data_from_db):  # kp_ul_opis
        con_to_DB = sqlite3.connect('asv_db.db')
        cur = con_to_DB.cursor()
        data_for_tab = []
        for i in range(len(data_from_db)):
            cur.execute("""
                        SELECT
                        banks.small_name, banks.id, clients.inn, clients.name,
                        REPLACE(clients.doc_seria,' ','') || ' ' || REPLACE(clients.doc_number,' ',''),
                        kp_ul_opis.ur_dela_bankrot || ' от ' || kp_ul_opis.date_dela as UR_DELA,                        
                        kp_ul_opis.beneficiar, kp_ul_opis.fin_po, kp_ul_opis.obsluz_dolga_bank_exp,
                        kp_ul_opis.korr_asv_exp, kp_ul_opis.korr_asv_590
                        FROM banks, clients, kp_ul_opis
                        WHERE
                        banks.small_name = '""" + str(data_from_db[i][0]) + """'
                        and clients.id_client = '""" + str(data_from_db[i][12]) + """'
                        and clients.inn = kp_ul_opis.inn and banks.id = kp_ul_opis.bank_id
                        group by banks.small_name, banks.id, clients.inn, clients.name, clients.doc_seria, 
                        clients.doc_number, kp_ul_opis.ur_dela_bankrot, 
                        kp_ul_opis.date_dela, kp_ul_opis.beneficiar, kp_ul_opis.fin_po, kp_ul_opis.obsluz_dolga_bank_exp, 
                        kp_ul_opis.korr_asv_exp, kp_ul_opis.korr_asv_590""")
            data_prep_tab = cur.fetchall()
            if data_prep_tab:
                data_for_tab.append(data_prep_tab[0])
        cur.close()
        con_to_DB.close()
        return data_for_tab

    def zapros_3(self, data_from_db):  # kp_ul_spark
        con_to_DB = sqlite3.connect('asv_db.db')
        cur = con_to_DB.cursor()
        data_for_tab = []
        for i in range(len(data_from_db)):
            cur.execute("""
                        SELECT
                        banks.small_name, banks.id, clients.inn, clients.name, 
                        REPLACE(clients.doc_seria,' ','') || ' ' || REPLACE(clients.doc_number,' ',''),                        
                        kp_ul_spark.date_gos_reg, CAST(REPLACE(kp_ul_spark.uk, ',', '.') AS real) AS ustav_cap, kp_ul_spark.chislennost, kp_ul_spark.adres_reg, 
                        kp_ul_spark.vid, kp_ul_spark.status, kp_ul_spark.rukovoditel
                        FROM banks, clients, kp_ul_spark
                        WHERE
                        banks.small_name = '""" + str(data_from_db[i][0]) + """'
                        and clients.id_client = '""" + str(data_from_db[i][12]) + """'
                        and clients.inn = kp_ul_spark.inn and banks.id = kp_ul_spark.bank_id
                        group by banks.small_name, banks.id, clients.inn, clients.name, clients.doc_seria, 
                        clients.doc_number, kp_ul_spark.date_gos_reg, kp_ul_spark.uk, kp_ul_spark.chislennost, kp_ul_spark.adres_reg, 
                                kp_ul_spark.vid, kp_ul_spark.status, kp_ul_spark.rukovoditel""")
            data_prep_tab = cur.fetchall()
            if data_prep_tab:
                data_for_tab.append(data_prep_tab[0])
        cur.close()
        con_to_DB.close()
        return data_for_tab

    def zapros_4(self, data_from_db):  # obespechenie - общая сумма и виды обеспечения
        con_to_DB = sqlite3.connect('asv_db.db')
        cur = con_to_DB.cursor()
        data_for_tab = []
        for i in range(len(data_from_db)):
            cur.execute("""
                          SELECT
                          banks.small_name, banks.id, clients.inn, clients.name,
                          REPLACE(clients.doc_seria,' ','') || ' ' || REPLACE(clients.doc_number,' ',''),
                          ob_for_sum_obesp.summa_obesp, ob_for_vid_ob.vid_ob
                          FROM banks, clients,
                              (SELECT obespechenie.bank_id, obespechenie.inn, SUM(CAST(REPLACE(obespechenie.summa_s_nds, ',', '.') AS real)) AS summa_obesp
                              FROM obespechenie GROUP BY obespechenie.bank_id, obespechenie.inn) as ob_for_sum_obesp,
                              (SELECT obespechenie.bank_id, obespechenie.inn, GROUP_CONCAT(DISTINCT obespechenie.vid) AS vid_ob
                              FROM obespechenie                        
                              GROUP BY obespechenie.bank_id, obespechenie.inn) as ob_for_vid_ob
                          WHERE
                          banks.small_name = '""" + str(data_from_db[i][0]) + """'
                          and clients.id_client = '""" + str(data_from_db[i][12]) + """'
                          and clients.inn = ob_for_sum_obesp.inn
                          and banks.id = ob_for_sum_obesp.bank_id
                          and clients.inn = ob_for_vid_ob.inn
                          and banks.id = ob_for_vid_ob.bank_id
                          group by banks.small_name, banks.id, clients.inn, clients.name, clients.doc_seria,
                          clients.doc_number, ob_for_sum_obesp.summa_obesp, ob_for_vid_ob.vid_ob
                          """
                        )
            data_prep_tab = cur.fetchall()
            if data_prep_tab:
                data_for_tab.append(data_prep_tab[0])
        cur.close()
        con_to_DB.close()
        return data_for_tab

    def zapros_5(self, data_from_db):  # opz - обслуживается или нет
        con_to_DB = sqlite3.connect('asv_db.db')
        cur = con_to_DB.cursor()
        data_for_tab = []
        for i in range(len(data_from_db)):
            cur.execute("""
                        SELECT
                        banks.small_name, banks.id, clients.inn, clients.name, 
                        REPLACE(clients.doc_seria,' ','') || ' ' || REPLACE(clients.doc_number,' ',''),                        
                        opz.dolg_ne_obsl_posle
                        FROM banks, clients,
                        (SELECT bank_id, inn, dolg_ne_obsl_posle FROM opz) as opz
                        WHERE
                        banks.small_name = '""" + str(data_from_db[i][0]) + """'
                        and clients.id_client = '""" + str(data_from_db[i][12]) + """'
                        and clients.inn = opz.inn and banks.id = opz.bank_id
                        group by banks.small_name, banks.id, clients.inn, clients.name, clients.doc_seria, 
                        clients.doc_number, opz.dolg_ne_obsl_posle""")
            data_prep_tab = cur.fetchall()
            if data_prep_tab:
                data_for_tab.append(data_prep_tab[0])
        cur.close()
        con_to_DB.close()
        return data_for_tab

    def zapros_6(self, data_from_db):  # accounts - все счета клиента
        con_to_DB = sqlite3.connect('asv_db.db')
        cur = con_to_DB.cursor()
        data_for_tab = []
        for i in range(len(data_from_db)):
            cur.execute("""
                        SELECT
                        banks.small_name, banks.id, clients.inn, clients.name, 
                        accounts.account, accounts.acc_name
                        FROM banks, clients, accounts
                        WHERE
                        banks.small_name = '""" + str(data_from_db[i][0]) + """'
                        and clients.id_client = '""" + str(data_from_db[i][12]) + """'
                        and clients.id_client = accounts.id_client
                        and accounts.bank_id = banks.id""")
            data_prep_tab = cur.fetchall()
            for j in data_prep_tab:
                if j:
                    data_for_tab.append(j)
            # print(data_for_tab)
        cur.close()
        con_to_DB.close()
        return data_for_tab

    def zapros_7(self, data_from_db):  # obespechenie - информация об обеспечении
        con_to_DB = sqlite3.connect('asv_db.db')
        cur = con_to_DB.cursor()
        data_for_tab = []
        for i in range(len(data_from_db)):
            cur.execute("""
                        SELECT
                        banks.small_name, banks.id, clients.inn, clients.name, 
                        obespechenie.kred_dog, obespechenie.dog_zaloga, obespechenie.vid, 
                        obespechenie.name_obespechenia, obespechenie.adres_obesp, obespechenie.ploshad, obespechenie.god_vipuska, 
                        CAST(REPLACE(obespechenie.summa_s_nds, ',', '.') as real) AS summa_ob_s_nds
                        FROM banks, clients, obespechenie
                        WHERE
                        banks.small_name = '""" + str(data_from_db[i][0]) + """'
                        and clients.id_client = '""" + str(data_from_db[i][12]) + """'
                        and clients.inn = obespechenie.inn
                        and obespechenie.bank_id = banks.id""")
            data_prep_tab = cur.fetchall()
            for j in data_prep_tab:
                if j:
                    data_for_tab.append(j)
            # print(data_for_tab)
        cur.close()
        con_to_DB.close()
        return data_for_tab

    def zapros_8(self, data_from_db):  # KD - информация об Кредитах
        con_to_DB = sqlite3.connect('asv_db.db')
        cur = con_to_DB.cursor()
        data_for_tab = []
        for i in range(len(data_from_db)):
            cur.execute("""
                        SELECT
                        banks.small_name, banks.id, clients.inn, clients.name,
                        kp_ul_fl_raschet.kred_dog, obespechenie.date_kd, kp_ul_fl_raschet.srok_kd,
                        kp_ul_fl_raschet.percent_kd, kp_ul_fl_raschet.prosrochka, kp_ul_fl_raschet.balance_cost,
                        kp_ul_fl_raschet.reservi, obespechenie.sum_ob, kp_ul_fl_raschet.corr_expert,
                        kp_ul_fl_raschet.real_cost_exp, kp_ul_fl_raschet.gruppa
                        FROM
                        banks, clients, kp_ul_fl_raschet,
                        (SELECT kred_dog, date_kd, sum(CAST(REPLACE(summa_s_nds, ',', '.') as real)) AS sum_ob
                        FROM obespechenie GROUP BY kred_dog, date_kd) AS obespechenie
                        WHERE
                        banks.small_name = '""" + str(data_from_db[i][0]) + """'
                        and clients.id_client = '""" + str(data_from_db[i][12]) + """'
                        and clients.inn = kp_ul_fl_raschet.inn
                        and kp_ul_fl_raschet.bank_id = banks.id
                        and kp_ul_fl_raschet.kred_dog = obespechenie.kred_dog""")
            data_prep_tab = cur.fetchall()
            for j in data_prep_tab:
                if j:
                    data_for_tab.append(j)
            # print(data_for_tab)
        cur.close()
        con_to_DB.close()
        return data_for_tab

    def zapros_9(self, data_from_db):  # OPZ - информация OPZ
        con_to_DB = sqlite3.connect('asv_db.db')
        cur = con_to_DB.cursor()
        data_for_tab = []
        for i in range(len(data_from_db)):
            cur.execute("""
                        SELECT
                        banks.small_name, banks.id, clients.inn, clients.name,
                        opz.ocenka_fin_po, opz.priznak_n_buh_otch, opz.n_n_factor_fin_po, opz.n_otch_iz_fns, opz.n_otch_iz_spark,
                        opz.priznak_refinans_od, opz.priznak_refinans_p, opz.dolg_ne_obsl_posle, opz.bad_kach_obs_dolga, opz.other_neg_fact_obs_dolga,
                        opz.nalogi, opz.arenda, opz.sod_pers, opz.other_payments, opz.scheta_v_drugih_ko, opz.scheta_v_drugih_ko_npa, opz.schemnie_oper,
                        opz.charak_plat_v_per_kred, opz.necelevoe_isp_kred_sr, opz.zavisimost_ot_kred_sred,
                        opz.economic_relations, opz.legal_connections, opz.economic_relations_with_other_cl, opz.legal_connections_with_other_cl,
                        opz.mass_adres, opz.mass_adres_po_fns, opz.plohoy_dogovor_arendi, opz.registration_flat, opz.net_zaemchika_tam, opz.mass_tel,
                        opz.net_cite, opz.uc, opz.mass_dir, opz.mass_uch, opz.dir_uch, opz.no_buhgalter, opz.chislennost, opz.tehnika_v_drugom_banke,
                        opz.ploho_v_actah, opz.ploho_v_smi, opz.nedeistvuet_ze, opz.bankrotstvo, opz.ugolovka, opz.pravonarucheniya_nalogovie,
                        opz.ne_mozem_nayti, opz.net_nichego, opz.voobshe_nichego_net, opz.important_info
                        FROM
                        banks, clients, opz
                        WHERE
                        banks.small_name = '""" + str(data_from_db[i][0]) + """'
                        and clients.id_client = '""" + str(data_from_db[i][12]) + """'
                        and clients.inn = opz.inn
                        and opz.bank_id = banks.id""")
            data_prep_tab = cur.fetchall()
            for j in data_prep_tab:
                if j:
                    data_for_tab.append(j)
            # print(data_for_tab)
        cur.close()
        con_to_DB.close()
        return data_for_tab

    def zapros_10(self, data_from_db):  # OPZ - информация OPZ
        con_to_DB = sqlite3.connect('asv_db.db')
        cur = con_to_DB.cursor()
        data_for_tab = []
        for i in range(len(data_from_db)):
            cur.execute("""
                        SELECT
                        bank.small_name, bank.id, client.inn, client.name, ul.kharakteristika_deyat, ul.opis_finpo_www, ul.analiz_opr, ul.vivod_po_ssude, ul.data_otchetnosti, ul.istochnik,
                        ul.valuta_bal, ul.os, ul.zapasi, ul.deb_zad, ul.fin_vlozenia, ul.dengi, ul.prochie_aktivi, ul.kap_rez, ul.kred_zaymi, ul.kred_dolg,
                        ul.prochie_obyazatelstva, ul.viruchka, ul.ebitda, fl.kharakteristika_deyat, fl.celevoe, fl.vivod
                        FROM
                        (SELECT small_name, id FROM banks WHERE small_name = '""" + str(data_from_db[i][0]) + """') AS bank
                        LEFT JOIN
                        (SELECT id_client, inn, name, bank_id FROM clients WHERE id_client = '""" + str(data_from_db[i][12]) + """') AS client
                        ON client.bank_id = bank.id
                        LEFT JOIN
                        (SELECT
                         bank_id, inn, kharakteristika_deyat, opis_finpo_www, analiz_opr, vivod_po_ssude, data_otchetnosti, istochnik,
                         valuta_bal, os, zapasi, deb_zad, fin_vlozenia, dengi, prochie_aktivi, kap_rez, kred_zaymi, kred_dolg,
                         prochie_obyazatelstva, viruchka, ebitda FROM kp_ul_opis) AS ul
                        ON ul.inn = client.inn AND ul.bank_id = bank.id
                        LEFT JOIN
                        (SELECT bank_id, id_client, kharakteristika_deyat, celevoe, vivod FROM kp_fl_opis) AS fl 
                        ON fl.id_client = client.id_client AND fl.bank_id = bank.id""")
            data_prep_tab = cur.fetchall()
            for j in data_prep_tab:
                if j:
                    data_for_tab.append(j)
            #print(data_for_tab)
        cur.close()
        con_to_DB.close()
        return data_for_tab