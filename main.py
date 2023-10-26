import os
import sqlite3
import pandas as pd
import xlrd

from db import *


def from_excel_to_db():
    xls_file_dir_name = "./data/excel/2022/"
    xls_files_list = os.listdir(xls_file_dir_name)
    for xls_file in xls_files_list:
        print(xls_file)
    """in sheet.py comment 3 lines:
     #if self.biff_version >= 80:
         self.utter_max_rows = 65536
     #else:
     #   self.utter_max_rows = 16384"""
    workbook = xlrd.open_workbook(xls_file_dir_name + "кофе_22_01_1.xls", encoding_override="cp1251")
    df = pd.read_excel(workbook, header=None, skiprows=2)
    df.columns = db_column_name_list
    print(df[[doc_date_col, organization_col]].head(2))
    conn = create_connection(sqlite_db_file)
    with conn:
        curs = conn.cursor()
        try:
            # print(execute_read_query(conn, "PRAGMA encoding;"))
            execute_query(conn, drop_table_sales)
            # df.to_sql(sales_table_name, conn, if_exists="append", index=False, chunksize=1000)
        except sqlite3.Error as e:
            print(f"Error: {e}")
        finally:
            if curs:
                curs.close()


def main():
    from_excel_to_db()


if __name__ == '__main__':
    main()
