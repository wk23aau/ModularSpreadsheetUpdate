import logging

def update_column_ae_sheet(worksheet, details_raw_column_index, start_row, num_rows, new_rows):
    """
    Updates column AE (Details - Raw) in the Google Sheet with the raw 'details' data from new_rows.

    Args:
        worksheet: The Google Sheet worksheet object.
        details_raw_column_index: The column index for 'Details - Raw' (e.g., "AE").
        start_row: The starting row number for updates.
        num_rows: The number of rows to update.
        new_rows: A list of lists, where each inner list is a row of data.
                   It is expected that 'details' data is in the last element of each inner list.
    """
    logging.info("Updating Column AE (Details - Raw) in Google Sheet...")
    cells_to_update = []
    for i in range(num_rows):
        row_index = start_row + i
        details_raw_value = new_rows[i][-1] if new_rows[i] else '' # Get raw details from the last element of new_row_data
        cell_coordinate = f"{details_raw_column_index}{row_index}"
        cells_to_update.append({'range': cell_coordinate, 'values': [[details_raw_value]]})

    if cells_to_update:
        worksheet.batch_update(cells_to_update)
        logging.info(f"Column AE (Details - Raw) updated for rows {start_row} to {start_row + num_rows - 1}.")
    else:
        logging.info("No updates needed for Column AE (Details - Raw).")