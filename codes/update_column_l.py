def update_column_l_sheet(worksheet, key_feature_1_column_index, start_row, num_rows, new_rows):
    key_feature_1_range = f"{key_feature_1_column_index}{str(start_row)}:{key_feature_1_column_index}{str(start_row + num_rows - 1)}"
    key_feature_1_values = [[row[11]] for row in new_rows] # Key Feature 1 is the 12th element in new_rows
    worksheet.update(key_feature_1_range, key_feature_1_values)