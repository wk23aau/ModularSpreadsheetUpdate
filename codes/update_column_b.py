def update_column_b_sheet(worksheet, product_id_col_index, start_row, num_rows, new_rows):
    product_id_range = f"{product_id_col_index}{str(start_row)}:{product_id_col_index}{str(start_row + num_rows - 1)}"
    product_id_values = [[row[1]] for row in new_rows] # Product ID is the 2nd element in new_rows
    worksheet.update(product_id_range, product_id_values)