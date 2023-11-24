# db, table names
sqlite_db_file = "./data/sqlite.db"
sales_raw_table_name = "sales_raw"
sales_table_name = "sales"
organization_table_name = "organization"
operator_table_name = "operator"
ta_table_name = "ta"
division_table_name = "division"
tt_table_name = "tt"
product_table_name = "product"

# column names
id_col = "id"
deleted_col = "deleted"
registered_col = "registered"
doc_number_col = "doc_number"
doc_date_col = "doc_date"
doc_date_time_col = "doc_date_time"
organization_col = "organization"
organization_id_col = "organization_id"
operator_col = "operator"
operator_id_col = "operator_id"
ta_id_col = "ta_id"
ta_brand_col = "ta_brand"
ta_model_col = "ta_model"
ta_serial_col = "ta_serial"
ta_type_col = "ta_type"
division_col = "division"
division_id_col = "division_id"
tt_id_col = "tt_id"
tt_name_col = "tt_name"
tt_location_col = "tt_location"
ta_cell_number_col = "ta_cell_number"
ta_cell_is_snack_col = "ta_cell_is_snack"
product_id_col = "product_id"
product_col = "product"
ta_cell_deficit_col = "ta_cell_deficit"
number_of_sales_col = "number_of_sales"
sum_of_sales_col = "sum_of_sales"
product_cost_price_col = "product_cost_price"
product_control_cost_price_col = "product_control_cost_price"

db_column_name_list = [deleted_col, registered_col, doc_number_col, doc_date_col, doc_date_time_col, organization_col,
                       operator_col, ta_brand_col, ta_model_col, ta_serial_col, ta_type_col, division_col, tt_name_col,
                       tt_location_col, ta_cell_number_col, ta_cell_is_snack_col, product_col, ta_cell_deficit_col,
                       number_of_sales_col, sum_of_sales_col, product_cost_price_col, product_control_cost_price_col]

# vending machine type in db
coffee_ta_type = "Кофейный ТА"
snack_ta_type = "Снековый ТА"

# column types
int_field_type = "INTEGER"
real_field_type = "REAL"
text_field_type = "TEXT"

# query's

# creating table with source data from Excel table
create_table_sales_raw = f"""
CREATE TABLE {sales_raw_table_name} (
    {deleted_col} {int_field_type},
    {registered_col} {int_field_type},
    {doc_number_col} {int_field_type},
    {doc_date_col} {text_field_type},
    {doc_date_time_col} {text_field_type},
    {organization_col} {text_field_type},
    {operator_col} {text_field_type},
    {ta_brand_col} {text_field_type},
    {ta_model_col} {text_field_type},
    {ta_serial_col} {text_field_type},
    {ta_type_col} {text_field_type},
    {division_col} {text_field_type},
    {tt_name_col} {text_field_type},
    {tt_location_col} {text_field_type},
    {ta_cell_number_col} {int_field_type},
    {ta_cell_is_snack_col} {int_field_type},
    {product_col} {text_field_type},
    {ta_cell_deficit_col} {int_field_type},
    {number_of_sales_col} {int_field_type},
    {sum_of_sales_col} {int_field_type},
    {product_cost_price_col} {real_field_type},
    {product_control_cost_price_col} {real_field_type},
    PRIMARY KEY ({doc_number_col}, {doc_date_col}, {ta_cell_number_col})
);
"""
drop_table_sales_raw = f"""DROP TABLE {sales_raw_table_name};"""
clear_table_sales_raw = f"DELETE FROM {sales_raw_table_name};"

# creating normalized sales table
create_table_sales = f"""
CREATE TABLE IF NOT EXISTS {sales_table_name} (
    {doc_number_col} {int_field_type},
    {doc_date_col} {text_field_type},
    {organization_id_col} {int_field_type} DEFAULT NULL,
    {operator_id_col} {int_field_type} DEFAULT NULL,
    {ta_id_col} {int_field_type} DEFAULT NULL,
    {division_id_col} {text_field_type} DEFAULT NULL,
    {tt_id_col} {int_field_type} DEFAULT NULL,
    {ta_cell_number_col} {int_field_type},
    {product_id_col} {int_field_type} DEFAULT NULL,
    {number_of_sales_col} {int_field_type},
    {sum_of_sales_col} {int_field_type},
    {product_cost_price_col} {real_field_type},
    {product_control_cost_price_col} {real_field_type},
    FOREIGN KEY({organization_id_col}) REFERENCES {organization_table_name}({id_col}),
    FOREIGN KEY({operator_id_col}) REFERENCES {operator_table_name}({id_col}),
    FOREIGN KEY({ta_id_col}) REFERENCES {ta_table_name}({id_col}),
    FOREIGN KEY({division_id_col}) REFERENCES {division_table_name}({id_col}),
    FOREIGN KEY({tt_id_col}) REFERENCES {tt_table_name}({id_col}),
    FOREIGN KEY({product_id_col}) REFERENCES {product_table_name}({id_col}),
    PRIMARY KEY ({doc_number_col}, {doc_date_col}, {ta_cell_number_col})
);
"""

create_table_organization = f"""
CREATE TABLE IF NOT EXISTS {organization_table_name} (
    {id_col} {int_field_type} PRIMARY KEY AUTOINCREMENT,
    {organization_col} {text_field_type} NOT NULL UNIQUE
);
"""

create_table_operator = f"""
CREATE TABLE IF NOT EXISTS {operator_table_name} (
    {id_col} {int_field_type} PRIMARY KEY AUTOINCREMENT,
    {operator_col} {text_field_type} NOT NULL UNIQUE
);
"""

create_table_ta = f"""
CREATE TABLE IF NOT EXISTS {ta_table_name} (
    {id_col} {int_field_type} PRIMARY KEY AUTOINCREMENT,
    {ta_brand_col} {text_field_type},
    {ta_model_col} {text_field_type},
    {ta_serial_col} {text_field_type},
    {ta_type_col} {text_field_type} NOT NULL,
    UNIQUE({ta_brand_col}, {ta_model_col}, {ta_serial_col})
);
"""

create_table_division = f"""
CREATE TABLE IF NOT EXISTS {division_table_name} (
    {id_col} {int_field_type} PRIMARY KEY AUTOINCREMENT,
    {division_col} {text_field_type} NOT NULL UNIQUE
);
"""

create_table_tt = f"""
CREATE TABLE IF NOT EXISTS {tt_table_name} (
    {id_col} {int_field_type} PRIMARY KEY AUTOINCREMENT,
    {tt_name_col} {text_field_type} NOT NULL,
    {tt_location_col} {text_field_type},
    UNIQUE({tt_name_col}, {tt_location_col})
);
"""

create_table_product = f"""
CREATE TABLE IF NOT EXISTS {product_table_name} (
    {id_col} {int_field_type} PRIMARY KEY AUTOINCREMENT,
    {product_col} {text_field_type} NOT NULL UNIQUE
);
"""

create_normalized_tables = "".join([create_table_sales,
                                    create_table_organization,
                                    create_table_operator,
                                    create_table_ta,
                                    create_table_division,
                                    create_table_tt,
                                    create_table_product])

query_sales_raw_group_by_div = f"""
SELECT
    {division_col},
    SUM({number_of_sales_col}) AS 'Кол-во',
    SUM({sum_of_sales_col}) AS Сумма,
    SUM({sum_of_sales_col}) - SUM({product_control_cost_price_col}) AS ВП
FROM {sales_raw_table_name}
WHERE
    {deleted_col} = 0 AND
    {registered_col} = 1 AND
    {ta_type_col} = ? AND
    {ta_cell_number_col} <= 90 AND
    {doc_date_col} = ?
GROUP BY {division_col}
ORDER BY Сумма DESC;
"""

delete_unreg_record = f"""
DELETE FROM {sales_raw_table_name}
WHERE
    {deleted_col} = 1 OR
    {registered_col} = 0;
"""

insert_distinct_organization = f"""
INSERT OR IGNORE  INTO {organization_table_name} ({organization_col})
SELECT DISTINCT {organization_col}  FROM {sales_raw_table_name};
"""

insert_distinct_operator = f"""
INSERT OR IGNORE  INTO {operator_table_name} ({operator_col})
SELECT DISTINCT {operator_col}  FROM {sales_raw_table_name};
"""

insert_distinct_ta = f"""
INSERT OR IGNORE  INTO {ta_table_name} ({ta_brand_col},
                                        {ta_model_col},
                                        {ta_serial_col},
                                        {ta_type_col})
SELECT DISTINCT {ta_brand_col},
                {ta_model_col},
                {ta_serial_col},
                {ta_type_col}                
FROM {sales_raw_table_name};
"""

insert_distinct_division = f"""
INSERT OR IGNORE  INTO {division_table_name} ({division_col})
SELECT DISTINCT {division_col}  FROM {sales_raw_table_name};
"""

insert_distinct_tt = f"""
INSERT OR IGNORE  INTO {tt_table_name} ({tt_name_col}, {tt_location_col})
SELECT DISTINCT {tt_name_col}, {tt_location_col}  FROM {sales_raw_table_name};
"""

insert_distinct_product = f"""
INSERT OR IGNORE  INTO {product_table_name} ({product_col})
SELECT DISTINCT {product_col}  FROM {sales_raw_table_name};
"""

insert_distinct_to_tables = "".join([insert_distinct_organization,
                                     insert_distinct_operator,
                                     insert_distinct_ta,
                                     insert_distinct_division,
                                     insert_distinct_tt,
                                     insert_distinct_product])

migrate_from_sales_raw_to_sales = f"""
INSERT OR IGNORE INTO {sales_table_name}
SELECT
    {doc_number_col},
    {doc_date_col},
    {organization_table_name}.{id_col},
    {operator_table_name}.{id_col},
    {ta_table_name}.{id_col},
    {division_table_name}.{id_col},
    {tt_table_name}.{id_col},
    {ta_cell_number_col},
    {product_table_name}.{id_col},
    {number_of_sales_col},
    {sum_of_sales_col},
    {product_cost_price_col},
    {product_control_cost_price_col}
FROM {sales_raw_table_name}
LEFT JOIN {ta_table_name}
    ON {sales_raw_table_name}.{ta_brand_col} = {ta_table_name}.{ta_brand_col} 
    AND {sales_raw_table_name}.{ta_model_col}  = {ta_table_name}.{ta_model_col} 
    AND {sales_raw_table_name}.{ta_serial_col}  = {ta_table_name}.{ta_serial_col}
LEFT JOIN {organization_table_name}
    ON {sales_raw_table_name}.{organization_col}  = {organization_table_name}.{organization_col}
LEFT JOIN {operator_table_name}
    ON {sales_raw_table_name}.{operator_col} = {operator_table_name}.{operator_col}
LEFT JOIN {division_table_name}
    ON {sales_raw_table_name}.{division_col} = {division_table_name}.{division_col}
LEFT JOIN {tt_table_name}
    ON {sales_raw_table_name}.{tt_name_col} = {tt_table_name}.{tt_name_col}
    AND {sales_raw_table_name}.{tt_location_col} = {tt_table_name}.{tt_location_col}
LEFT JOIN {product_col}
    ON {sales_raw_table_name}.{product_col} = {product_col}.{product_col}
;"""
