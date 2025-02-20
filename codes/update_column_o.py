def update_column_o_sheet(worksheet, category_1_column_index, start_row, num_rows, new_rows):
    category_1_range = f"{category_1_column_index}{str(start_row)}:{category_1_column_index}{str(start_row + num_rows - 1)}"
    category_1_values = [[row[14]] for row in new_rows] # Category 1 is the 15th element in new_rows
    worksheet.update(category_1_range, category_1_values)