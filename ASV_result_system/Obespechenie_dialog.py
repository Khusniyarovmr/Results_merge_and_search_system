# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\NEW\proga\Obespechenie_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(750, 290)
        self.label_16 = QtWidgets.QLabel(Dialog)
        self.label_16.setGeometry(QtCore.QRect(10, 10, 731, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 40, 731, 241))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 2)
        self.listView_2 = QtWidgets.QListView(self.layoutWidget)
        self.listView_2.setObjectName("listView_2")
        self.gridLayout.addWidget(self.listView_2, 2, 2, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget)
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setWordWrap(True)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 2, 3, 1, 2)
        self.listView_11 = QtWidgets.QListView(self.layoutWidget)
        self.listView_11.setObjectName("listView_11")
        self.gridLayout.addWidget(self.listView_11, 2, 5, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 2)
        self.listView_3 = QtWidgets.QListView(self.layoutWidget)
        self.listView_3.setObjectName("listView_3")
        self.gridLayout.addWidget(self.listView_3, 3, 2, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.layoutWidget)
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setWordWrap(True)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 3, 3, 1, 2)
        self.listView_12 = QtWidgets.QListView(self.layoutWidget)
        self.listView_12.setObjectName("listView_12")
        self.gridLayout.addWidget(self.listView_12, 3, 5, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 2)
        self.listView_4 = QtWidgets.QListView(self.layoutWidget)
        self.listView_4.setObjectName("listView_4")
        self.gridLayout.addWidget(self.listView_4, 4, 2, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget)
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setWordWrap(True)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 4, 3, 1, 2)
        self.listView_13 = QtWidgets.QListView(self.layoutWidget)
        self.listView_13.setObjectName("listView_13")
        self.gridLayout.addWidget(self.listView_13, 4, 5, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setWordWrap(True)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 9, 0, 1, 2)
        self.listView_7 = QtWidgets.QListView(self.layoutWidget)
        self.listView_7.setObjectName("listView_7")
        self.gridLayout.addWidget(self.listView_7, 9, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setWordWrap(True)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 10, 0, 1, 2)
        self.listView_8 = QtWidgets.QListView(self.layoutWidget)
        self.listView_8.setObjectName("listView_8")
        self.gridLayout.addWidget(self.listView_8, 10, 2, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.layoutWidget)
        self.label_18.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_18.setWordWrap(True)
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 10, 3, 1, 2)
        self.listView_17 = QtWidgets.QListView(self.layoutWidget)
        self.listView_17.setObjectName("listView_17")
        self.gridLayout.addWidget(self.listView_17, 10, 5, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setWordWrap(True)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 11, 0, 2, 2)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 2, 2)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        self.label_9.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setWordWrap(True)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 0, 3, 2, 2)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 7, 0, 2, 2)
        self.label_19 = QtWidgets.QLabel(self.layoutWidget)
        self.label_19.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_19.setWordWrap(True)
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 11, 3, 2, 2)
        self.listView_15 = QtWidgets.QListView(self.layoutWidget)
        self.listView_15.setObjectName("listView_15")
        self.gridLayout.addWidget(self.listView_15, 9, 5, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.layoutWidget)
        self.label_17.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_17.setWordWrap(True)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 9, 3, 1, 2)
        self.label_14 = QtWidgets.QLabel(self.layoutWidget)
        self.label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_14.setWordWrap(True)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 7, 3, 2, 2)
        self.listView = QtWidgets.QListView(self.layoutWidget)
        self.listView.setObjectName("listView")
        self.gridLayout.addWidget(self.listView, 1, 2, 1, 1)
        self.listView_10 = QtWidgets.QListView(self.layoutWidget)
        self.listView_10.setObjectName("listView_10")
        self.gridLayout.addWidget(self.listView_10, 1, 5, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 2, 2)
        self.label_15 = QtWidgets.QLabel(self.layoutWidget)
        self.label_15.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_15.setWordWrap(True)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 5, 3, 2, 2)
        self.listView_9 = QtWidgets.QListView(self.layoutWidget)
        self.listView_9.setObjectName("listView_9")
        self.gridLayout.addWidget(self.listView_9, 11, 2, 1, 1)
        self.listView_18 = QtWidgets.QListView(self.layoutWidget)
        self.listView_18.setObjectName("listView_18")
        self.gridLayout.addWidget(self.listView_18, 11, 5, 1, 1)
        self.listView_6 = QtWidgets.QListView(self.layoutWidget)
        self.listView_6.setObjectName("listView_6")
        self.gridLayout.addWidget(self.listView_6, 7, 2, 1, 1)
        self.listView_16 = QtWidgets.QListView(self.layoutWidget)
        self.listView_16.setObjectName("listView_16")
        self.gridLayout.addWidget(self.listView_16, 7, 5, 1, 1)
        self.listView_5 = QtWidgets.QListView(self.layoutWidget)
        self.listView_5.setObjectName("listView_5")
        self.gridLayout.addWidget(self.listView_5, 5, 2, 1, 1)
        self.listView_14 = QtWidgets.QListView(self.layoutWidget)
        self.listView_14.setObjectName("listView_14")
        self.gridLayout.addWidget(self.listView_14, 5, 5, 1, 1)
        self.gridLayout.setColumnMinimumWidth(0, 5)
        self.gridLayout.setColumnMinimumWidth(1, 1)
        self.gridLayout.setColumnMinimumWidth(2, 2)
        self.gridLayout.setColumnMinimumWidth(3, 5)
        self.gridLayout.setColumnMinimumWidth(4, 1)
        self.gridLayout.setColumnMinimumWidth(5, 2)
        self.gridLayout.setRowMinimumHeight(1, 1)
        self.gridLayout.setRowMinimumHeight(2, 1)
        self.gridLayout.setRowMinimumHeight(3, 1)
        self.gridLayout.setRowMinimumHeight(4, 1)
        self.gridLayout.setRowMinimumHeight(5, 1)
        self.gridLayout.setRowMinimumHeight(6, 1)
        self.gridLayout.setRowMinimumHeight(7, 1)
        self.gridLayout.setRowMinimumHeight(8, 1)
        self.gridLayout.setRowMinimumHeight(9, 1)
        self.gridLayout.setRowMinimumHeight(10, 1)
        self.gridLayout.setRowMinimumHeight(11, 1)
        self.gridLayout.setRowMinimumHeight(12, 1)
        self.gridLayout.setColumnStretch(0, 5)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnStretch(2, 7)
        self.gridLayout.setColumnStretch(3, 5)
        self.gridLayout.setColumnStretch(4, 1)
        self.gridLayout.setColumnStretch(5, 7)
        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout.setRowStretch(2, 1)
        self.gridLayout.setRowStretch(3, 1)
        self.gridLayout.setRowStretch(4, 1)
        self.gridLayout.setRowStretch(5, 1)
        self.gridLayout.setRowStretch(6, 1)
        self.gridLayout.setRowStretch(7, 1)
        self.gridLayout.setRowStretch(8, 1)
        self.gridLayout.setRowStretch(9, 1)
        self.gridLayout.setRowStretch(10, 1)
        self.gridLayout.setRowStretch(11, 1)
        self.gridLayout.setRowStretch(12, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_16.setText(_translate("Dialog", "TextLabel"))
        self.label_3.setText(_translate("Dialog", "Вид обеспечения"))
        self.label_11.setText(_translate("Dialog", "Наименование обеспечения"))
        self.label_2.setText(_translate("Dialog", "Залогодатель"))
        self.label_13.setText(_translate("Dialog", "ИНН Залогодателя"))
        self.label_4.setText(_translate("Dialog", "Идентификатор"))
        self.label_12.setText(_translate("Dialog", "Первичный / последующий залог"))
        self.label_7.setText(_translate("Dialog", "Адрес / Место хранения"))
        self.label_8.setText(_translate("Dialog", "Наличие обременения в пользу банка"))
        self.label_18.setText(_translate("Dialog", "Наличие оригинала договора залога"))
        self.label_10.setText(_translate("Dialog", "Принимается к минимизации ущерба"))
        self.label.setText(_translate("Dialog", "№ Кредитного договора"))
        self.label_9.setText(_translate("Dialog", "Номер договора залога"))
        self.label_5.setText(_translate("Dialog", "Справедливая стоимость, руб."))
        self.label_19.setText(_translate("Dialog", "Сотрудник, проводивший оценку"))
        self.label_17.setText(_translate("Dialog", "Кадастровый номер / VIN"))
        self.label_14.setText(_translate("Dialog", "Основные характеристики (площадь / год выпуска)"))
        self.label_6.setText(_translate("Dialog", "Агрегатор"))
        self.label_15.setText(_translate("Dialog", "Описание агрегатора"))


class someclass(QtWidgets.QDialog,Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    win = someclass()
    win.show()
    sys.exit(app.exec_())