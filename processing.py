import pandas as pd
import numpy as np
from db import *


def export_tables_to_csv():
    table_to_sql(division_table_name)
    table_to_sql(ta_table_name)
    table_to_sql(tt_table_name)
    table_to_sql(product_table_name)
    process_table_sales()


def process_table_sales():
    cnx = sqlite3.connect(sqlite_db_file)
    sales = pd.read_sql_query(f"SELECT * FROM {sales_table_name}", cnx)
    sales.drop([doc_number_col, organization_id_col, operator_id_col, product_cost_price_col], axis=1, inplace=True)
    sales.replace([None], np.nan, inplace=True)
    sales = sales.astype({division_id_col: "Int64", tt_id_col: "Int64", product_id_col: "Int64"})
    # группировка для уменьшения размера
    sales_group = sales.groupby([doc_date_col,
                                 ta_id_col,
                                 division_id_col,
                                 tt_id_col,
                                 ta_cell_number_col,
                                 product_id_col],
                                dropna=False).sum()
    sales_group = sales_group.reset_index()
    # дополнительная таблица для уменьшения размера основной
    uniq_combo_id = sales_group.drop_duplicates(subset=[doc_date_col, ta_id_col, division_id_col, tt_id_col])
    uniq_combo_id.drop(labels=[ta_cell_number_col,
                               product_id_col,
                               number_of_sales_col,
                               sum_of_sales_col,
                               product_cost_price_col], axis=1, inplace=True)
    combo_id = "combo_id"
    uniq_combo_id[combo_id] = range(1, len(uniq_combo_id) + 1)
    uniq_combo_id.to_csv(f"./temp/{combo_id}.csv")
    sales_group = sales_group.merge(uniq_combo_id, how='left')
    sales_group.drop(labels=[doc_date_col, ta_id_col, division_id_col, tt_id_col], axis=1, inplace=True)
    sales_group.to_csv(f"./temp/{sales_table_name}.csv", index=False)


def table_to_sql(table_name):
    (pd.read_sql_table(table_name,
                       f"sqlite:///{division_table_name}",
                       index_col=id_col).to_csv(f"./temp/{table_name}.csv"))