def update_column_k_sheet(worksheet, summary_column_index, start_row, num_rows, new_rows):
    summary_range = f"{summary_column_index}{str(start_row)}:{summary_column_index}{str(start_row + num_rows - 1)}"
    summary_values = [[row[10]] for row in new_rows] # Summary is the 11th element in new_rows
    worksheet.update(summary_range, summary_values)