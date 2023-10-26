import os
import sqlite3
import pandas as pd
import xlrd

from db import *


def from_excel_to_db():
    xls_file_dir_name = "./data/excel/2022/"
    xls_files_list = os.listdir(xls_file_dir_name)
    conn = create_connection(sqlite_db_file)
    with conn:
        curs = conn.cursor()
        try:
            execute_query(conn, create_table_sales)
            # print(execute_read_query(conn, "PRAGMA encoding;"))
            for xls_file in xls_files_list:
                """in sheet.py comment 3 lines:
                 #if self.biff_version >= 80:
                     self.utter_max_rows = 65536
                 #else:
                 #   self.utter_max_rows = 16384"""
                workbook = xlrd.open_workbook(xls_file_dir_name + xls_file, encoding_override="cp1251")
                df = pd.read_excel(workbook, header=None, skiprows=2)
                df.columns = db_column_name_list
                print(xls_file + " прочитан.")
                print(df[[doc_date_col, organization_col]].head(2))
                df.to_sql(sales_table_name, conn, if_exists="append", index=False, chunksize=1000)
                print(xls_file + " копирован в БД")
        except sqlite3.Error as e:
            print(f"Error: {e}")
        finally:
            if curs:
                curs.close()


def simple_read_query():
    conn = create_connection(sqlite_db_file)
    with conn:
        curs = conn.cursor()
        try:
            print(execute_read_query(conn, "PRAGMA encoding;"))
        except sqlite3.Error as e:
            print(f"Error: {e}")
        finally:
            if curs:
                curs.close()


def main():
    simple_read_query()


if __name__ == '__main__':
    main()
