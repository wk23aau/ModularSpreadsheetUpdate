def update_column_u_sheet(worksheet, category_3_url_index, start_row, num_rows, new_rows):
    category_3_url_range = f"{category_3_url_index}{str(start_row)}:{category_3_url_index}{str(start_row + num_rows - 1)}"
    category_3_url_values = [[row[20]] for row in new_rows] # Category 3 URL is the 21st element in new_rows
    worksheet.update(category_3_url_range, category_3_url_values)