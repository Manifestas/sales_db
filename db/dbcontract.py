# column names
deleted_col = "deleted"
registered_col = "registered"
doc_number_col = "doc_number"
doc_date_col = "doc_date"
doc_date_time_col = "doc_date_time"
organization_col = "organization"
operator_col = "operator"
ta_brand_col = "ta_brand"
ta_model_col = "ta_model"
ta_serial_col = "ta_serial"
ta_type_col = "ta_type"
division_col = "division"
tt_name_col = "tt_name"
tt_location_col = "tt_location"
ta_cell_number_col = "ta_cell_number"
ta_cell_is_snack_col = "ta_cell_is_snack"
product_col = "product"
ta_cell_deficit_col = "ta_cell_deficit"
number_of_sales_col = "number_of_sales"
sum_of_sales_col = "sum_of_sales"
product_cost_price_col = "product_cost_price"
product_control_cost_price_col = "product_control_cost_price"

sqlite_db_file = "../data/sqlite.db"
sales_table_name = "sales"

int_field_type = "INTEGER"
real_field_type = "REAL"
text_field_type = "TEXT"

create_table_sales = f"""
CREATE TABLE {sales_table_name} (
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
    {product_control_cost_price_col} {real_field_type}
    PRIMARY KEY ({number_of_sales_col}, {doc_date_col})
);
"""
