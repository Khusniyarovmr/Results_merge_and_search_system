import win32com.client as win32
word = win32.Dispatch("Word.Application")
word.Documents.Open("C:\\NEW\\Файлы_заключений_для_системы\\Заключения\\ООО КБ «Жилкредит».docx")
doc = word.ActiveDocument
stranica = 15
word.Selection.GoTo(win32.constants.wdGoToPage, win32.constants.wdGoToAbsolute, stranica)
doc.visible = 1