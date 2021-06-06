# -*- coding: utf-8 -*-
import os
import sys

import docx
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 200)
        Dialog.setWindowTitle("Текст результатов поиска")
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.listWidget = QtWidgets.QListWidget()
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 400, 200))
        self.gridLayout.addWidget(self.listWidget)
        self.listWidget.setWordWrap(True)
        self.listWidget.setTextElideMode(QtCore.Qt.ElideNone)
        self.listWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.listWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.listWidget.setFont(QtGui.QFont('Times New Roman', 10))
        QtCore.QMetaObject.connectSlotsByName(Dialog)

class SearchHighLight(QSyntaxHighlighter):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.pattern = QRegularExpression()
        self.format = QTextCharFormat()
        #self.format.setBackground(Qt.green)
        self.format.setForeground(Qt.blue)
        font = QFont()
        font.setFamily('Times New Roman')
        font.setPointSize(12)
        font.setBold(True)
        self.format.setFont(font)

    def highlightBlock(self, text):
        match_iterator = self.pattern.globalMatch(text.lower())
        while match_iterator.hasNext():
            match = match_iterator.next();
            self.setFormat(match.capturedStart(), match.capturedLength(), self.format)

    def searchText(self, text):
        self.pattern = QRegularExpression(text)
        self.rehighlight()

class Paragraph(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


    def paragraph_text(self, path, spisok):
        self.listWidget.clear()
        dirname, file_name = os.path.split(path)
        dirname = str(dirname) + '/Поиск'
        full_file_path = os.path.join(dirname, file_name)
        font = QFont()
        font.setFamily('Times New Roman')
        font.setPointSize(12)
        font.setBold(True)
        doc = docx.Document(full_file_path)
        k = 0
        for paragraph in doc.paragraphs:
            for s_name in spisok:
                if paragraph.text.lower().find(s_name) != -1:
                    item = QListWidgetItem()
                    textitem = QTextEdit()
                    textitem.document().setPlainText(paragraph.text)
                    textitem.setWordWrapMode(QTextOption.WordWrap)
                    self.searchHighLight = SearchHighLight(textitem.document())
                    self.searchHighLight.searchText(s_name)
                    textitem.document().adjustSize()
                    item.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEditable)
                    item.setTextAlignment(QtCore.Qt.AlignLeft)
                    w = textitem.document().size().width()
                    h = textitem.document().size().height()
                    item.setSizeHint(QSize(int(w), int(h)))
                    self.listWidget.addItem(item)
                    self.listWidget.setItemWidget(item, textitem)
                    k += 1


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    win = Paragraph()
    win.paragraph_text('C:/NEW/Файлы_заключений_для_системы/Заключения/ПАО КБ «ПФС-БАНК».docx', ['попова'])
    win.show()
    sys.exit(app.exec_())
