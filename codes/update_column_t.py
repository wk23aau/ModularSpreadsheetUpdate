def update_column_t_sheet(worksheet, category_2_url_index, start_row, num_rows, new_rows):
    category_2_url_range = f"{category_2_url_index}{str(start_row)}:{category_2_url_index}{str(start_row + num_rows - 1)}"
    category_2_url_values = [[row[19]] for row in new_rows] # Category 2 URL is the 20th element in new_rows
    worksheet.update(category_2_url_range, category_2_url_values)