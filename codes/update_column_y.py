def update_column_y_sheet(worksheet, shipping_col_index, start_row, num_rows, new_rows):
    shipping_range = f"{shipping_col_index}{str(start_row)}:{shipping_col_index}{str(start_row + num_rows - 1)}"
    shipping_values = [[""] for _ in range(num_rows)] # Shipping is set to empty string
    worksheet.update(shipping_range, shipping_values)