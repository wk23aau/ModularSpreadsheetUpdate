import logging
import json

def update_column_ad_sheet(worksheet, details_column_index, start_row, num_rows, new_rows):
    """
    Updates column AD (Details) in the Google Sheet by processing data from Column AE (Details - Raw) locally in Python.
    This function extracts key-value pairs from the JSON-like string in 'Details - Raw' and formats them as '{key1: value1}, {key2: value2}',
    assuming the 'details' values in the JSON are in pairs.

    Args:
        worksheet: The Google Sheet worksheet object.
        details_column_index: The column index for 'Details' (e.g., "AD").
        start_row: The starting row number for updates.
        num_rows: The number of rows to update.
        new_rows: A list of lists, where each inner list is a row of data,
                   and the 'details' raw string is expected to be the last element.
    """
    logging.info("Updating Column AD (Details) in Google Sheet with key-value pair format (value as key, next value as value)...")
    cells_to_update = []
    for i in range(num_rows):
        row_index = start_row + i
        details_raw_value = new_rows[i][-1] if new_rows[i] else '' # Get raw details from new_rows
        formatted_details_list = [] # Initialize list to hold formatted detail strings

        try:
            # Attempt to parse the details_raw_value as JSON
            details_list = json.loads(details_raw_value)
            # Iterate through details_list in pairs (assuming key-value pairs are sequential)
            for j in range(0, len(details_list), 2): # Increment by 2 to process pairs
                if j + 1 < len(details_list): # Ensure there's a pair (check for next element)
                    key_item = details_list[j]
                    value_item = details_list[j+1]

                    key_value = key_item.get("details", "") if isinstance(key_item, dict) else "" # Extract key (first 'details' value)
                    value_value = value_item.get("details", "") if isinstance(value_item, dict) else "" # Extract value (second 'details' value)

                    if key_value and value_value: # Only format if both key and value are extracted
                        formatted_details_list.append(f"{{{key_value}: {value_value}}}") # Format as "{key: value}"

        except json.JSONDecodeError:
            logging.warning(f"Could not parse JSON for row {row_index}: {details_raw_value}. Handling as string.")
            # If JSON parsing fails, handle as a simple string or apply other logic if needed
            extracted_details = "Parsing Failed: " + details_raw_value # Or handle differently

        extracted_details = ", ".join(formatted_details_list) # Join formatted pairs with commas and spaces
        cell_coordinate = f"{details_column_index}{row_index}"
        cells_to_update.append({'range': cell_coordinate, 'values': [[extracted_details]]})

    if cells_to_update:
        worksheet.batch_update(cells_to_update)
        logging.info(f"Column AD (Details) updated with value-as-key format for rows {start_row} to {start_row + num_rows - 1}.")
    else:
        logging.info("No updates needed for Column AD (Details).")