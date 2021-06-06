import sqlite3


try:
    sqlite_connection = sqlite3.connect('asv_db.db')
    cursor = sqlite_connection.cursor()
    print("База данных подключена к SQLite")



    cursor.execute("""
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
                    banks.small_name = 'ПАО КБ «ПФС-БАНК»'
                    and clients.id_client = '652'
                    and clients.inn = ob_for_sum_obesp.inn
                    and banks.id = ob_for_sum_obesp.bank_id
                    and clients.inn = ob_for_vid_ob.inn
                    and banks.id = ob_for_vid_ob.bank_id
                    group by banks.small_name, banks.id, clients.inn, clients.name, clients.doc_seria,
                    clients.doc_number, ob_for_sum_obesp.summa_obesp, ob_for_vid_ob.vid_ob
                    """)
    # cursor.execute("""
    #                 SELECT obespechenie.bank_id, obespechenie.inn, group_concat(DISTINCT ob.vid)
    #                 FROM obespechenie, banks, clients,
    #                     (SELECT obespechenie.vid
    #                     FROM obespechenie, banks, clients
    #                     WHERE banks.small_name = 'ПАО КБ «ПФС-БАНК»' and clients.id_client = '652' and clients.inn = obespechenie.inn
    #                     ) AS ob
    #                 WHERE banks.small_name = 'ПАО КБ «ПФС-БАНК»' and clients.id_client = '652' and clients.inn = obespechenie.inn
    #                 GROUP BY obespechenie.bank_id, obespechenie.inn
    #                 """)

    all_data = cursor.fetchall()
    print(cursor.fetchall())
    print("Скрипт SQLite успешно выполнен")
    cursor.close()

except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)
finally:
    if (sqlite_connection):
        sqlite_connection.close()
        print("Соединение с SQLite закрыто")