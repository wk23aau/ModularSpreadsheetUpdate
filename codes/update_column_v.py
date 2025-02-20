def update_column_v_sheet(worksheet, category_4_url_index, start_row, num_rows, new_rows):
    category_4_url_range = f"{category_4_url_index}{str(start_row)}:{category_4_url_index}{str(start_row + num_rows - 1)}"
    category_4_url_values = [[row[21]] for row in new_rows] # Category 4 URL is the 22nd element in new_rows
    worksheet.update(category_4_url_range, category_4_url_values)