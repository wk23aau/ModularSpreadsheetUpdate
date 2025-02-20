def update_column_x_sheet(worksheet, referral_fee_percentage_col_index, start_row, num_rows, new_rows):
    referral_fee_percentage_range = f"{referral_fee_percentage_col_index}{str(start_row)}:{referral_fee_percentage_col_index}{str(start_row + num_rows - 1)}"
    referral_fee_percentage_values = [[row[23]] for row in new_rows] # Referral Fee Percentage is the 24th element in new_rows
    worksheet.update(referral_fee_percentage_range, referral_fee_percentage_values)