import sqlite3


try:
    sqlite_connection = sqlite3.connect('asv_db.db')
    cursor = sqlite_connection.cursor()
    print("База данных подключена к SQLite")

    with open('db_for_sqlite.sql', 'r', encoding='UTF-8') as sqlite_file:
        sql_script = sqlite_file.read()

    cursor.executescript(sql_script)
    print("Скрипт SQLite успешно выполнен")
    cursor.close()

except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)
finally:
    if (sqlite_connection):
        sqlite_connection.close()
        print("Соединение с SQLite закрыто")