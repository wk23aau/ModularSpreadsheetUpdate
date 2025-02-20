def update_column_d_sheet(worksheet, brand_col_index, start_row, num_rows, new_rows):
    brand_range = f"{brand_col_index}{str(start_row)}:{brand_col_index}{str(start_row + num_rows - 1)}"
    brand_values = [[row[3]] for row in new_rows] # Brand is the 4th element in new_rows
    worksheet.update(brand_range, brand_values)