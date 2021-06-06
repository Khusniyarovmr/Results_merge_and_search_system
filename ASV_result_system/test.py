import sqlite3
from CONSTANTS import DATA_BASE


con_to_DB = sqlite3.connect(DATA_BASE)
cur = con_to_DB.cursor()
data_for_tab = []
cur.execute("""
            SELECT
            banks.small_name, banks.id, clients.inn, clients.name, 
            REPLACE(clients.doc_seria,' ','') || ' ' || REPLACE(clients.doc_number,' ',''),                        
            SUM(CAST(REPLACE(kp_ul_fl_raschet.balance_cost, ',', '.') AS real)) AS balance_cost,
            SUM(CAST(REPLACE(kp_ul_fl_raschet.real_cost_exp, ',', '.') AS real)) AS real_cost_exp,
            SUM(CAST(REPLACE(kp_ul_fl_raschet.reservi, ',', '.') AS real)) AS reservi,
            SUM(CAST(REPLACE(kp_ul_fl_raschet.corr_expert, ',', '.') AS real)) AS corr_expert,
            GROUP_CONCAT(DISTINCT kp_ul_fl_raschet.gruppa) AS gruppa
            FROM 
            banks,                         
            clients,
            kp_ul_fl_raschet                         
            --(SELECT DISTINCT kp_ul_fl_raschet.gruppa FROM kp_ul_fl_raschet) as grp
            WHERE
            banks.small_name = 'ПАО КБ «ПФС-БАНК»'
            AND clients.id_client = '652'
            AND clients.inn = kp_ul_fl_raschet.inn and banks.id = kp_ul_fl_raschet.bank_id
            GROUP BY banks.small_name, banks.id, clients.inn, clients.name, clients.doc_seria, 
            clients.doc_number, kp_ul_fl_raschet.gruppa""")
data_prep_tab = cur.fetchall()
print(data_prep_tab)