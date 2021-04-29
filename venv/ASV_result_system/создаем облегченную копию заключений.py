import os
import os.path
from os import path
import re
import time
from datetime import datetime
import docx
import pandas as pd
import openpyxl

f_directory_ok = ['C:/NEW/Файлы_заключений_для_системы/Заключения', 'C:/NEW/Файлы_заключений_для_системы/Отчет_АБ'
                  , 'C:/NEW/Файлы_заключений_для_системы/Мастер_файлы', 'C:/NEW/Файлы_заключений_для_системы/Табл_3'
                  , 'C:/NEW/Файлы_заключений_для_системы/Целевое']
for dir in f_directory_ok:
    se_dir = str(dir) + '/Поиск'
    files_ok = os.listdir(dir)
    files_se = os.listdir(se_dir)
    for file in files_ok:
        if file.endswith(".docx"):
            if not file in files_se:
                doc = docx.Document(os.path.join(dir, file))
                doc2 = docx.Document()
                for paragraph in doc.paragraphs:
                    if not paragraph.text == '':
                        doc2.add_paragraph(re.sub("^\s+|\n|\r|\s+$", '', paragraph.text))
                for t in doc.tables:
                    for row in t.rows:
                        text = ''
                        for cell in row.cells:
                            text += cell.text + ' '
                        doc2.add_paragraph(re.sub("^\s+|\n|\r|\s+$", '', text))
                doc2.save(os.path.join(se_dir, file))
        if file.endswith(".xlsx"):
            if not file.replace('xlsx', 'csv') in files_se:
                dataframe = pd.read_excel(io=os.path.join(dir, file), engine='openpyxl', sheet_name=None,
                                          dtype=str)
                for key, value in dataframe.items():
                    dataframe[key].to_csv(str(os.path.join(se_dir, file.replace('xlsx', 'csv'))), sep=',',
                                          na_rep='', float_format=None, columns=None, header=True, index=True,
                                          index_label=None, mode='a',
                                          encoding='UTF-8', compression='infer', quoting=None, quotechar='"',
                                          line_terminator=None, chunksize=None,
                                          date_format=None, doublequote=True, escapechar=None, decimal=',',
                                          errors='strict')