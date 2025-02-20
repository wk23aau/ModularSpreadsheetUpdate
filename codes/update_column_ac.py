import logging
import gspread # Ensure gspread is imported

def update_column_ac_sheet(worksheet, profit_loss_column_index, shipping_col_index, selling_price_column_index, price_col_index, label_fee_column_index, processing_fee_column_index, start_row, num_rows):
    """
    Updates Column AC (Profit/Loss) with the profit/loss formula, explicitly using USER_ENTERED option.
    """
    logging.info("Updating Column AC (Profit/Loss) with formulas and USER_ENTERED option...")
    cells_to_update = []
    for i in range(num_rows): # Loop through each row to update
        row_index = start_row + i
        # Construct the Profit/Loss formula, now with the correct row_index
        formula = f'=(Y{row_index}+Z{row_index})-(E{row_index}+AA{row_index}+AB{row_index})'

        cell_coordinate = f"{profit_loss_column_index}{row_index}"
        cells_to_update.append({'range': cell_coordinate, 'values': [[formula]]}) # Add update for the specific cell

    if cells_to_update:
        worksheet.batch_update(cells_to_update, value_input_option='USER_ENTERED') # <--- ADDED value_input_option
        logging.info(f"Column AC (Profit/Loss) updated with formulas (USER_ENTERED) for rows {start_row} to {start_row + num_rows - 1}.")
    else:
        logging.info("No updates needed for Column AC (Profit/Loss).")