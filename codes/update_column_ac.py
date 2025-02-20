def update_column_ac_sheet(worksheet, profit_loss_column_index, shipping_col_index, selling_price_column_index, price_col_index, label_fee_column_index, processing_fee_column_index, start_row, num_rows):
    profit_loss_range = f"{profit_loss_column_index}{str(start_row)}:{profit_loss_column_index}{str(start_row + num_rows - 1)}"
    profit_loss_formula = f"=(Y{start_row}+Z{start_row})-(E{start_row}+AA{start_row}+AB{start_row})"
    formula_values = [[profit_loss_formula]] * num_rows
    worksheet.update(profit_loss_range, formula_values)