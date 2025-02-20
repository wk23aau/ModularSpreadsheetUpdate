def update_column_q_sheet(worksheet, category_3_column_index, start_row, num_rows, new_rows):
    category_3_range = f"{category_3_column_index}{str(start_row)}:{category_3_column_index}{str(start_row + num_rows - 1)}"
    category_3_values = [[row[16]] for row in new_rows] # Category 3 is the 17th element in new_rows
    worksheet.update(category_3_range, category_3_values)