LIGHT_ORANGE_HEX = "#FFE0B2" # Define LIGHT_ORANGE_HEX here as it's used in this module

def update_column_z_sheet(worksheet, selling_price_column_index, start_row, num_rows, new_rows):
    selling_price_range = f"{selling_price_column_index}{str(start_row)}:{selling_price_column_index}{str(start_row + num_rows - 1)}"
    selling_price_formatting = {
        "numberFormat": {"type": "NUMBER", "pattern": "#,##0.00"},
        "backgroundColor": {"red": 1.0, "green": 0.9, "blue": 0.7"}
    }
    worksheet.format(selling_price_range, selling_price_formatting)
    # Selling Price values are already inserted in main_modular_columns.py during row insertion