def update_column_w_sheet(worksheet, product_category_col_index, start_row, num_rows, new_rows):
    product_category_range = f"{product_category_col_index}{str(start_row)}:{product_category_col_index}{str(start_row + num_rows - 1)}"
    product_category_values = [[row[22]] for row in new_rows] # Product Category is the 23rd element in new_rows
    worksheet.update(product_category_range, product_category_values)