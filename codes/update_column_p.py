def update_column_p_sheet(worksheet, category_2_column_index, start_row, num_rows, new_rows):
    category_2_range = f"{category_2_column_index}{str(start_row)}:{category_2_column_index}{str(start_row + num_rows - 1)}"
    category_2_values = [[row[15]] for row in new_rows] # Category 2 is the 16th element in new_rows
    worksheet.update(category_2_range, category_2_values)