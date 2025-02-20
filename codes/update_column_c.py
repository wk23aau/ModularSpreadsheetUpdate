def update_column_c_sheet(worksheet, heading_col_index, start_row, num_rows, new_rows):
    heading_range = f"{heading_col_index}{str(start_row)}:{heading_col_index}{str(start_row + num_rows - 1)}"
    heading_values = [[row[2]] for row in new_rows] # Heading is the 3rd element in new_rows
    worksheet.update(heading_range, heading_values)