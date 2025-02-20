def update_column_ad_sheet(worksheet, detail_columns_start_index, start_row, num_rows, new_rows):
    detail_updates = []
    for row_index in range(num_rows):
        details_text = new_rows[row_index][-1] # Details text is the last element of each new_row
        cell_range = f"{detail_columns_start_index}{str(start_row + row_index)}"
        detail_updates.append({'range': cell_range, 'values': [[details_text]]})

    if detail_updates:
        worksheet.batch_update(detail_updates)