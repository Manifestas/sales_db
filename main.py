import os
import sqlite3
import pandas as pd
from db import *


def from_excel_to_db():
    xls_file_dir_name = "./data/excel/"
    xls_files_list = os.listdir(xls_file_dir_name)
    for xls_file in xls_files_list:
        print(xls_file)
    df = pd.read_excel(xls_file_dir_name + "test.xlsx", header=None, skiprows=2)
    df.columns = db_column_name_list
    print(df)
    conn = create_connection(sqlite_db_file)
    with conn:
        curs = conn.cursor()
        try:
            df.to_sql(sales_table_name, conn, if_exists="append", index=False, chunksize=1000)
        except sqlite3.Error as e:
            print(f"Error: {e}")
        finally:
            if curs:
                curs.close()


def main():
    from_excel_to_db()


if __name__ == '__main__':
    main()
