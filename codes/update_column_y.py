import logging
import gspread # Ensure gspread is imported

DEFAULT_SHIPPING_PRICE = 9.99 # Define default shipping price

def update_column_y_sheet(worksheet, shipping_col_index, start_row, num_rows, new_rows):
    """
    Updates Column Y (Shipping) in the Google Sheet with the default shipping price (9.99)
    and sets background color to white using worksheet.format().

    Args:
        worksheet: The Google Sheet worksheet object.
        shipping_col_index: The column index for 'Shipping' (e.g., "Y").
        start_row: The starting row number for updates.
        num_rows: The number of rows to update.
        new_rows:  This argument is included for consistency with other update functions,
                   but it's not directly used in this function as we are now setting a default value.
    """
    logging.info(f"START: update_column_y_sheet - Updating Column Y (Shipping) for rows {start_row} to {start_row + num_rows - 1}...")

    value_updates = [] # List for value updates


    for i in range(num_rows):
        row_index = start_row + i
        cell_coordinate = f"{shipping_col_index}{row_index}"
        logging.info(f"Processing row {row_index}, cell_coordinate: {cell_coordinate}, setting value: {DEFAULT_SHIPPING_PRICE}, setting background to white") # Log row and value

        # 1. Prepare value update
        value_updates.append({
            'range': cell_coordinate,
            'values': [[DEFAULT_SHIPPING_PRICE]] # Set default shipping price to 9.99
        })

        # 2. Apply format using worksheet.format() -  Moved from batch_update
        cell_range = f"{shipping_col_index}{row_index}" # Define cell_range for format
        formatting_rules = {'backgroundColor': {"red": 1.0, "green": 1.0, "blue": 1.0}} # White background
        worksheet.format(cell_range, formatting_rules) # Apply formatting directly using worksheet.format()


    if value_updates:
        logging.info("Calling worksheet.batch_update for value updates in Column Y...") # Log before batch_update for values
        worksheet.batch_update(value_updates, value_input_option='USER_ENTERED') # Specify value_input_option
        logging.info(f"Column Y (Shipping) values updated for rows {start_row} to {start_row + num_rows - 1}. Value batch_update call completed.") # Log after value batch_update


    logging.info("END: update_column_y_sheet - Column Y update process finished.")