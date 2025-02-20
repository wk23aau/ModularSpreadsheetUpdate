def update_column_r_sheet(worksheet, category_4_column_index, start_row, num_rows, new_rows):
    category_4_range = f"{category_4_column_index}{str(start_row)}:{category_4_column_index}{str(start_row + num_rows - 1)}"
    category_4_values = [[row[17]] for row in new_rows] # Category 4 is the 18th element in new_rows
    worksheet.update(category_4_range, category_4_values)