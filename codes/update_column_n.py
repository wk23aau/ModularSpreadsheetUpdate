def update_column_n_sheet(worksheet, remaining_key_features_column_index, start_row, num_rows, new_rows):
    remaining_key_features_range = f"{remaining_key_features_column_index}{str(start_row)}:{remaining_key_features_column_index}{str(start_row + num_rows - 1)}"
    remaining_key_features_values = [[row[13]] for row in new_rows] # Remaining Key Features is the 14th element in new_rows
    worksheet.update(remaining_key_features_range, remaining_key_features_values)