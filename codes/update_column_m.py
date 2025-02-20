def update_column_m_sheet(worksheet, key_feature_2_column_index, start_row, num_rows, new_rows):
    key_feature_2_range = f"{key_feature_2_column_index}{str(start_row)}:{key_feature_2_column_index}{str(start_row + num_rows - 1)}"
    key_feature_2_values = [[row[12]] for row in new_rows] # Key Feature 2 is the 13th element in new_rows
    worksheet.update(key_feature_2_range, key_feature_2_values)