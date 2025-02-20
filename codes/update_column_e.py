LIGHT_ORANGE_HEX = "#FFE0B2" # Define LIGHT_ORANGE_HEX here as it's used in this module
LIGHT_GREEN_HEX = "#C8E6C9" # Define LIGHT_GREEN_HEX here as it's used in this module
DEFAULT_LABEL_FEE = 4.5 # Define DEFAULT_LABEL_FEE here as it's used in this module
DEFAULT_PROCESSING_FEE = 0.5 # Define DEFAULT_PROCESSING_FEE here as it's used in this module

def update_column_e_sheet(worksheet, price_col_index, selling_price_column_index, referral_fee_percentage_col_index, label_fee_column_index, processing_fee_column_index, shipping_col_index, profit_loss_column_index, detail_columns_start_index, start_row, num_rows):
    price_range = f"{price_col_index}{str(start_row)}:{price_col_index}{str(start_row + num_rows - 1)}" # Column E - Price
    price_formatting = {
        "numberFormat": {"type": "NUMBER", "pattern": "#,##0.00"}
    }
    worksheet.format(price_range, price_formatting)
    # Price values are already inserted in main_modular.py during row insertion

    selling_price_range = f"{selling_price_column_index}{str(start_row)}:{selling_price_column_index}{str(start_row + num_rows - 1)}" # Column Z - Selling Price
    selling_price_formatting = {
        "numberFormat": {"type": "NUMBER", "pattern": "#,##0.00"},
        "backgroundColor": {"red": 1.0, "green": 0.9, "blue": 0.7}
    }
    worksheet.format(selling_price_range, selling_price_formatting)
    # Selling Price values are already inserted in main_modular.py during row insertion

    referral_fee_range = f"{referral_fee_percentage_col_index}{str(start_row)}:{referral_fee_percentage_col_index}{str(start_row + num_rows - 1)}" # Column X - Referral Fee
    referral_fee_formatting = {
        "numberFormat": {"type": "NUMBER", "pattern": "#,##0.00"},
        "backgroundColor": {"red": 1.0, "green": 0.9, "blue": 0.7}
    }
    worksheet.format(referral_fee_range, referral_fee_formatting)
    # Referral Fee Percentage values are already inserted in main_modular.py during row insertion

    label_fee_range = f"{label_fee_column_index}{str(start_row)}:{label_fee_column_index}{str(start_row + num_rows - 1)}" # Column AA - Label Fee
    worksheet.format(label_fee_range, {"numberFormat": {"type": "NUMBER", "pattern": "#,##0.00"}})
    worksheet.update(label_fee_range, [[DEFAULT_LABEL_FEE]] * num_rows)

    processing_fee_range = f"{processing_fee_column_index}{str(start_row)}:{processing_fee_column_index}{str(start_row + num_rows - 1)}" # Column AB - Processing Fee
    worksheet.format(processing_fee_range, {"numberFormat": {"type": "NUMBER", "pattern": "#,##0.00"}})
    worksheet.update(processing_fee_range, [[DEFAULT_PROCESSING_FEE]] * num_rows)

    shipping_col_range = f"{shipping_col_index}{str(start_row)}:{shipping_col_index}{str(start_row + num_rows - 1)}" # Column Y - Shipping
    # Shipping values are already inserted as empty strings in main_modular.py during row insertion

    profit_loss_range = f"{profit_loss_column_index}{str(start_row)}:{profit_loss_column_index}{str(start_row + num_rows - 1)}" # Column AC - Profit/Loss
    profit_loss_formula = f"=(Y{start_row}+Z{start_row})-(E{start_row}+AA{start_row}+AB{start_row})"
    formula_values = [[profit_loss_formula]] * num_rows
    worksheet.update(profit_loss_range, formula_values)