def update_column_s_sheet(worksheet, category_1_url_column_index, start_row, num_rows, new_rows):
    category_1_url_range = f"{category_1_url_column_index}{str(start_row)}:{category_1_url_column_index}{str(start_row + num_rows - 1)}"
    category_1_url_values = [[row[18]] for row in new_rows] # Category 1 URL is the 19th element in new_rows
    worksheet.update(category_1_url_range, category_1_url_values)