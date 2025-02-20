def update_column_a_sheet(worksheet, sku_column_index, start_row, num_rows, new_rows):
    sku_range = f"{sku_column_index}{str(start_row)}:{sku_column_index}{str(start_row + num_rows - 1)}"
    sku_values = [[row[0]] for row in new_rows] # SKU is the 1st element in new_rows
    worksheet.update(sku_range, sku_values)